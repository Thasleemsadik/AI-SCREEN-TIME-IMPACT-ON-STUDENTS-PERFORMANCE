# AI and Screen Time Impact on Students' Academic Performance and Well-Being

## 📌 Project Overview

This project analyzes the relationship between AI usage, screen time, study habits, sleep, physical activity, anxiety, attention, and students' academic performance.

The project follows an end-to-end data analytics workflow, beginning with data cleaning and preparation using Python and Pandas, followed by data transformation, correlation analysis, and interactive visualization using Power BI.

The raw Kaggle dataset contained **7,380 student records** with missing values, duplicate records, and inconsistent/incorrect entries. After cleaning and preprocessing, the final dataset contained **7,200 records** ready for analysis.

## 🎯 Project Objectives

* Analyze the relationship between screen time and academic performance.
* Examine the relationship between study hours and GPA.
* Analyze the association between screen time and anxiety levels.
* Understand the relationship between sleep and anxiety.
* Examine physical activity and academic performance.
* Compare student performance across different age groups.
* Identify patterns in students' lifestyle, technology usage, and well-being.
* Present the findings through an interactive Power BI dashboard.
* 

## 📊 Dataset

The dataset was obtained from Kaggle and contains information related to students' technology usage, lifestyle, well-being, and academic performance.

### Raw Dataset

* Records: **7,380**
* Contains missing values
* Contains duplicate records
* Contains inconsistent/typo-filled categorical values

### Cleaned Dataset

* Records: **7,200**
* Missing values handled
* Duplicate records removed
* Inconsistent values standardized
* Data prepared for analysis

## 🧹 Data Cleaning Using Python

Python and the Pandas library were used to prepare the raw dataset for analysis.

The major cleaning steps included:

1. Loading the raw dataset into Python.
2. Inspecting the dataset structure and data types.
3. Identifying missing values.
4. Handling missing values using appropriate Pandas techniques.
5. Identifying and removing duplicate records.
6. Detecting inconsistent and typo-filled categorical values.
7. Standardizing categorical values.
8. Checking numerical columns for consistency.
9. Validating the cleaned dataset.

**Raw records:** 7,380
**Final cleaned records:** 7,200

## 🔄 Data Transformation

After cleaning, numerical variables were transformed into meaningful levels/categories to make the analysis easier to understand.

Examples include:

* Study Hours → Study Level
* Screen Time → Screen Time Level
* Sleep Time → Sleep Level
* Anxiety Score → Anxiety Level
* Physical Activity → Physical Activity Level
* Focus Span → Focus Level
* Attention → Attention Level
* GPA → GPA/Performance Level

These transformed variables were used for comparative analysis and Power BI visualizations.

## 📈 Analysis Performed

The project analyzes several important relationships:

### Screen Time and Academic Performance

Examines whether different levels of screen time are associated with differences in students' GPA and academic performance.

### Study Hours and GPA

Analyzes how study patterns vary across students and how study hours are associated with academic performance.

### Screen Time and Anxiety

Examines whether students with higher screen-time levels also show differences in anxiety levels.

### Sleep and Anxiety

Analyzes the relationship between students' sleep levels and anxiety levels.

### Physical Activity and GPA

Examines whether physical activity levels are associated with differences in academic performance.

### Age-wise Analysis

Student performance and behavioral patterns are compared across different age/education groups.

## 🔎 Correlation Analysis

Correlation analysis was performed to identify relationships between important numerical variables.

The analysis focuses on variables such as:

* Daily Study Hours
* Total Screen Time
* Sleep Time
* Anxiety Level
* Physical Activity
* Focus Span
* GPA

Correlation values are used to identify the strength and direction of relationships between variables.

> **Note:** Correlation indicates an association between variables and does not necessarily prove causation.

## 📊 Power BI Dashboard

<img width="1366" height="720" alt="Screenshot 2026-08-19 121038" src="https://github.com/user-attachments/assets/48a680af-0af4-4a1b-9b3f-91462158e0a6" />
<img width="1366" height="720" alt="Screenshot 2026-08-19 121048" src="https://github.com/user-attachments/assets/36bb83f3-b360-4160-a199-7b0cf4d74964" />


An interactive Power BI dashboard was created to present the analysis in an easy-to-understand format.

The dashboard includes analysis of:

* Screen Time
* Study Level
* Sleep Level
* Anxiety Level
* Physical Activity
* GPA/Academic Performance
* Student demographics
* Relationships between behavioral and academic variables

Interactive filters and drill-through functionality allow users to explore the data at a deeper level.

## 🔄 Project Workflow

```text
Raw Kaggle Dataset
        ↓
7,380 Records
        ↓
Data Inspection
        ↓
Missing Value Handling
        ↓
Duplicate Removal
        ↓
Typo & Inconsistency Correction
        ↓
Data Standardization
        ↓
7,200 Cleaned Records
        ↓
Feature/Level Creation
        ↓
Exploratory Analysis
        ↓
Correlation Analysis
        ↓
Power BI Dashboard
        ↓
Insights & Findings
```

## 🛠️ Tools & Technologies

* **Python**
* **Pandas**
* **Jupyter Notebook**
* **Excel**
* **Power BI**
* **Data Cleaning**
* **Data Transformation**
* **Exploratory Data Analysis**
* **Correlation Analysis**
* **Data Visualization**

## 💡 Key Outcome

This project demonstrates an end-to-end data analytics workflow, from working with a messy real-world dataset to cleaning, transforming, analyzing, and visualizing the data.

The final Power BI dashboard provides an interactive way to explore how students' technology usage, study habits, lifestyle factors, well-being, and academic performance are related.

## 👤 Author

**Thasleem Sadik**
