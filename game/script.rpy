# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default mcI = Information("Liam", 20, "Unknown", relationships.engaged, girl, "Unknown")
define mc = Character("{b}[mcI.name]{/b}", who_color="#37b3f3")

default friendI = Information("Nick", 26, "Unknown", relationships.unknown, "Unknown", "Unknown")
define friend = Character("{b}[friendI.name]{/b}", who_color="#37c68f")
default friendR = Relationship("friend", "friend", True)
default friendS = FriendStats(10)
image friend normal = "/friend.webp"

default girlI = Information("Eileen", 18, "university student", relationships.engaged, mc, "she has always been before class.")
define girl = Character("{b}[girlI.name]{/b}", who_color="#f337ba")
default girlR = Relationship("girlfriend", "boyfriend", True)
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
        "[girl]":
            menu:
                "Change labels":
                    "Her name is:"
                    $ girlI.changeName()
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
                    $ friendI.changeName()
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
