init python:
    class Relationships():
        def __init__(self):
            self.unknown = 0
            self.single = 1
            self.engaged = 2
            self.married = 3
            self.divorced = 4
            self.widow = 5
    class Job():
        def __init__(self):
            self.unknown = 0
            self.unemployed = 1
            self.programmer = 2
            self.university_student = 3
            # here you can add your favorite works
    ## Information about a character
    # to use: default ... = Information("NPC name", age)
    # exemple:
    # default girlI = Information("Eileen", 18, "university student" [or job.university_student if it is a registered job], Relationships.engaged, mc,
    # "she has always been before class. as a child they made fun of her because she had the appliance. ...")
    # default boyI = Information("Unknown Boy", "Unknown", job.unknown, relationships.unknown, "Unknown", "Unknown")
    class Information():
        def __init__(self, name, age, active, job, relationship_status, relationship_partner, story):
            self.name_default = name
            self.name = name
            self.age_default = age
            self.age = age
            self.active = active
            self.job = job
            self.relationship_status = relationship_status
            self.relationship_partner = relationship_partner
            self.story = story
        def changeName(self):
            val = ""
            val = renpy.input("(Default: " + self.name_default + ")")
            val = val.strip()
            if val != "":
                self.name = val
        def changeAge(self):
            val = ""
            val = renpy.input("(Default: " + str(self.age_default) + ")")
            val = val.strip()
            if val != "":
                self.age = val
        def is_engaged(self):
            return (relationship_status == relationships.engaged or relationship_status == relationships.married)
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
            val = ""
            val = renpy.input("(Default: " + self.NPClabel_default + ")")
            val = val.strip()
            if val != "":
                self.NPClabel = val
        def changeMClabel(self):
            val = ""
            val = renpy.input("(Default: " + self.MClabel_default + ")")
            val = val.strip()
            if val != "":
                self.MClabel = val
        def setActive(self, amt):
            self.active = amt

define relationships = Relationships()
define job = Job()

label renaming_mc:
    "Player" "My name is:"
    $ mcI.changeName()
    return
