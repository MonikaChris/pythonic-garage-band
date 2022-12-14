from abc import ABC, abstractmethod

class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Band("{self.name}"'

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return Band.instances


class Musician(ABC):

    def __init__(self, name):
        self.name = name


class Guitarist(Musician):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'guitar'

    @staticmethod
    def play_solo():
        return 'face melting guitar solo'


class Bassist(Musician):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = Meshell Ndegeocello'

    @staticmethod
    def get_instrument():
        return 'bass'

    @staticmethod
    def play_solo():
        return 'bom bom buh bom'


class Drummer(Musician):

    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'

    @staticmethod
    def get_instrument():
        return 'drums'

    @staticmethod
    def play_solo():
        return 'rattle boom crash'


class Keyboardist(Musician):
    def __init__(self, name):
        super().__init__(name)

