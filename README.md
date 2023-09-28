# Dating sim toolkit (character info) for Ren'Py

![Last commit](https://img.shields.io/github/last-commit/DRincs-Productions/DS-toolkit)
![License](https://img.shields.io/github/license/DRincs-Productions/DS-toolkit)
<span class="discord">
<a href="https://discord.gg/5UFPjP9" title="Discord"><img src="https://img.shields.io/discord/688162156151439536" alt="Discord" /></a>
</span>

This repo is a set of basic tools for Visual Novel / Game developers who are planning to create a Dating sim.

Feel free to contribute, fork this and send a pull request. 😄

----

## TO DOWNLOAD THIS TEST PROJECT

```shell
# Basic command to download projects from git
git clone https://github.com/DRincs-Productions/DS-toolkit
# IMPORTANT -> Will add the libraries needed to run the program
cd DS-toolkit
git submodule update --init --recursive

```

----

## Documentation

**[Wiki](https://github.com/DRincs-Productions/DS-toolkit/wiki)**

## Code snippets ([VSCode](https://code.visualstudio.com/))

(all begin with `DR_`)

Download the: [link](https://github.com/DRincs-Productions/DS-toolkit/releases/tag/code-snippets%2Fv2.0.0)

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/67595890/179365279-0d0b6d45-0048-4a0d-8c6d-9571b9c328f4.gif)

## Install LTS Version

To install a precise version install it manually: [Releases](https://github.com/DRincs-Productions/DS-toolkit/releases).

But I recommend you to use git submodule:

```bash
# renpy-utility-lib
git submodule add -b python-lib -- https://github.com/DRincs-Productions/renpy-utility-lib 'pythonpackages/renpy_utility'
git submodule add -b renpy-lib -- https://github.com/DRincs-Productions/renpy-utility-lib 'game/renpy_utility_tool'
# renpy-utility-lib
git submodule add -b main -- https://github.com/DRincs-Productions/renpy-screens-style 'game/screens_style'
# Dating sim toolkit
git submodule add -b python-lib -- https://github.com/DRincs-Productions/DS-toolkit 'pythonpackages/ds'
git submodule add -b renpy-lib -- https://github.com/DRincs-Productions/DS-toolkit 'game/ds_tool'
git submodule add -b screens -- https://github.com/DRincs-Productions/DS-toolkit 'game/ds_screens'

```

**AND** create a empty file `__init__.py` into `pythonpackages/` so `pythonpackages/__init__.py`.

## Update new version

```bash
git submodule update --init --recursive

```

## Preview

![image](https://user-images.githubusercontent.com/67595890/198900451-6b379a7b-5e0a-4a81-a397-a3f0328a34b6.png)

![image](https://user-images.githubusercontent.com/67595890/198900475-87def00c-8291-4d68-9235-4fdc1333967b.png)

![Characters statistics and ability](https://user-images.githubusercontent.com/67595890/181107510-c6affb34-1310-4100-8975-a16cc3645c76.png)

![Clothes management](https://user-images.githubusercontent.com/67595890/181107522-d255666e-9b96-4aa8-93a9-a09d3320b47e.png)
