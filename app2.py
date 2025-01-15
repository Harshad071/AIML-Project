import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import numpy as np
from PIL import Image, ImageTk
# Load the models from the .pkl file
with open('all_models.pkl', 'rb') as file:
    models = pickle.load(file)

# Extract individual models
seasonal_crop_yield_model = models['seasonal_classifier']
rainfall_impact_model = models['rainfall_regressor']
optimal_fertilizer_model = models['fertilizer_regressor']
state_based_yield_model = models['state_regressor']

# Input options
crops = ['Arecanut', 'Arhar/Tur', 'Castor seed', 'Coconut', 'Cotton(lint)', 
         'Dry chillies', 'Gram', 'Jute', 'Linseed', 'Maize', 'Mesta', 'Niger seed', 
         'Onion', 'Other Rabi pulses', 'Potato', 'Rapeseed & Mustard', 'Rice', 
         'Sesamum', 'Small millets', 'Sugarcane', 'Sweet potato', 'Tapioca', 
         'Tobacco', 'Turmeric', 'Wheat', 'Bajra', 'Black pepper', 'Cardamom', 
         'Coriander', 'Garlic', 'Ginger', 'Groundnut', 'Horse-gram', 'Jowar', 
         'Ragi', 'Cashewnut', 'Banana', 'Soyabean', 'Barley', 'Khesari', 'Masoor', 
         'Moong(Green Gram)', 'Other Kharif pulses', 'Safflower', 'Sannhamp', 
         'Sunflower', 'Urad', 'Peas & beans (Pulses)', 'other oilseeds', 
         'Other Cereals', 'Cowpea(Lobia)', 'Oilseeds total', 'Guar seed', 
         'Other Summer Pulses', 'Moth']

seasons = ['Whole Year', 'Kharif', 'Rabi', 'Autumn', 'Summer', 'Winter']
states = ['Assam', 'Karnataka', 'Kerala', 'Meghalaya', 'West Bengal', 'Puducherry', 
          'Goa', 'Andhra Pradesh', 'Tamil Nadu', 'Odisha', 'Bihar', 'Gujarat', 
          'Madhya Pradesh', 'Maharashtra', 'Mizoram', 'Punjab', 'Uttar Pradesh', 
          'Haryana', 'Himachal Pradesh', 'Tripura', 'Nagaland', 'Chhattisgarh', 
          'Uttarakhand', 'Jharkhand', 'Delhi', 'Manipur', 'Jammu and Kashmir', 
          'Telangana', 'Arunachal Pradesh', 'Sikkim']

# Create the main application window
root = tk.Tk()
root.title("Crop Yield Prediction Models")
root.geometry("1700x1100")

# Load the background image
background_image = Image.open(r"D:\Users\mihar\OneDrive\Desktop\AIml Project\pexels-quang-nguyen-vinh-222549-2132250.jpg")  # Replace with the path to your image
background_image = background_image.resize((1700, 1100), Image.Resampling.LANCZOS)  # Resize to fit the window
bg = ImageTk.PhotoImage(background_image)

# Create a Label widget to display the background image in the root window
bg_label = tk.Label(root, image=bg)
bg_label.place(relwidth=1, relheight=1)  # Make the background fill the entire window

# Create the main frame for navigation
main_frame = tk.Frame(root)
main_frame.place(relwidth=1, relheight=1)  # Use the entire space of the window

# Create a Label for the main frame background
main_frame_bg_label = tk.Label(main_frame, image=bg)  # Reuse the same background image
main_frame_bg_label.place(relwidth=1, relheight=1)  # Make the background fill the frame


def navigate_to_frame(frame):
    # Destroy any existing widgets in the main window
    for widget in root.winfo_children():
        widget.pack_forget()
    
    # Safeguard to ensure the frame exists
    if frame:
        frame.pack(expand=True, fill="both")


def create_rainfall_impact_frame():
    frame = tk.Frame(root, bg="white", padx=20, pady=20)
    frame.place(width=700, height=500)  # Set the frame size

    # Add background image
    bg_image = Image.open(r"D:\Users\mihar\OneDrive\Desktop\AIml Project\pexels-enginakyurt-1435904.jpg")  # Replace with your image path
    bg_image = bg_image.resize((1800, 1400), Image.Resampling.LANCZOS)  # Resize image to fit the frame size
    bg_image = ImageTk.PhotoImage(bg_image)
    
    # Store reference to avoid garbage collection
    frame.bg_image = bg_image  # Prevent image from being garbage collected
    bg_label = tk.Label(frame, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place background image

    # Create a new frame for input fields and center it within the main frame
    input_frame = tk.Frame(frame, bg="white", padx=20, pady=20)
    input_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center this frame within the main frame

    # Set the column and row weights to center content inside the input_frame
    input_frame.grid_columnconfigure(0, weight=1)
    input_frame.grid_columnconfigure(1, weight=3)
    input_frame.grid_rowconfigure(0, weight=1)
    input_frame.grid_rowconfigure(1, weight=1)
    input_frame.grid_rowconfigure(2, weight=1)
    input_frame.grid_rowconfigure(3, weight=1)
    input_frame.grid_rowconfigure(4, weight=1)
    input_frame.grid_rowconfigure(5, weight=1)
    input_frame.grid_rowconfigure(6, weight=1)
    input_frame.grid_rowconfigure(7, weight=1)

    # Title Label (Centered inside the input frame)
    tk.Label(input_frame, text="Rainfall Impact on Yield Prediction", font=("Arial", 16), bg="white").grid(row=0, columnspan=2, pady=10)

    # Annual Rainfall input (Centered)
    tk.Label(input_frame, text="Annual Rainfall (mm):", bg="white").grid(row=1, column=0, sticky='w', pady=5)
    rainfall_entry = tk.Entry(input_frame, width=30)
    rainfall_entry.grid(row=1, column=1, pady=5, padx=10, sticky='ew')

    # Area input (Centered)
    tk.Label(input_frame, text="Area (ha):", bg="white").grid(row=2, column=0, sticky='w', pady=5)
    area_entry = tk.Entry(input_frame, width=30)
    area_entry.grid(row=2, column=1, pady=5, padx=10, sticky='ew')

    # Fertilizer input (Centered)
    tk.Label(input_frame, text="Fertilizer (kg/ha):", bg="white").grid(row=3, column=0, sticky='w', pady=5)
    fertilizer_entry = tk.Entry(input_frame, width=30)
    fertilizer_entry.grid(row=3, column=1, pady=5, padx=10, sticky='ew')

    # Pesticide input (Centered)
    tk.Label(input_frame, text="Pesticide (kg/ha):", bg="white").grid(row=4, column=0, sticky='w', pady=5)
    pesticide_entry = tk.Entry(input_frame, width=30)
    pesticide_entry.grid(row=4, column=1, pady=5, padx=10, sticky='ew')

    # Crop input (Centered)
    tk.Label(input_frame, text="Crop:", bg="white").grid(row=5, column=0, sticky='w', pady=5)
    crop_var = ttk.Combobox(input_frame, values=crops, state="readonly", width=28)
    crop_var.grid(row=5, column=1, pady=5, padx=10, sticky='ew')
    crop_var.set(crops[0])

    # Output display (Prediction result)
    result_label = tk.Label(input_frame, text="", font=("Arial", 14), bg="lightyellow", width=40, height=2, anchor="center")
    result_label.grid(row=6, columnspan=2, pady=20, padx=10)

    # Prediction function
    def predict_rainfall_impact():
        try:
            # Collect inputs
            inputs = [
                float(rainfall_entry.get()),     # Annual Rainfall
                float(area_entry.get()),         # Area
                float(fertilizer_entry.get()),   # Fertilizer
                float(pesticide_entry.get()),    # Pesticide
                crops.index(crop_var.get())      # Crop as index
            ]

            # Predict and display result
            result = rainfall_impact_model.predict([inputs])[0]
            result_label.config(text=f"Predicted Yield: {result:.2f} tons")
        except ValueError:
            messagebox.showerror("Input Error", "Please ensure all fields are filled and valid.")
        except Exception as e:
            messagebox.showerror("Error", f"Prediction Failed: {str(e)}")

    # Predict button (Centered)
    tk.Button(input_frame, text="Predict", command=predict_rainfall_impact, bg="green", fg="white").grid(row=7, columnspan=2, pady=10)

    # Back button (Centered)
    tk.Button(input_frame, text="Back", command=lambda: navigate_to_frame(main_frame), bg="red", fg="white").grid(row=8, columnspan=2, pady=10)

    # Navigate to this frame
    navigate_to_frame(frame)


def predict_optimal_fertilizer(crop_var, area_entry, production_entry, rainfall_entry, season_var):
    try:
        # Collect inputs
        inputs = [
            crops.index(crop_var.get()),         # Crop as index
            float(area_entry.get()),            # Area
            float(production_entry.get()),      # Production
            float(rainfall_entry.get()),        # Annual Rainfall
            seasons.index(season_var.get())     # Season as index
        ]

        # Predict the optimal fertilizer
        fertilizer = optimal_fertilizer_model.predict([inputs])[0]
        messagebox.showinfo("Prediction Result", f"Recommended Fertilizer: {fertilizer:.2f} kg/ha")
    except ValueError:
        messagebox.showerror("Input Error", "Please ensure all fields are filled and valid.")
    except Exception as e:
        messagebox.showerror("Error", f"Prediction Failed: {str(e)}")

# Create the frame for inputs and buttons
def create_optimal_fertilizer_frame():
    # Create a frame with padding
    frame = tk.Frame(root, bg="white", padx=20, pady=20)
    frame.place(width=700, height=500)  # Set frame size to ensure it fits well on screen

    # Add background image (same as previous frame)
    bg_image = Image.open(r"D:\Users\mihar\OneDrive\Desktop\AIml Project\pexels-pixabay-325944.jpg")  # Replace with your image path
    bg_image = bg_image.resize((1600, 1100), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(bg_image)
    
    # Store reference to avoid garbage collection
    frame.bg_image = bg_image  # Prevent image from being garbage collected
    bg_label = tk.Label(frame, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place background image

    # Create a new frame for input fields and align it in the middle of the main frame
    input_frame = tk.Frame(frame, bg="white", padx=20, pady=20)
    input_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center this frame within the main frame

    # Title Label (Centered inside the input frame)
    tk.Label(input_frame, text="Optimal Fertilizer Prediction", font=("Arial", 16), bg="white").grid(row=0, columnspan=2, pady=10)

    # Set the column and row weights to center content inside the input_frame
    input_frame.grid_columnconfigure(0, weight=1)
    input_frame.grid_columnconfigure(1, weight=3)
    input_frame.grid_rowconfigure(0, weight=1)
    input_frame.grid_rowconfigure(1, weight=1)
    input_frame.grid_rowconfigure(2, weight=1)
    input_frame.grid_rowconfigure(3, weight=1)
    input_frame.grid_rowconfigure(4, weight=1)
    input_frame.grid_rowconfigure(5, weight=1)
    input_frame.grid_rowconfigure(6, weight=1)
    input_frame.grid_rowconfigure(7, weight=1)

    # Crop input (Centered)
    tk.Label(input_frame, text="Crop:", bg="white").grid(row=1, column=0, sticky='w', pady=5)
    crop_var = ttk.Combobox(input_frame, values=crops, state="readonly", width=18)
    crop_var.grid(row=1, column=1, pady=5, sticky='ew')  # Center horizontally
    crop_var.set(crops[0])

    # Area input (Centered)
    tk.Label(input_frame, text="Area (ha):", bg="white").grid(row=2, column=0, sticky='w', pady=5)
    area_entry = tk.Entry(input_frame, width=20)
    area_entry.grid(row=2, column=1, pady=5, sticky='ew')  # Center horizontally

    # Production input (Centered)
    tk.Label(input_frame, text="Production (tons):", bg="white").grid(row=3, column=0, sticky='w', pady=5)
    production_entry = tk.Entry(input_frame, width=20)
    production_entry.grid(row=3, column=1, pady=5, sticky='ew')  # Center horizontally

    # Annual Rainfall input (Centered)
    tk.Label(input_frame, text="Annual Rainfall (mm):", bg="white").grid(row=4, column=0, sticky='w', pady=5)
    rainfall_entry = tk.Entry(input_frame, width=20)
    rainfall_entry.grid(row=4, column=1, pady=5, sticky='ew')  # Center horizontally

    # Season input (Centered)
    tk.Label(input_frame, text="Season:", bg="white").grid(row=5, column=0, sticky='w', pady=5)
    season_var = ttk.Combobox(input_frame, values=seasons, state="readonly", width=18)
    season_var.grid(row=5, column=1, pady=5, sticky='ew')  # Center horizontally
    season_var.set(seasons[0])

    # Buttons inside the input frame (Centered)
    tk.Button(input_frame, text="Predict", command=lambda: predict_optimal_fertilizer(crop_var, area_entry, production_entry, rainfall_entry, season_var), bg="green", fg="white").grid(row=6, columnspan=2, pady=10)
    tk.Button(input_frame, text="Back", command=lambda: navigate_to_frame(main_frame), bg="red", fg="white").grid(row=7, columnspan=2, pady=10)

    # Navigate to this frame
    navigate_to_frame(frame)


# Function to create input forms for State-based Yield Prediction
def create_state_based_yield_frame():
    # Create the main frame
    frame = tk.Frame(root, bg="white", padx=20, pady=20)
    frame.place(width=700, height=500)  # Set frame size to ensure it fits well on screen

    # Add background image to the main frame
    bg_image = Image.open(r"D:\Users\mihar\OneDrive\Desktop\AIml Project\pexels-blooddrainer-221016.jpg")  # Replace with your image path
    bg_image = bg_image.resize((1600, 1100), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(bg_image)
    
    # Store reference to avoid garbage collection
    frame.bg_image = bg_image  # Prevent image from being garbage collected
    bg_label = tk.Label(frame, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Place background image

    # Create a new frame for input fields and align it in the middle of the main frame
    input_frame = tk.Frame(frame, bg="white", padx=20, pady=20)
    input_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center this frame within the main frame

    # Title Label (Centered inside the input frame)
    tk.Label(input_frame, text="State-based Yield Prediction", font=("Arial", 16), bg="white").grid(row=0, columnspan=2, pady=10)

    # Set the column and row weights to center content inside the input_frame
    input_frame.grid_columnconfigure(0, weight=1)
    input_frame.grid_columnconfigure(1, weight=3)
    input_frame.grid_rowconfigure(0, weight=1)
    input_frame.grid_rowconfigure(1, weight=1)
    input_frame.grid_rowconfigure(2, weight=1)
    input_frame.grid_rowconfigure(3, weight=1)
    input_frame.grid_rowconfigure(4, weight=1)
    input_frame.grid_rowconfigure(5, weight=1)
    input_frame.grid_rowconfigure(6, weight=1)
    input_frame.grid_rowconfigure(7, weight=1)
    input_frame.grid_rowconfigure(8, weight=1)

    # State input
    tk.Label(input_frame, text="State:", bg="white").grid(row=1, column=0, sticky='w', pady=5)
    state_var = ttk.Combobox(input_frame, values=states, state="readonly", width=18)
    state_var.grid(row=1, column=1, pady=5, sticky='ew')
    state_var.set(states[0])

    # Area input
    tk.Label(input_frame, text="Area (ha):", bg="white").grid(row=2, column=0, sticky='w', pady=5)
    area_entry = tk.Entry(input_frame, width=20)
    area_entry.grid(row=2, column=1, pady=5, sticky='ew')

    # Production input
    tk.Label(input_frame, text="Production (tons):", bg="white").grid(row=3, column=0, sticky='w', pady=5)
    production_entry = tk.Entry(input_frame, width=20)
    production_entry.grid(row=3, column=1, pady=5, sticky='ew')

    # Annual Rainfall input
    tk.Label(input_frame, text="Annual Rainfall (mm):", bg="white").grid(row=4, column=0, sticky='w', pady=5)
    rainfall_entry = tk.Entry(input_frame, width=20)
    rainfall_entry.grid(row=4, column=1, pady=5, sticky='ew')

    # Fertilizer input
    tk.Label(input_frame, text="Fertilizer (kg/ha):", bg="white").grid(row=5, column=0, sticky='w', pady=5)
    fertilizer_entry = tk.Entry(input_frame, width=20)
    fertilizer_entry.grid(row=5, column=1, pady=5, sticky='ew')

    # Pesticide input
    tk.Label(input_frame, text="Pesticide (kg/ha):", bg="white").grid(row=6, column=0, sticky='w', pady=5)
    pesticide_entry = tk.Entry(input_frame, width=20)
    pesticide_entry.grid(row=6, column=1, pady=5, sticky='ew')

    # Season input
    tk.Label(input_frame, text="Season:", bg="white").grid(row=7, column=0, sticky='w', pady=5)
    season_var = ttk.Combobox(input_frame, values=seasons, state="readonly", width=18)
    season_var.grid(row=7, column=1, pady=5, sticky='ew')
    season_var.set(seasons[0])

    def predict_state_yield():
        try:
            # Gather inputs
            inputs = [
                states.index(state_var.get()),    # State as index
                float(area_entry.get()),          # Area
                float(production_entry.get()),    # Production
                float(rainfall_entry.get()),      # Annual Rainfall
                float(fertilizer_entry.get()),    # Fertilizer
                float(pesticide_entry.get()),     # Pesticide
                seasons.index(season_var.get())   # Season as index
            ]

            # Prediction
            yield_prediction = state_based_yield_model.predict([inputs])[0]
            messagebox.showinfo("Prediction Result", f"Predicted Yield: {yield_prediction:.2f} tons")
        except Exception as e:
            messagebox.showerror("Error", f"Prediction Failed: {str(e)}")

    # Buttons inside the input frame
    tk.Button(input_frame, text="Predict", command=predict_state_yield, bg="green", fg="white").grid(row=8, columnspan=2, pady=10)
    tk.Button(input_frame, text="Back", command=lambda: navigate_to_frame(main_frame), bg="red", fg="white").grid(row=9, columnspan=2, pady=10)
    
    navigate_to_frame(frame)

# Main menu options
tk.Label(main_frame, text="Crop Yield Prediction", font=("Arial", 26), bg="white").pack(pady=35)

tk.Button(main_frame, text="Rainfall Impact on Yield Prediction", command=create_rainfall_impact_frame, width=40, height=2, bg="blue", fg="white").pack(pady=10)
tk.Button(main_frame, text="Optimal Fertilizer Prediction", command=create_optimal_fertilizer_frame, width=40, height=2, bg="blue", fg="white").pack(pady=10)
tk.Button(main_frame, text="State-based Yield Prediction", command=create_state_based_yield_frame, width=40, height=2, bg="blue", fg="white").pack(pady=10)

root.mainloop()
