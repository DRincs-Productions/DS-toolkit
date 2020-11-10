init -999 python:
    def enum(*sequential, **named):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        return type(str('Enum'), (), enums)
