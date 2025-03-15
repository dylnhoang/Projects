import requests
import sys
import re
from person import Person
import csv
#https://fdc.nal.usda.gov/api-guide.html#bkmk-3

person = Person()
person_dict = {}
global current_day

def main():
    while(True):
        main_menu()


def search_food(food):
    results = ""
    response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/search?api_key=guzwWpYL3xh2JQNT7AM4zFfwjGiMNb3Aa4mJRtfc&query=" + food)
    o = response.json()
    for f in o["foods"]:
        results += (f["description"].upper() + " | FDC ID: " + str(f["fdcId"]) + "\n")
        return results

def add_food(id, grams):
    global current_day
    try:
        response = requests.get("https://api.nal.usda.gov/fdc/v1/food/" + id + "?api_key=guzwWpYL3xh2JQNT7AM4zFfwjGiMNb3Aa4mJRtfc")
        o = response.json()
        for n in o["foodNutrients"]:
            if n["nutrient"]["id"] == 1003:
                person_dict[current_day].add_protein(float(n["amount"] * grams))
            elif n["nutrient"]['id'] == 1004:
                person_dict[current_day].add_fats(float(n["amount"] * grams))
            elif n["nutrient"]['id'] == 1005:
                person_dict[current_day].add_carbs(float(n["amount"] * grams))
            elif n["nutrient"]['id'] == 1008:
                person_dict[current_day].add_cals(float(n["amount"] * grams))
        return "\nFood added successfully\n"
    except (ValueError, TypeError):
        return "\nInvalid input. FDC ID and amount must both be numeric.\n"
    except (KeyError, NameError):
        return "\nDate has not been set properly.\n"

def set_date(day):
    global current_day
    if re.search(r"^(0[1-9]|1[012])[/](0[1-9]|[12][0-9]|3[01])[/](19|20)\d\d$", day):
        if day not in person_dict:
            person_dict[day] = Person()
            current_day = day
            return("\nDate created: " + day + "\n")
        else:
            current_day = day
            return("\nDate set to: " + day + "\n")
    else:
        return("\nInvalid date." + "\n")

def write_to_file():
    for _ in person_dict:
        with open("nutrition.csv", "w") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "cals", "carbs", "fats", "protein"])
            for date in person_dict:
                writer.writerow({"date": date, "cals": str(round(person_dict[date].get_cals(), 2)), "carbs": str(round(person_dict[date].get_carbs(), 2)), "fats": str(round(person_dict[date].get_fats(), 2)), "protein": str(round(person_dict[date].get_prot(), 2))})

def import_from_file():
    try:
        with open("nutrition.csv") as file:
            for line in file:
                date, cals, carbs, fats, prot = line.rstrip().split(",")
                person_dict[date] = Person(float(carbs), float(fats), float(prot), float(cals))
        return("\nData has been imported from nutrition.csv\n")
    except FileNotFoundError:
        return("\nFile not found.\n")

def clear_file():
    key = input("Are you sure you want to clear this file? This action cannot be undone. (Y/N): ")
    if(key.upper().strip() == "Y"):
        file_to_delete = open("nutrition.csv",'w')
        file_to_delete.close()
        return "\nFile cleared.\n"
    elif(key.upper().strip() == "N"):
        return "\nFile has not been cleared.\n"
    else:
        print("\nPlease input \'Y\' or \'N\' to continue.\n")
        clear_file()


def main_menu():
    print("[1] Search FDC ID")
    print("[2] Input food using FDC ID")
    print("[3] See nutrition")
    print("[4] Set current date")
    print("[5] See current date")
    print("[6] Save to nutrition.csv")
    print("[7] Import from nutrition.csv")
    print("[8] Clear nutrition.csv")
    print("[Q] Quit")
    key = input("\nInput: ")
    if(key == '1'):
        food = input("Food: ").replace(" ", "%20").title().strip()
        print("\n" + search_food(food))
    elif key == "2":
        id = input("FDC ID: ")
        grams = float(input("Amount in Grams: "))/100
        print(add_food(id, grams))
    elif key == "3":
        try:
            print(person_dict[current_day])
        except NameError:
            print("\nCurrent date has not been set.\n")
    elif key == "4":
        day = input("Date (MM/DD/YYYY): ")
        print(set_date(day))
    elif key == "5":
        try:
            print("\n" + current_day + "\n")
        except NameError:
            print("\nCurrent date has not been set.\n")
    elif key == "6":
        write_to_file()
        print("\nData has been saved to file\n")
    elif key == "7":
        print(import_from_file())
    elif key == "8":
        print(clear_file())
    elif key.upper() == "Q":
        sys.exit("\nProgram ended\n")
    else:
        print("\nInvalid input.\n")


if __name__ == "__main__":
    main()

