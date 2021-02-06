init python:
    # Multi Game Persistent Character Names
    # Recommended: male_fname, male_sname, female_fname, female_sname, futa_fname, futa_sname, other_fname or other_sname (or any, or all of these).
    # Other recommendations: bigsis_fname, lilsis_fname, bigbro_fname, lilbro_fname, mom_fname, dad_fname, malebff_fname or femalebff_fname. (Again, use any or use none).
    mp_ndata = MultiPersistent("namedata.f95zone.to")

    class Information():
        """Information about a character
        to use: default ... = Information("NPC name", age)
        exemple:
        default girlI = Information("Eileen", 18, "university student" [or job.university_student if it is a registered job], rel.get('engaged'), mc,
        "she has always been before class. as a child they made fun of her because she had the appliance. ...")
        default boyI = Information("Unknown Boy")"""
        def __init__(self,
            name,
            sname = None,
            age = None,
            active = True,
            rel_status = None,
            rel_partner = None,
            story = None,
            other_values = {}):
            # I use a dictionary because it is the best solution for compatibility and not to create variables that may not be used.
            self.memory = {}
            self.memory.update(other_values)
            # Great for reporting that a character has not yet been discovered
            self.active = active

            self.name = name
            self.sname = sname
            self.age = age
            # default values
            self.set("name_default", name)
            self.set("sname_default", sname)
            self.set("age_default", age)
            # default values
            self.set("rel_status", rel_status)
            self.set("rel_partner", rel_partner)
            self.set("story", story)

        def changeName(self):
            """Rename character name"""
            self.name = renpy.input("{i}(Default: " + self.get("name_default") + "){/i}")
            self.name = self.name.strip() or self.get("name_default")
            if (self.get("name_default") == "Unknown"):
                self.set("name_default", self.name)
        def changeSurname(self):
            """Rename the character's last name"""
            self.sname = renpy.input("{i}(Default: " + self.get("sname_default") + "){/i}")
            self.sname = self.sname.strip() or self.get("sname_default")
            if (self.get("sname_default") == "Unknown"):
                self.set("sname_default", self.sname)
        def changeAge(self):
            """Age changes"""
            self.age = renpy.input("{i}(Default: " + str(self.get("age_default")) + "){/i}")
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
                remove(text)
        def remove(self, text):
            """Delete the text value"""
            del memory[text]
        def setActive(self, amt):
            """Cabia the active value according to the parameter (Tip: True/False)"""
            self.active = amt
        def getRelStatus(self, amt):
            """Returns the state of the character relationship (I recommend using rel values)"""
            return self.get("rel_status")
        def getRelPartner(self, amt):
            """It recalls the name of the character with whom it has a relationship"""
            return self.get("rel_partner")
        def is_engaged(self):
            """Return True if the character is currently in a romantic relationship with someone"""
            return (rel_status == rel.get('engaged') or rel_status == rel.get('married'))

    class Relationship():
        """Type fi relationship between you (MClabel) and NPC NPClabel
        to use: default ... = Relationship("type of relationship that NCP has with MC", 
        "type of relationship that MC has with NCP", boolean (if this relationship is active))
        exemple:
        default girlR = Relationship("girlfriend", "boyfriend", True)"""
        def __init__(self,
            NPClabel = None,
            MClabel = None,
            active = True):

            self.memory = {}
            # nickname by which MC calls NCP
            self.NPClabel = NPClabel
            # nickname by which NCP calls MC
            self.MClabel = MClabel
            # default values
            self.set("NPClabel_default", NPClabel)
            self.set("MClabel_default", MClabel)

            self.active = active
        def changeNPClabel(self):
            """Change the nickname of the PCN"""
            self.NPClabel = renpy.input("{i}(Default: " + self.get("NPClabel_default") + "){/i}")
            self.NPClabel = self.NPClabel.strip() or self.get("NPClabel_default")
            if (self.get("NPClabel_default") == "Unknown"):
                self.set("NPClabel_default", self.NPClabel)
        def changeMClabel(self):
            """Edit the nickname of the MC"""
            self.MClabel = renpy.input("{i}(Default: " + self.get("MClabel_default") + "){/i}")
            self.MClabel = self.MClabel.strip() or self.get("MClabel_default")
            if (self.get("MClabel_default") == "Unknown"):
                self.set("MClabel_default", self.MClabel)
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
                remove(text)
        def remove(self, text):
            """Delete the text value"""
            del memory[text]
        def setActive(self, amt):
            """Change the active value according to the parameter (Tip: True/False)"""
            self.active = amt

define rel = {
        'rel_single'    :   0,
        'rel_engaged'   :   1,
        'rel_married'   :   2,
        'rel_divorced'  :   3,
        'rel_widow'     :   4,
    }


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
