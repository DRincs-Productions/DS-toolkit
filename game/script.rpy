# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc_name = "Unknown"
define mc = Character("{b}[mc_name]{/b}", who_color="#37b3f3")

default friendR = Relationship("Nick", "friend", "friend", True)
define friend = Character("{b}[friendR.name]{/b}", who_color="#37c68f")
default friendS = FriendStats(10)

default girlR = Relationship("Eileen", "girlfriend", "boyfriend", True)
define girl = Character("{b}[girlR.name]{/b}", who_color="#f337ba")
default girlS = GirlStats(10, 0, 0, 0, 0, 0, 0, 0)

# The game starts here.

label start:
    stop music fadeout 1.0
    call check_age
    "Welcome to [config.name]"
    call renaming_mc
    "Hi [mc]"
    mc "Hi"

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
        "End":  # This ends the game.
            call temporary_end_game
            return
    jump loop

label character:
    menu:
        "Girl":
            menu:
                "Change labels":
                    "Her name is:"
                    $ girlR.changeName()
                    "She is my:"
                    $ girlR.changeNPClabel()
                    "I'm [girl]'s:"
                    $ girlR.changeMClabel()
                    girl "Hi my [girlR.MClabel]"
                    mc "Hi my [girlR.NPClabel]"
                "I love you":
                    $ girlS.changeLove(10)
                    "Love: [girlS.love]"
                "Fuck you":
                    $ girlS.changeLove(-10)
                    "Love: [girlS.love]"
                "Speaks":
                    girl "Hi my [girlR.MClabel]"
                    mc "Hi my [girlR.NPClabel]"
                "Back":
                    jump character
        "Friend":
            menu:
                "Change label":
                    "His name is:"
                    $ friendR.changeName()
                    "He is my:"
                    $ friendR.changeNPClabel()
                    "I'm [friend]'s:"
                    $ friendR.changeMClabel()
                    friend "Hi my [friendR.MClabel]"
                    mc "Hi my [friendR.NPClabel]"
                "Give me five":
                    $ friendS.change(10)
                    "Friendship: [friendS.friendship]"
                "Fuck you":
                    $ friendS.change(-10)
                    "Friendship: [friendS.friendship]"
                "Speaks":
                    friend "Hi my [friendR.MClabel]"
                    mc "Hi my [friendR.NPClabel]"
                    if (friendS.is_friend()):
                        friend "We are friends"
                    else:
                        friend "We are not friends"
                "Back":
                    jump character
        "Back":
            jump loop
    jump character