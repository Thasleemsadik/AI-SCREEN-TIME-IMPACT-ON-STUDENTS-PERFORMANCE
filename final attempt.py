import numpy as np
import pandas as pd
df=pd.read_excel(r"C:\Users\acer\Downloads\master file\final attempt for making project\cleaned excel for python.xlsx")
print(df.head())
print(df.shape)
print(df.dtypes)
#check column name
print(df.columns)
#check missing value
print(df.isnull().sum())
# check duplicate rows
print("Duplicate rows:", df.duplicated().sum())
#check duplicate student id
print("Duplicate Student IDs:",
      df["Student_ID"].duplicated().sum())
#remove duplicates
df=df.drop_duplicates(subset=["Student_ID"])
print(df)
#Check Student IDs
print("Number of Student IDs:", df["Student_ID"].nunique())
#Clean unwanted spaces
text_columns = df.select_dtypes(include=["object", "string"]).columns

for col in text_columns:
    df[col] = df[col].str.strip()
#Standardize Gender
df["Gender"] = df["Gender"].str.title()
#Standardize City names
city_corrections = {
    "Banglore": "Bangalore",
    "Chenni": "Chennai",
    "Hydrabad": "Hyderabad",
    "Kolkatha": "Kolkata",
    "Mumabi": "Mumbai"
}

df["City"] = df["City"].replace(city_corrections)
#Make sure numerical columns are numeric
numeric_columns = [
    "Age",
    "Daily_AI_Usage_Hrs",
    "Daily_SocialMedia_Hrs",
    "Daily_ScreenTime_Total_Hrs",
    "Daily_Study_Hrs",
    "Daily_Sleep_Hrs",
    "Daily_PhysicalActivity_Hrs",
    "Total_Daily_Hrs",
    "Attention_Span_Mins",
    "GPA_10",
    "Anxiety_Score_1_10"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="raise")
#Check the ranges
print(df["Age"].min())
print(df["Age"].max())
#GPA
print(df["GPA_10"].min())
print(df["GPA_10"].max())
#Anxiety
print(df["Anxiety_Score_1_10"].min())
print(df["Anxiety_Score_1_10"].max())
#Sleep
print(df["Daily_Sleep_Hrs"].min())
print(df["Daily_Sleep_Hrs"].max())
#Check categorical values
print(df["Gender"].value_counts())
print(df["Age_Group"].value_counts())
print(df["City"].value_counts())
print(df["Primary_AI_Tool"].value_counts())
#Final missing-value check
print("Total missing values:",
      df.isnull().sum().sum())
#Final duplicate check
print("Duplicate rows:",
      df.duplicated().sum())

print("Duplicate Student IDs:",
      df["Student_ID"].duplicated().sum())
#Check final shape
print("Final shape:", df.shape)
#Save the cleaned dataset
df.to_excel(
    "cleaned_dataset_reproduced.xlsx",
    index=False
)
print("Sucessfully coding done")
