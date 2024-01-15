class EmojiMixin:
    emoji_map = {
        "Electric": "⚡",
        "Fire": "🔥",
        "Water": "💧",
        "Grass": "🌿",
    }

    def __str__(self):
        category_emoji = self.emoji_map.get(self.category, self.category)
        return f"{self.name}/{category_emoji}"

class BasePokemon():
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name}/{self.category}"

class Pokemon(EmojiMixin, BasePokemon):
    def __init__(self, name: str, category: str, weakness=()):
        super().__init__(name, category)
        self.weakness = weakness


pok = Pokemon("Pikachu", "Electric")

print(pok)

