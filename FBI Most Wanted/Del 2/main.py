import json
import requests
from missing_person import Missing_person
from gang_member import Gang_member


def get_most_wanted(url):
    most_wanted = requests.get(url)
    return most_wanted.json()


def filter_most_wanted(most_wanted):
    filtered_most_wanted = []
    for item in most_wanted["items"]:
        i = item["title"].index(" ")
        filter_dict = {
            "categories": item["subjects"],
            "id": item["uid"],
            "fname": item["title"][:i],
            "lname": item["title"][i+1:],
        }
        filtered_most_wanted.append(filter_dict)

    return filtered_most_wanted


def menu(missing_persons, gang_memebers):
    print("1. Show Missing Persons")
    print("2. Show Gang Members")
    print("3. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            for mp in missing_persons:
                print(f"{mp.fname} {mp.lname} - {mp.last_seen}")
        case "2":
            for gm in gang_memebers:
                print(gm)
        case "3":
            exit()
        case _:
            print("Invalid choice")


def main():
    url = "https://api.fbi.gov/wanted/v1/list"
    most_wanted = get_most_wanted(url)
    filtered_most_wanted = filter_most_wanted(most_wanted)
    missing_persons = []
    gang_members = []
    search_string = ["missing person", "Criminal Enterprise Investigations"]
    for item in filtered_most_wanted:
        if search_string[0].lower() in item["categories"][0].lower():
            mp = Missing_person(item["id"], item["fname"], item["lname"])
            missing_persons.append(mp)
        if search_string[1].lower() in item["categories"][0].lower():
            gm = Gang_member(item["id"], item["fname"], item["lname"])
            gang_members.append(gm)
    while(True):
        menu(missing_persons, gang_members)


if __name__ == "__main__":
    main()