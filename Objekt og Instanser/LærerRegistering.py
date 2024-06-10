

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


    def get_full_name(self):
        return self.fname + " " + self.lname


class Teacher(Person):
    def __init__(self, fname, lname, subject):
        super().__init__(fname, lname)
        self.subject = subject


    def create_teacher(self):

        pass


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


    def create_teacher(self, Teacher):
        self.teachers.append(Teacher)
    

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
                



# filname = "teacher_register.txt"
prefix = "Objekt og Instanser/"
filename = prefix + "demofile.txt"
tec = TEC(filename)


def write_to_file(filename, obj):
    with open(filename, "w") as f:
        f.write(obj)


def read_from_file(filename):
    with open(filename) as f:
        content = f.read()
        return content


def switch_loop():

    # switch case with 4 options
    # [1] opret lærer
    # [2] opdater lærer
    # [3] vis liste af alle lærere
    # [4] Gem of Afslut

    while True:

        print("[1] opret lærer")
        print("[2] opdater lærer")
        print("[3] vis liste af alle lærere")
        print("[4] Gem of Afslut")
        print()

        inp = input("Vælg 1, 2, 3 eller 4:\n")

        print()

        match inp:
            case '1':
                pass

            case '2':
                tec.update_teacher()
                pass

            case '3':
                tec.print_teachers()

            case '4':
                print("Afslutter programmet...")
                quit()

            case _:
                print("Ugyldigt Input...")
                print()


def main():
    switch_loop()


if __name__ == "__main__":
    main()

