# Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Relaction#relactions-dict
define relactions = {
    "mom": __("Mom"),
    "dad": __("Dad"),
    "son": __("Son"),
    "daughter": __("Daughter"),
    "brother": __("Brother"),
    "sister": __("Sister"),
    "uncle": __("Uncle"),
    "aunt": __("Aunt"),
    "cousin": __("Cousin"),
    "friend": __("Friend"),
    "girlfriend": __("Girlfriend"),
    "boyfriend": __("Boyfriend"),
}

init python:
    # Multi Game Persistent Character Names
    # Recommended: male_fname, male_sname, female_fname, female_sname, futa_fname, futa_sname, other_fname or other_sname (or any, or all of these).
    # Other recommendations: bigsis_fname, lilsis_fname, bigbro_fname, lilbro_fname, mom_fname, dad_fname, malebff_fname or femalebff_fname. (Again, use any or use none).
    mp_ndata = MultiPersistent("namedata.f95zone.to")

    from typing import Optional
    from typing import Literal

    class CharacterInfo():
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information """

        def __init__(
                    self,
                    name: str,
                    gender: GENDER_TYPE,
                    sname:Optional[str]=None,
                    age:Optional[int]=None,
                    relationships:dict[Character, str]=None,
                    other_values:dict[Character, str]=None,
                    ):
            # I use a dictionary because it is the best solution for compatibility and not to create variables that may not be used.
            self.memory = {}
            self.memory.update(other_values if other_values else {})
            # Great for reporting that a character has not yet been discovered
            self.name = name
            self.sname = sname
            self.age = age
            # default values
            self.set("name_default", name)
            self.set("sname_default", sname)
            self.set("age_default", age)
            # default values
            self.relationships = relationships if relationships else {}

        def changeName(self) -> None:
            """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#change-name """
            self.name = renpy.input(
                "{i}(Default: " + self.get("name_default") + "){/i}")
            self.name = self.name.strip() or self.get("name_default")
            if (self.get("name_default") == "Unknown"):
                self.set("name_default", self.name)
            return

        def changeSurname(self) -> None:
            """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#change-surname """
            self.sname = renpy.input(
                "{i}(Default: " + self.get("sname_default") + "){/i}")
            self.sname = self.sname.strip() or self.get("sname_default")
            if (self.get("sname_default") == "Unknown"):
                self.set("sname_default", self.sname)
            return

        def changeAge(self) -> None:
            """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#change-age """
            self.age = renpy.input(
                "{i}(Default: " + str(self.get("age_default")) + "){/i}")
            self.age = self.age.strip() or self.get("age_default")
            if (self.get("age_default") == "Unknown"):
                self.set("age_default", self.age)
            return

        def get(self, name: str) -> str:
            """Returns the value "name", in case it does not exist returns \"Unknown\""""
            if name in self.memory:
                return self.memory[name]
            else:
                return "Unknown"

        def set(self, name: str, value) -> None:
            """Function to set or add a new value"""
            if (not IsNullOrWhiteSpace(name)):
                self.memory[name] = value
            else:
                self.remove(name)
            return

        def remove(self, name: str) -> None:
            """Delete the name value"""
            del self.memory[name]
            return

        def getRelationNameByCharacter(self, character: Character) -> Optional[str]:
            """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Relaction#get-relation-name-by-character """
            if character in self.relationships:
                return self.relationships[character]
            else:
                return None

        def setRelationNameByCharacter(self, character: Character, relation: str = None) -> None:
            """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Relaction#set-relation-name-by-character """
            if IsNullOrWhiteSpace(relation):
                value = renpy.input(self.name+" is:")
                self.relationships[character] = value
                del value
            else:
                self.relationships[character] = relation
            return

# https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#renaming_mc
label renaming_mc:
    # allow default name(s) to be saved across multiple games
    if renpy.variant("pc"):
        if mp_ndata.male_fname != None:
            $ mcI.set("name_default", mp_ndata.male_fname)
        if mp_ndata.male_sname != None:
            $ mcI.set("sname_default", mp_ndata.male_sname)

    "Player" "My name is:"
    $ mcI.changeName()
    "Player" "My surname is:"
    $ mcI.changeSurname()

    if renpy.variant("pc"):
        if mcI.name != mcI.get("name_default"):
            $ mp_ndata.male_fname = mcI.name
        if mcI.sname != mcI.get("sname_default"):
            $ mp_ndata.male_sname = mcI.sname
        $ mp_ndata.save()
    return
