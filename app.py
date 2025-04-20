import json
import random

# Character class to encapsulate character data and logic
class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.stats = {
            "str": 0,
            "dex": 0,
            "agi": 0,
            "int": 0,
            "initiative": 0,
            "saves": 0
        }

    def roll_stats(self):
        for stat in self.stats:
            self.stats[stat] = random.randint(1, 6)

    def to_dict(self):
        return {
            "name": self.name,
            "class": self.char_class,
            **self.stats
        }

    def save_to_file(self, filename="character.json"):
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)

    @staticmethod
    def load_from_file(filename="character.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                character = Character(data["name"], data["class"])
                character.stats = {k: data[k] for k in data if k in character.stats}
                return character
        except FileNotFoundError:
            print(f"File '{filename}' not found. Starting with a new character.")
            return None

# Function to get character name and class
def create_character():
    print("First, we have to make....you.")
    name = input("What is your name? ")
    print(f'You are... {name}')

    while True:
        print("Would you be a Warrior, a Rogue, or a Magician?")
        char_class = input().lower()
        if char_class in ["warrior", "rogue", "magician"]:
            class_descriptions = {
                "warrior": "You have chosen the way of the Warrior. You will have a hard time sneaking or casting spells but you will be a threat.",
                "rogue": "You have chosen the way of the Rogue. You will stick to the shadows as a fair fight was never your plan, neither are spells.",
                "magician": "You wield great and terrible magic, but you can't take much damage and you'll need magic to unlock ways forward rather than your wits."
            }
            print(class_descriptions[char_class])
            break
        else:
            print("Invalid choice. Please choose Warrior, Rogue, or Magician.")

    return Character(name, char_class)

# Main program logic
def main():
    character = create_character()
    character.roll_stats()
    print("Your stats are:")
    for stat, value in character.stats.items():
        print(f"{stat.capitalize()}: {value}")
    character.save_to_file()

if __name__ == "__main__":
    main()