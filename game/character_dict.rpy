init -1 python:
    from pythonpackages.renpy_utility.character_custom import DRCharacter

init 9:
    # Wiki: https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Character-Disct
    define character_dict = {
        "mc"        :   DRCharacter(character = mc, icon = "", info_screen = "mc_character_info"),
        "girl"      :   DRCharacter(character = girl, icon = "", info_screen = "girl_character_info"),
        "friend"    :   DRCharacter(character = friend, icon = "", info_screen = "friend_character_info"),
    }
