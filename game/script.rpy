# The script of the game goes in this file.

image bg blue = "#b1e3ff"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init 10 python:
    from pythonpackages.ds.character_info import CharacterInfo


default mcI = CharacterInfo(name = "Liam", sname = "Johnson", age = 20, gender = "M",
relationships = {
    girl : relactions["girlfriend"],
    friend : relactions["friend"],
})
define mc = Character("{b}[mcI.name]{/b}", color="#37b3f3", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])

default friendI = CharacterInfo(name = "Nick", sname = "Valentine", age = 26, gender = "M",
relationships = {
    mc : relactions["friend"],
})
define friend = Character("{b}[friendI.name] C.J.{/b}", color="#37c68f", who_outlines=[(2,"#000000")], what_prefix="\"", what_suffix="\"", what_outlines=[(2,"#000000")])
image friend normal = "/friend.webp"

default girlI = CharacterInfo(name = "Eileen", sname = "Fisher", age = 18, gender = "F",
other_values ={
    "story": __("She has always been before class.")
}, 
relationships = {
    mc : relactions["boyfriend"],
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
default girlSentimental = SentimentalStatistic(gender_attracted = "M", virgin = True)
default friendSentimental = SentimentalStatistic(gender_attracted = "F", virgin = False, against = 20)

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
    call enable_notifyEx

label loop:
    menu:
        "Screens":
            call screen menu_userinfo()
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
            if (friendSentimental.isFriend()):
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
    $ ffr = friendSentimental.get("friendship")
    $ flov = friendSentimental.get("love")
    menu:
        "+ Friendship [friend]. Friendship: [ffr]":
            $ friendSentimental.improveFriendship(10)
        "- Friendship [friend]. Friendship: [ffr]":
            $ friendSentimental.improveFriendship(-10)
        "+ Love [friend]. Love: [flov]":
            $ friendSentimental.improveLove(10)
        "- Love [friend]. Love: [flov]":
            $ friendSentimental.improveLove(-10)
        "Pag2":
            jump relaction2
        "Back":
            return
    jump relaction1
label relaction2:
    $ gfr = girlSentimental.get("favour")
    $ glov = girlSentimental.get("love")
    menu:
        "Pag1":
            jump relaction1
        "+ Favour [girl]. Favour: [gfr]":
            $ girlSentimental.improveFavour(10)
        "- Favour [girl]. Favour: [gfr]":
            $ girlSentimental.improveFavour(-10)
        "+ Love [girl]. Love: [glov]":
            $ girlSentimental.improveLove(10)
        "- Love [girl]. Love: [glov]":
            $ girlSentimental.improveLove(-10)
        "Pag3":
            jump relaction3
        "Back":
            return
    jump relaction2
label relaction3:
    $ gcor = girlSentimental.get("corruption")
    $ gfe = girlSentimental.get("fear")
    $ gan = girlSentimental.get("anger")
    menu:
        "Pag2":
            jump relaction2
        "+ Corruption [girl]. Corruption: [gcor]":
            $ girlSentimental.improveCorruption(10)
        "- Corruption [girl]. Corruption: [gcor]":
            $ girlSentimental.improveCorruption(-10)
        "+ Fear [girl]. Fear: [gfe]":
            $ girlSentimental.improveFear(10)
        "- Fear [girl]. Fear: [gfe]":
            $ girlSentimental.improveFear(-10)
        "+ Anger [girl]. Anger: [gan]":
            $ girlSentimental.improveAnger(10)
        "- Anger [girl]. Anger: [gan]":
            $ girlSentimental.improveAnger(-10)
        "Back":
            return
    jump relaction3

label character1:
    $ gen = girlSentimental.get("energy")
    $ gwi = girlSentimental.get("willpower")
    $ ginh = girlSentimental.get("inhibition")
    menu:
        "+ Energy [girl]. Energy: [gen]":
            $ girlSentimental.improveEnergy(10)
        "- Energy [girl]. Energy: [gen]":
            $ girlSentimental.improveEnergy(-10)
        "+ Willpower [girl]. Willpower: [gwi]":
            $ girlSentimental.improveWillpower(10)
        "- Willpower [girl]. Willpower: [gwi]":
            $ girlSentimental.improveWillpower(-10)
        "+ Inhibition [girl]. Inhibition: [ginh]":
            $ girlSentimental.improveInhibition(10)
        "- Inhibition [girl]. Inhibition: [ginh]":
            $ girlSentimental.improveInhibition(-10)
        "Pag2":
            jump character2
        "Back":
            return
    jump character1
label character2:
    $ gad = girlSentimental.get("addiction")
    $ glu = girlSentimental.get("lust")
    menu:
        "Pag1":
            jump character1
        "+ Addiction [girl]. Addiction: [gad]":
            $ girlSentimental.improveAddiction(10)
        "- Addiction [girl]. Addiction: [gad]":
            $ girlSentimental.improveAddiction(-10)
        "+ Lust [girl]. Lust: [glu]":
            $ girlSentimental.improveLust(10)
        "- Lust [girl]. Lust: [glu]":
            $ girlSentimental.improveLust(-10)
        "Back":
            return
    jump character2

label emblem1:
    menu:
        "Set not Virgin [girl]. Virgin: True" if (girlSentimental.isVirgin()):
            $ girlSentimental.set("virgin", False)
        "Set Virgin [girl]. Virgin: False" if (girlSentimental.isVirgin() == False):
            $ girlSentimental.set("virgin", True)
        "Set not Bisexual [girl]. Bisexual: True" if (girlSentimental.isBisexual()):
            $ girlSentimental.set("bisexual", False)
        "Set Bisexual [girl]. Bisexual: False" if (girlSentimental.isBisexual() == False):
            $ girlSentimental.set("bisexual", True)
        "Set not Polyamorous [girl]. Polyamorous: True" if (girlSentimental.isPolyamorous()):
            $ girlSentimental.set("polyamorous", False)
        "Set Polyamorous [girl]. Polyamorous: False" if (girlSentimental.isPolyamorous() == False):
            $ girlSentimental.set("polyamorous", True)
        "Set Against false [girl]. Against: True" if (girlSentimental.isAgainst()):
            $ girlSentimental.set("against", 20)
        "Set Against=0 [girl]. Against: True" if (girlSentimental.isAgainst()):
            $ girlSentimental.set("against", 0)
        "Set Against [girl]. Against: False" if (girlSentimental.isAgainst() == False):
            $ girlSentimental.set("against", True)
        "Set not Healthy [girl]. Healthy: True" if (girlSentimental.isHealthy()):
            $ girlSentimental.improveEnergy(-100)
            $ girlSentimental.improveWillpower(-100)
            $ girlSentimental.improveInhibition(-100)
            $ girlSentimental.improveCorruption(100)
            $ girlSentimental.improveAddiction(100)
        "Set Healthy [girl]. Healthy: False" if (girlSentimental.isHealthy() == False):
            $ girlSentimental.improveEnergy(100)
            $ girlSentimental.improveWillpower(100)
            $ girlSentimental.improveInhibition(100)
            $ girlSentimental.improveCorruption(-100)
            $ girlSentimental.improveAddiction(-100)
            $ girlSentimental.improveFear(-50)
            $ girlSentimental.improveLust(-50)
            $ girlSentimental.against = False
        "Set not Unfaithful [girl]. Unfaithful: True" if (girlSentimental.isUnfaithful()):
            $ girlSentimental.improveWillpower(-100)
            $ girlSentimental.improveLust(-100)
            $ girlSentimental.improveAnger(-100)
        "Set Unfaithful [girl]. Unfaithful: False" if (girlSentimental.isUnfaithful() == False):
            $ girlSentimental.improveWillpower(100)
            $ girlSentimental.improveLust(100)
            $ girlSentimental.improveAnger(100)
        "Pag2":
            jump emblem2
        "Back":
            return
    jump emblem1
label emblem2:
    menu:
        "Pag1":
            jump emblem1
        "Set not Slut [girl]. Slut: True" if (girlSentimental.isSlut()):
            $ girlSentimental.improveLust(-100)
            $ girlSentimental.improveCorruption(-100)
            $ girlSentimental.improveAddiction(-100)
        "Set Slut [girl]. Slut: False" if (girlSentimental.isSlut() == False):
            $ girlSentimental.improveLust(100)
            $ girlSentimental.improveCorruption(100)
            $ girlSentimental.improveAddiction(100)
        "Set not Nymphomaniac [girl]. Nymphomaniac: True" if (girlSentimental.isNymphomaniac()):
            $ girlSentimental.improveCorruption(-100)
            $ girlSentimental.improveLust(-100)
            $ girlSentimental.improveInhibition(100)
        "Set Nymphomaniac [girl]. Nymphomaniac: False" if (girlSentimental.isNymphomaniac() == False):
            $ girlSentimental.improveCorruption(100)
            $ girlSentimental.improveLust(100)
            $ girlSentimental.improveInhibition(-100)
        "Set not Submissive [girl]. Submissive: True" if (girlSentimental.isSubmissive()):
            $ girlSentimental.improveWillpower(100)
            $ girlSentimental.improveFear(-100)
        "Set Submissive [girl]. Submissive: False" if (girlSentimental.isSubmissive() == False):
            $ girlSentimental.improveWillpower(-100)
            $ girlSentimental.improveFear(100)
        "Set not Celebrolesis [girl]. Celebrolesis: True" if (girlSentimental.isCelebrolesis()):
            $ girlSentimental.improveWillpower(100)
            $ girlSentimental.improveInhibition(100)
            $ girlSentimental.improveAddiction(-100)
        "Set Celebrolesis [girl]. Celebrolesis: False" if (girlSentimental.isCelebrolesis() == False):
            $ girlSentimental.improveWillpower(-100)
            $ girlSentimental.improveInhibition(-100)
            $ girlSentimental.improveAddiction(100)
        "Set not Free Use [girl]. Free Use: True" if (girlSentimental.isFreeUse()):
            $ girlSentimental.improveWillpower(100)
            $ girlSentimental.improveInhibition(100)
            $ girlSentimental.improveFear(-100)
            $ girlSentimental.improveLust(-100)
            $ girlSentimental.improveCorruption(-100)
            $ girlSentimental.improveAddiction(-100)
        "Set Free Use [girl]. Free Use: False" if (girlSentimental.isFreeUse() == False):
            $ girlSentimental.improveWillpower(-100)
            $ girlSentimental.improveInhibition(-100)
            $ girlSentimental.improveFear(100)
            $ girlSentimental.improveLust(100)
            $ girlSentimental.improveCorruption(100)
            $ girlSentimental.improveAddiction(100)
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
