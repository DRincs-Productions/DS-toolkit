# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default mcI = Information(name = "Liam", sname = "Johnson", age = 20, active = True, rel_status = rel.engaged, rel_partner = girl, story = "Unknown")
define mc = Character("{b}[mcI.name]{/b}", color="#37b3f3", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])

default friendI = Information(name = "Nick", sname = "Valentine", age = 26, active = True, rel_status = rel.unknown, rel_partner = "Unknown", story = "Unknown")
define friend = Character("{b}[friendI.name]{/b}", color="#37c68f", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])
default friendR = Relationship("friend", "friend", active = True)
default friendS = PartnerStats(friendship = 80, love = 0, virgin = False, bisexual = False, polyamorous = False, against = 20, addiction = 0)
image friend normal = "/friend.webp"

default girlI = Information(name = "Eileen", sname = "Fisher", age = 18, active = True, rel_status = rel.engaged, rel_partner = mc, story = "she has always been before class.")
define girl = Character("{b}[girlI.name]{/b}", color="#f337ba", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])
default girlR = Relationship("girlfriend", "boyfriend", active = True)
default girlS = PartnerStats(friendship = 40, love = 80, virgin = True, bisexual = False, polyamorous = False, against = False, addiction = 0)

# Clothes
default girl_dress = "homesuit"
label set_girl_homesuit:
    $ girl_dress = "homesuit"
    return
label set_girl_null:
    $ girl_dress = ""
    return
image girl normal = Composite( (gui.width, gui.height),
    (0, 0), "/girl.webp",
    (0, 0), "check:[girl_dress]/girl.webp")

# The game starts here.
label start:
    stop music fadeout 1.0
    call screen check_age
    "Welcome to [config.name]"
    call renaming_mc
    mc "I am ... years old"
    $ mcI.changeAge()
    "Hi [mc] ([mcI.age])"
    mc "Hi"
    show sky
    show friend normal
    show girl normal

label loop:
    menu:
        "Ads":
            menu:
                "Notifications Test":
                    $ notifyEx(msg="Hello")
                "Coming soon test":
                    call coming_soon
                "Back":
                    jump loop
        "Character":
            call character
        "Clothes":
            call clothes
        "Time":
            call time_test
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
        "End":  # This ends the game.
            call temporary_end_game
            return
    jump loop

label character:
    menu:
        "Change labels [girl]":
            "Her name is:"
            $ girlI.changeName()
            "She is my:"
            $ girlR.changeNPClabel()
            "I'm [girl]'s:"
            $ girlR.changeMClabel()
            girl "Hi my [girlR.MClabel]"
            mc "Hi my [girlR.NPClabel]"
        "Speaks [girl]":
            girl "Hi my [girlR.MClabel]"
            mc "Hi my [girlR.NPClabel]"
        "Change label [friend]":
            "His name is:"
            $ friendI.changeName()
            "He is my:"
            $ friendR.changeNPClabel()
            "I'm [friend]'s:"
            $ friendR.changeMClabel()
            friend "Hi my [friendR.MClabel]"
            mc "Hi my [friendR.NPClabel]"
        "Speaks [friend]":
            friend "Hi my [friendR.MClabel]"
            mc "Hi my [friendR.NPClabel]"
            if (friendS.is_friend()):
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
        "Get dressed [girl]" if (girl_dress != "homesuit"):
            call set_girl_homesuit
        "Take off your clothes [girl]" if (girl_dress != ""):
            call set_girl_null
        "Back":
            return
    jump clothes

label relaction1:
    menu:
        "+ Friendship [friend]. Friendship: [friendS.friendship]":
            $ friendS.changeFriendship(10)
        "- Friendship [friend]. Friendship: [friendS.friendship]":
            $ friendS.changeFriendship(-10)
        "+ Love [friend]. Love: [friendS.love]":
            $ friendS.changeLove(10)
        "- Love [friend]. Love: [friendS.love]":
            $ friendS.changeLove(-10)
        "Pag2":
            jump relaction2
        "Back":
            return
    jump relaction1
label relaction2:
    menu:
        "Pag1":
            jump relaction1
        "+ Favour [girl]. Favour: [girlS.favour]":
            $ girlS.changeFavour(10)
        "- Favour [girl]. Favour: [girlS.favour]":
            $ girlS.changeFavour(-10)
        "+ Love [girl]. Love: [girlS.love]":
            $ girlS.changeLove(10)
        "- Love [girl]. Love: [girlS.love]":
            $ girlS.changeLove(-10)
        "Pag3":
            jump relaction3
        "Back":
            return
    jump relaction2
label relaction3:
    menu:
        "Pag2":
            jump relaction2
        "+ Corruption [girl]. Corruption: [girlS.corruption]":
            $ girlS.changeCorruption(10)
        "- Corruption [girl]. Corruption: [girlS.corruption]":
            $ girlS.changeCorruption(-10)
        "+ Fear [girl]. Fear: [girlS.fear]":
            $ girlS.changeFear(10)
        "- Fear [girl]. Fear: [girlS.fear]":
            $ girlS.changeFear(-10)
        "+ Anger [girl]. Anger: [girlS.anger]":
            $ girlS.changeAnger(10)
        "- Anger [girl]. Anger: [girlS.anger]":
            $ girlS.changeAnger(-10)
        "Back":
            return
    jump relaction3

label character1:
    menu:
        "+ Energy [girl]. Energy: [girlS.energy]":
            $ girlS.changeEnergy(10)
        "- Energy [girl]. Energy: [girlS.energy]":
            $ girlS.changeEnergy(-10)
        "+ Willpower [girl]. Willpower: [girlS.willpower]":
            $ girlS.changeWillpower(10)
        "- Willpower [girl]. Willpower: [girlS.willpower]":
            $ girlS.changeWillpower(-10)
        "+ Inhibition [girl]. Inhibition: [girlS.inhibition]":
            $ girlS.changeInhibition(10)
        "- Inhibition [girl]. Inhibition: [girlS.inhibition]":
            $ girlS.changeInhibition(-10)
        "Pag2":
            jump character2
        "Back":
            return
    jump character1
label character2:
    menu:
        "Pag1":
            jump character1
        "+ Addiction [girl]. Addiction: [girlS.addiction]":
            $ girlS.changeAddiction(10)
        "- Addiction [girl]. Addiction: [girlS.addiction]":
            $ girlS.changeAddiction(-10)
        "+ Lust [girl]. Lust: [girlS.lust]":
            $ girlS.changeLust(10)
        "- Lust [girl]. Lust: [girlS.lust]":
            $ girlS.changeLust(-10)
        "Back":
            return
    jump character2

label emblem1:
    menu:
        "Set not Virgin [girl]. Virgin: True" if (girlS.is_virgin()):
            $ girlS.virgin = False
        "Set Virgin [girl]. Virgin: False" if (girlS.is_virgin() == False):
            $ girlS.virgin = True
        "Set not Bisexual [girl]. Bisexual: True" if (girlS.is_bisexual()):
            $ girlS.bisexual = False
        "Set Bisexual [girl]. Bisexual: False" if (girlS.is_bisexual() == False):
            $ girlS.bisexual = True
        "Set not Polyamorous [girl]. Polyamorous: True" if (girlS.is_polyamorous()):
            $ girlS.polyamorous = False
        "Set Polyamorous [girl]. Polyamorous: False" if (girlS.is_polyamorous() == False):
            $ girlS.polyamorous = True
        "Set Against false [girl]. Against: True" if (girlS.is_against()):
            $ girlS.against = 20
        "Set Against=0 [girl]. Against: True" if (girlS.is_against()):
            $ girlS.against = 0
        "Set Against [girl]. Against: False" if (girlS.is_against() == False):
            $ girlS.against = True
        "Set not Healthy [girl]. Healthy: True" if (girlS.is_healthy()):
            $ girlS.changeEnergy(-100)
            $ girlS.changeWillpower(-100)
            $ girlS.changeInhibition(-100)
            $ girlS.changeCorruption(100)
            $ girlS.changeAddiction(100)
        "Set Healthy [girl]. Healthy: False" if (girlS.is_healthy() == False):
            $ girlS.changeEnergy(100)
            $ girlS.changeWillpower(100)
            $ girlS.changeInhibition(100)
            $ girlS.changeCorruption(-100)
            $ girlS.changeAddiction(-100)
            $ girlS.changeFear(-50)
            $ girlS.changeLust(-50)
            $ girlS.against = False
        "Set not Unfaithful [girl]. Unfaithful: True" if (girlS.is_unfaithful()):
            $ girlS.changeWillpower(-100)
            $ girlS.changeLust(-100)
            $ girlS.changeAnger(-100)
        "Set Unfaithful [girl]. Unfaithful: False" if (girlS.is_unfaithful() == False):
            $ girlS.changeWillpower(100)
            $ girlS.changeLust(100)
            $ girlS.changeAnger(100)
        "Pag2":
            jump emblem2
        "Back":
            return
    jump emblem1
label emblem2:
    menu:
        "Pag1":
            jump emblem1
        "Set not Slut [girl]. Slut: True" if (girlS.is_slut()):
            $ girlS.changeLust(-100)
            $ girlS.changeCorruption(-100)
            $ girlS.changeAddiction(-100)
        "Set Slut [girl]. Slut: False" if (girlS.is_slut() == False):
            $ girlS.changeLust(100)
            $ girlS.changeCorruption(100)
            $ girlS.changeAddiction(100)
        "Set not Nymphomaniac [girl]. Nymphomaniac: True" if (girlS.is_nymphomaniac()):
            $ girlS.changeCorruption(-100)
            $ girlS.changeLust(-100)
            $ girlS.changeInhibition(100)
        "Set Nymphomaniac [girl]. Nymphomaniac: False" if (girlS.is_nymphomaniac() == False):
            $ girlS.changeCorruption(100)
            $ girlS.changeLust(100)
            $ girlS.changeInhibition(-100)
        "Set not Submissive [girl]. Submissive: True" if (girlS.is_submissive()):
            $ girlS.changeWillpower(100)
            $ girlS.changeFear(-100)
        "Set Submissive [girl]. Submissive: False" if (girlS.is_submissive() == False):
            $ girlS.changeWillpower(-100)
            $ girlS.changeFear(100)
        "Set not Celebrolesis [girl]. Celebrolesis: True" if (girlS.is_celebrolesis()):
            $ girlS.changeWillpower(100)
            $ girlS.changeInhibition(100)
            $ girlS.changeAddiction(-100)
        "Set Celebrolesis [girl]. Celebrolesis: False" if (girlS.is_celebrolesis() == False):
            $ girlS.changeWillpower(-100)
            $ girlS.changeInhibition(-100)
            $ girlS.changeAddiction(100)
        "Set not Free Use [girl]. Free Use: True" if (girlS.is_free_use()):
            $ girlS.changeWillpower(100)
            $ girlS.changeInhibition(100)
            $ girlS.changeFear(-100)
            $ girlS.changeLust(-100)
            $ girlS.changeCorruption(-100)
            $ girlS.changeAddiction(-100)
        "Set Free Use [girl]. Free Use: False" if (girlS.is_free_use() == False):
            $ girlS.changeWillpower(-100)
            $ girlS.changeInhibition(-100)
            $ girlS.changeFear(100)
            $ girlS.changeLust(100)
            $ girlS.changeCorruption(100)
            $ girlS.changeAddiction(100)
        "Back":
            return
    jump emblem2

label time_test:
    menu:
        "Rest":
            call new_hour
            $ test = time_handler.get_hour_name()
            "[test]"
        "Sleep":
            call new_day
            $ test = time_handler.get_weekday_name()
            "[test]"
        "Back":
            jump loop
    jump time_test
