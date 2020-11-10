init python:
    def null_or_image(s):
        """It checks for the presence of an image, in case it is not there it returns a null value. Possible use: avoid mistakes in the management of clothes."""
        # s = renpy.substitute(s)
        if renpy.has_image(s):
            return s
        elif renpy.list_files(s):
            return s
        else:
            return Null()
    config.displayable_prefix['check'] = null_or_image