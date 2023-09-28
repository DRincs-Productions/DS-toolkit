import renpy.character as character

from pythonpackages.renpy_utility.utility import all_characters


def all_characters_with_screen(store) -> dict[str, character.ADVCharacter]:
    my_dict: dict[str, character.ADVCharacter] = {}
    list_c = all_characters(store)
    for ch in list_c:
        if "info_screen" in ch.who_args and isinstance(ch.who_args["info_screen"], str):
            info_screen: str = str(ch.who_args["info_screen"])
            my_dict[info_screen] = ch
    return my_dict
