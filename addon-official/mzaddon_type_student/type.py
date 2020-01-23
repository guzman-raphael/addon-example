
class Student:
    def __init__(self, first_name=None, last_name=None, enrolled=None):
        self.first_name = first_name
        self.last_name = last_name
        self.enrolled = enrolled2

    def __str__(self):
        return str(self.__dict__)

student1 = Student('Raphael', 'Guzman', '2020-01-23')