# Retail Customer Segmentation Analysis

## 📊 Project Overview

This project analyzes retail customer sales data to generate business insights and perform customer segmentation.

It represents a **full end-to-end data pipeline**:

* Raw (dirty) CSV data
* Data cleaning with Python (pandas)
* SQLite database creation
* SQL-based business analysis
* Customer segmentation reporting

---

## ⚙️ Tech Stack

* Python
* pandas
* SQLite
* SQL
* CTE (Common Table Expressions)
* CASE WHEN
* Aggregations
* Revenue share analysis

---

## 📁 Project Structure

```text
retail-customer-segmentation-analysis/
│
├── data/
│   ├── raw_customer_data.csv
│   └── clean_customer_data.csv
│
├── outputs/
│   └── customer_segments_report.csv
│
├── scripts/
│   ├── clean_data.py
│   ├── load_to_sqlite.py
│   └── customer_analysis_report.py
│
├── sql/
│   └── sql_analysis.sql
│
├── sales.db
└── README.md
```

---

## 🧹 Data Cleaning

The raw dataset contained multiple data quality issues:

* Missing values
* Inconsistent date formats
* Mixed data types
* Duplicate rows
* Extra spaces in text fields

### Cleaning Steps:

1. Load raw CSV data
2. Standardize column names
3. Convert numeric columns
4. Normalize date formats
5. Handle missing values
6. Remove duplicates
7. Create business features:

   * `revenue`
   * `month`
8. Save cleaned dataset

---

## 🧠 SQL Analysis

The SQL layer performs business analytics including:

* Revenue by city
* Revenue by product category
* Monthly revenue trends
* Revenue share by city
* Revenue share by category
* Customer-level revenue contribution
* Customer segmentation

---

## 👥 Customer Segmentation Logic

Customers are segmented based on revenue contribution:

* **VIP** → revenue share ≥ 5%
* **Regular** → 3% ≤ revenue share < 5%
* **Low Value** → revenue share < 3%

---

## 📈 Key Insights

* Yerevan generates the highest revenue share
* Home and Electronics are top-performing categories
* A small number of customers drive a large portion of revenue
* Monthly trends reveal strong and weak sales periods
* Segmentation enables targeted marketing and retention strategies

---

## 📂 Outputs

The project generates:

```
outputs/customer_segments_report.csv
```

### Report Includes:

* `customer_name`
* `city`
* `orders_count`
* `total_revenue`
* `revenue_share`
* `customer_segment`

---

## ▶️ How to Run

### 1. Clean the raw data

```bash
python scripts/clean_data.py
```

### 2. Load cleaned data into SQLite

```bash
python scripts/load_to_sqlite.py
```

### 3. Generate customer segmentation report

```bash
python scripts/customer_analysis_report.py
```

---

## 💼 Business Value

This project helps businesses:

* Identify VIP customers
* Understand revenue concentration
* Analyze performance by city and category
* Improve customer retention strategies
* Support data-driven marketing decisions

---

## Author

**Grigor Hovhannisyan**
