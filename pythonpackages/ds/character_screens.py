import renpy.character as character

from pythonpackages.renpy_utility.utility import all_characters


def all_characters_with_screen(store) -> list[character.ADVCharacter]:
    my_list: list[character.ADVCharacter] = []
    list_c = all_characters(store)
    for ch in list_c:
        if "info_screen" in ch.who_args and isinstance(ch.who_args["info_screen"], str):
            my_list.append(ch)
    return my_list
