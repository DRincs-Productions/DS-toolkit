init python:
    ## Type of relationship
    # to use: default ... = RelationshipType("...", "...", "...")
    class RelationshipType():
        def __init__(self, name, NPClabel, MClabel):
            self.name_default = name
            self.name = name
            self.NPClabel_default = NPClabel
            self.NPClabel = NPClabel
            self.MClabel_default = MClabel
            self.MClabel = MClabel
        def changeName(self):
            n = ""
            n = renpy.input("(Default: " + self.name_default + ")")
            n = n.strip()
            if n != "":
                self.name = n
        def changeNPClabel(self):
            n = ""
            n = renpy.input("(Default: " + self.NPClabel_default + ")")
            n = n.strip()
            if n != "":
                self.NPClabel = n
        def changeMClabel(self):
            n = ""
            n = renpy.input("(Default: " + self.MClabel_default + ")")
            n = n.strip()
            if n != "":
                self.MClabel = n

label renaming_mc:
    "Player" "My name is:"
    $ name = ""
    $ name = renpy.input("(Default: Liam)")
    $ name = name.strip()
    if name == "":
        $ mc_name = "Liam"
    else:
        $ mc_name = name
    hide profile
    return
