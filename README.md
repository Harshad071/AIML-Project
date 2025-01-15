# Comprehensive Analysis of Crop Yield Prediction and Input Optimization Using Machine Learning

## Introduction

This project aims to leverage machine learning techniques to predict crop yield, optimize input usage, and assist in agricultural decision-making. It includes detailed analyses and tools for:

- Predicting the effect of annual rainfall on crop yield.
- Recommending optimal fertilizer and pesticide usage.
- Yield prediction based on state-specific conditions.

A user-friendly interface was developed using Tkinter for real-time interaction and predictions.

---

## Features

1. **Rainfall Impact on Yield Prediction**
   - Inputs: Annual Rainfall, Cultivated Area, Fertilizer, Pesticide, Crop Type.
   - Model: Regression Forest.
   - Metrics: R², MAE, MSE.
   - Insights: Highlights the need for irrigation planning and optimized input usage.

2. **Optimal Fertilizer and Pesticide Recommendation**
   - Model: Regression Forest with feature engineering.
   - Outputs: Suggested optimal levels for fertilizers and pesticides per crop.

3. **State-based Yield Prediction**
   - Inputs: State, Area, Annual Rainfall, Fertilizer, Pesticide, Crop, Season.
   - Outputs: Region-specific yield predictions and input optimization.

4. **Tkinter GUI**
   - Real-time predictions with an easy-to-use interface.
   - Input fields for rainfall, fertilizers, pesticides, and other features.
   - Displays yield predictions and recommendations interactively.

---

## Methodology

1. **Data Preprocessing**
   - Normalized numerical inputs.
   - One-hot encoded categorical variables (e.g., Crop, Season).
   - Handled missing values effectively.

2. **Model Development**
   - Chosen Model: Regression Forest for its accuracy and interpretability.
   - Metrics: High R², low MAE and MSE validated the model's reliability.

3. **Feature Engineering**
   - Combined features to model interactions.
   - Incorporated regional and seasonal trends.

---

## Installation

### Prerequisites
- Python 3.8+
- Required libraries: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `tkinter`.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Harshad071/AIML-Project.git
   cd AIML-Project
## Code and Notebooks

### Feature Engineering
The repository includes a Jupyter Notebook for **Feature Engineering**, which performs the following:
- Handles missing values using appropriate strategies for numerical and categorical columns.
- Encodes categorical variables using `LabelEncoder`.
- Scales numerical features using `StandardScaler` for improved model performance.
- Saves the cleaned and preprocessed data for further analysis.

**File:** `feature_engineering.ipynb`

### Model Training
The **Model Training** notebook demonstrates:
- Training multiple models for various prediction tasks, including classification and regression.
- Tasks covered:
  1. Seasonal crop yield comparison (classification).
  2. Rainfall impact on yield prediction (regression).
  3. Optimal fertilizer and pesticide recommendation (regression).
  4. State-based yield prediction (regression).
- Saving all trained models in a single `.pkl` file for easy reuse.

**File:** `model_training.ipynb`

> **Tip:** To replicate the results:
> 1. Ensure the dataset file `crop_yield.csv` is placed in the correct directory.
> 2. Run the notebooks in sequence:
>    - Start with `feature_engineering.ipynb` to preprocess the data.
>    - Proceed with `model_training.ipynb` to train and save the models.
> 3. Use the saved models (`all_models.pkl`) for predictions in downstream tasks.

### Visualization
The notebooks also include:
- Histograms, boxplots, and count plots to explore data distributions and detect outliers.
- A correlation heatmap to analyze relationships between numerical features.

These visualizations provide valuable insights into the dataset and inform feature engineering decisions.

