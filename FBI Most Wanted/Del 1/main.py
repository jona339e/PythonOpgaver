import requests
from bs4 import BeautifulSoup

url = "https://api.fbi.gov/wanted/v1/list"


def get_most_wanted_from_api():
    x = requests.get(url).json()
    return x

def filter_most_wanted(most_wanted):
    filtered_most_wanted = []
    for item in most_wanted["items"]:
        # got an error when simply passing the raw data into soup, so i had to check if details was empty
        details = item.get("details", "")
        
        if details:
            soup = BeautifulSoup(details, 'html.parser')
            clean_details = soup.get_text(separator=' ').strip()
        else:
            clean_details = ""

        filter_dict = {
            "categories": item.get("subjects", []),
            "name": item.get("title", ""),
            "aliases": item.get("aliases", []),
            "details": clean_details
        }
        filtered_most_wanted.append(filter_dict)

    return filtered_most_wanted


def main():
    filepath = "FBI Most Wanted/Del 1/most_wanted.csv"
    most_wanted = get_most_wanted_from_api()
    # print(most_wanted)
    filtered_most_wanted = filter_most_wanted(most_wanted)

    with open(filepath, "w") as file:
        for item in filtered_most_wanted:
            file.write(f"{item['categories']}, {item['name']}, {item['aliases']}, {item['details']}\n")
    
    



if __name__ == "__main__":
    main()