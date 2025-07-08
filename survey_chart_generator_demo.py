"""
survey_chart_generator_demo.py

This script demonstrates how to automate the generation of bar charts 
from survey data using pandas and matplotlib. All personal, student, or 
institution-specific data has been removed for demonstration purposes.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
import re

# ----------------------------
# Configuration (For Demo)
# ----------------------------

# Path to demo survey data (replace with your own CSV/XLSX in practice)
excel_file = "demo_survey_data.xlsx"  

# Folder to save output charts
output_folder = "output_charts"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Load Excel data (all data read as string for consistent formatting)
df = pd.read_excel(excel_file, dtype=str)

# ----------------------------
# Utility to clean column names for file saving
# ----------------------------
def clean_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

# ----------------------------
# Generate bar chart for each column in the dataset
# ----------------------------
for column in df.columns:
    plt.figure(figsize=(10, 5))

    # Clean data: remove blanks and NaNs
    filtered = df[column].dropna()
    filtered = filtered[filtered != ""]

    value_counts = filtered.value_counts()
    total = value_counts.sum()
    percentages = (value_counts / total * 100).round(0)

    # Plotting
    bars = plt.bar(value_counts.index.astype(str), value_counts.values, color='steelblue', edgecolor='black')

    # Add count + % labels
    for bar, count, percent in zip(bars, value_counts, percentages):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 f'{count} ({int(percent)}%)',
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("")
    # Save chart
    filename = clean_filename(column) + ".png"
    plt.savefig(os.path.join(output_folder, filename), bbox_inches='tight', dpi=300)
    plt.close()

print(f"✅ All charts saved in '{output_folder}' folder.")
