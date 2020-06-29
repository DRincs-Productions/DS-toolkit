## image example:
# image girl = Composite( (gui.width, gui.height),
#     (0, 0), "/girl/photo.webp",
#     (0, 0), "check:girl/[girl_dress]/photo.webp")
## or:
# show expression "check:images/girl/[girl_dress]/photo.webp"

default girl_dress = "homesuit"

label set_girl_homesuit:
    $ girl_dress = "homesuit"
    return

label set_girl_null:
    $ girl_dress = ""
    return