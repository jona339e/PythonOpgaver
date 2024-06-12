from person import Person


class Teacher(Person):
    def __init__(self, fname, lname, subjects):
        super().__init__(fname, lname)
        self.subjects = subjects
        self.role = "Teacher"
    
    def get_person_role_in_tec(self):
        return self.role
