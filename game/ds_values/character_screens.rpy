define gui.userinfo_lateralframe_ypos = convert_to_int(150 * gui.dr_multiplicateur)
define gui.userinfo_lateralframe_xpos = convert_to_int(1050 * gui.dr_multiplicateur)
define gui.userinfo_lateralframe_xsize = convert_to_int(300 * gui.dr_multiplicateur) + gui.ds_userinfo_textdistance_xsize
define gui.userinfo_lateralframe_ysize = convert_to_int(900 * gui.dr_multiplicateur)
define gui.userinfo_vbox_xpos = convert_to_int(45 * gui.dr_multiplicateur)
define gui.userinfo_area = (0, 0, convert_to_int(525 * gui.dr_multiplicateur), convert_to_int(30 * gui.dr_multiplicateur))

screen base_character_info(cur_character_info, cur_character_statistic = None, cur_character_sentimental = None):
    frame:
        ypos gui.userinfo_lateralframe_ypos
        xpos gui.userinfo_lateralframe_xpos
        xsize gui.userinfo_lateralframe_xsize
        ysize gui.userinfo_lateralframe_ysize
        background None
        viewport mousewheel True draggable True id 'vp3':
            has vbox spacing 5
            if cur_character_info:
                # Start Space
                frame area gui.userinfo_area:
                    background None

                vbox:
                    xpos gui.userinfo_vbox_xpos
                    use menu_userinfo_character_info(cur_character_info)
                    
                    if cur_character_statistic:
                        use menu_userinfo_character_statistic(_("Statistic:"), cur_character_statistic)

                    if cur_character_sentimental:
                        use menu_userinfo_character_statistic(_("Sentimental:"), cur_character_sentimental)

                # End Space
                frame area gui.userinfo_area:
                    background None

        vbar value YScrollValue('vp3') style 'dr_menu_vscroll'

screen mc_character_info():
    imagebutton:
        align (0.33, 1)
        idle 'mc normal'

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
