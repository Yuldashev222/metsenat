from enum import Enum



class StudentType(Enum):
    bachelor = 'bachelor'
    master = 'master'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)

