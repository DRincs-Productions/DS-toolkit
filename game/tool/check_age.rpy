define pegi_18 = "/images_tool/pegi_18.webp"
define button_no_idle = "/images_tool/button-no.webp"
define button_no_hover = im.MatrixColor("/images_tool/button-no.webp", im.matrix.brightness(0.2))
define button_yes_idle = "/images_tool/button-yes.webp"
define button_yes_hover = im.MatrixColor("/images_tool/button-yes.webp", im.matrix.brightness(0.2))

screen check_age():
    add Frame(pegi_18, xfill=True, yfill=True)
    hbox:
        xalign 0.5
        yalign 0.93
        spacing 70
        imagebutton:
            idle Frame(button_yes_idle, xfill=True, yfill=True)
            hover Frame(button_yes_hover, xfill=True, yfill=True)
            action Return()
            xsize 360
            ysize 80
        imagebutton:
            idle Frame(button_no_idle, xfill=True, yfill=True)
            hover Frame(button_no_hover, xfill=True, yfill=True)
            action MainMenu(confirm=False)
            xsize 360
            ysize 80
