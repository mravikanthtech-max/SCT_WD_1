import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- FUNCTION ---------------- #
def convert_temperature():
    try:
        temp = float(entry_temp.get())
        from_unit = from_combo.get()
        to_unit = to_combo.get()

        celsius = 0
        result = 0

        # Convert to Celsius first
        if from_unit == "Celsius":
            celsius = temp

        elif from_unit == "Fahrenheit":
            celsius = (temp - 32) * 5 / 9

        elif from_unit == "Kelvin":
            celsius = temp - 273.15

        # Convert Celsius to target unit
        if to_unit == "Celsius":
            result = celsius

        elif to_unit == "Fahrenheit":
            result = (celsius * 9 / 5) + 32

        elif to_unit == "Kelvin":
            result = celsius + 273.15

        # Show Result
        result_label.config(
            text=f"{round(result, 2)} {to_unit}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number"
        )


# ---------------- MAIN WINDOW ---------------- #
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("700x500")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# ---------------- TITLE ---------------- #
title_label = tk.Label(
    root,
    text="Temperature Converter",
    font=("Arial", 26, "bold"),
    bg="#1e1e1e",
    fg="white"
)
title_label.pack(pady=25)

# ---------------- INPUT ---------------- #
entry_temp = tk.Entry(
    root,
    font=("Arial", 22),
    width=18,
    justify="center"
)
entry_temp.pack(pady=20)

# ---------------- DROPDOWNS ---------------- #
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=20)

from_combo = ttk.Combobox(
    frame,
    values=["Celsius", "Fahrenheit", "Kelvin"],
    font=("Arial", 16),
    state="readonly",
    width=12
)
from_combo.current(0)
from_combo.grid(row=0, column=0, padx=15)

arrow_label = tk.Label(
    frame,
    text="→",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="white"
)
arrow_label.grid(row=0, column=1)

to_combo = ttk.Combobox(
    frame,
    values=["Celsius", "Fahrenheit", "Kelvin"],
    font=("Arial", 16),
    state="readonly",
    width=12
)
to_combo.current(1)
to_combo.grid(row=0, column=2, padx=15)

# ---------------- BUTTON ---------------- #
convert_button = tk.Button(
    root,
    text="CONVERT",
    font=("Arial", 18, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=25,
    pady=10,
    command=convert_temperature
)
convert_button.pack(pady=30)

# ---------------- RESULT ---------------- #
result_label = tk.Label(
    root,
    text="Result Appears Here",
    font=("Arial", 28, "bold"),
    bg="#1e1e1e",
    fg="#00FFFF"
)
result_label.pack(pady=30)

# ---------------- RUN APP ---------------- #
root.mainloop()