from random import random
from time import sleep

class Character():

    def __init__(self, name: str, gender: str, eye_color: str, hair_descs: list, hat_boolean: bool, bald_boolean: bool, facial_hair_descs: list, glasses_boolean: bool, rosy_cheeks_boolean: bool):
        self.name = name
        self.letter_gender = gender
        if gender == 'f':
            self.gender = ["female", "woman"]
        else:
            self.gender = ["male", "man"]
        self.eye_color = eye_color
        self.hair_descs = hair_descs
        self.hat_boolean = hat_boolean
        self.bald_boolean = bald_boolean
        self.facial_hair_descs = facial_hair_descs
        self.glasses_boolean = glasses_boolean
        self.rosy_cheeks_boolean = rosy_cheeks_boolean
        self.flipped_down = False

    def list(self):
        temp_list = []
        temp_list.append(self.name)
        temp_list.append(self.gender)
        temp_list.append(self.eye_color)
        temp_list.append(self.hair_descs)
        temp_list.append(self.hat_boolean)
        temp_list.append(self.bald_boolean)
        temp_list.append(self.facial_hair_descs)
        temp_list.append(self.glasses_boolean)
        temp_list.append(self.rosy_cheeks_boolean)
        return temp_list
    
    def gender_logic(self, user_input) -> bool:
        for gender in self.gender:
            if gender in user_input.split():
                return True
        return False

    def hair_logic(self, user_input) -> bool:
        for hair_desc in self.hair_descs:
            if hair_desc in user_input.split():
                return True
        return False
    
    def facial_hair_logic(self, user_input) -> bool:
        if self.facial_hair_descs == ['']:
            return False
        for facial_hair_desc in self.facial_hair_descs:
            if facial_hair_desc in user_input:
                return True
        for description in ["beard","mustache","short","long"]:
            if description in user_input:
                return False
        return True

    def check_aspect(self, user_input, aspect) -> bool:
        if aspect == "gender":
            return self.gender_logic(user_input)
        elif aspect == "eyes":
            return self.eye_color in user_input.split()
        elif aspect == "hair":
            return self.hair_logic(user_input)
        elif aspect == "hat":
            return self.hat_boolean
        elif aspect == "bald":
            return self.bald_boolean
        elif aspect == "facial hair":
            return self.facial_hair_logic(user_input)
        elif aspect == "glasses":
            return self.glasses_boolean
        elif aspect == "rosy cheeks":
            return self.rosy_cheeks_boolean
        elif aspect == "character":
            return self.name in user_input.split()
        else:
            return False

    def flip_down(self):
        print(f"[PLAYER] Flipping down {self.name}...")
        sleep(random())
        self.flipped_down = True
    def flip_up(self):
        self.flipped_down = False
    def is_flipped(self):
        return self.flipped_down