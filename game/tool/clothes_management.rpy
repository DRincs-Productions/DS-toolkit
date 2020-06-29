init python:
    def null_or_image(s):
        # s = renpy.substitute(s)
        if renpy.has_image(s):
            return s
        elif renpy.list_files(s):
            return s
        else:
            return Null()
    config.displayable_prefix['check'] = null_or_image

## image example::
# image girl = Composite( (gui.width, gui.height),
#     (0, 0), "/girl/photo.webp",
#     (0, 0), "check:girl/[girl_dress]/photo.webp"))
## or:
# show expression "check:images/girl/[girl_dress]/photo.webp"

default girl_dress = "homesuit"

label set_girl_homesuit:
    $ girl_dress = "homesuit"
    return
