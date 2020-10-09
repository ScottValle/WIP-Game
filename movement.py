import random
import Character
import Shop
import Functions

locations = [1, 2, 3,
             4, 5, 6,
             7, 8, 9]
character = {
    'hit-points': 100,
    'location': locations[4],
    'inventory': ['Wooden Sword', 'Wooden Shield', 'Magical Amulet'],
    'photo': "▼",
}


def move_right(x):
    if (character['location'] + x) <= locations[-1]:
        character['location'] += x
        print("Character is located at " + str(character['location']))
    else:
        print("Character cannot move past the boundaries.")


def move_left(x):
    if (character['location'] - x) >= locations[0]:
        character['location'] -= x
        print("Character is located at " + str(character['location']))
    else:
        print("Character cannot move past the boundaries.")


def move_up(x):
    if (character['location'] - (3 * x)) >= locations[0]:
        character['location'] -= (3 * x)
        print("Character is located at " + str(character['location']))
    else:
        print("Character cannot move past boundaries.")


def move_down(x):
    if (character['location'] + (3 * x)) <= locations[-1]:
        character['location'] += (3 * x)
        print("Character is located at " + str(character['location']))
    else:
        print("Character cannot move past boundaries.")


def search():
    chance_to_find = 10 * character['location']
    if chance_to_find >= 90:
        if 'Godly Warhammer' not in character['inventory']:
            print("Rare item found!")
            character['inventory'].append('Godly Warhammer')
    elif chance_to_find == 10:
        locations.append(10)
        print("Secret location unlocked!")
    elif 10 < chance_to_find < 90:
        item_choices = ['Stone Sword', 'Battered Shield', 'Health Potion', 'Mana Potion']
        added_item = random.choice(item_choices)
        if added_item not in character['inventory']:
            character['inventory'].append(added_item)
            print("Common item found.")
            print(character['inventory'])
