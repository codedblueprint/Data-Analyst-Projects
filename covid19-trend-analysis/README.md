# COVID-19 Global Trends Analysis


### 📁 Project Summary

This project analyzes COVID-19 global trends using data from **Our World in Data**. It includes **time-series visualizations**, **vaccination progress**, **continent-level comparisons**, and **correlation analysis** (e.g., GDP vs vaccination rate). The analysis is performed using **Python (Pandas, Matplotlib, Seaborn)** and **SQLite for SQL-based exploration**.

---

### 📌 Objectives

* Analyze confirmed cases, death rates, and vaccinations globally and by country.
* Visualize monthly and daily trends.
* Compare regions and continents.
* Correlate GDP per capita with vaccination coverage.

---

### 📂 Files in This Repository

| File                     | Description                                            |
| ------------------------ | ------------------------------------------------------ |
| `owid-covid-data.csv`    | Original COVID-19 dataset from OWID                     |
| `cleaned_covid_data.csv` | Cleaned COVID-19 dataset from OWID                     |
| `gdp_per_capita.csv`     | Sample GDP per capita dataset for correlation analysis |
| `covid.db`               | SQLite database version of the cleaned dataset         |
| `covid_analysis.py`      | Python file with full analysis and visualizations      |
| `data loading.py`        | Python file with data loading and cleaning             |
| `queries.sql`            | SQL scripts used for data aggregation and insights     |
| `README.md`              | This file – documentation and project overview         |

---

### 🔧 Tools & Technologies

* Python (Pandas, Matplotlib, Seaborn)
* SQLite & SQL (via `sqlite3`)
* Jupyter Notebook
* Visual Studio Code (optional)
* Our World in Data COVID-19 dataset
* GDP data (World Bank or manually provided)

---

### 📈 Key Visualizations

* Global daily new cases (line chart)
* Vaccination rate per 100 people by country
* Total cases vs total deaths (log scale scatter plot)
* Monthly new cases (e.g., United Kingdom)
* Continent-level case & death comparisons (grouped bar chart)
* Pie chart of top 6 vaccinated countries
* Correlation heatmap: GDP per capita vs vaccination & death rate

---

### 🚀 How to Run This Project

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/covid19-analysis.git
   cd covid19-analysis
   ```

2. Install dependencies

   ```bash
   pip install pandas matplotlib seaborn jupyter
   ```

3. Launch Python
   
   covid_analysis



4. Run SQL in `covid.db` using DB Browser or VS Code + SQLTools

---

### 📚 Data Sources

* **COVID-19 Dataset**: [Our World in Data](https://github.com/owid/covid-19-data)
* **GDP per Capita**: [World Bank Open Data](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)

---

