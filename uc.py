import tkinter as tk
from tkinter import ttk, messagebox

def convert_length(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254
    }
    if from_unit in length_units and to_unit in length_units:
        return value * (length_units[from_unit] / length_units[to_unit])
    else:
        raise ValueError("Invalid length units.")

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "kilograms": 1,
        "grams": 0.001,
        "milligrams": 0.000001,
        "pounds": 0.453592,
        "ounces": 0.0283495
    }
    if from_unit in weight_units and to_unit in weight_units:
        return value * (weight_units[from_unit] / weight_units[to_unit])
    else:
        raise ValueError("Invalid weight units.")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return (value - 273.15) * 9/5 + 32
    elif from_unit == to_unit:
        return value
    else:
        raise ValueError("Invalid temperature units.")

def perform_conversion():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get().lower()
        to_unit = combo_to.get().lower()
        conversion_type = combo_type.get().lower()

        if conversion_type == "length":
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type == "weight":
            result = convert_weight(value, from_unit, to_unit)
        elif conversion_type == "temperature":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            raise ValueError("Invalid conversion type.")

        label_result.config(text=f"Result: {result:.4f} {to_unit}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def update_units(event):
    conversion_type = combo_type.get().lower()
    if conversion_type == "length":
        units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"]
    elif conversion_type == "weight":
        units = ["kilograms", "grams", "milligrams", "pounds", "ounces"]
    elif conversion_type == "temperature":
        units = ["celsius", "fahrenheit", "kelvin"]
    else:
        units = []

    combo_from.config(values=units)
    combo_to.config(values=units)
    combo_from.set("")
    combo_to.set("")

# Create the main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x300")
root.config(bg="#ee1c7b")  # Set background color of the main window

# Create a style for ttk widgets
style = ttk.Style()
style.configure("TLabel", background="#f0f8ff", foreground="#333333")
style.configure("TCombobox", padding=5)
style.configure("TButton", background="#ee1c7b", foreground="red", padding=5)

# Input value
label_value = ttk.Label(root, text="Value:")
label_value.pack(pady=5)
entry_value = tk.Entry(root, bg="#ffffff", fg="#000000")
entry_value.pack(pady=5)

# Conversion type
label_type = ttk.Label(root, text="Conversion Type:")
label_type.pack(pady=5)
combo_type = ttk.Combobox(root, values=["Length", "Weight", "Temperature"])
combo_type.bind("<<ComboboxSelected>>", update_units)
combo_type.pack(pady=5)

# From unit
label_from = ttk.Label(root, text="From Unit:")
label_from.pack(pady=5)
combo_from = ttk.Combobox(root)
combo_from.pack(pady=5)

# To unit
label_to = ttk.Label(root, text="To Unit:")
label_to.pack(pady=5)
combo_to = ttk.Combobox(root)
combo_to.pack(pady=5)

# Convert button
button_convert = tk.Button(root, text="Convert", command=perform_conversion, bg="#ffff00", fg="black", relief=tk.FLAT)
button_convert.pack(pady=10)

# Result label
label_result = ttk.Label(root, text="Result: ")
label_result.pack(pady=5)

# Run the application
root.mainloop()
