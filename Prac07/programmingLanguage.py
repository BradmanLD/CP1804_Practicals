

class ProgrammingLanguage:
    def __init__(self, name="", typing_type="Static", can_reflect="True", year=0):
        self.name = name
        self.typing_type = typing_type
        self.can_reflect = can_reflect
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection = {}, First appeared in {}" \
            .format(self.name, self.typing_type, self.can_reflect, self.year)

    def is_dynamic(self):
        if self.typing_type == "Dynamic":
            return True
