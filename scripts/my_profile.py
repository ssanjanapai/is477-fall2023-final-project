import os
import pandas as pd
from ydata_profiling import ProfileReport

# Assuming this is the correct path to the dataset
data_path = './data/car_evaluation_dataset.csv'
column_names = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
# Create the 'profiling' directory if it doesn't exist
profiling_directory = "./profiling"
os.makedirs(profiling_directory, exist_ok=True)

# Load the dataset
df = pd.read_csv(data_path,header=None,names=column_names)

# Generate the profiling report
profile = ProfileReport(df, title="Pandas Profiling Report")

# Save the report to the 'profiling' directory
report_path = os.path.join(profiling_directory, "report.html")
profile.to_file(report_path)
