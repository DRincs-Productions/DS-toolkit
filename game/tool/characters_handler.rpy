init python:
    # Multi Game Persistent Character Names
    # Recommended: male_fname, male_sname, female_fname, female_sname, futa_fname, futa_sname, other_fname or other_sname (or any, or all of these).
    # Other recommendations: bigsis_fname, lilsis_fname, bigbro_fname, lilbro_fname, mom_fname, dad_fname, malebff_fname or femalebff_fname. (Again, use any or use none).
    mp_ndata = MultiPersistent("namedata.f95zone.to")

    class Relationships():
        def __init__(self):
            self.unknown = 0
            self.single = 1
            self.engaged = 2
            self.married = 3
            self.divorced = 4
            self.widow = 5
    ## Information about a character
    # to use: default ... = Information("NPC name", age)
    # exemple:
    # default girlI = Information("Eileen", 18, "university student" [or job.university_student if it is a registered job], rel.engaged, mc,
    # "she has always been before class. as a child they made fun of her because she had the appliance. ...")
    # default boyI = Information("Unknown Boy", "Unknown", job.unknown, rel.unknown, "Unknown", "Unknown")
    class Information():
        def __init__(self, name, sname, age, active, rel_status, rel_partner, story):
            self.name_default = name
            self.name = name
            self.sname_default = sname
            self.sname = sname
            self.age_default = age
            self.age = age
            self.active = active
            self.rel_status = rel_status
            self.rel_partner = rel_partner
            self.story = story
        def changeName(self):
            self.name = renpy.input("{i}(Default: " + self.name_default + "){/i}")
            self.name = self.name.strip() or self.name_default
        def changeSurname(self):
            self.sname = renpy.input("{i}(Default: " + self.sname_default + "){/i}")
            self.sname = self.sname.strip() or self.sname_default
        def changeAge(self):
            self.age = renpy.input("{i}(Default: " + str(self.age_default) + "){/i}")
            self.age = self.age.strip() or self.age_default
        def is_engaged(self):
            return (rel_status == rel.engaged or rel_status == rel.married)
        def setActive(self, amt):
            self.active = amt
    ## Type of relationship
    # to use: default ... = Relationship("type of relationship that NCP has with MC", 
    # "type of relationship that MC has with NCP", boolean (if this relationship is active))
    # exemple:
    # default girlR = Relationship("girlfriend", "boyfriend", True)
    class Relationship():
        def __init__(self, NPClabel, MClabel, active):
            self.NPClabel_default = NPClabel
            self.NPClabel = NPClabel
            self.MClabel_default = MClabel
            self.MClabel = MClabel
            self.active = active
        def changeNPClabel(self):
            self.NPClabel = renpy.input("{i}(Default: " + self.NPClabel_default + "){/i}")
            self.NPClabel = self.NPClabel.strip() or self.NPClabel_default
        def changeMClabel(self):
            self.MClabel = renpy.input("{i}(Default: " + self.MClabel_default + "){/i}")
            self.MClabel = self.MClabel.strip() or self.MClabel_default
        def setActive(self, amt):
            self.active = amt

define rel = Relationships()

label renaming_mc:
    # allow default name(s) to be saved across multiple games
    if renpy.variant("pc"):
        if mp_ndata.male_fname != None:
            $ mcI.name_default = mp_ndata.male_fname
        if mp_ndata.male_sname != None:
            $ mcI.sname_default = mp_ndata.male_sname

    "Player" "My name is:"
    $ mcI.changeName()
    "Player" "My surname is:"
    $ mcI.changeSurname()

    if renpy.variant("pc"):
        if mcI.name != mcI.name_default:
            $ mp_ndata.male_fname = mcI.name
        if mcI.sname != mcI.sname_default:
            $ mp_ndata.male_sname = mcI.sname
        $ mp_ndata.save()
    return
