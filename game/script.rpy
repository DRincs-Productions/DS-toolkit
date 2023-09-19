# The script of the game goes in this file.

image bg blue = "#b1e3ff"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -10 python:
    from pythonpackages.ds.character_info import CharacterInfo
    from pythonpackages.ds.character_type import GenderEnum


default mcI = CharacterInfo(name = "Liam", surname = "Johnson", age = 20, gender = GenderEnum.MALE,
relationships = {
    girl : "girlfriend",
    friend : "friend",
})
define mc = Character("{b}[mcI.name]{/b}", color="#37b3f3", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])

default friendI = CharacterInfo(name = "Nick", surname = "Valentine", age = 26, gender = GenderEnum.MALE,
relationships = {
    mc : relactions["friend"],
})
define friend = Character("{b}[friendI.name] C.J.{/b}", color="#37c68f", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])
image friend normal = "/friend.webp"

default girlI = CharacterInfo(name = "Eileen", surname = "Fisher", age = 18, gender = GenderEnum.FEMALE,
other_values ={
    "story": __("She has always been before class.")
},
relationships = {
    mc : "boyfriend",
})
define girl = Character("{b}[girlI.name]{/b}", color="#f337ba", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])

# Statistic
default mcStatistic = Statistic()
default friendStatistic = Statistic(
    values= {
        "strength"      :   7,
        "intelligence"  :   7,
        "agility"       :   7,
    }
)

# statsSentimental
default girlSentimental = SentimentalStatistic(virgin = True, love = 10)
default friendSentimental = SentimentalStatistic(virgin = False, against = 20)

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
            call screen menu_userinfo(character_dict)
        "Character":
            call character
        "Clothes (To move)":
            call clothes
        "Timed menu (To move)":
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
        "Set not Unfaithful [girl]. Unfaithful: True" if (girlSentimental.is_unfaithful):
            $ girlSentimental.is_unfaithful = False
        "Set Unfaithful [girl]. Unfaithful: False" if (not girlSentimental.is_unfaithful):
            $ girlSentimental.is_unfaithful = True
        "Pag2":
            jump emblem2
        "Back":
            return
    jump emblem1
label emblem2:
    menu:
        "Pag1":
            jump emblem1
        "Set not Slut [girl]. Slut: True" if (girlSentimental.is_slut):
            $ girlSentimental.is_slut = False
        "Set Slut [girl]. Slut: False" if (not girlSentimental.is_slut):
            $ girlSentimental.is_slut = True
        "Set not Nymphomaniac [girl]. Nymphomaniac: True" if (girlSentimental.is_nymphomaniac):
            $ girlSentimental.is_nymphomaniac = False
        "Set Nymphomaniac [girl]. Nymphomaniac: False" if (not girlSentimental.is_nymphomaniac):
            $ girlSentimental.is_nymphomaniac = True
        "Set not Submissive [girl]. Submissive: True" if (girlSentimental.is_submissive):
            $ girlSentimental.is_submissive = False
        "Set Submissive [girl]. Submissive: False" if (not girlSentimental.is_submissive):
            $ girlSentimental.is_submissive = True
        "Set not Celebrolesis [girl]. Celebrolesis: True" if (girlSentimental.is_celebrolesis):
            $ girlSentimental.is_celebrolesis = False
        "Set Celebrolesis [girl]. Celebrolesis: False" if (not girlSentimental.is_celebrolesis):
            $ girlSentimental.is_celebrolesis = True
        "Set not Free Use [girl]. Free Use: True" if (girlSentimental.is_free_use):
            $ girlSentimental.is_free_use = False
        "Set Free Use [girl]. Free Use: False" if (not girlSentimental.is_free_use):
            $ girlSentimental.is_free_use = True
        "Back":
            return
    jump emblem2

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
