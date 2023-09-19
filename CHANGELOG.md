# LTS Version

## Install

You can install this library manually: download the zip and extract it in your project folder.
But I recommend you to use git submodule:

```bash
# renpy-utility-lib
git submodule add -b python-lib -- https://github.com/DRincs-Productions/renpy-utility-lib 'pythonpackages/renpy_utility'
git submodule add -b renpy-lib -- https://github.com/DRincs-Productions/renpy-utility-lib 'game/renpy_utility_tool'
# renpy-utility-lib
git submodule add -b main -- https://github.com/DRincs-Productions/renpy-screens-style 'game/screens_style'
# Dating sim toolkit

```

**AND** create a empty file `__init__.py` into pythonpackages `pythonpackages/` so `pythonpackages/__init__.py`.

## Migrations

Use search and replace of vscode with regex functionality enabled

![image](https://user-images.githubusercontent.com/67595890/224504331-1f546922-5673-4fa9-8cc7-e3fc4e671305.png)

### updateFlags

* `updateFlags\((.*)\)`
* `update_flags($1)`

### getFlags

* `getFlags\((.*)\)`
* `get_flags($1)`

### setFlags

* `setFlags\((.*)\)`
* `set_flags($1)`

### notifyEx

* `notifyEx\((.*)\)`
* `notify_add($1)`

### notifyExPreventsLoops

* `notifyExPreventsLoops\((.*)\)`
* `notify_prevents_loops($1)`

### notifyExClean

* `notifyExClean\((.*)\)`
* `notify_remove($1)`

### GENDER_TYPE

* `GENDER_TYPE`
* `GenderEnum`

### gender_attracted

* `gender_attracted`
* `attraction_genders`
