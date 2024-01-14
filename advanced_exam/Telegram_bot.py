
"""
Bot for playing tic tac toe game with multiple CallbackQueryHandlers.
"""
import random
from copy import deepcopy
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
)
import os

from information import token_tic_tac_toe

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s '
           '- %(message)s', level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger('httpx').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# get token using BotFather
TOKEN = token_tic_tac_toe

CONTINUE_GAME, FINISH_GAME, CHOOSING_OPPONENT = range(3)

FREE_SPACE = '.'
CROSS = 'X'
ZERO = 'O'


DEFAULT_STATE = [ [FREE_SPACE for _ in range(3) ] for _ in range(3) ]


def get_default_state():
    """Helper function to get default state of the game"""
    return deepcopy(DEFAULT_STATE)


def generate_keyboard(state: list[list[str]]) \
        -> list[list[InlineKeyboardButton]]:
    """Generate tic tac toe keyboard 3x3 (telegram buttons)"""
    return [
        [
            InlineKeyboardButton(state[r][c], callback_data=f'{r}{c}')
            for r in range(3)
        ]
        for c in range(3)
    ]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Send message on `/start`."""
    keyboard = [
        [InlineKeyboardButton("Play with human", callback_data='play_human')],
        [InlineKeyboardButton("Play with computer",
                              callback_data='play_computer')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose game type:',
                                    reply_markup=reply_markup)
    return CHOOSING_OPPONENT


def computer_move(fields: list[list[str]]) -> (int, int):
    counter = 0
    for i in range(3):
        for j in range(3):
            if fields[i][j] == FREE_SPACE:
                counter += 1

    pos = random.randint(1, counter)

    for i in range(3):
        for j in range(3):
            if fields[i][j] == FREE_SPACE:
                pos -= 1
                if pos == 0:
                    return i, j


def swap_player(current_position: str) -> str:
    """
    Changes current player

    :param current_position:
    :return: new player position
    """
    if current_position == CROSS:
        return ZERO
    return CROSS


async def game(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Main processing of the game"""

    query = update.callback_query
    await query.answer()

    update_row, update_col = int(query.data[0]), int(query.data[1])

    if context.user_data['keyboard_state'][update_row][update_col] \
            == FREE_SPACE:
        context.user_data['keyboard_state'][update_row][update_col] =\
            context.user_data['current_player']

        if won(context.user_data['keyboard_state']):
            await query.edit_message_text\
                (f"{context.user_data['current_player']} win!")
            return FINISH_GAME

        if context.user_data['opponent'] == 'human':
            context.user_data['current_player'] =\
                swap_player(context.user_data['current_player'])
        else:
            computer_row, computer_col = \
                computer_move(context.user_data['keyboard_state'])
            context.user_data['keyboard_state'][computer_row][computer_col] = \
                swap_player(context.user_data['current_player'])

            if won(context.user_data['keyboard_state']):
                await query.edit_message_text \
                    (f"Computer win!")
                return FINISH_GAME

        keyboard = generate_keyboard(context.user_data['keyboard_state'])

        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=f"Now {context.user_data['current_player']}'s turn",
            reply_markup=reply_markup
        )

        return CONTINUE_GAME
    else:
        await query.edit_message_text('This space is not free.')
        return CONTINUE_GAME


def won(fields: list[list[str]]) -> bool:
    """Check if crosses or zeros have won the game"""
    for i in range(3):
        if fields[i][0] == fields[i][1] == fields[i][2] != FREE_SPACE or \
                fields[0][i] == fields[1][i] == fields[2][i] != FREE_SPACE:
            return True

    if fields[0][0] == fields[1][1] == fields[2][2] != FREE_SPACE or \
            fields[0][2] == fields[1][1] == fields[2][0] != FREE_SPACE:
        return True

    return False



async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    # reset state to default so you can play again with /start
    context.user_data['keyboard_state'] = get_default_state()
    return ConversationHandler.END


async def choose_opponent(update: Update,
                          context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    if query.data == 'play_human':
        context.user_data['opponent'] = 'human'
    elif query.data == 'play_computer':
        context.user_data['opponent'] = 'computer'

    context.user_data['keyboard_state'] = get_default_state()
    context.user_data['current_player'] = CROSS
    keyboard = generate_keyboard(context.user_data['keyboard_state'])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.message.reply_text(
        f"X's turn! Please, put X to the free place",
        reply_markup=reply_markup)
    return CONTINUE_GAME


def main() -> None:
    """Run the bot"""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Setup conversation handler with the states CONTINUE_GAME and FINISH_GAME
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CONTINUE_GAME: [
                CallbackQueryHandler(game, pattern='^' + f'{r}{c}' + '$')
                for r in range(3)
                for c in range(3)
            ],
            FINISH_GAME: [
                CallbackQueryHandler(end, pattern='^' + f'{r}{c}' + '$')
                for r in range(3)
                for c in range(3)
            ],
            CHOOSING_OPPONENT: [
                CallbackQueryHandler(choose_opponent,
                                     pattern='^play_(human|computer)$')
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to application that will be used for handling updates
    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()