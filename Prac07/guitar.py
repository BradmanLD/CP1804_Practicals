

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2017 - self.cost
        return "The {} is 2017-{} = {} years old".\
            format(self.name, self.year, age)