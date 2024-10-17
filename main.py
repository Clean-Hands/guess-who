from random import random
import player as p
import cpu as c
from character import Character

ai_character = None
player_character = None

def init_characters():

    character_list = []

    with open('characters.txt', 'r') as f:
        file_lines = f.readlines()
        f.close()
    
    for line in file_lines:
        line = line.strip("\n")
        line_items = line.split(';')
        new_character = Character(line_items[0], line_items[1], line_items[2], line_items[3].split(','), line_items[4] == 't', line_items[5] == 't', line_items[6].split(','), line_items[7] == 't', line_items[8] == 't')
        character_list.append(new_character)

    return character_list

def get_names(character_list):
    name_list = []
    for character in character_list:
        name_list.append(character.name)
    return name_list
    
def shuffle_characters(character_list):
    list_length = len(character_list)
    for i in range(5):
        for j in range(list_length):
            temp_character = character_list[j]
            random_index = int(random() * list_length)
            character_list[j] = character_list[random_index]
            character_list[random_index] = temp_character
    return character_list

def get_unflipped_characters(character_list):
    unflipped_characters = []
    for character in character_list:
        if not character.is_flipped():
            unflipped_characters.append(character.name)
    return unflipped_characters

def print_unflipped_characters(character_list):
    print_string = "\nUNFLIPPED CHARACTERS:"
    unflipped_characters = get_unflipped_characters(character_list)
    for character in unflipped_characters:
        print_string += f"\n{character}"
    print(print_string)

def player_win():
    print("Congratulations! You win!")
    exit(0)

if __name__ == "__main__":
    while True:
        character_list = init_characters()
        character_list = shuffle_characters(character_list)
        available_characters = []
        available_characters = character_list.copy()
        player = p.Player(available_characters.pop(), shuffle_characters(character_list))
        cpu = c.CPU(available_characters.pop(), shuffle_characters(character_list))
        character_list = shuffle_characters(character_list)

        while True:
            print("")
            # get user input as to what question to ask cpu, flip down characters based on result
            aspect = player.ask_question()
            if aspect == None:
                print("No recognizable trait within question, please try again.")
                continue
            cpu_has_aspect = cpu.has_aspect(player.player_input, aspect)
            if aspect == "character" and cpu_has_aspect:
                player_win()
            player.flip_matching_descs(aspect, cpu_has_aspect)
            print_unflipped_characters(player.character_list)