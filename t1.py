import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd


# Create a new Tkinter window
window = tk.Tk()
global var1
label = tk.Label(window, text="Please enter your input:")
label.pack()
# Add your code here to customize the window
text_box = tk.Entry(window)
text_box.pack()


def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn
con=create_connection("destinations.db")
# Replace MySQL connection with SQLite3 connection
conn = create_connection('travel_app.db')


df = pd.read_sql_query("SELECT * FROM destinations",con)
#
data=df.to_dict(orient='rows')

# Define global variables
user_budget = 0
season = ""
vacation_spots = data
#print(vacation_spots[0])

def suggest_vacation_spot(budget, season):
    suggested_spots = []
    #print(vacation_spots)
    for i in vacation_spots:
        if i.get('budgetf') >= budget and (
            season in i.get('season') or "all" in i.get('season')
        ):
            suggested_spots.append(i.get('name'))
    return str(suggested_spots)


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
        var1 = f"Based on your preferences, we suggest these vacation spots: {suggestions}"
        # Create and configure the label in the new window
        label = tk.Label(
            window,
            text=var1
        )
        label.pack()
    else:
        var1 = "Sorry, we couldn't find a matching vacation spot."
        print(var1)
        # Create and configure the label in the new window
        label = tk.Label(
            window, text=var1
        )
        label.pack()
    import bakchodi
    bakchodi.main(var1=var1)


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
window.destroy()
