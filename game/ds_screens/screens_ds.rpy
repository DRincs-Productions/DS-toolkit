# character selected in the menu
default cur_character_id = None
default cur_character_info = None
default cur_character_statistic = None
default cur_character_sentimental = None

define gui.userinfo_textdistance_xsize = 250
define gui.userinfo_lateralframe_ypos = 100
define gui.userinfo_lateralframe_xpos = 700
define gui.userinfo_lateralframe_ysize = 600
define gui.userinfo_lateralframe_xsize = 200 + gui.userinfo_textdistance_xsize


init -10 python:
    from pythonpackages.ds.character_type import GenderEnum

screen menu_userinfo():

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
        ypos gui.nqtr_menu_memo_ypos
        xpos gui.nqtr_menu_memo_xpos
        ysize gui.nqtr_menu_memo_ysize
        xsize gui.nqtr_menu_memo_xsize
        background None
        # task title list
        viewport mousewheel True draggable True id 'menu_userinfo_task_title_list':
            has vbox
            spacing 5
            # MC
            button:
                xpos 30
                xsize 390
                background None
                xpadding 0
                ypadding 0
                xmargin 0
                ymargin 0
                textbutton "[mc]":
                    action [
                        SetVariable('cur_character_id', "mc"),
                        SetVariable('cur_character_info', mcI),
                        SetVariable('cur_character_statistic', mcStatistic),
                        SetVariable('cur_character_sentimental', None),
                    ]
                    selected cur_character_id == "mc"
            # Girl
            button:
                xpos 30
                xsize 390
                background None
                xpadding 0
                ypadding 0
                xmargin 0
                ymargin 0
                textbutton "[girl]":
                    action [
                        SetVariable('cur_character_id', "girl"),
                        SetVariable('cur_character_info', girlI),
                        SetVariable('cur_character_statistic', None),
                        SetVariable('cur_character_sentimental', girlSentimental),
                    ]
                    selected cur_character_id == "girl"
            # Friend
            button:
                xpos 30
                xsize 390
                background None
                xpadding 0
                ypadding 0
                xmargin 0
                ymargin 0
                textbutton "[friend]":
                    action [
                        SetVariable('cur_character_id', "friend"),
                        SetVariable('cur_character_info', friendI),
                        SetVariable('cur_character_statistic', friendStatistic),
                        SetVariable('cur_character_sentimental', friendSentimental),
                    ]
                    selected cur_character_id == "friend"
        # scroll bar
        vbar value YScrollValue('menu_userinfo_task_title_list') style 'dr_menu_vscroll'

    # Image
    if cur_character_id == "friend":
        imagebutton:
            align (0.33, 1)
            idle 'friend normal'
    elif cur_character_id == "girl":
        imagebutton:
            align (0.33, 1)
            idle 'girl normal'

    frame:
        ypos 100
        xpos gui.userinfo_lateralframe_xpos
        xsize gui.userinfo_lateralframe_xsize
        ysize gui.userinfo_lateralframe_ysize
        background None
        viewport mousewheel True draggable True id 'vp3':
            has vbox spacing 5
            if cur_character_info:
                # Start Space
                frame area (0, 0, 350, 20):
                    background None

                vbox:
                    xpos 30
                    use menu_userinfo_character_info(cur_character_info)
                    
                    if cur_character_statistic:
                        use menu_userinfo_character_statistic(_("Statistic:"), cur_character_statistic)

                    if cur_character_sentimental:
                        use menu_userinfo_character_statistic(_("Sentimental:"), cur_character_sentimental)

                # End Space
                frame area (0, 0, 350, 20):
                    background None

        vbar value YScrollValue('vp3') style 'dr_menu_vscroll'

    key 'K_ESCAPE' action Hide('menu_userinfo')
    key 'mouseup_3' action Hide('menu_userinfo')
