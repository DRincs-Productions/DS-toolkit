
from typing import Optional, Union

import renpy.exports as renpy
from renpy.character import Character

from pythonpackages.ds.character_type import GENDER_TYPE
from pythonpackages.utility import IsNullOrWhiteSpace

UNKNOWN_STRING = "Unknown"


class CharacterInfo():
    """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information """

    def __init__(
        self,
        name: str,
        gender: GENDER_TYPE,
        sname: Optional[str] = None,
        age: Optional[int] = None,
        relationships: Optional[dict[Character, str]] = None,
        other_values: Optional[dict[Character, str]] = None,
    ):
        self.memory = other_values
        self.name = name
        self.sname = sname
        self.age = age
        self.gender = gender
        self.set("name_default", name)
        self.set("surname_default", sname)
        self.set("age_default", age)
        self.relationships = relationships

    @property
    def name(self) -> str:
        """Name of the character"""
        return self._name or UNKNOWN_STRING

    @name.setter
    def name(self, value: Optional[str]) -> None:
        if IsNullOrWhiteSpace(value):
            self._name = self.get("name_default")
        else:
            self._name = value

    @property
    def gender(self) -> GENDER_TYPE:
        """Gender of the character"""
        return self._gender  # type: ignore

    @gender.setter
    def gender(self, value: GENDER_TYPE) -> None:
        self._gender = value

    @property
    def sname(self) -> str:
        """Surname of the character"""
        return self._surname or UNKNOWN_STRING

    @property
    def surname(self) -> str:
        """Surname of the character"""
        return self._surname or UNKNOWN_STRING

    @sname.setter
    def sname(self, value: Optional[str]) -> None:
        if IsNullOrWhiteSpace(value):
            self._surname = self.get("surname_default")
        else:
            self._surname = value

    @surname.setter
    def surname(self, value: Optional[str]) -> None:
        if IsNullOrWhiteSpace(value):
            self._surname = self.get("surname_default")
        else:
            self._surname = value

    @property
    def age(self) -> Union[int, str]:
        """Age of the character"""
        return self._age or UNKNOWN_STRING

    @age.setter
    def age(self, value: Optional[Union[int, str]]) -> None:
        if (isinstance(value, int)):
            self._age = value
            return
        if IsNullOrWhiteSpace(value):
            self._age = self.get("age_default")
        else:
            self._age = value

    @property
    def relationships(self) -> dict[Character, str]:
        """Relationships of the character"""
        return self._relationships or {}

    @relationships.setter
    def relationships(self, value: Optional[dict[Character, str]]) -> None:
        self._relationships = value

    @property
    def memory(self) -> dict[str, str]:
        """I use a dictionary because it is the best solution for compatibility and not to create variables that may not be used."""
        return self._memory or {}

    @memory.setter
    def memory(self, value: Optional[dict[str, str]]) -> None:
        if (self._memory is None):
            self._memory = {}
        self._memory.update(value if value else {})

    def changeName(self) -> None:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#change-name """
        self.name = renpy.input(
            "{i}(Default: " + self.get("name_default") + "){/i}")
        if (self.get("name_default") == UNKNOWN_STRING):
            self.set("name_default", self.name)
        return

    def changeSurname(self) -> None:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#change-surname """
        self.sname = renpy.input(
            "{i}(Default: " + self.get("surname_default") + "){/i}")
        if (self.get("surname_default") == UNKNOWN_STRING):
            self.set("surname_default", self.sname)
        return

    def changeAge(self) -> None:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#change-age """
        self.age = renpy.input(
            "{i}(Default: " + str(self.get("age_default")) + "){/i}")
        if (self.get("age_default") == UNKNOWN_STRING):
            self.set("age_default", self.age)
        return

    def get(self, name: str) -> str:
        """Returns the value "name", in case it does not exist returns \"Unknown\""""
        if name in self.memory:
            return self.memory[name]
        else:
            return UNKNOWN_STRING

    def set(self, name: str, value) -> None:
        """Function to set or add a new value"""
        if (not IsNullOrWhiteSpace(name)):
            self.memory[name] = value
        else:
            self.remove(name)
        return

    def remove(self, name: str) -> None:
        """Delete the name value"""
        del self.memory[name]
        return

    def getRelationNameByCharacter(self, character: Character) -> Optional[str]:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Relaction#get-relation-name-by-character """
        if character in self.relationships:
            return self.relationships[character]
        else:
            return None

    def setRelationNameByCharacter(self, character: Character, relation: Optional[str] = None) -> None:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Relaction#set-relation-name-by-character """
        if IsNullOrWhiteSpace(relation):
            value = renpy.input(self.name+" is:")
            self.relationships[character] = value
            del value
        else:
            self.relationships[character] = relation  # type: ignore
        return