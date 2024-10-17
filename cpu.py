from random import random

class CPU():

    def __init__(self, chosen_character: str, character_list: list):
        self.chosen_character = chosen_character
        self.character_list = character_list

    def has_aspect(self, player_input, aspect) -> bool:
        if self.chosen_character.check_aspect(player_input, aspect):
            print("\n[CPU] Yes")
            return True
        else:
            print("\n[CPU] No")
            return False