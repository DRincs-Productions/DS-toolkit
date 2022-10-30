# character selected in the menu
default cur_character_id = None
default cur_character_info = None

default chars = {}

screen menu_userinfo():
    add 'interface phon'
    style_prefix 'userinfo' tag menu

    frame area (150, 95, 350, 50) background None:
        text _("ПЕРСОНАЖИ") color gui.accent_color size 28 #font 'hermes.ttf'

    # button for closure
    imagebutton:
        align (0.95, 0.05)
        idle '/interface/button/close_idle.webp'
        action [
            Hide('menu_userinfo'),
        ]
        if renpy.variant("pc"):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_mobile

    frame:
        ypos 170
        xpos 80
        xsize 400
        ysize 850
        background None
        # task title list
        viewport mousewheel 'change' draggable True id 'vp1':
            has vbox spacing 5
            # MC
            button:
                xpos 30
                xsize 390
                background None
                action [
                    SetVariable('cur_character_id', "mc"),
                    SetVariable('cur_character_info', mcI)
                ]
                xpadding 0
                ypadding 0
                xmargin 0
                ymargin 0
                textbutton "[mc]":
                    action [
                        SetVariable('cur_character_id', "mc"),
                        SetVariable('cur_character_info', mcI),
                    ]
                    selected cur_character_id == "mc"
            # Girl
            button:
                xpos 30
                xsize 390
                background None
                action [
                    SetVariable('cur_character_id', "girl"),
                    SetVariable('cur_character_info', girlI)
                ]
                xpadding 0
                ypadding 0
                xmargin 0
                ymargin 0
                textbutton "[girl]":
                    action [
                        SetVariable('cur_character_id', "girl"),
                        SetVariable('cur_character_info', girlI),
                    ]
                    selected cur_character_id == "girl"
            # Friend
            button:
                xpos 30
                xsize 390
                background None
                action [
                    SetVariable('cur_character_id', "friend"),
                    SetVariable('cur_character_info', friendI)
                ]
                xpadding 0
                ypadding 0
                xmargin 0
                ymargin 0
                textbutton "[friend]":
                    action [
                        SetVariable('cur_character_id', "friend"),
                        SetVariable('cur_character_info', friendI),
                    ]
                    selected cur_character_id == "friend"
        # scroll bar
        vbar value YScrollValue('vp1') style 'menu_vscroll'

    hbox pos (450, 150) spacing 30:
        # hbox ypos 25 xsize 190 spacing 5:
        #     viewport mousewheel 'change' draggable True id 'vp':
        #         has vbox spacing 5
        #         button background None action SetVariable('cur_character_info', 'max') xsize 180:
        #             textbutton _("Макс") action SetVariable('cur_character_info', 'max') selected cur_character_info == 'max' text_selected_color gui.text_color
        #             foreground 'interface marker'
        #         for char in sorted(chars.keys()):
        #             button background None action SetVariable('cur_character_info', char) xsize 180:
        #                 textbutton chars[char].name action SetVariable('cur_character_info', char) selected cur_character_info == char text_selected_color gui.text_color
        #                 foreground 'interface marker'
        #     vbar value YScrollValue('vp') style 'info_vscroll'

        # add 'Max info '+"mgg.clothes.casual.GetCur().info" size (550, 900) xpos -50 ypos 10

        viewport area (0, 30, 880, 800):
            # has vbox spacing 20
            # frame xsize 850 background None:
            #     if cur_character_id == 'max':
            #         text "mgg.desc" size 24 justify True first_indent 30
            #     else:
            #         text renpy.config.say_menu_text_filter(renpy.translate_string(chars[cur_character_id].desc)) size 24 justify True

            hbox pos (20, 0) xsize 810 spacing 5:
                viewport mousewheel 'change' draggable True id 'vp3':
                    has vbox spacing 5
                    frame xfill True background None:
                        if cur_character_id:
                            vbox spacing -1:
                                # for char in sorted(chars.keys()):

                                #     hbox xfill True:
                                #         frame xsize 350 background None:
                                #             $ char_name = chars[char].name_4
                                #             text _("Отношения с [char_name!t]:") size 24 color gui.accent_color
                                #         frame xfill True background None:
                                #             if char != 'eric':
                                #                 text GetRelMax(char)[1] size 24
                                #             else:
                                #                 text get_rel_eric()[1] size 24
                                frame area (0, 0, 350, 25):
                                    background None

                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Запас сил:") size 24 color gui.accent_color
                                    frame xfill True background None:
                                        text str(round(1, 1))+"%" size 24

                                frame area (0, 0, 350, 25):
                                    background None
                                frame xsize 350 background None:
                                    text _("Навыки:") size 26 #font 'trebucbd.ttf'
                                hbox xfill True:
                                    frame xsize 350 background None:
                                        text _("Навык убеждения:") size 24 color gui.accent_color
                                    frame xfill True background None:
                                        text str(round(1*10, 1)) size 24

                vbar value YScrollValue('vp3') style 'info_vscroll'

    key 'K_ESCAPE' action Jump('AfterWaiting')
    key 'mouseup_3' action Jump('AfterWaiting')
