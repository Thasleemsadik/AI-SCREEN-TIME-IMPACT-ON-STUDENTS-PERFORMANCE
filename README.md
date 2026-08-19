# AI & Screen Time Impact on Students' Academic Performance and Well-Being

> From messy data (7380 rows) to meaningful insights (7200 clean rows) — analyzing how AI usage, screen time, sleep, anxiety, study time & physical activity affect student GPA.

### 📸 Live Dashboard Preview

#### Page 1 - Overview: KPIs + Core Insights
![Overview Dashboard](images/dashboard_page1_overview.png)

#### Page 2 - Detailed Analysis by Age Group
![Detailed Analysis](images/dashboard_page2_detailed.png)

---

### 🔗 Dataset Source
- Raw dirty dataset from Kaggle (7380 rows with missing values, typos, duplicates) - `data/raw/`
- Cleaned version after Python preprocessing (7200 rows) - `data/cleaned/`

### 🧹 What I Did

**1. Data Cleaning with Python (Pandas)**
- Loaded raw Excel with `pandas`
- Checked `shape`, `dtypes`, `isnull().sum()`, `duplicated()`
- Removed duplicate `Student_ID` rows -> 7380 to 7200
- Trimmed unwanted spaces: `df[col].str.strip()`
- Standardized categorical values (Gender, City, Study Level etc.)
- Filled missing numeric with median, categorical with mode
- File: `scripts/data_cleaning.py`

**2. Feature Engineering - Created Levels**
- `AI_Usage_Level`, `SocialMedia_Level`, `Screen_Level`
- `Study_Level`, `Sleep_Level`, `PhysicalActivity_Level`
- `Anxiety_Level`, `GPA_Level`, `Attention_Level`, `Focus_Level`, `Age_Group`

**3. Exploratory Analysis**
- Average GPA: **7.35/10**
- Average Screen Time: **5.9 hrs**
- Average Study Time: **3.2 hrs**
- Average Anxiety: **5.9/10**
- Average Sleep: **6.9 hrs**
- Total Students after cleaning: **7200**

**4. Power BI Dashboard (2 Pages)**
*Page 1 - Overview:*
- GPA by Age_Group (Primary 8.7 -> College 6.4 - GPA decreases with age)
- Screen Time VS Study Level (Low Study = 8.7 hrs screen, High Study = 3.3 hrs)
- GPA by PhysicalActivity_Level (High activity 8.3 GPA vs Low 6.1)
- Sleep_Hrs vs Anxiety_Score - clear negative trend
- ScreenTime vs GPA_10 - strong negative correlation

*Page 2 - Detailed Analysis by Age Group:*
- Primary AI Tool Usage: ChatGPT, Gemini, Copilot, Perplexity, Canva AI, Grammarly, Photomath (~13-14% each)
- Study Time by Age_Group drops from 5.0 hrs (Primary) to 1.9 hrs (College)
- Study_Level Distribution: Medium 3.9K, High 2.0K, Low 1.3K
- Key Takeaways section included in dashboard

### 📁 Repo Structure
```
├── data/
│   ├── raw/Dirty_Student_Dataset_7380.xlsx
│   └── cleaned/cleaned_dataset_7200_rows.xlsx
├── scripts/
│   └── data_cleaning.py
├── powerbi/
│   └── dashboard.pbix
├── images/
│   ├── dashboard_page1_overview.png
│   └── dashboard_page2_detailed.png
├── docs/
│   └── Project_Report_With_Dashboards.docx
├── requirements.txt
├── .gitignore
└── README.md
```

### 🚀 How to Run the Cleaning Script
```bash
pip install -r requirements.txt
python scripts/data_cleaning.py
```

### 🛠️ Tech Stack
- Python, Pandas, NumPy
- Power BI for interactive dashboard
- Excel

### 📌 Key Takeaways
> Higher screen time and AI usage are associated with lower GPA, while study time and physical activity show positive associations with academic performance. Sleep, anxiety, social-media use and student level also show noticeable differences across groups.

### 📄 Full Documentation
Full report with screenshots: `docs/Project_Report_With_Dashboards.docx`

---
Made with ❤️ by Thasleem Sadik | Beginner Data Analyst | Chennai, India
