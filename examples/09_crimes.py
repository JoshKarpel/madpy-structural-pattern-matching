# This nightmare is courtesy of Hillel Wayne!
# https://www.hillelwayne.com/post/python-abc/

from abc import ABC


class PalindromicName(ABC):
    @classmethod
    def __subclasshook__(cls, other: type):
        name = other.__name__.lower()
        return name[::-1] == name


class Abba:
    ...


class Baba:
    ...


print(f"{isinstance(Abba(), PalindromicName)=}")
print(f"{isinstance(Baba(), PalindromicName)=}")
