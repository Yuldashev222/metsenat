from enum import Enum



class SponsorType(Enum):
    y = 'yuridik shaxs'
    j = 'jismoniy shaxs'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)


class SponsorStatus(Enum):
    new = 'new'
    in_moderation = 'in moderation'
    approved = 'approved'
    canceled = 'canceled'

    @classmethod
    def choices(cls):
        return ((i.name, i.value) for i in cls)