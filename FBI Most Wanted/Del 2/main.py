import json
import os
import requests
from missing_person import Missing_person
from gang_member import Gang_member


def does_file_exist(filename):
    return os.path.exists(filename)


def get_most_wanted(url):
    try:
        most_wanted = requests.get(url)
        return most_wanted.json()
    except:
        return None


def filter_most_wanted(most_wanted):
    filtered_most_wanted = []
    for item in most_wanted["items"]:
        # some of the names also include city, so we also need to split at '-' and discard the rest
        if "-" in item["title"]:
            item["title"] = item["title"].split("-")[0].strip()
        i = item["title"].index(" ")

        filter_dict = {
            "categories": item["subjects"],
            "id": item["uid"],
            "fname": item["title"][:i],
            "lname": item["title"][i+1:],
        }
        filtered_most_wanted.append(filter_dict)

    return filtered_most_wanted


def create_json_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def read_json_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data


def update_last_seen(data):
    for index, mp in enumerate(data["missing_persons"]):
        print(f"{index+1}: {mp['fname']} {mp['lname']} - Last seen on {mp['last_seen']}")
    
    print()

    try:
        person_index = int(input("Enter the number of the person you want to modify last seen date for: ")) - 1
        if person_index < 0 or person_index >= len(data["missing_persons"]):
            raise IndexError
    except:
        print("Invalid choice")
        print()
        return False
    
    selected_person = data["missing_persons"][person_index]
    print(f"Modifying entry: {selected_person['fname']} {selected_person['lname']}")
    selected_person["last_seen"] = input("Enter new last seen date: ")
    print("Entry updated successfully!")
    print(f"Updated entry: {selected_person['fname']} {selected_person['lname']} - Last seen on {selected_person['last_seen']}")


def update_gang_name(data):
    for index, gm in enumerate(data["gang_members"]):
        print(f"{index+1}: {gm['fname']} {gm['lname']} - {gm['gang_name']}")
    
    print()

    try:
        person_index = int(input("Enter the number of the person you want to modify gang name for: ")) - 1
        if person_index < 0 or person_index >= len(data["gang_members"]):
            raise IndexError
    except:
        print("Invalid choice")
        print()
        return False
    
    selected_person = data["gang_members"][person_index]
    print(f"Modifying entry: {selected_person['fname']} {selected_person['lname']}")
    selected_person["gang_name"] = input("Enter new gang name: ")
    print("Entry updated successfully!")
    print(f"Updated entry: {selected_person['fname']} {selected_person['lname']} - {selected_person['gang_name']}")


def menu(data):
    print("1. Show Missing Persons")
    print("2. Show Gang Members")
    print("3. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            update_last_seen(data)

        case "2":
            update_gang_name(data)

        case "3":
            return True

        case _:
            print("Invalid choice")
            return False

    return False


def init():
    url = "https://api.fbi.gov/wanted/v1/list"
    filepath = "FBI Most Wanted/Del 2/most_wanted.json"
    most_wanted = get_most_wanted(url)
    if most_wanted is None:
        filtered_most_wanted = read_json_file(filepath)
    else:
        filtered_most_wanted = filter_most_wanted(most_wanted)
    
    missing_persons = []
    gang_members = []
    search_string = ["missing person", "Criminal Enterprise"]

    for item in filtered_most_wanted:
        if search_string[0].lower() in item["categories"][0].lower():
            mp = Missing_person(item["id"], item["fname"], item["lname"])
            missing_persons.append(mp)
        elif search_string[1].lower() in item["categories"][0].lower():
            gm = Gang_member(item["id"], item["fname"], item["lname"])
            gang_members.append(gm)
    
    return missing_persons, gang_members


def main():
    missing_persons, gang_members = init()

    # if file exist, read from file
    filepath = "FBI Most Wanted/Del 2/most_wanted.json"
    if does_file_exist(filepath):
        data = read_json_file(filepath)
        for i in range(len(missing_persons)):
            # if id of missing_persons[i] is not in any of the missing_persons in the file, add the missing person to the file
            if missing_persons[i].id not in [mp["id"] for mp in data["missing_persons"]]: # uses a foreach loop to check if the id is in the list of ids in the file, where mp is the current missing person in the file
                data["missing_persons"].append(missing_persons[i].to_dict())
        for i in range(len(gang_members)):
            # same as above but for gang_members
            if gang_members[i].id not in [gm["id"] for gm in data["gang_members"]]:
                data["gang_members"].append(gang_members[i].to_dict())
    else:
        #create new file with data
        data = {
            "missing_persons": [mp.to_dict() for mp in missing_persons],
            "gang_members": [gm.to_dict() for gm in gang_members]
        }

        create_json_file(data, filepath)

    while True:
        if menu(data):
            break
        
    # on exist overwrite file with new content
    create_json_file(data, filepath)


if __name__ == "__main__":
    main()
