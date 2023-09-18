screen menu_userinfo_character_info(character_info):
    hbox xfill True:
        frame xsize gui.userinfo_textdistance_xsize background None:
            text _("Name:") size gui.label_text_size color gui.accent_color
        frame xfill True background None:
            text "[character_info.name] [character_info.sname]" size gui.label_text_size

    if character_info.age:
        hbox xfill True:
            frame xsize gui.userinfo_textdistance_xsize background None:
                text _("Age:") size gui.label_text_size color gui.accent_color
            frame xfill True background None:
                text "[character_info.age]" size gui.label_text_size

    if character_info.attraction_genders:
        hbox xfill True:
            frame xsize gui.userinfo_textdistance_xsize background None:
                text _("Sexuality:") size gui.label_text_size color gui.accent_color
            frame xfill True background None:
                if character_info.is_heterosexual:
                    text _("Straight") size gui.label_text_size
                else:
                    if character_info.gender == GenderEnum.MALE:
                        text _("Gay") size gui.label_text_size
                    elif character_info.gender == GenderEnum.FEMALE:
                        text _("Lesbo") size gui.label_text_size

    if character_info.relationships and len(character_info.relationships) > 0:
        frame area (0, 0, 350, 25):
            background None
        frame xsize 300 background None:
            text _("Relationships:") size gui.name_text_size
        for ch in character_info.relationships.keys():
            $ relationship_name = character_info.getRelationNameByCharacter(character = ch, relaction_types = relactions)
            hbox xfill True:
                frame xsize gui.userinfo_textdistance_xsize background None:
                    text "[ch]:" size gui.label_text_size color gui.accent_color
                frame xfill True background None:
                    text "[relationship_name]" size gui.label_text_size

screen menu_userinfo_character_statistic(name, character_statistic):
    $ statistic_memory = character_statistic.getAll()
    $ max_value = character_statistic.getDefaultMaxValue()
    if len(statistic_memory) > 0:
        frame area (0, 0, 350, 25):
            background None
        frame xsize 300 background None:
            text name size gui.name_text_size
        for stat in statistic_memory.keys():
            $ value = statistic_memory[stat]
            if stat in ds_translations:
                $ stat = ds_translations[stat]
            hbox xfill True:
                frame xsize gui.userinfo_textdistance_xsize background None:
                    text _("[stat]:") size gui.label_text_size color gui.accent_color
                frame xfill True background None:
                    text "[value]" size gui.label_text_size
