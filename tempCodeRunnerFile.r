import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# Path for saving the updated dataset
CSV_FILE = 'crop_production_data.csv'

# Ensure the CSV file exists with proper headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["State_Name", "District_Name", "Crop_Year", "Season", "Crop", "Area", "Production"])

# Function to save data to the CSV file
def save_data():
    state_name = state_entry.get()
    district_name = district_entry.get()
    crop_year = crop_year_entry.get()
    season = season_var.get()
    crop = crop_entry.get()
    area = area_entry.get()
    production = production_entry.get()

    # Validate inputs
    if not state_name or not district_name or not crop_year or not season or not crop or not area or not production:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        crop_year = int(crop_year)
        area = float(area)
        production = float(production)
    except ValueError:
        messagebox.showerror("Error", "Crop Year, Area, and Production must be numeric values!")
        return

    # Append data to the CSV file
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([state_name, district_name, crop_year, season, crop, area, production])

    # Clear the input fields
    state_entry.delete(0, tk.END)
    district_entry.delete(0, tk.END)
    crop_year_entry.delete(0, tk.END)
    crop_entry.delete(0, tk.END)
    area_entry.delete(0, tk.END)
    production_entry.delete(0, tk.END)
    season_var.set("Select Season")

    messagebox.showinfo("Success", "Data saved successfully!")

# Create the main application window
root = tk.Tk()
root.title("Crop Production Input")

# State Name
state_label = tk.Label(root, text="State Name:")
state_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
state_entry = tk.Entry(root)
state_entry.grid(row=0, column=1, padx=10, pady=5)

# District Name
district_label = tk.Label(root, text="District Name:")
district_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
district_entry = tk.Entry(root)
district_entry.grid(row=1, column=1, padx=10, pady=5)

# Crop Year
crop_year_label = tk.Label(root, text="Crop Year:")
crop_year_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
crop_year_entry = tk.Entry(root)
crop_year_entry.grid(row=2, column=1, padx=10, pady=5)

# Season
season_label = tk.Label(root, text="Season:")
season_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
season_var = tk.StringVar(value="Select Season")
season_dropdown = ttk.Combobox(root, textvariable=season_var, state="readonly")
season_dropdown["values"] = ["Rabi", "Kharif", "Summer", "Winter", "Whole Year"]
season_dropdown.grid(row=3, column=1, padx=10, pady=5)

# Crop
crop_label = tk.Label(root, text="Crop:")
crop_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
crop_entry = tk.Entry(root)
crop_entry.grid(row=4, column=1, padx=10, pady=5)

# Area
area_label = tk.Label(root, text="Area (ha):")
area_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
area_entry = tk.Entry(root)
area_entry.grid(row=5, column=1, padx=10, pady=5)

# Production
production_label = tk.Label(root, text="Production (tons):")
production_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
production_entry = tk.Entry(root)
production_entry.grid(row=6, column=1, padx=10, pady=5)

# Save Button
save_button = tk.Button(root, text="Save", command=save_data)
save_button.grid(row=7, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
