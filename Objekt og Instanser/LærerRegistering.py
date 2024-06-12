from tec import TEC

def switch_loop():

    # switch case with 4 options
    # [1] opret lærer1
    # [2] opdater lærer
    # [3] vis liste af alle lærere
    # [4] Gem of Afslut

    filepath = "Objekt og Instanser/teachers.txt"
    tec = TEC(filepath)

    while True:

        print("[1] opret lærer")
        print("[2] opdater lærer")
        print("[3] vis liste af alle lærere")
        print("[4] Gem of Afslut")
        print()
        print("Du vil altid kunne indtaste 'q' for at gå tilbage til hovedmenuen")
        print()
        inp = input("Vælg 1, 2, 3 eller 4:\n")

        print()

        match inp:
            case '1':
                tec.create_teacher()
                pass

            case '2':
                tec.update_teacher()
                pass

            case '3':
                tec.print_teachers()

            case '4':
                tec.save_and_exit()

            case _:
                print("Ugyldigt Input...")
                print()


def main():
    switch_loop()


if __name__ == "__main__":
    main()



