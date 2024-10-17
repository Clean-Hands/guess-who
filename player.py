import re

class Player():

    chosen_character = None
    character_list = None
    player_input = None

    def __init__(self, chosen_character: str, character_list: list):
        self.chosen_character = chosen_character
        self.character_list = character_list

    def flip_matching_descs(self, aspect, cpu_has_aspect):
        matches = []
        not_matches = []
        for character in self.character_list:
            if character.check_aspect(self.player_input, aspect):
                matches.append(character)
            else:
                not_matches.append(character)

        # if the opponent has the aspect we asked about,
        # flip down all characters that don't have that aspect
        if cpu_has_aspect:
            to_flip = not_matches
        else:
            to_flip = matches

        for character in to_flip:
            if not character.is_flipped():
                character.flip_down()

    def ask_question(self) -> str:
        # get a question from the user, removing punction and making it lowercase
        self.player_input = re.sub(r"[^\w\s]", "", input("[PLAYER] ")).lower()

        # determine which trait the user is asking about 
        if "man" in self.player_input or \
            "male" in self.player_input: # matches: man, woman, male, female
            return "gender"
        elif "eye" in self.player_input:
            return "eyes"
        elif "hat" in self.player_input:
            return "hat"
        elif "bald" in self.player_input:
            return "bald"
        elif "facial" in self.player_input or \
            "mustache" in self.player_input or \
            "beard" in self.player_input:
            return "facial hair"
        elif "hair" in self.player_input:
            return "hair"
        elif "glasses" in self.player_input:
            return "glasses"
        elif "rosy cheeks" in self.player_input:
            return "rosy cheeks"
        else:
            # check if the user guessed a specific character
            for character in self.character_list:
                if character.name.lower() in self.player_input:
                    return "character"
            return None