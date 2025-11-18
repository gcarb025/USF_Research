import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
file_path = "./Biofilm_11.07.csv"
df = pd.read_csv(file_path)

# Drop the "Row" column
df = df.drop(columns=["Row"])
strain_cols = df.columns

# Calculate means and SEMs
means = df[strain_cols].mean()
sems = df[strain_cols].std(ddof=1) / np.sqrt(len(df))

# Set up figure
plt.figure(figsize=(9,6))

# Generate a color for each strain
colors = plt.cm.tab10(np.linspace(0, 1, len(strain_cols)))

# Plot bars with matching colors
x = np.arange(len(strain_cols))
plt.bar(x, means, yerr=sems, capsize=5, color=colors, edgecolor='black', label='Mean ± SEM')

# Plot individual replicate points with matching colors
for i, col in enumerate(strain_cols):
    plt.scatter([x[i]]*len(df), df[col], color=colors[i], edgecolors='black', alpha=0.8, zorder=3)

# Customize axes and labels
plt.xticks(x, strain_cols, rotation=45)
plt.ylabel("Absorbance$_{595}$", fontsize=12)
plt.xlabel("Strain", fontsize=12)
plt.title("Biofilm Formation per Strain", fontsize=14)
plt.tight_layout()

plt.show()
