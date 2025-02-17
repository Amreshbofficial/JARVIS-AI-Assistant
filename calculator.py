import tkinter as tk

# Function to update the expression in the entry field
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

# Function to evaluate the expression and show the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry field for input
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers and operations
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create and place the buttons
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    else:
        button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

# Create the Clear button
clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
