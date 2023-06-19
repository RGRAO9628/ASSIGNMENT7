import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_operation(operator):
    global first_number
    global operation
    first_number = float(entry.get())
    operation = operator
    entry.delete(0, tk.END)

def button_equal():
    second_number = float(entry.get())
    entry.delete(0, tk.END)

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Error: Division by zero"
    
    entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to
