from random import random
from Character import Character

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
    i = 0
    while i < 5:
        j = 0
        while j < list_length:
            temp_character = character_list[j]
            random_index = int(random() * list_length)
            character_list[j] = character_list[random_index]
            character_list[random_index] = temp_character
            j += 1
        i += 1
    return character_list

def get_unflipped_characters(character_list):
    unflipped_characters = []
    for character in character_list:
        if not character.is_flipped():
            unflipped_characters.append(character.get_name())
    return unflipped_characters

def print_unflipped_characters(character_list):
    print_string = "\nUNFLIPPED CHARACTERS:"
    unflipped_characters = get_unflipped_characters(character_list)
    for character in unflipped_characters:
        print_string += f"\n{character}"
    print(print_string)

def flip_matching_descs(character_list, user_input, aspect):
    matches = []
    not_matches = []
    for character in character_list:
        if character.check_aspect(user_input, aspect):
            matches.append(character)
        else:
            not_matches.append(character)

    if ai_character.check_aspect(user_input, aspect):
        print("\n[CPU] Yes")
        chosen_list = not_matches
    else:
        print("\n[CPU] No")
        chosen_list = matches

    for character in chosen_list:
        if not character.is_flipped():
            character.flip_down()

if __name__ == "__main__":
    while True:
        character_list = init_characters()
        character_list = shuffle_characters(character_list)
        available_characters = []
        available_characters = character_list.copy()
        ai_character = available_characters.pop()
        player_character = available_characters.pop()
        character_list = shuffle_characters(character_list)
        # print(ai_character.list())

        while True:
            print("")
            user_input = input("[PLAYER] ")
            if "male" in user_input:
                flip_matching_descs(character_list, user_input, "gender")
            elif "eye" in user_input:
                flip_matching_descs(character_list, user_input, "eyes")
            elif "hat" in user_input:
                flip_matching_descs(character_list, user_input, "hat")
            elif "bald" in user_input:
                flip_matching_descs(character_list, user_input, "bald")
            elif "facial" in user_input or \
                "mustache" in user_input or \
                "beard" in user_input:
                flip_matching_descs(character_list, user_input, "facial hair")
            elif "hair" in user_input:
                flip_matching_descs(character_list, user_input, "hair")
            elif "glasses" in user_input:
                flip_matching_descs(character_list, user_input, "glasses")
            elif "rosy cheeks" in user_input:
                flip_matching_descs(character_list, user_input, "rosy cheeks")
            elif "restart" == user_input:
                break

            print_unflipped_characters(character_list)