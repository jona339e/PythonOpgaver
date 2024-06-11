from person import Person


class Gang_member(Person):
    def __init__(self, id, fname, lname, gang_name = "Unknown"):
        super().__init__(id, fname, lname)
        self.gang_name = gang_name

