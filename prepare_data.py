import pandas as pd

# List of input files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

# Read and combine all CSV files
df = pd.concat([pd.read_csv(file) for file in files])

# Keep only Pink Morsel rows
df = df[df["product"] == "pink morsel"]

# Remove the $ sign and convert price to number
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Calculate sales
df["sales"] = df["price"] * df["quantity"]

# Keep only required columns
output = df[["sales", "date", "region"]]

# Save output
output.to_csv("formatted_output.csv", index=False)

print("formatted_output.csv has been created successfully!")