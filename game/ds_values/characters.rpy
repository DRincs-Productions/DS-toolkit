# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -10 python:
    from pythonpackages.ds.character_info import CharacterInfo
    from pythonpackages.ds.character_type import GenderEnum

init -1:
    default mcI = CharacterInfo(
        name = "Liam", surname = "Johnson", age = 20, gender = GenderEnum.MALE,
        other_values = {},
        relationships = {
            girl : "girlfriend",
            friend : "friend",
        }
    )
    define mc = Character("{b}[mcI.name]{/b}",
        icon = None,
        info_screen = "mc_character_info",
        color = "#37b3f3", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )

    default friendI = CharacterInfo(
        name = "Nick", surname = "Valentine", age = 26, gender = GenderEnum.MALE,
        other_values = {},
        relationships = {
            mc : relactions["friend"],
        }
    )
    define friend = Character("{b}[friendI.name] C.J.{/b}",
        icon = None,
        info_screen = "friend_character_info",
        color = "#37c68f", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )

    default girlI = CharacterInfo(
        name = "Eileen", surname = "Fisher", age = 18, gender = GenderEnum.FEMALE,
        other_values ={
            "story": __("She has always been before class.")
        },
        relationships = {
            mc : "boyfriend",
        }
    )
    define girl = Character("{b}[girlI.name]{/b}",
        icon = None,
        info_screen = "girl_character_info",
        color = "#f337ba", who_outlines = [(2,"#000000")], what_prefix = "", what_suffix = "", what_outlines = [(2,"#000000")]
    )

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
