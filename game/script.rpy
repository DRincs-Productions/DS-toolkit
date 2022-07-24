# The script of the game goes in this file.

image bg blue = "#b1e3ff"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default mcI = Information(name = "Liam", sname = "Johnson", age = 20, relationships = {
    girl : relactions["girlfriend"],
    friend : relactions["friend"],
})
define mc = Character("{b}[mcI.name]{/b}", color="#37b3f3", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])

default friendI = Information(name = "Nick", sname = "Valentine", age = 26, relationships = {
    mc : relactions["friend"],
})
define friend = Character("{b}[friendI.name] C.J.{/b}", color="#37c68f", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])
image friend normal = "/friend.webp"

default girlI = Information(name = "Eileen", sname = "Fisher", age = 18, story = __("She has always been before class."), relationships = {
    mc : relactions["boyfriend"],
})
define girl = Character("{b}[girlI.name]{/b}", color="#f337ba", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])

# Clothes
default girl_dress = "-homesuit"
label set_girl_homesuit:
    $ girl_dress = "-homesuit"
    return
label set_girl_null:
    $ girl_dress = ""
    return
image girl normal = "check:girl[girl_dress].webp"

# The game starts here.
label start:
    "Welcome to [config.name]"
    call renaming_mc
    mc "I am ... years old"
    $ mcI.changeAge()
    "Hi [mc] ([mcI.age])"
    mc "Hi"
    scene bg blue with fade
    show friend normal at left
    show girl normal at right

label loop:
    menu:
        "Notifications Test":
            $ notifyEx(msg="Hello")
        "Character":
            call character
        "Clothes":
            call clothes
        "Timed menu":
            "Train boxing."
            show screen countdown(timer_range=5, timer_call='menu_slow')
            menu:
                "Attacks":
                    hide screen countdown
                    "You punched."
                "Defend":
                    hide screen countdown
                    "You defended yourself."
                "Do nothing":
                    hide screen countdown
                    "You didn't do anything."
        "Ability":
            call ability
        "End":  # This ends the game.
            return
    jump loop

label character:
    menu:
        "Change labels [girl]":
            "Her name is:"
            $ girlI.changeName()
            "She is my:"
            $ girlI.setRelationNameByCharacter(character= mc)
            "I'm [girl]'s:"
            $ mcI.setRelationNameByCharacter(character= girl)
            $ relaction = mcI.getRelationNameByCharacter(girl)
            girl "Hi my [relaction]"
            $ relaction = mcI.getRelationNameByCharacter(girl)
            mc "Hi my [relaction]"
        "Speaks [girl]":
            $ relaction = mcI.getRelationNameByCharacter(girl)
            girl "Hi my [relaction]"
            $ relaction = mcI.getRelationNameByCharacter(girl)
            mc "Hi my [relaction]"
        "Change label [friend]":
            "His name is:"
            $ friendI.changeName()
            "He is my:"
            $ friendI.setRelationNameByCharacter(character= mc)
            "I'm [friend]'s:"
            $ mcI.setRelationNameByCharacter(character= friend)
            $ relaction = mcI.getRelationNameByCharacter(friend)
            friend "Hi my [relaction]"
            $ relaction = friendI.getRelationNameByCharacter(mc)
            mc "Hi my [relaction]"
        "Speaks [friend]":
            $ relaction = mcI.getRelationNameByCharacter(friend)
            friend "Hi my [relaction]"
            $ relaction = friendI.getRelationNameByCharacter(mc)
            mc "Hi my [relaction]"
            if (stats["friend"].is_friend()):
                friend "We are friends"
            else:
                friend "We are not friends"
        "Relaction":
            call relaction1
        "Characteristics":
            call character1
        "Emblem":
            call emblem1
        "Back":
            jump loop
    jump character

label clothes:
    menu:
        "Get dressed [girl]" if (girl_dress != "-homesuit"):
            call set_girl_homesuit
        "Take off your clothes [girl]" if (girl_dress != ""):
            call set_girl_null
        "Back":
            return
    jump clothes

label relaction1:
    $ ffr = stats["friend"].get("friendship")
    $ flov = stats["friend"].get("love")
    menu:
        "+ Friendship [friend]. Friendship: [ffr]":
            $ stats["friend"].changeFriendship(10)
        "- Friendship [friend]. Friendship: [ffr]":
            $ stats["friend"].changeFriendship(-10)
        "+ Love [friend]. Love: [flov]":
            $ stats["friend"].changeLove(10)
        "- Love [friend]. Love: [flov]":
            $ stats["friend"].changeLove(-10)
        "Pag2":
            jump relaction2
        "Back":
            return
    jump relaction1
label relaction2:
    $ gfr = stats["girl"].get("favour")
    $ glov = stats["girl"].get("love")
    menu:
        "Pag1":
            jump relaction1
        "+ Favour [girl]. Favour: [gfr]":
            $ stats["girl"].changeFavour(10)
        "- Favour [girl]. Favour: [gfr]":
            $ stats["girl"].changeFavour(-10)
        "+ Love [girl]. Love: [glov]":
            $ stats["girl"].changeLove(10)
        "- Love [girl]. Love: [glov]":
            $ stats["girl"].changeLove(-10)
        "Pag3":
            jump relaction3
        "Back":
            return
    jump relaction2
label relaction3:
    $ gcor = stats["girl"].get("corruption")
    $ gfe = stats["girl"].get("fear")
    $ gan = stats["girl"].get("anger")
    menu:
        "Pag2":
            jump relaction2
        "+ Corruption [girl]. Corruption: [gcor]":
            $ stats["girl"].changeCorruption(10)
        "- Corruption [girl]. Corruption: [gcor]":
            $ stats["girl"].changeCorruption(-10)
        "+ Fear [girl]. Fear: [gfe]":
            $ stats["girl"].changeFear(10)
        "- Fear [girl]. Fear: [gfe]":
            $ stats["girl"].changeFear(-10)
        "+ Anger [girl]. Anger: [gan]":
            $ stats["girl"].changeAnger(10)
        "- Anger [girl]. Anger: [gan]":
            $ stats["girl"].changeAnger(-10)
        "Back":
            return
    jump relaction3

label character1:
    $ gen = stats["girl"].get("energy")
    $ gwi = stats["girl"].get("willpower")
    $ ginh = stats["girl"].get("inhibition")
    menu:
        "+ Energy [girl]. Energy: [gen]":
            $ stats["girl"].changeEnergy(10)
        "- Energy [girl]. Energy: [gen]":
            $ stats["girl"].changeEnergy(-10)
        "+ Willpower [girl]. Willpower: [gwi]":
            $ stats["girl"].changeWillpower(10)
        "- Willpower [girl]. Willpower: [gwi]":
            $ stats["girl"].changeWillpower(-10)
        "+ Inhibition [girl]. Inhibition: [ginh]":
            $ stats["girl"].changeInhibition(10)
        "- Inhibition [girl]. Inhibition: [ginh]":
            $ stats["girl"].changeInhibition(-10)
        "Pag2":
            jump character2
        "Back":
            return
    jump character1
label character2:
    $ gad = stats["girl"].get("addiction")
    $ glu = stats["girl"].get("lust")
    menu:
        "Pag1":
            jump character1
        "+ Addiction [girl]. Addiction: [gad]":
            $ stats["girl"].changeAddiction(10)
        "- Addiction [girl]. Addiction: [gad]":
            $ stats["girl"].changeAddiction(-10)
        "+ Lust [girl]. Lust: [glu]":
            $ stats["girl"].changeLust(10)
        "- Lust [girl]. Lust: [glu]":
            $ stats["girl"].changeLust(-10)
        "Back":
            return
    jump character2

label emblem1:
    menu:
        "Set not Virgin [girl]. Virgin: True" if (stats["girl"].is_virgin()):
            $ stats["girl"].set("virgin", False)
        "Set Virgin [girl]. Virgin: False" if (stats["girl"].is_virgin() == False):
            $ stats["girl"].set("virgin", True)
        "Set not Bisexual [girl]. Bisexual: True" if (stats["girl"].is_bisexual()):
            $ stats["girl"].set("bisexual", False)
        "Set Bisexual [girl]. Bisexual: False" if (stats["girl"].is_bisexual() == False):
            $ stats["girl"].set("bisexual", True)
        "Set not Polyamorous [girl]. Polyamorous: True" if (stats["girl"].is_polyamorous()):
            $ stats["girl"].set("polyamorous", False)
        "Set Polyamorous [girl]. Polyamorous: False" if (stats["girl"].is_polyamorous() == False):
            $ stats["girl"].set("polyamorous", True)
        "Set Against false [girl]. Against: True" if (stats["girl"].is_against()):
            $ stats["girl"].set("against", 20)
        "Set Against=0 [girl]. Against: True" if (stats["girl"].is_against()):
            $ stats["girl"].set("against", 0)
        "Set Against [girl]. Against: False" if (stats["girl"].is_against() == False):
            $ stats["girl"].set("against", True)
        "Set not Healthy [girl]. Healthy: True" if (stats["girl"].is_healthy()):
            $ stats["girl"].changeEnergy(-100)
            $ stats["girl"].changeWillpower(-100)
            $ stats["girl"].changeInhibition(-100)
            $ stats["girl"].changeCorruption(100)
            $ stats["girl"].changeAddiction(100)
        "Set Healthy [girl]. Healthy: False" if (stats["girl"].is_healthy() == False):
            $ stats["girl"].changeEnergy(100)
            $ stats["girl"].changeWillpower(100)
            $ stats["girl"].changeInhibition(100)
            $ stats["girl"].changeCorruption(-100)
            $ stats["girl"].changeAddiction(-100)
            $ stats["girl"].changeFear(-50)
            $ stats["girl"].changeLust(-50)
            $ stats["girl"].against = False
        "Set not Unfaithful [girl]. Unfaithful: True" if (stats["girl"].is_unfaithful()):
            $ stats["girl"].changeWillpower(-100)
            $ stats["girl"].changeLust(-100)
            $ stats["girl"].changeAnger(-100)
        "Set Unfaithful [girl]. Unfaithful: False" if (stats["girl"].is_unfaithful() == False):
            $ stats["girl"].changeWillpower(100)
            $ stats["girl"].changeLust(100)
            $ stats["girl"].changeAnger(100)
        "Pag2":
            jump emblem2
        "Back":
            return
    jump emblem1
label emblem2:
    menu:
        "Pag1":
            jump emblem1
        "Set not Slut [girl]. Slut: True" if (stats["girl"].is_slut()):
            $ stats["girl"].changeLust(-100)
            $ stats["girl"].changeCorruption(-100)
            $ stats["girl"].changeAddiction(-100)
        "Set Slut [girl]. Slut: False" if (stats["girl"].is_slut() == False):
            $ stats["girl"].changeLust(100)
            $ stats["girl"].changeCorruption(100)
            $ stats["girl"].changeAddiction(100)
        "Set not Nymphomaniac [girl]. Nymphomaniac: True" if (stats["girl"].is_nymphomaniac()):
            $ stats["girl"].changeCorruption(-100)
            $ stats["girl"].changeLust(-100)
            $ stats["girl"].changeInhibition(100)
        "Set Nymphomaniac [girl]. Nymphomaniac: False" if (stats["girl"].is_nymphomaniac() == False):
            $ stats["girl"].changeCorruption(100)
            $ stats["girl"].changeLust(100)
            $ stats["girl"].changeInhibition(-100)
        "Set not Submissive [girl]. Submissive: True" if (stats["girl"].is_submissive()):
            $ stats["girl"].changeWillpower(100)
            $ stats["girl"].changeFear(-100)
        "Set Submissive [girl]. Submissive: False" if (stats["girl"].is_submissive() == False):
            $ stats["girl"].changeWillpower(-100)
            $ stats["girl"].changeFear(100)
        "Set not Celebrolesis [girl]. Celebrolesis: True" if (stats["girl"].is_celebrolesis()):
            $ stats["girl"].changeWillpower(100)
            $ stats["girl"].changeInhibition(100)
            $ stats["girl"].changeAddiction(-100)
        "Set Celebrolesis [girl]. Celebrolesis: False" if (stats["girl"].is_celebrolesis() == False):
            $ stats["girl"].changeWillpower(-100)
            $ stats["girl"].changeInhibition(-100)
            $ stats["girl"].changeAddiction(100)
        "Set not Free Use [girl]. Free Use: True" if (stats["girl"].is_free_use()):
            $ stats["girl"].changeWillpower(100)
            $ stats["girl"].changeInhibition(100)
            $ stats["girl"].changeFear(-100)
            $ stats["girl"].changeLust(-100)
            $ stats["girl"].changeCorruption(-100)
            $ stats["girl"].changeAddiction(-100)
        "Set Free Use [girl]. Free Use: False" if (stats["girl"].is_free_use() == False):
            $ stats["girl"].changeWillpower(-100)
            $ stats["girl"].changeInhibition(-100)
            $ stats["girl"].changeFear(100)
            $ stats["girl"].changeLust(100)
            $ stats["girl"].changeCorruption(100)
            $ stats["girl"].changeAddiction(100)
        "Back":
            return
    jump emblem2

label ability:
    $ MCint = stats["mc"].get("intelligence")
    $ MCstr = stats["mc"].get("strength")
    $ FRint = stats["friend"].get("intelligence")
    $ FRstr = stats["friend"].get("strength")
    menu:
        "Train":
            $ stats["mc"].improve_ability("strength")
        "Study":
            $ stats["mc"].improve_ability("intelligence")
        "Popeye: [mc]([MCstr]) vs [friend]([FRstr])":
            if MCstr > FRstr:
                "You have won"
            else:
                "You lost"
        "Quiz: [mc]([MCint]) vs [friend]([FRint])":
            if MCint > FRint:
                "You have won"
            else:
                "You lost"
        "Back":
            return
    jump ability
