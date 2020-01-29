import ast

with open("core_races.txt", "r") as in_file:
    core_races = ast.literal_eval(in_file.read())

# print(core_races['dwarf']['size'])

character = {}

character['race'] = core_races[input('Pick your race: >\n\tDwarf\n\tElf\n\tHalf-Elf\n\tHalf-Orc\n\tHalfling\n\tHuman\n\tGnome\n> ').lower()]
char_race_name = character['race']['name']

print(character)
