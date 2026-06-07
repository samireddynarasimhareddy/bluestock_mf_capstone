# Bluestock Mutual Fund Analytics Capstone Project

## 📌 Project Overview

This project is an end-to-end Mutual Fund Analytics solution developed as part of the Bluestock Data Analyst Capstone Program.

The project analyzes mutual fund data using Python, SQLite, and Power BI to generate business insights related to Assets Under Management (AUM), SIP trends, fund performance, investor behavior, and portfolio holdings.

---

## 🎯 Objectives

* Build an automated ETL pipeline.
* Store cleaned data in SQLite.
* Perform Exploratory Data Analysis (EDA).
* Calculate mutual fund performance metrics.
* Create interactive Power BI dashboards.
* Generate business insights and recommendations.

---

## 🛠️ Technology Stack

| Tool         | Purpose                |
| ------------ | ---------------------- |
| Python       | Data Processing        |
| Pandas       | Data Analysis          |
| NumPy        | Numerical Computations |
| Matplotlib   | Visualization          |
| Seaborn      | Visualization          |
| SQLite       | Database               |
| Power BI     | Dashboard Development  |
| Git & GitHub | Version Control        |

---

## 📂 Project Structure

```text
bluestock_mf_capstone/

├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   └── etl_pipeline.py
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_Performance_Analytics.ipynb
│
├── dashboard/
│   └── Bluestock_MF_Dashboard.pbix
│
├── reports/
│   └── Bluestock_MF_Report.pdf
│
├── bluestock.db
├── requirements.txt
└── README.md
```

## 📊 Dataset Description

The project uses 10 mutual fund datasets:

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## ⚙️ ETL Pipeline

### Extract

* Load CSV files
* Validate dataset availability

### Transform

* Handle missing values
* Remove duplicates
* Standardize column names
* Convert data types

### Load

* Store cleaned data into SQLite Database

Output:

```text
bluestock.db
```

---

## 📈 Exploratory Data Analysis (EDA)

Analysis Performed:

* Missing Value Analysis
* Duplicate Analysis
* AUM Trend Analysis
* SIP Growth Analysis
* Fund Category Distribution
* Investor Trend Analysis
* Performance Comparison

Notebook:

```text
notebooks/01_EDA.ipynb
```

---

## 📉 Performance Analytics

Metrics Calculated:

### Return Metrics

* 1-Year Return
* 3-Year Return
* 5-Year Return

### Risk Metrics

* Standard Deviation
* Sharpe Ratio
* Risk Category

### Rankings

* Top Performing Funds
* Best Risk Adjusted Funds

Notebook:

```text
notebooks/02_Performance_Analytics.ipynb
```

---

# 📊 Power BI Dashboard

## Page 1: Executive Summary

KPIs:

* Total Funds
* Total AUM
* Total SIP Inflow
* Total Investors
* Average Return

---

## Page 2: AUM Analysis

Visualizations:

* Top Fund Houses by AUM
* Monthly AUM Trend
* Fund House Market Share

Filters:

* Fund House
* Year

---

## Page 3: SIP Trends

Visualizations:

* Monthly SIP Inflow Trend
* Payment Mode Distribution
* State-wise Investments

Filters:

* State
* Payment Mode

---

## Page 4: Fund Performance Dashboard

Visualizations:

* Top 10 Funds by 5-Year Return
* Risk vs Return Scatter Plot
* Expense Ratio vs Return
* Risk Category Distribution

Filters:

* Category
* Fund House

---

## Page 5: Portfolio Holdings Dashboard

Visualizations:

* Top Holdings
* Sector Allocation
* Market Capitalization Allocation
* Fund House Allocation

Filters:

* Fund House
* Sector

---

## 🔍 Key Insights

### AUM Analysis

* AUM increased consistently across major fund houses.
* Leading fund houses dominated market share.

### SIP Trends

* SIP inflows showed strong growth.
* Active SIP accounts increased year over year.

### Fund Performance

* High-return funds generally carried higher risk.
* Risk-adjusted returns identified top-performing schemes.

### Portfolio Analysis

* Financial and Technology sectors formed significant allocations.
* Large-cap holdings dominated portfolios.

---

## 💡 Business Recommendations

1. Promote SIP investments among new investors.
2. Focus on high-performing fund categories.
3. Improve portfolio diversification.
4. Monitor risk-adjusted performance regularly.
5. Increase exposure to emerging sectors.

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone <repository-url>
```

### Navigate to Project Folder

```bash
cd bluestock_mf_capstone
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

### Open Power BI Dashboard

```text
dashboard/Bluestock_MF_Dashboard.pbix
```

---

## 📦 Deliverables

* ETL Pipeline Script (.py)
* SQLite Database (.db)
* EDA Notebook (.ipynb)
* Performance Analytics Notebook (.ipynb)
* Power BI Dashboard (.pbix)
* Project Report (.pdf)
* GitHub Repository

---

## 👨‍💻 Author

**S. Narasimha Reddy**

Bluestock Mutual Fund Analytics Capstone Project

Year: 2026
