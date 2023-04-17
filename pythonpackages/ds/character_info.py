
from typing import Optional, Union

import renpy.exports as renpy
from renpy.character import Character

from pythonpackages.ds.character_type import GenderEnum
from pythonpackages.utility import IsNullOrWhiteSpace

UNKNOWN_STRING = "Unknown"
DEFAULT_SURNAME_KEY = "default_surname"
DEFAULT_NAME_KEY = "default_name"
DEFAULT_AGE_KEY = "default_age"


class CharacterInfo():
    """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information """

    def __init__(
        self,
        name: str,
        gender: GenderEnum,
        surname: Optional[str] = None,
        age: Optional[int] = None,
        relationships: Optional[dict[Character, str]] = None,
        other_values: Optional[dict[Character, str]] = None,
        attraction_genders: Optional[Union[list[GenderEnum],
                                           GenderEnum]] = None,
    ):
        self._memory = {}
        self._relationships = {}
        self.memory = other_values
        self.name = name
        self.default_name = name
        self.surname = surname
        if (surname != None):
            self.default_surname = surname
        self.age = age
        if (age != None):
            self.default_age = age
        self.gender = gender
        self.relationships = relationships
        self.attraction_genders = attraction_genders

    # Memory

    @property
    def memory(self) -> dict[str, str]:
        """I use a dictionary because it is the best solution for compatibility and not to create variables that may not be used."""
        return self._memory if self._memory else {}

    @memory.setter
    def memory(self, value: Optional[dict[str, str]]) -> None:
        self._memory.update(value if value else {})

    def get(self, name: str) -> str:
        """Returns the value "name", in case it does not exist returns UNKNOWN_STRING"""
        if name in self._memory.keys():
            return self._memory[name]
        else:
            return UNKNOWN_STRING

    def set(self, key: str, value) -> None:
        """Function to set or add a new value"""
        if value == None:
            self.remove(key)
        elif isinstance(value, str) and IsNullOrWhiteSpace(value):
            self.remove(key)
        else:
            self._memory[key] = value
        return

    def remove(self, key: str) -> None:
        """Delete the name value"""
        if key in self._memory.keys():
            del self._memory[key]
        return

    # Name

    @property
    def name(self) -> str:
        """Name of the character"""
        if self._name == None or IsNullOrWhiteSpace(self._name):
            return self.default_name
        return self._name

    @name.setter
    def name(self, value: Optional[str]) -> None:
        self._name = value

    @property
    def default_name(self) -> str:
        """Default name of the character"""
        return self.get(DEFAULT_NAME_KEY)

    @default_name.setter
    def default_name(self, value: str) -> None:
        self.set(DEFAULT_NAME_KEY, value)

    def changeName(self) -> None:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#change-name """
        self.name = renpy.input(
            "{i}(Default: " + self.default_name + "){/i}")
        if self.default_name == UNKNOWN_STRING:
            self.default_name = self.name
        return

    # Surname

    @property
    def sname(self) -> str:
        """Surname of the character"""
        return self.surname

    @property
    def surname(self) -> str:
        """Surname of the character"""
        if self._surname == None or IsNullOrWhiteSpace(self._surname):
            return self.default_surname
        return self._surname

    @sname.setter
    def sname(self, value: Optional[str]) -> None:
        self.surname = value

    @surname.setter
    def surname(self, value: Optional[str]) -> None:
        if IsNullOrWhiteSpace(value):
            self._surname = self.get(DEFAULT_SURNAME_KEY)
        else:
            self._surname = value

    @property
    def default_surname(self) -> str:
        """Default surname of the character"""
        return self.get(DEFAULT_SURNAME_KEY)

    @default_surname.setter
    def default_surname(self, value: str) -> None:
        self.set(DEFAULT_SURNAME_KEY, value)

    def changeSurname(self) -> None:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#change-surname """
        self.surname = renpy.input(
            "{i}(Default: " + self.default_surname + "){/i}")
        if self.default_surname == UNKNOWN_STRING:
            self.default_surname = self.surname
        return

    # Age

    @property
    def age(self) -> Union[int, str]:
        """Age of the character"""
        if (self._age == None):
            return self.default_age
        return self._age

    @age.setter
    def age(self, value: Optional[Union[int, str]]) -> None:
        if (isinstance(value, int)):
            self._age = value
            return
        if IsNullOrWhiteSpace(value):
            self._age = self.get(DEFAULT_AGE_KEY)
        else:
            self._age = value

    @property
    def default_age(self) -> Union[int, str]:
        """Default age of the character"""
        return self.get(DEFAULT_AGE_KEY)

    @default_age.setter
    def default_age(self, value: Union[int, str]) -> None:
        self.set(DEFAULT_AGE_KEY, value)

    def changeAge(self) -> None:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Information#change-age """
        self.age = renpy.input(
            "{i}(Default: " + str(self.default_age) + "){/i}")
        if (self.default_age == UNKNOWN_STRING):
            self.default_age = self.age
        return

    # Relationships

    @property
    def relationships(self) -> dict[Character, str]:
        """Relationships of the character"""
        return self._relationships if self._relationships else {}

    @relationships.setter
    def relationships(self, value: Optional[dict[Character, str]]) -> None:
        self._relationships.update(value if value else {})

    def getRelationNameByCharacter(self, character: Character, relaction_types: dict[str, tuple[str]] = {}) -> Optional[str]:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Relaction#get-relation-name-by-character """
        if character in self.relationships:
            key = self._relationships[character]
            if key in relaction_types:
                value = relaction_types[key]
                if isinstance(value, tuple):
                    return value[0]
                else:
                    return value
        else:
            return None

    def setRelationNameByCharacter(self, character: Character, default_relation_key: str, relaction_types: dict[str, tuple[str]] = {}) -> None:
        """Wiki: https://github.com/DRincs-Productions/DS-toolkit/wiki/Relaction#set-relation-name-by-character """
        default_value = default_relation_key
        if default_value in relaction_types:
            default_value = relaction_types[default_value]

        if isinstance(default_value, tuple):
            default_value = default_value[0]

        value = renpy.input("{i}(Default: " + str(default_value) + "){/i}")
        if IsNullOrWhiteSpace(value):
            self._relationships[character] = default_relation_key
        else:
            self._relationships[character] = value
        return

    def delete_relation(self, character: Character) -> None:
        """Delete relation with character"""
        if character in self.relationships:
            del self._relationships[character]
        return

    # Gender

    @property
    def gender(self) -> GenderEnum:
        """Gender of the character"""
        return self._gender

    @gender.setter
    def gender(self, value: GenderEnum) -> None:
        self._gender = value

    @property
    def attraction_genders(self) -> list[GenderEnum]:
        """Gender attracted to the character"""
        if (self._attraction_genders == None):
            if (GenderEnum.MALE == self.gender):
                return [GenderEnum.FEMALE]
            else:
                return [GenderEnum.MALE]
        else:
            return self._attraction_genders

    @attraction_genders.setter
    def attraction_genders(self, value: Optional[Union[list[GenderEnum], GenderEnum]]):
        if (isinstance(value, GenderEnum)):
            value = [value]
        self._attraction_genders = value

    @property
    def is_heterosexual(self) -> bool:
        return not self.gender in self.attraction_genders

    @is_heterosexual.setter
    def is_heterosexual(self, value: bool):
        if value:
            if self.gender == GenderEnum.MALE:
                self.attraction_genders = [GenderEnum.FEMALE]
            else:
                self.attraction_genders = [GenderEnum.MALE]
        else:
            if self.gender == GenderEnum.MALE:
                self.attraction_genders.append(GenderEnum.MALE)
            else:
                self.attraction_genders.append(GenderEnum.FEMALE)
