# Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Relaction
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

    class Information():
        """Information about a character
        to use: default ... = Information("NPC name", age)
        exemple:
        default girlI = Information("Eileen", 18, "university student" [or job.university_student if it is a registered job], rel.get('engaged'), mc,
        "she has always been before class. as a child they made fun of her because she had the appliance. ...")
        default boyI = Information("Unknown Boy")"""

        def __init__(self,
                    name,
                    sname=None,
                    age=None,
                    story=None,
                    relationships=None,
                    other_values={}):
            # I use a dictionary because it is the best solution for compatibility and not to create variables that may not be used.
            self.memory = {}
            self.memory.update(other_values)
            # Great for reporting that a character has not yet been discovered

            self.name = name
            self.sname = sname
            self.age = age
            # default values
            self.set("name_default", name)
            self.set("sname_default", sname)
            self.set("age_default", age)
            # default values
            self.relationships = relationships
            self.set("story", story)

        def changeName(self):
            """Rename character name"""
            self.name = renpy.input(
                "{i}(Default: " + self.get("name_default") + "){/i}")
            self.name = self.name.strip() or self.get("name_default")
            if (self.get("name_default") == "Unknown"):
                self.set("name_default", self.name)

        def changeSurname(self):
            """Rename the character's last name"""
            self.sname = renpy.input(
                "{i}(Default: " + self.get("sname_default") + "){/i}")
            self.sname = self.sname.strip() or self.get("sname_default")
            if (self.get("sname_default") == "Unknown"):
                self.set("sname_default", self.sname)

        def changeAge(self):
            """Age changes"""
            self.age = renpy.input(
                "{i}(Default: " + str(self.get("age_default")) + "){/i}")
            self.age = self.age.strip() or self.get("age_default")
            if (self.get("age_default") == "Unknown"):
                self.set("age_default", self.age)

        def get(self, text):
            """Returns the value "text", in case it does not exist returns \"Unknown\""""
            if text in self.memory:
                return self.memory[text]
            else:
                return "Unknown"

        def set(self, text, value):
            """Function to set or add a new value"""
            if (text != None and text != ""):
                self.memory[text] = value
            else:
                self.remove(text)

        def remove(self, text):
            """Delete the text value"""
            del self.memory[text]

        def setActive(self, amt):
            """Cabia the active value according to the parameter (Tip: True/False)"""
            self.active = amt

        def getRelationNameByCharacter(self, character: str) -> Optional[str]:
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
