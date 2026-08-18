import tkinter as tk
from calculator import calculate


def perform_calculation():

    try:
        num1 = float(first_number.get())
        num2 = float(second_number.get())

        operation = operation_var.get()

        result = calculate(num1, num2, operation)

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Error: Enter valid numbers.")


# Create the main window
window = tk.Tk()

window.title("Calculator")
window.geometry("400x400")


# Title
title_label = tk.Label(
    window,
    text="Calculator",
    font=("Arial", 24)
)

title_label.pack(pady=20)


# First number
first_label = tk.Label(
    window,
    text="Enter your first number:"
)

first_label.pack()

first_number = tk.Entry(window)

first_number.pack(pady=5)


# Second number
second_label = tk.Label(
    window,
    text="Enter your second number:"
)

second_label.pack()

second_number = tk.Entry(window)

second_number.pack(pady=5)


# Operation selection
operation_var = tk.IntVar()

operation_var.set(1)


addition = tk.Radiobutton(
    window,
    text="Addition",
    variable=operation_var,
    value=1
)

addition.pack()


subtraction = tk.Radiobutton(
    window,
    text="Subtraction",
    variable=operation_var,
    value=2
)

subtraction.pack()


multiplication = tk.Radiobutton(
    window,
    text="Multiplication",
    variable=operation_var,
    value=3
)

multiplication.pack()


division = tk.Radiobutton(
    window,
    text="Division",
    variable=operation_var,
    value=4
)

division.pack()


# Calculate button
calculate_button = tk.Button(
    window,
    text="Calculate",
    command=perform_calculation
)

calculate_button.pack(pady=20)


# Result
result_label = tk.Label(
    window,
    text="Result:",
    font=("Arial", 16)
)

result_label.pack()


# Start the GUI
window.mainloop()