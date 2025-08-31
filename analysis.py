import pandas as pd

# Load dataset
file_path = "IPL sample data.xlsx"
df = pd.read_excel(file_path)

# Drop fully empty rows/columns
df = df.dropna(how="all").dropna(axis=1, how="all")

print("✅ Available Columns:", df.columns.tolist())

# Build a summary of fielding stats
summary = {
    "Good Pick": df["Y->"].count() if "Y->" in df.columns else 0,
    "Clean Pick": df["Clean Pick"].count() if "Clean Pick" in df.columns else 0,
    "Fumble": df["Fumble"].count() if "Fumble" in df.columns else 0,
    "Catch": df["Catch"].count() if "Catch" in df.columns else 0,
    "Dropped Catch": df["Dropped Catch"].count() if "Dropped Catch" in df.columns else 0,
    "Stumping": df["Stumping"].count() if "Stumping" in df.columns else 0,
}

# Convert to DataFrame
summary_df = pd.DataFrame([summary])

print("\n📊 Fielding Summary:")
print(summary_df)

# Save to Excel for easy viewing
summary_df.to_excel("fielding_summary.xlsx", index=False)
print("\n✅ Saved summary to 'fielding_summary.xlsx'")
