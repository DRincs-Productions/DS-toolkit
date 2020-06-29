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