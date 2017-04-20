

class ProgrammingLanguage:
    def __init__(self, name, typing_type, can_reflect, year):
        self.name = name
        self.typing_type = typing_type
        self.can_reflect = can_reflect
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection = {}, First appeared in {}" \
            .format(self.name, self.typing_type, self.can_reflect, self.year)
