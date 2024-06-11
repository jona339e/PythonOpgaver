from person import Person


class Gang_member(Person):
    def __init__(self, id, fname, lname, gang_name = "Unknown"):
        super().__init__(id, fname, lname)
        self.gang_name = gang_name

    def to_dict(self):
        return {
            "id": self.id,
            "fname": self.fname,
            "lname": self.lname,
            "gang_name": self.gang_name
        }