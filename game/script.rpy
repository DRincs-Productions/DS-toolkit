# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc_name = "Unknown"
define mc = Character("{b}[mc_name]{/b}", who_color="#37b3f3")

default friendR = Relationship("Nick", "friend", "friend", True)
define friend = Character("{b}[friendR.name]{/b}", who_color="#37c68f")
default friendS = FriendStats(10)
image friend normal = "/friend.webp"

default girlR = Relationship("Eileen", "girlfriend", "boyfriend", True)
define girl = Character("{b}[girlR.name]{/b}", who_color="#f337ba")
default girlS = GirlStats(10, 0, 0, 0)
image girl normal = Composite( (gui.width, gui.height),
    (0, 0), "/girl.webp",
    (0, 0), "check:[girl_dress]/girl.webp")

# The game starts here.

label start:
    stop music fadeout 1.0
    call check_age
    "Welcome to [config.name]"
    call renaming_mc
    "Hi [mc]"
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
        "Time":
            call time_test
        "End":  # This ends the game.
            call temporary_end_game
            return
    jump loop

label character:
    menu:
        "[girl]":
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
                "Fuck you!":
                    $ girlS.changeLove(-10)
                    "Love: [girlS.love]"
                "Speaks":
                    girl "Hi my [girlR.MClabel]"
                    mc "Hi my [girlR.NPClabel]"
                "Get dressed" if (girl_dress != "homesuit"):
                    call set_girl_homesuit
                "Take off your clothes" if (girl_dress != ""):
                    call set_girl_null
                "Back":
                    jump character
        "[friend]":
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
                "Fuck you!":
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
