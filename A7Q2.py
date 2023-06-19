import calendar
import tkinter as tk
from tkinter import messagebox

def show_calendar():
    year = entry.get()
    
    try:
        year = int(year)
        cal_data = calendar.calendar(year)
        calendar_label.config(text=cal_data)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid year.")

# Create the main window
window = tk.Tk()
window.title("Calendar Application")

# Create a label and an entry for user input
input_frame = tk.Frame(window)
input_frame.pack(pady=100)

label = tk.Label(input_frame, text="Enter a year:")
label.pack(side=tk.LEFT)

entry = tk.Entry(input_frame, width=110)
entry.pack(side=tk.LEFT)

# Create a button to display the calendar
button = tk.Button(window, text="Show Calendar", command=show_calendar)
button.pack(pady=90)

# Create a label to display the calendar
calendar_label = tk.Label(window, justify=tk.LEFT, font=("Courier", 10), anchor="w")
calendar_label.pack()

# Start the main loop
window.mainloop()
