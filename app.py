import tkinter as tk

# Function to update the display
def click(button_text):
    current = display_var.get()
    display_var.set(current + button_text)

# Function to clear the display
def clear():
    display_var.set("")

# Function to remove last character (Backspace)
def backspace():
    current = display_var.get()
    display_var.set(current[:-1])

# Function to evaluate the expression
def calculate():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except:
        display_var.set("Error")

# Create the main window
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("350x500")
app.config(bg="#242424")

# String variable for the display
display_var = tk.StringVar()

# Display (Entry widget)
display = tk.Entry(app, textvariable=display_var, font=("Consolas", 20), width=15, bd=8, justify="right")
display.pack(pady=10)

# Button Grid
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Frame for buttons
button_frame = tk.Frame(app)
button_frame.pack()

# Create buttons
for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack()
    for btn_text in row:
        if btn_text == "C":
            btn = tk.Button(row_frame, text=btn_text, font=("Consolas", 18), width=5, height=2, bg="red", fg="white", command=clear)
        elif btn_text == "=":
            btn = tk.Button(row_frame, text=btn_text, font=("Consolas", 18), width=5, height=2, bg="green", fg="white", command=calculate)
        else:
            btn = tk.Button(row_frame, text=btn_text, font=("Consolas", 18), width=5, height=2, command=lambda b=btn_text: click(b))
        btn.pack(side=tk.LEFT, padx=5, pady=5)

# Backspace Button
backspace_btn = tk.Button(app, text="⌫", font=("Consolas", 18), width=5, height=2, bg="orange", fg="white", command=backspace)
backspace_btn.pack(pady=5)

# Run the application
app.mainloop()
