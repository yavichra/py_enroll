class Course:

    def __init__(self, **kw):
        self.name = kw.pop('name')

    #def full_name(self):
    #    return self.first_name + " " + self.last_name