import pandas as pd
import numpy as np

# Load the dataset
file_path = 'threshold_dataset.csv'  # Replace with your dataset file path
data = pd.read_csv(file_path)

# Parse the EM Traces values into numerical arrays
data['EM Traces Parsed'] = data['EM Traces'].apply(
    lambda x: np.array([float(val) for val in x.split()])
)

# Calculate statistical properties for each trace
data['Mean'] = data['EM Traces Parsed'].apply(np.mean)

# Define thresholds for vulnerability
mean_lower_threshold = 0.45
mean_upper_threshold = 0.54

# Add the Vulnerable column
data['Vulnerable'] = data['Mean'].apply(
    lambda x: 'Yes' if x < mean_lower_threshold or x > mean_upper_threshold else 'No'
)

# Save the updated dataset
updated_file_path = 'updated_threshold_dataset.csv'  # Replace with your desired file path
data.to_csv(updated_file_path, index=False)

print(f"Updated dataset saved to {updated_file_path}")
