from person import Person


class Missing_person(Person):
    def __init__(self, id, fname, lname, last_seen = "00-00-0000"):
        super().__init__(id, fname, lname)
        self.last_seen = last_seen

