# character selected in the menu
default ds_cur_character = None
default ds_cur_character_screen = None

init -10 python:
    from pythonpackages.ds.character_type import GenderEnum

screen menu_userinfo(character_dict):

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    modal True
    style_prefix "game_menu"
    add "gui/overlay/game_menu.png"

    use menu_tile(_("Characters"))

    # button for closure
    use close_button('menu_userinfo')

    frame:
        ypos gui.dr_drawer_ypos
        xpos gui.dr_drawer_xpos
        ysize gui.dr_drawer_ysize
        xsize gui.dr_drawer_xsize
        background None
        # task title list
        viewport mousewheel True draggable True id 'menu_userinfo_task_title_list':
            has vbox
            spacing 5
            # for into dictioanry to get key and value
            for ch_id, value in character_dict.items():
                if value.info_screen:
                    button:
                        xpos 30
                        xsize 390
                        background None
                        xpadding 0
                        ypadding 0
                        xmargin 0
                        ymargin 0
                        textbutton "[value.character]":
                            action [
                                SetVariable('ds_cur_character', ch_id),
                                SetVariable('ds_cur_character_screen', value.info_screen),
                            ]
                            selected ds_cur_character == ch_id

        # scroll bar
        vbar value YScrollValue('menu_userinfo_task_title_list') style 'dr_menu_vscroll'
    
    # character info
    if ds_cur_character_screen:
        use expression ds_cur_character_screen

    key 'K_ESCAPE' action Hide('menu_userinfo')
    key 'mouseup_3' action Hide('menu_userinfo')
