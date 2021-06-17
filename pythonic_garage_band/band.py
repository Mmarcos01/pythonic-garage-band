from attr.validators import instance_of

class Band:
    # instances = []

    def __init__(self, name, members=None):
        self.name = name
        self.members = members
        # Band.instances.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"


class Musician:

    def __init__(self, name, instruments, instance):
        self.name = name
        self.instruments = instruments
        self.instance = instance
        # self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instruments}"

    def __repr__(self):
        return f"{self.instance} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instruments}"

    # def play_solo(self):
    #     return f""


class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, "guitar", "Guitarist")


class Bassist(Musician, Band):
    def __init__(self, name):
         super().__init__(name, "bass", "Bassist")


class Drummer(Musician, Band):
    def __init__(self, name):
        super().__init__(name, "drums", "Drummer")


