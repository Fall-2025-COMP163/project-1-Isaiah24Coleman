"""
# Chronicles Project - Simple Text RPG Character System
# AI usage: This code was created with AI assistance for structure and debugging. I also used my tutor on upswing to make it easier for me to write tyhe code
# I understand how each function works and can explain all logic used.
"""

def create_character(name, character_class):
      """
    Creates a new character dictionary with calculated stats.
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    """
    strength, magic, health = calculate_stats(character_class, 1)
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return character
    

def calculate_stats(character_class, level):
   """
    Calculates base stats based on class and level.
    Returns: tuple of (strength, magic, health)
    """
    character_class = character_class.lower()

    if character_class == "warrior":
        strength = 10 + level * 3
        magic = 3 + level * 1
        health = 120 + level * 10
    elif character_class == "mage":
        strength = 5 + level * 1
        magic = 15 + level * 6
        health = 80 + level * 10
    elif character_class == "rogue":
        strength = 8 + level * 2
        magic = 8 + level * 2
        health = 90 + level * 8
    elif character_class == "cleric":
        strength = 7 + level * 2
        magic = 12 + level * 4
        health = 100 + level * 9
    else:
        # default case if user enters invalid class
        strength = 5 + level
        magic = 5 + level
        health = 80 + level * 5

    return strength, magic, health
    

def save_character(character, filename):
    """
    Saves character to text file in specific format.
    Returns: True if successful, False if error occurred.
    """
    try:
        file = open(filename, "w")
        file.write("Character Name: " + character["name"] + "\n")
        file.write("Class: " + character["class"] + "\n")
        file.write("Level: " + str(character["level"]) + "\n")
        file.write("Strength: " + str(character["strength"]) + "\n")
        file.write("Magic: " + str(character["magic"]) + "\n")
        file.write("Health: " + str(character["health"]) + "\n")
        file.write("Gold: " + str(character["gold"]) + "\n")
        file.close()
        return True
    except:
        print("Error: Could not save character.")
        return False

    

def load_character(filename):
   """
    Loads character from text file.
    Returns: character dictionary if successful, None if file not found.
    """
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        character = {}
        for line in lines:
            parts = line.strip().split(": ")
            if len(parts) == 2:
                key = parts[0]
                value = parts[1]

                # Match text keys to dictionary keys
                if key == "Character Name":
                    character["name"] = value
                elif key == "Class":
                    character["class"] = value
                elif key == "Level":
                    character["level"] = int(value)
                elif key == "Strength":
                    character["strength"] = int(value)
                elif key == "Magic":
                    character["magic"] = int(value)
                elif key == "Health":
                    character["health"] = int(value)
                elif key == "Gold":
                    character["gold"] = int(value)

        return character
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    

def display_character(character):
   """
    Prints formatted character sheet.
    Returns: None (prints to console)
    """
    print("\n=== CHARACTER SHEET ===")
    print("Name:", character["name"])
    print("Class:", character["class"])
    print("Level:", character["level"])
    print("Strength:", character["strength"])
    print("Magic:", character["magic"])
    print("Health:", character["health"])
    print("Gold:", character["gold"])
    print("=======================")
    

def level_up(character):
   """
    Increases character level and recalculates stats.
    Modifies the character dictionary directly.
    Returns: None
    """
    character["level"] = character["level"] + 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    print(character["name"], "has leveled up to Level", character["level"], "!")
    

# Main program area (optional - for testing your functions)
# === MAIN PROGRAM ===
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    name = input("Enter your character's name: ")
    character_class = input("Choose a class (Warrior, Mage, Rogue, Cleric): ")

    # Create character
    char = create_character(name, character_class)
    display_character(char)

    # Save to file
    filename = name.lower() + "_save.txt"
    if save_character(char, filename):
        print("Character saved to", filename)
    else:
        print("Save failed.")

    # Load character
    loaded = load_character(filename)
    if loaded:
        print("\nLoaded character from file:")
        display_character(loaded)

    # Level up once
    print("\nLeveling up your character...")
    level_up(loaded)
    display_character(loaded)

    
