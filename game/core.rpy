define config.log = "log.txt"

label after_load:
    # renpy-utility-lib
    call update_current_flags(update_dictionary = True)
    return
