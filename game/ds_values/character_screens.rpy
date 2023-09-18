define gui.userinfo_textdistance_xsize = 250
define gui.userinfo_lateralframe_ypos = 100
define gui.userinfo_lateralframe_xpos = 700
define gui.userinfo_lateralframe_ysize = 600
define gui.userinfo_lateralframe_xsize = 200 + gui.userinfo_textdistance_xsize

screen base_character_info(cur_character_info, cur_character_statistic = None, cur_character_sentimental = None):
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

screen mc_character_info():
    use base_character_info(mcI, mcStatistic)

screen girl_character_info():
    imagebutton:
        align (0.33, 1)
        idle 'girl normal'

    use base_character_info(girlI, None, girlSentimental)

screen friend_character_info():
    imagebutton:
        align (0.33, 1)
        idle 'friend normal'

    use base_character_info(friendI, friendStatistic, friendSentimental)
