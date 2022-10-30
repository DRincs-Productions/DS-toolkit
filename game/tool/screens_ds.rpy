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

define ds_translations = {
    "gender_attracted"      :   _("Sexuality"),
    "friendship"            :   _("Friendship"),
    "favour"                :   _("Favour"),
    "love"                  :   _("Love"),
    "corruption"            :   _("Corruption"),
    "virgin"                :   _("Virgin"),
    "bisexual"              :   _("Bisexual"),
    "polyamorous"           :   _("Polyamorous"),
    "against"               :   _("Against"),
    "addiction"             :   _("Addiction"),
    "max_values"            :   _("Max_values"),
    "strength"              :   _("Strength"),
    "intelligence"          :   _("Intelligence"),
    "agility"               :   _("Agility"),
}

screen menu_userinfo():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    modal True
    style_prefix "game_menu"
    add "gui/overlay/game_menu.png"

    frame area (150, 70, 350, 50) background None:
        text _("{b}Characters{/b}") color gui.accent_color size gui.name_text_size

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
        ysize gui.lateralframescroll_ysize
        background None
        # task title list
        viewport mousewheel 'change' draggable True id 'vp1':
            has vbox spacing 5
            # TODO: add a scrollbar: https://github.com/DRincs-Productions/DS-toolkit/wiki/Screen-&-Translations
        # scroll bar
        vbar value YScrollValue('vp1') style 'menu_vscroll'

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
        viewport mousewheel 'change' draggable True id 'vp3':
            has vbox spacing 5
            if cur_character_info:
                # Start Space
                frame area (0, 0, 350, 20):
                    background None

                vbox:
                    xpos 30
                    hbox xfill True:
                        frame xsize gui.userinfo_textdistance_xsize background None:
                            text _("Name:") size gui.label_text_size color gui.accent_color
                        frame xfill True background None:
                            text "[cur_character_info.name] [cur_character_info.sname]" size gui.label_text_size

                    if cur_character_info.age:
                        hbox xfill True:
                            frame xsize gui.userinfo_textdistance_xsize background None:
                                text _("Age:") size gui.label_text_size color gui.accent_color
                            frame xfill True background None:
                                text "[cur_character_info.age]" size gui.label_text_size

                    if cur_character_info.relationships and len(cur_character_info.relationships) > 0:
                        frame area (0, 0, 350, 25):
                            background None
                        frame xsize 300 background None:
                            text _("Relationships:") size gui.name_text_size
                        for ch in cur_character_info.relationships.keys():
                            $ relationship_name = cur_character_info.relationships[ch]
                            hbox xfill True:
                                frame xsize gui.userinfo_textdistance_xsize background None:
                                    text "[relationship_name]:" size gui.label_text_size color gui.accent_color
                                frame xfill True background None:
                                    text "[ch]" size gui.label_text_size

                    if cur_character_statistic:
                        $ statistic_memory = cur_character_statistic.getAll()
                        $ max_value = cur_character_statistic.getDefaultMaxValue()
                        if len(statistic_memory) > 0:
                            frame area (0, 0, 350, 25):
                                background None
                            frame xsize 300 background None:
                                text _("Statistic:") size gui.name_text_size
                            for stat in statistic_memory.keys():
                                $ value = statistic_memory[stat]
                                if stat in ds_translations:
                                    $ stat = ds_translations[stat]
                                hbox xfill True:
                                    frame xsize gui.userinfo_textdistance_xsize background None:
                                        text _("[stat]:") size gui.label_text_size color gui.accent_color
                                    frame xfill True background None:
                                        text "[value]" size gui.label_text_size

                    if cur_character_sentimental:
                        $ sentimental_memory = cur_character_sentimental.getAll()
                        if len(sentimental_memory) > 0:
                            frame area (0, 0, 350, 25):
                                background None
                            frame xsize 300 background None:
                                text _("Sentimental:") size gui.name_text_size
                            for sent in sentimental_memory.keys():
                                $ value = sentimental_memory[sent]
                                if sent == "gender_attracted" and cur_character_info:
                                    if cur_character_info.gender == "M" and value == "M":
                                        $ value = _("Gay")
                                    elif cur_character_info.gender == "F" and value == "F":
                                        $ value = _("Lesbo")
                                    elif not cur_character_info.gender == value:
                                        $ value = _("Straight")
                                if sent in ds_translations:
                                    $ sent = ds_translations[sent]
                                hbox xfill True:
                                    frame xsize gui.userinfo_textdistance_xsize background None:
                                        text _("[sent]:") size gui.label_text_size color gui.accent_color
                                    frame xfill True background None:
                                        text "[value]" size gui.label_text_size

                # End Space
                frame area (0, 0, 350, 20):
                    background None

        vbar value YScrollValue('vp3') style 'menu_vscroll'

    key 'K_ESCAPE' action Hide('menu_userinfo')
    key 'mouseup_3' action Hide('menu_userinfo')
