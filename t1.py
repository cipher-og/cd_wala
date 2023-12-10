import tkinter as tk
from tkinter import ttk

# Create a new Tkinter window
window = tk.Tk()

label = tk.Label(window, text="Please enter your input:")
label.pack()
# Add your code here to customize the window
text_box = tk.Entry(window)
text_box.pack()

# Define global variables
user_budget = 0
season = ""
vacation_spots = {
    "Beach Paradise": {"budget": 10000, "season": ["summer"], "activities": ["beach"]},
    "Mountain Retreat": {
        "budget": 80000,
        "season": ["winter", "spring"],
        "activities": ["hiking", "skiing"],
    },
    "City Exploration": {
        "budget": 12000,
        "season": ["all"],
        "activities": ["sightseeing", "cultural experiences"],
    },
    "Tropical Adventure": {
        "budget": 15000,
        "season": ["summer", "spring"],
        "activities": ["snorkeling", "hiking"],
    },
    "Ski Resort Getaway": {
        "budget": 90000,
        "season": ["winter"],
        "activities": ["skiing", "snowboarding"],
    },
    "Historical Tour": {
        "budget": 11000,
        "season": ["all"],
        "activities": ["historical sites", "guided tours"],
    },
    "Desert Expedition": {
        "budget": 130000,
        "season": ["spring", "fall"],
        "activities": ["camel rides", "stargazing"],
    },
}


def suggest_vacation_spot(budget, season):
    suggested_spots = []
    for spot, details in vacation_spots.items():
        if details["budget"] <= budget and (
            season in details["season"] or "all" in details["season"]
        ):
            suggested_spots.append(spot)
    return suggested_spots


def retrieve_input():
    input_value = text_box.get()
    selected_option = variable.get()
    # Store the values in global variables
    global text_input
    global season
    user_budget = int(input_value)
    season = selected_option
    suggestions = suggest_vacation_spot(user_budget, season)

    if suggestions:
        print(
            "Based on your preferences, we suggest these vacation spots:", suggestions
        )
        # Create and configure the label in the new window
        label = tk.Label(
            window,
            text=f"Based on your preferences, we suggest these vacation spots: {suggestions}",
        )
        label.pack()
    else:
        print("Sorry, we couldn't find a matching vacation spot.")
        # Create and configure the label in the new window
        label = tk.Label(
            window, text=f"Sorry, we couldn't find a matching vacation spot."
        )
        label.pack()


variable = tk.StringVar(window)

# Define the options for the dropdown menu
options = [
    "Please select the season you want to travel in",
    "Summer",
    "Spring",
    "Fall",
    "Winter",
]

# Set the default value for the dropdown menu
variable.set(options[0])

# Create the dropdown menu
dropdown = tk.OptionMenu(window, variable, *options)
dropdown.pack()


submit_button = tk.Button(window, text="Submit", command=retrieve_input)
submit_button.pack()

label = tk.Label(window, text="")
label.pack()

# Start the Tkinter event loop
window.mainloop()

print(user_budget, season)


print("Welcome to the Vacation Spot Guessing Game!")

# Create a new window
new_window = tk.Toplevel(window)

label.pack()

window.mainloop()
