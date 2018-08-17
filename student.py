class Student:

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name', 'N/A')
        self.last_name = kwargs.get('last_name', 'N/A')
        self.passport = kwargs.get('passport')

    def full_name(self):
        return self.first_name + " " + self.last_name