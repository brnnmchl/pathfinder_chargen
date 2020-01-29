# character_creator.py
# helps to generate a character for some rpg system

# roll stats
# pick race
# pick class
# roll hit points
# select equipment
# select weapons

import random
import ast

# class Dice(object):
#     def __init__(self, sides):
#         self.sides = sides

def rolldice(sides, numdice):
    total = 0
    for num in range(int(numdice)):
        total = total + random.randint(1, int(sides))

    return total

# sides = input("Which dice would you like to roll? [2,4,6,8,10,12,20,100] > ")
# numdice = input("How many d" + sides + " would you like to roll? > ")
#
# total = rolldice(sides, numdice)
#
# print(total)


character = {}
abilities = ['strength', 'constitution', 'dexterity', 'intelligence', 'wisdom', 'charisma']
skills = [['acrobatics', 2], ['appraise', 3], ['bluff', 5], ['climb', 0], ['craft', 3], ['diplomacy', 5], ['disable device', 2],
          ['disguise', 5], ['escape artist', 2], ['fly', 2], ['handle animal', 5], ['heal', 4], ['intimidate', 5], ['linguistics', 3],
          ['perception', 4], ['perform', 5], ['profession', 4], ['ride', 2], ['sense motive', 4], ['sleight of hand', 2],
          ['spellcraft', 3], ['stealth', 2], ['survival', 4], ['swim', 0], ['use magic device', 5], ['knowledge (arcana)', 3],
          ['knowledge (dungeoneering)', 3], ['knowledge (engineering)', 3], ['knowledge (geography)', 3], ['knowledge (history)', 3],
          ['knowledge (local)', 3], ['knowledge (nature)', 3], ['knowledge (nobility)', 3], ['knowledge (planes)', 3],
          ['knowledge (religion)', 3]]


# Rolling up a set of stats values

def rollStats():
    statvalues = []

    for stat in range(6):
        rolls = []
        for x in range(4):
            roll = rolldice(6,1)
            if roll > 1:
                rolls.append(roll)
            else:
                roll = 2
                rolls.append(roll)

        rolls.sort()
        statvalue = rolls[1] + rolls[2] + rolls[3]
        statvalues.append(statvalue)

    return statvalues


# Calculating ability modifiers

def abilityMods(scores):
    modifiers = []

    for score in scores:
        if score >= 18:
            modifiers.append("+4")
        elif score >= 16:
            modifiers.append("+3")
        elif score >= 14:
            modifiers.append("+2")
        elif score >= 12:
            modifiers.append("+1")
        elif score >= 10:
            modifiers.append("0")
        elif score >= 8:
            modifiers.append("-1")
        else:
            modifiers.append("-2")

    return modifiers

def modUpdate(score):

    if score >= 18:
        modifier = "+4"
    elif score >= 16:
        modifier = "+3"
    elif score >= 14:
        modifier = "+2"
    elif score >= 12:
        modifier = "+1"
    elif score >= 10:
        modifier = "0"
    elif score >= 8:
        modifier = "-1"
    else:
        modifier = "-2"

    return modifier


# Print formatted statsblock

def statsBlock(scores, modifiers):
    print("    | Score | Modifier\t|\n"
          "STR |   " + str(scores[0]) + "  |\t" + modifiers[0] + "\t\t|\n"
          "CON |   " + str(scores[1]) + "  |\t" + modifiers[1] + "\t\t|\n"
          "DEX |   " + str(scores[2]) + "  |\t" + modifiers[2] + "\t\t|\n"
          "INT |   " + str(scores[3]) + "  |\t" + modifiers[3] + "\t\t|\n"
          "WIS |   " + str(scores[4]) + "  |\t" + modifiers[4] + "\t\t|\n"
          "CHA |   " + str(scores[5]) + "  |\t" + modifiers[5] + "\t\t|")


# Setting ability scores

values = rollStats()

statoptions = "Your values are:" \
              "\n\t1. " + str(values[0]) + "\n\t2. " + str(values[1]) + "\n\t3. " + str(values[2]) + "\n\t4. " + str(values[3]) + "\n\t5. " + str(values[4]) + "\n\t6. " + str(values[5])

print(statoptions)

print("\nEnter which value you would like to set for each ability score.\n")

statblock = []
statblock.append(int(input("Set value for STRENGTH: ")))
statblock.append(int(input("Set value for CONSTITUTION: ")))
statblock.append(int(input("Set value for DEXTERITY: ")))
statblock.append(int(input("Set value for INTELLIGENCE: ")))
statblock.append(int(input("Set value for WISDOM: ")))
statblock.append(int(input("Set value for CHARISMA: ")))

character['statblock'] = statblock


# Setting ability modifiers

abilitymodifiers = abilityMods(statblock)

print("\nYour ability scores and modifiers are:\n")

statsBlock(statblock, abilitymodifiers)

character['abilitymods'] = abilitymodifiers


# Pick a race

with open("core_races.txt", "r") as in_file:
    core_races = ast.literal_eval(in_file.read())

character['race'] = core_races[input('Pick your race: >\n\tDwarf\n\tElf\n\tHalf-Elf\n\tHalf-Orc\n\tHalfling\n\tHuman\n\tGnome\n> ').lower()]

print(character)


# Update stats and modifiers with racial perks

for stat in range(6):
    if character['race']['abilityscores'][stat] == '-2':
        character['statblock'][stat] = character['statblock'][stat] - 2
        character['abilitymods'][stat] = modUpdate(character['statblock'][stat])
    elif character['race']['abilityscores'][stat] == '+2':
        character['statblock'][stat] = character['statblock'][stat] + 2
        character['abilitymods'][stat] = modUpdate(character['statblock'][stat])
    elif character['race']['abilityscores'][stat] == 'v':
        varymod = input('\nAs a ' + character['race']['name'] + ', you can +2 to one ability score.\nWould you like to +2 to ' + abilities[stat] + '? (Yes or No) > ')
        if varymod.lower() == 'yes':
            character['statblock'][stat] = character['statblock'][stat] + 2
            character['abilitymods'][stat] = modUpdate(character['statblock'][stat])
        elif varymod.lower() == 'no':
            character['statblock'][stat] = character['statblock'][stat]
            character['abilitymods'][stat] = character['abilitymods'][stat]
        else:
            print('Error')
    else:
        character['statblock'][stat] = character['statblock'][stat]
        character['abilitymods'][stat] = character['abilitymods'][stat]




print(character)
