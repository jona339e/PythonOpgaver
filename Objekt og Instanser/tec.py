from teacher import Teacher

class TEC:
    def __init__(self, filename):
        self.filename = filename
        self.teachers = []
        self.subjects = ["Grundlæggende Programmering", "OOP", "Python", "Big Data", "Gui Programmering"]
        try:
            with open(filename) as f:
                # read the content of the file
                for x in f:
                    x = x.strip().split(",")
                    subjects = []
                    for s in x[2].split("-"):
                        subjects.append(s)
                    teach = Teacher(x[0], x[1], subjects)
                    self.teachers.append(teach)
                
        except FileNotFoundError:
            # if the file does not exist, create it
            with open(filename, "w") as f:
                f.write("")
    

    def print_teachers(self):
        print("-"*20)
        for x in range(len(self.teachers)):
            print(self.teachers[x].get_full_name())
            for sub in self.teachers[x].subjects:
                print(f"\t- {sub}")
        print("-"*20)


    def create_teacher(self):
        print()
        print("Opret en ny lærer")
        print()
        fname = input("Fornavn: ")
        if self.q_entered(fname):
            print("Går tilbage til hovedmenu")
            return
        print()
        lname = input("Efternavn: ")
        if self.q_entered(lname):
            print("Går tilbage til hovedmenu")
            return
        print()
        for i in range(len(self.subjects)):
            print(f"[{i+1}] {self.subjects[i]}")
        try:
            subject_index = int(input("Vælg et fag fra listen:\n")) - 1
        except:
            print("Ugyldigt Input")
        print()
        subject = [self.subjects[subject_index]]
        self.teachers.append(Teacher(fname, lname, subject))
        print(f"Oprettet lærer: {self.teachers[-1].get_full_name()}. Med fag: {self.teachers[-1].subjects}")
        print()


    def update_teacher(self):
        if len(self.teachers) <= 0:
            print("Ingen lærerer oprettet. Returnere til hovedmenu")
            print()
            return
        teacher_index = 0
        for i in range(len(self.teachers)):
            print(f"[{i+1}] {self.teachers[i].fname} {self.teachers[i].lname}")
            for sub in self.teachers[i].subjects:
                print(f"\t- {sub}")
        print()
        try:
            teacher_index = int(input("Hvilken lære vil du opdatere?\n")) - 1
        except:
            print("Ugyldigt input")
            return
        print()

        print("[1] Tilføj Fag")
        print("[2] Slet Fag")
        print()
        inp = input("Vælg handling:\n")
        if self.q_entered(inp):
            print("Går tilbage til hovedmenu")
            return
        # update or remove subjects
        if inp == '1':
            self.update_subjects(teacher_index)
            
        elif inp == '2':
            self.delete_subject_from_teacher(teacher_index)

        else:
            print("Ugyldigt Input")
            return

    
    def update_subjects(self, teacher_index):
        # update subjects:
        print(f"Opdaterer {self.teachers[teacher_index].fname} {self.teachers[teacher_index].lname}")
        for x in self.teachers[teacher_index].subjects:
            print(f"{x}\t")
        for j in range(len(self.subjects)):
            print(f"[{j+1}] {self.subjects[j]}")

        print()
        try:
            inp = int(input("Tilføj Fag: ")) - 1
        except:
            return

        # if inp is inside scope proceed
        if inp >= 0 and inp <= len(self.subjects):

            # if subject already exist in teacher return with message teacher already has this subject
            if self.subjects[inp] in self.teachers[teacher_index].subjects:
                print()
                print("Lære har allerede dette fag")
                return
            
            self.teachers[teacher_index].subjects.append(self.subjects[inp])
            print()
            print(f"Tilføjet {self.subjects[inp]} til {self.teachers[teacher_index].get_full_name()}")
            print()
        else:
            print("Ugyldigt input")
            print()


    def delete_subject_from_teacher(self, teacher_index):
        print()
        print(f"Sletter Fag fra Lærer - {self.teachers[teacher_index].get_full_name()}")
        print()
        length = len(self.teachers[teacher_index].subjects)
        
        if length <= 1:
            print()
            print("Mindst 1 fag er obligatorisk")
            print("Går tilbage til hovedmenu")
            print()
            return

        for i in range(length):
            print(f"[{i+1}] - {self.teachers[teacher_index].subjects[i]}")
        try:
            subject_index = int(input("Vælg det fag der skal slættes:\n")) - 1
        except:
            print("Ugyldigt input")
            return
        if subject_index >= 0 and subject_index <= length:
            deleted_subject = self.teachers[teacher_index].subjects.pop(subject_index)    
            print()
            print(f"Fag - {deleted_subject} - slettet fra {self.teachers[teacher_index].get_full_name()}")
        else:
            print()
            print("Ugyldigt Input")


    def save_and_exit(self):
        # since we store all our teachers in the teacher variable inside tec, it is easier to overwrite the file
        with open(self.filename, "w") as F:
            for teacher in self.teachers:
                subject_string = ""
                for i in range(len(teacher.subjects)):
                    if i == len(teacher.subjects) - 1:
                        subject_string += f"{teacher.subjects[i]}"
                    else:
                        subject_string += f"{teacher.subjects[i]}-"

                F.write(f"{teacher.fname},{teacher.lname},{subject_string}\n")
            print("Fil Gemt...")
            print("Afslutter program...")
        quit()


    def q_entered(self, input):
        if input == 'q':
            return True

