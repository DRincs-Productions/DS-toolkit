define config.log = "log.txt"

label after_load:
    $ flags = updateFlags(flags, flag_keys)
    return

init python:
    def myrollback():
        ui.add(renpy.Keymap(rollback=If(renpy.get_screen('menu_userinfo'), NullAction(), Rollback())))

    config.overlay_functions.append(myrollback)
