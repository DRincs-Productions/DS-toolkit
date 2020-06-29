image pegi_18 = "/images_tool/pegi_18.webp"

label check_age:
    show pegi_18
    "Age Verification 18+: Are you aged 18 or over?"
    menu:
        "Yes":
            hide pegi_18
            return
        "No":
            "You have to be 18+ to play this game."
            $ renpy.run(MainMenu(confirm=False))