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
            "saves": 0,
            "gold": 0,
            "inventory": [],
            "level": 1,
            "xp": 0,
            "health": 0,
            "armor": 0,
            "damage": 0,
            "mana": 0,
            "magic_damage": 0,
            "magic_armor": 0,
            "magic_resistance": 0,
            "magic_health": 0,
            "magic_armor_class": 0,
            "magic_damage_bonus": 0
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

#class to handle random generated monsters
class Monster:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def to_dict(self):
        return {
            "name": self.name,
            **self.stats
        }

    @staticmethod
    def generate_monster():
        names = ["Goblin", "Orc", "Troll", "Dragon"]
        name = random.choice(names)
        stats = {
            "str": random.randint(1, 10),
            "dex": random.randint(1, 10),
            "agi": random.randint(1, 10),
            "int": random.randint(1, 10)
        }
        return Monster(name, stats)
    
#function to handle combat
def combat(character, monster):
    print(f"You encounter a {monster.name}!")
    #add logic for combat
    while True:
        action = input("Do you want to attack or flee? ").lower()
        if action == "attack":
            print(f"You attack the {monster.name}!")
            #add logic for attack
            break
        elif action == "flee":
            print("You flee from the battle!")
            break
        else:
            print("Invalid action. Please choose 'attack' or 'flee'.")

#add logic for the treasure event
def treasure(Character):
    #add logic to give the character treasure
    print("You open the treasure chest and find gold coins!")
    #add the treasure to the characters gold stat
    Character.stats['gold'] += random.randint(1, 100)
    print(f"You now have {Character.stats['gold']} gold coins.")

#function to generate exploration options
def explore():
    events = [
        "You find a treasure chest!",
        "You encounter a wild beast!",
        "You discover a hidden cave!",
        "You meet a mysterious stranger!",
        "You stumble upon an ancient ruin!"
    ]
    #randomly chooses an event
    event = random.choice(events)
    print(event)
    #add logic for specific events
    #for example, if the event is a treasure chest, you can add logic to open it
    if "treasure" in event:
        treasure(Character)
    elif "beast" in event:
        print("You prepare to fight the beast!")
        generatedMonster = Monster.generate_monster()
        monster = generatedMonster
        combat(Character, monster)
    elif "cave" in event:
        print("You enter the cave and find it filled with strange crystals!")
    elif "stranger" in event:
        print("The stranger offers you a quest!")
    elif "ruin" in event:
        print("You explore the ruins and find ancient artifacts!")
    #add more events and logic as needed
    #return the event for further processing if needed
    return event

# Main program logic
def main():
    #create the character
    character = create_character()
    character.roll_stats()
    print("Your stats are:")
    for stat, value in character.stats.items():
        print(f"{stat.capitalize()}: {value}")
    character.save_to_file()
    
    #start the game
    print("You start your adventure!")
    print("You are unfamiliar with these lands")
    print("But you are familiar with your abilities.")
    print("You can explore the world around you.")
    
    #gives the player the option to explore, save character, rest to heal, or exit the game.
    while True:
        print("What would you like to do? (explore, save, rest, exit)")
        action = input().lower()
        if action == "explore":
            explore()
        elif action == "save":
            character.save_to_file()
            print("Character saved!")
        elif action == "rest":
            print("You rest and regain your strength.")
            #add logic to heal the character
        elif action == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid action. Please choose 'explore', 'save', 'rest', or 'exit'.")
            
    #load character from file if it exists
    loaded_character = Character.load_from_file()
    if loaded_character:
        print(f"Loaded character: {loaded_character.name}, Class: {loaded_character.char_class}")
        for stat, value in loaded_character.stats.items():
            print(f"{stat.capitalize()}: {value}")
    else:
        print("No character loaded.")
if __name__ == "__main__":
    main()