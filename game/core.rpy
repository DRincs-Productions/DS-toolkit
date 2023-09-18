define config.log = "log.txt"

label after_load:
    $ update_flags()
    return

init python:
    def myrollback():
        ui.add(renpy.Keymap(rollback=If(renpy.get_screen('menu_userinfo'), NullAction(), Rollback())))

    config.overlay_functions.append(myrollback)
