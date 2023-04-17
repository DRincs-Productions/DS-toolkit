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
        viewport mousewheel True draggable True id 'vp1':
            has vbox spacing 5
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
        viewport mousewheel True draggable True id 'vp3':
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

                    if cur_character_info.attraction_genders:
                        hbox xfill True:
                            frame xsize gui.userinfo_textdistance_xsize background None:
                                text _("Sexuality:") size gui.label_text_size color gui.accent_color
                            frame xfill True background None:
                                if cur_character_info.is_heterosexual:
                                    text _("Straight") size gui.label_text_size
                                else:
                                    if cur_character_info.gender == GenderEnum.MALE:
                                        text _("Gay") size gui.label_text_size
                                    elif cur_character_info.gender == GenderEnum.FEMALE:
                                        text _("Lesbo") size gui.label_text_size

                    if cur_character_info.relationships and len(cur_character_info.relationships) > 0:
                        frame area (0, 0, 350, 25):
                            background None
                        frame xsize 300 background None:
                            text _("Relationships:") size gui.name_text_size
                        for ch in cur_character_info.relationships.keys():
                            $ relationship_name = cur_character_info.getRelationNameByCharacter(character = ch, relaction_types = relactions)
                            hbox xfill True:
                                frame xsize gui.userinfo_textdistance_xsize background None:
                                    text "[ch]:" size gui.label_text_size color gui.accent_color
                                frame xfill True background None:
                                    text "[relationship_name]" size gui.label_text_size

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
