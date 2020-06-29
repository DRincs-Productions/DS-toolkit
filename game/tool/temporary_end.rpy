image to_be_continued = "/images_tool/to_be_continued.webp"

# Temporary end of the story (then play other stories)
label temporary_end_story:
    "This is the temporary end (current version: [config.version]). You'll have to wait new update."
    "If you want more updates, support me on {a=https://www.patreon.com/}Patreon"
    return

# Temporary end of the game
label temporary_end_game:
    show to_be_continued
    call temporary_end_story
    $ old_version = config.version
    "Save the game now and not later."
    $ ShowMenu('save')()

    if (old_version == config.version):
        "Pressing ENTER will return to the Main Menu."
        $ renpy.run(MainMenu(confirm=False))
    hide to_be_continued
    return

# Coming soon text
label coming_soon:
    "(Coming soon)"
    "Support me on {a=https://www.patreon.com/}Patreon"
    return