init -1 python:
    from pythonpackages.renpy_utility.character_custom import DRCharacter

init 9:
    # Wiki: https://github.com/DRincs-Productions/renpy-utility-lib/wiki/Character-Disct
    define character_dict = {
        "mc"        :   DRCharacter(character = mc, icon = ""),
        "girl"      :   DRCharacter(character = girl, icon = ""),
        "friend"    :   DRCharacter(character = friend, icon = ""),
    }
