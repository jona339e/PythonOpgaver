from teacher import Teacher

class TEC:
    def __init__(self, filename):
        self.filename = filename
        self.teachers = []
        try:
            with open(filename) as f:
                # read the content of the file and convert it to a dictionary
                for x in f:
                    x = x.strip().split(",")
                    obj = Teacher(x[0], x[1], x[2])
                    self.teachers.append(obj)
                
        except FileNotFoundError:
            # if the file does not exist, create it
            with open(filename, "w") as f:
                f.write("")
    

    def print_teachers(self):
        print("-"*20)
        for x in self.teachers:
            print(x.get_full_name())
        print("-"*20)


    def create_teacher(self):
        print()
        print("Opret en ny lærer")
        print()
        fname = input("Fornavn: ")
        print()
        lname = input("Efternavn: ")
        print()
        subject = input("Fag: ")
        print()
        self.teachers.append(Teacher(fname, lname, subject))
        print(f"Oprettet lærer: {self.teachers[-1].get_full_name()}. Med fag: {self.teachers[-1].subject}")
        print()


    def update_teacher(self):
        for i in range(len(self.teachers)):
            print(f"[{i+1}] {self.teachers[i].fname} {self.teachers[i].lname} - {self.teachers[i].subject}")
            
        inp = input("Hvilken lære vil du opdatere?\n")
        print()

        for i in range(len(self.teachers)):
            if inp == str(i+1):
                print(f"Opdaterer {self.teachers[i].fname} {self.teachers[i].lname} - {self.teachers[i].subject}")
                fname = input("Fornavn: ")
                lname = input("Efternavn: ")
                subject = input("Fag: ")
                self.teachers[i] = Teacher(fname, lname, subject)
                break
            elif i == len(self.teachers-1):
                print()
                print("Ugyldigt input..")
                print()


    def save_and_exit(self):
        # since we store all our teachers in the teacher variable inside tec, it is easier to overwrite the file
        with open(self.filename, "w") as f:
            for teacher in self.teachers:
                f.write(f"{teacher.fname},{teacher.lname},{teacher.subject}\n")
            print("Fil Gemt...")
            print("Afslutter program...")
        quit()


