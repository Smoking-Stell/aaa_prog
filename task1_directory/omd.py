def step2_umbrella():
    print(
        'Утка комфортно прогулялась по парку под дождём. '
        'Затем сухая пришла в бар, поболтала с барменом и ушла'
    )


def step2_no_umbrella():
    print(
        'Утка бежала под страшным дождем поскорее в бар. '
        'В баре она отогрелась у камина. '
        'И осталась там до утра, рассказывая и слушая истории.'
    )


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
