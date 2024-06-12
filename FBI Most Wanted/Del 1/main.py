import requests
from bs4 import BeautifulSoup
import csv

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
    filtered_most_wanted = filter_most_wanted(most_wanted)
    
    with open(filepath, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["categories", "name", "aliases", "details"])
        writer.writeheader()
        writer.writerows(filtered_most_wanted)


if __name__ == "__main__":
    main()