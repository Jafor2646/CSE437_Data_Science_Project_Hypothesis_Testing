import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Load your dataset from the provided file path
data_file_path = r"D:\Bracu Course\CSE437\Project\Note-Taking-Method.xlsx"

# Load the data into a DataFrame
df = pd.read_excel(data_file_path)
df = df.drop('note_method_form', axis=1)
# Ensure columns of interest are correctly identified
# Assuming the columns are "Note-Taking Method" and "CGPA"
# Adjust these names if they differ in the dataset

# Separate CGPA data into groups based on note-taking method
handwritten_cgpa = df[df["Note-Taking Method"] == "Handwritten notes"]["CGPA"]
digital_cgpa = df[df["Note-Taking Method"] == "Digital notes"]["CGPA"]

# Removing any outliers greater than 4.0 as CGPA cannot exceed this limit
handwritten_cgpa_clean = handwritten_cgpa[handwritten_cgpa <= 4.0]
digital_cgpa_clean = digital_cgpa[digital_cgpa <= 4.0]

# Step 1: Descriptive Statistics
descriptive_stats_handwritten = handwritten_cgpa_clean.describe()
descriptive_stats_digital = digital_cgpa_clean.describe()

# Step 2: Hypothesis Testing (t-test for independent samples)
t_stat, p_value = ttest_ind(handwritten_cgpa_clean, digital_cgpa_clean, equal_var=False)

# Step 3: Visualization
plt.figure(figsize=(10, 6))
plt.boxplot([handwritten_cgpa_clean, digital_cgpa_clean], 
            labels=["Handwritten Notes", "Digital Notes"], patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red', linewidth=2),
            whiskerprops=dict(color='blue', linewidth=1.5),
            capprops=dict(color='blue', linewidth=1.5))

# Adding title and labels
plt.title("Comparison of CGPA by Note-Taking Method", fontsize=14, fontweight='bold')
plt.ylabel("CGPA (0 - 4.0)", fontsize=12)
plt.xlabel("Note-Taking Method", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Showing the plot
plt.show()

# Step 4: Results Summary
results_summary = {
    "Descriptive Statistics (Handwritten Notes)": descriptive_stats_handwritten.to_dict(),
    "Descriptive Statistics (Digital Notes)": descriptive_stats_digital.to_dict(),
    "T-Test Results": {
        "T-Statistic": t_stat,
        "P-Value": p_value
    },
    "Conclusion": "Reject Null Hypothesis" if p_value < 0.05 else "Fail to Reject Null Hypothesis"
}

# Print Results
print("Descriptive Statistics (Handwritten Notes):")
print(descriptive_stats_handwritten)
print("\nDescriptive Statistics (Digital Notes):")
print(descriptive_stats_digital)
print("\nT-Test Results:")
print(f"T-Statistic: {t_stat}, P-Value: {p_value}")
print(f"Conclusion: {results_summary['Conclusion']}")
