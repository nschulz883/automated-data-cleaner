import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.preprocessing import MinMaxScaler 


file_path = input("enter a csv file path: ")
df = pd.read_csv(file_path)

original_shape = df.shape 

df = df.drop_duplicates()

numeric_cols = df.select_dtypes(include=np.number).columns
categorical_cols = df.select_dtypes(exclude = np.number).columns


for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)


for col in numeric_cols:
    df[f"{col}_squared"] = df[col] ** 2
    df[f"{col}_log"] = np.log1p(df[col])

df = pd.get_dummies(df, drop_first=True)

scaler = MinMaxScaler()
scaled_cols = df.select_dtypes(include=np.number).columns
df[scaled_cols] = scaler.fit_transform(df[scaled_cols])

df.to_csv("cleaned_data.csv", index=False)

with open("report.txt", "w") as f:
    f.write("AUTOMATED DATA CLEANING REPORT\n")
    f.write("="*40 + "\n\n")
    f.write(f"Original shape: {original_shape}\n")
    f.write(f"Final shape: {df.shape}\n\n")
    f.write("Numeric columns:\n")
    f.write(", ".join(numeric_cols) + "\n\n")
    f.write("Categorical columns:\n")
    f.write(", ".join(categorical_cols) + "\n")


for col in numeric_cols[:3]:  # limit plots
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.savefig(f"{col}_distribution.png")
    plt.close()


print(" Cleaning complete!")
print("Files generated:")
print("- cleaned_data.csv")
print("- report.txt")
print("- distribution plots")  
