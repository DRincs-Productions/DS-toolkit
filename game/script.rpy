# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc_name = "Unknown"
define mc = Character("{b}[mc_name]{/b}", who_color="#37b3f3")

default friendRT = RelationshipType("Nick", "friend", "friend")
define friend = Character("{b}[friendRT.name]{/b}", who_color="#37c68f")
default friendR = Friendship(10)

default girlRT = RelationshipType("Eileen", "girlfriend", "boyfriend")
define girl = Character("{b}[girlRT.name]{/b}", who_color="#f337ba")
default girlR = Relationship(10, 0, 0, 0, 0, 0, 0, 0)

# The game starts here.

label start:
    stop music fadeout 1.0
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
                        $ girlRT.changeName()
                        "She is my:"
                        $ girlRT.changeNPClabel()
                        "I'm [girl]'s:"
                        $ girlRT.changeMClabel()
                        girl "Hi my [girlRT.MClabel]"
                        mc "Hi my [girlRT.NPClabel]"
                "I love you":
                    $ girlR.changeLove(10)
                    "Love: [girlR.love]"
                "Fuck you":
                    $ girlR.changeLove(-10)
                    "Love: [girlR.love]"
                "Speaks":
                    girl "Hi my [girlRT.MClabel]"
                    mc "Hi my [girlRT.NPClabel]"
                "Back":
                    jump character
        "Friend":
            menu:
                "Change label":
                        "His name is:"
                        $ friendRT.changeName()
                        "He is my:"
                        $ friendRT.changeNPClabel()
                        "I'm [friend]'s:"
                        $ friendRT.changeMClabel()
                        friend "Hi my [friendRT.MClabel]"
                        mc "Hi my [friendRT.NPClabel]"
                "Give me five":
                    $ friendR.changeFriendship(10)
                    "Friendship: [friendR.friendship]"
                "Fuck you":
                    $ friendR.changeFriendship(-10)
                    "Friendship: [friendR.friendship]"
                "Speaks":
                    friend "Hi my [friendRT.MClabel]"
                    mc "Hi my [friendRT.NPClabel]"
                    if (friendR.is_friend()):
                        friend "We are friends"
                    else:
                        friend "We are not friends"
                "Back":
                    jump character
        "Back":
            jump loop
    jump character