# The script of the game goes in this file.

image bg blue = "#b1e3ff"

# Clothes
default girl_dress = "-homesuit"
label set_girl_homesuit:
    $ girl_dress = "-homesuit"
    return
label set_girl_null:
    $ girl_dress = ""
    return
image girl normal = "check:girl[girl_dress].webp"
image friend normal = "/friend.webp"

# The game starts here.
label start:
    "Welcome to [config.name]"
    call renaming_mc(mcI)
    mc "I am ... years old"
    $ mcI.changeAge()
    "Hi [mc] ([mcI.age])"
    mc "Hi"
    scene bg blue with fade
    show friend normal at left
    show girl normal at right
    call enable_notifyEx

label loop:
    menu:
        "Screens":
            call screen menu_userinfo([ Return() ])
        "Character":
            call character
        "Clothes (To move)":
            call clothes
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
            "I am for [girl], his..."
            $ girlI.setRelationNameByCharacter(character = mc, default_relation_key = "boyfriend", relaction_types = relactions)
            "She is my..."
            $ mcI.setRelationNameByCharacter(character = girl, default_relation_key = "girlfriend", relaction_types = relactions)
            $ relaction = girlI.getRelationNameByCharacter(character = mc, relaction_types = relactions)
            girl "Hi my [relaction]"
            $ relaction = mcI.getRelationNameByCharacter(character = girl, relaction_types = relactions)
            mc "Hi my [relaction]"
        "Speaks [girl]":
            $ relaction = girlI.getRelationNameByCharacter(character = mc, relaction_types = relactions)
            girl "Hi my [relaction]"
            $ relaction = mcI.getRelationNameByCharacter(character = girl, relaction_types = relactions)
            mc "Hi my [relaction]"
        "Change label [friend]":
            "His name is:"
            $ friendI.changeName()
            "I am for [friend], his..."
            $ friendI.setRelationNameByCharacter(character = mc, default_relation_key = "friend", relaction_types = relactions)
            "He is my..."
            $ mcI.setRelationNameByCharacter(character= friend, default_relation_key = "friend", relaction_types = relactions)
            $ relaction = mcI.getRelationNameByCharacter(character = friend, relaction_types = relactions)
            friend "Hi my [relaction]"
            $ relaction = friendI.getRelationNameByCharacter(character = mc, relaction_types = relactions)
            mc "Hi my [relaction]"
        "Speaks [friend]":
            $ relaction = mcI.getRelationNameByCharacter(character = friend, relaction_types = relactions)
            friend "Hi my [relaction]"
            $ relaction = friendI.getRelationNameByCharacter(character = mc, relaction_types = relactions)
            mc "Hi my [relaction]"
            if (friendSentimental.is_friend):
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
    menu:
        "+ Friendship [friend]. Friendship: [friendSentimental.friendship]":
            $ friendSentimental.friendship += 10
        "- Friendship [friend]. Friendship: [friendSentimental.friendship]":
            $ friendSentimental.friendship -= 10
        "+ Love [friend]. Love: [friendSentimental.love]":
            $ friendSentimental.love += 10
        "- Love [friend]. Love: [friendSentimental.love]":
            $ friendSentimental.love -= 10
        "Pag2":
            jump relaction2
        "Back":
            return
    jump relaction1
label relaction2:
    menu:
        "Pag1":
            jump relaction1
        "+ Favour [girl]. Favour: [girlSentimental.favour]":
            $ girlSentimental.favour += 10
        "- Favour [girl]. Favour: [girlSentimental.favour]":
            $ girlSentimental.favour -= 10
        "+ Love [girl]. Love: [girlSentimental.love]":
            $ girlSentimental.love += 10
        "- Love [girl]. Love: [girlSentimental.love]":
            $ girlSentimental.love -= 10
        "Pag3":
            jump relaction3
        "Back":
            return
    jump relaction2
label relaction3:
    menu:
        "Pag2":
            jump relaction2
        "+ Corruption [girl]. Corruption: [girlSentimental.corruption]":
            $ girlSentimental.corruption += 10
        "- Corruption [girl]. Corruption: [girlSentimental.corruption]":
            $ girlSentimental.corruption -= 10
        "+ Fear [girl]. Fear: [girlSentimental.fear]":
            $ girlSentimental.fear += 10
        "- Fear [girl]. Fear: [girlSentimental.fear]":
            $ girlSentimental.fear -= 10
        "+ Anger [girl]. Anger: [girlSentimental.anger]":
            $ girlSentimental.anger += 10
        "- Anger [girl]. Anger: [girlSentimental.anger]":
            $ girlSentimental.anger -= 10
        "Back":
            return
    jump relaction3

label character1:
    menu:
        "+ Energy [girl]. Energy: [girlSentimental.energy]":
            $ girlSentimental.energy += 10
        "- Energy [girl]. Energy: [girlSentimental.energy]":
            $ girlSentimental.energy -= 10
        "+ Willpower [girl]. Willpower: [girlSentimental.willpower]":
            $ girlSentimental.willpower += 10
        "- Willpower [girl]. Willpower: [girlSentimental.willpower]":
            $ girlSentimental.willpower -= 10
        "+ Inhibition [girl]. Inhibition: [girlSentimental.inhibition]":
            $ girlSentimental.inhibition += 10
        "- Inhibition [girl]. Inhibition: [girlSentimental.inhibition]":
            $ girlSentimental.inhibition -= 10
        "Pag2":
            jump character2
        "Back":
            return
    jump character1
label character2:
    menu:
        "Pag1":
            jump character1
        "+ Addiction [girl]. Addiction: [girlSentimental.addiction]":
            $ girlSentimental.addiction += 10
        "- Addiction [girl]. Addiction: [girlSentimental.addiction]":
            $ girlSentimental.addiction -= 10
        "+ Lust [girl]. Lust: [girlSentimental.lust]":
            $ girlSentimental.lust += 10
        "- Lust [girl]. Lust: [girlSentimental.lust]":
            $ girlSentimental.lust -= 10
        "Back":
            return
    jump character2

label emblem1:
    menu:
        "Set not Virgin [girl]. Virgin: True" if (girlSentimental.is_virgin):
            $ girlSentimental.is_virgin = False
        "Set Virgin [girl]. Virgin: False" if (not girlSentimental.is_virgin):
            $ girlSentimental.is_virgin = True
        "Set not Against false [girl]. Against: True" if (girlSentimental.is_against):
            $ girlSentimental.is_against = False
        "Set Against [girl]. Against: False" if (not girlSentimental.is_against):
            $ girlSentimental.is_against = True
        "Set not Healthy [girl]. Healthy: True" if (girlSentimental.is_healthy):
            $ girlSentimental.is_healthy = False
        "Set Healthy [girl]. Healthy: False" if (not girlSentimental.is_healthy):
            $ girlSentimental.is_healthy = True
        "Back":
            return
    jump emblem1

label ability:
    $ MCint = mcStatistic.get("intelligence")
    $ MCstr = mcStatistic.get("strength")
    $ FRint = friendStatistic.get("intelligence")
    $ FRstr = friendStatistic.get("strength")
    menu:
        "Train":
            $ mcStatistic.improve("strength")
        "Study":
            $ mcStatistic.improve("intelligence")
        "Popeye: [mc]([MCstr]) vs [friend]([FRstr])":
            if isGreaterThan(MCstr, FRstr):    # MCstr > FRstr
                "You have won"
            else:
                "You lost"
        "Quiz: [mc]([MCint]) vs [friend]([FRint])":
            if isGreaterThan(MCint, FRint):     #MCint > FRint:
                "You have won"
            else:
                "You lost"
        "Back":
            return
    jump ability
