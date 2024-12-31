
import pandas as pd
import requests

# Define the adventure activities by location in Pernambuco
activities_pe = {
    "Fernando de Noronha": [
        {"name": "Diving", "description": "Dive into the marine diversity.",
         "curiosity": "Best diving spot in Brazil.",
         "days": "Monday to Sunday", "hours": "8am to 5pm", "price": 200, "restriction": "Must know how to swim."},
        {"name": "Paragliding", "description": "Fly over the scenic landscapes of Noronha.",
         "curiosity": "Breathtaking aerial views of the island.",
         "days": "Wednesday to Sunday", "hours": "9am to 4pm", "price": 300, "restriction": "Minimum height 1.5m."}
    ],
    "Porto de Galinhas": [
        {"name": "Buggy Tour", "description": "Ride along the beaches and dunes.",
         "curiosity": "Covers 4 unique beaches.",
         "days": "Daily", "hours": "9am to 6pm", "price": 150, "restriction": "Suitable for all ages."}
    ]
    # Additional activities for more places can be added here.
}

# Functions for loading data from Excel files if available
def load_data():
    try:
        users = pd.read_excel('users.xlsx')
    except FileNotFoundError:
        users = pd.DataFrame(columns=["username", "password", "preferences"])
    return users

# Function for registering a new user
def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")
    preferences = choose_preferences()
    global users
    new_user = pd.DataFrame({"username": [username], "password": [password], "preferences": [", ".join(preferences)]})
    users = pd.concat([users, new_user], ignore_index=True)
    print("User registered successfully!")

# Function for choosing preferences from a menu
def choose_preferences():
    options = ["Diving", "Buggy Tour", "Paragliding"]
    print("Choose your preferences:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choices = input("Select preferences by numbers (e.g., 1,2): ")
    indices = [int(i.strip()) - 1 for i in choices.split(',') if i.strip().isdigit()]
    return [options[i] for i in indices if 0 <= i < len(options)]

# Function to search for activities by location
def search_activities():
    print("Available locations:")
    for i, location in enumerate(activities_pe.keys(), 1):
        print(f"{i}. {location}")
    choice = int(input("Choose a location: "))
    selected_location = list(activities_pe.keys())[choice - 1]
    print(f"Activities in {selected_location}:")
    for i, act in enumerate(activities_pe[selected_location], 1):
        print(f"{i}. {act['name']} - {act['description']}")
    return selected_location

# Run main menu
def main_menu():
    while True:
        print("Welcome to Nomad Adventure!")
        print("1. Register
2. Search Activities
3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            location = search_activities()
        elif choice == '3':
            print("Goodbye!")
            break

# Initialize app
if __name__ == "__main__":
    users = load_data()
    main_menu()
