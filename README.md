# 📊 Website Traffic Analysis

A **Flask-based Website Traffic Analysis Dashboard** that processes website traffic datasets, extracts key insights, and visualizes traffic patterns using interactive data visualizations. The application allows users to upload CSV datasets and automatically generates analytical charts based on available country, city, and date information.

The project demonstrates the practical application of **Python, Data Analytics, Data Visualization, and Web Development** to transform raw website traffic data into meaningful insights.

---

## 🚀 Features

* **📁 CSV File Upload:** Upload website traffic datasets through a web interface.
* **📈 Dataset Overview:** Display the total number of records and columns in the uploaded dataset.
* **🌍 Country-wise Traffic Analysis:** Identify the top 10 countries based on recorded website traffic events.
* **🏙️ City-wise Traffic Analysis:** Identify the top 10 cities based on recorded website traffic events.
* **📅 Daily Traffic Trends:** Visualize daily website activity using a line chart.
* **🔢 Geographic Insights:** Calculate the number of unique countries and cities represented in the dataset.
* **🧹 Data Preprocessing:** Normalize column names, remove completely empty rows, and handle different CSV encodings.
* **🔍 Automatic Column Detection:** Identify country, city, and date columns using supported column names.
* **📊 Automated Visualization:** Generate charts automatically when the required data is available.
* **🖥️ Web-based Dashboard:** Present analytical results through a Flask-powered dashboard.

---

## 🛠️ Technologies Used

| Technology | Purpose                                    |
| ---------- | ------------------------------------------ |
| Python     | Core application logic and data processing |
| Flask      | Web application framework                  |
| Pandas     | Data loading, cleaning, and analysis       |
| Matplotlib | Chart generation and visualization         |
| Seaborn    | Statistical data visualization             |
| HTML       | Web page structure                         |
| CSS        | Dashboard styling                          |
| CSV        | Input dataset format                       |

---

## 📂 Project Structure

```text
Website-Traffic-Analysis/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── templates/
│   ├── index.html           # Dataset upload page
│   └── dashboard.html       # Traffic analysis dashboard
│
├── static/
│   ├── traffic_by_country.png
│   ├── traffic_by_city.png
│   └── daily_events.png
│
└── uploads/                 # Uploaded CSV datasets
```

*Note: The `static/` and `uploads/` directories are created automatically when the application starts. The HTML templates and `requirements.txt` must be present in the project if they are not generated separately.*

---

## 📊 Dashboard Insights

The application generates analytical insights from the uploaded dataset.

### 1. Dataset Overview

Provides a summary of the uploaded dataset, including:

* Total number of records.
* Total number of columns.
* Number of unique countries.
* Number of unique cities.

### 2. Country-wise Traffic Analysis

Identifies the top 10 countries with the highest number of recorded events.

**Visualization:** Bar chart.

**Purpose:** Understand the geographic distribution of website activity across countries.

### 3. City-wise Traffic Analysis

Displays the top 10 cities based on the frequency of recorded events.

**Visualization:** Bar chart.

**Purpose:** Identify cities contributing the most recorded website activity.

### 4. Daily Website Traffic

Groups records by date and visualizes the number of events recorded each day.

**Visualization:** Line chart.

**Purpose:** Observe daily traffic fluctuations and identify potential trends or spikes in website activity.

> **Note:** The application counts dataset records as traffic events. Actual visitor counts, sessions, and page views require appropriate tracking fields and analysis logic.

---

## ⚙️ How It Works

The application follows a simple data analytics workflow:

1. **Upload Dataset:** The user uploads a website traffic CSV file through the web interface.
2. **Load Data:** Pandas reads the uploaded dataset and attempts to handle different CSV encodings.
3. **Preprocess Data:** Column names are normalized, and completely empty rows are removed.
4. **Identify Columns:** The application searches for supported country, city, and date column names.
5. **Analyze Traffic:** It calculates dataset statistics, geographic distributions, and daily event counts.
6. **Generate Charts:** Matplotlib and Seaborn create the relevant visualizations.
7. **Display Dashboard:** Flask passes the analysis results to the dashboard template for presentation.

---

## 💻 Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

Ensure that the following are installed:

* Python 3.9 or later
* pip
* Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/Tarun-2006-Mdu/Website-Traffic-Analysis.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Website-Traffic-Analysis
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### Step 5: Install Dependencies

If the repository contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the required packages:

```bash
pip install Flask pandas matplotlib seaborn
```

### Step 6: Run the Application

```bash
python app.py
```

### Step 7: Open the Application

Open your browser and navigate to:

```text
http://127.0.0.1:5000/
```

Upload a supported CSV dataset to generate the traffic analysis dashboard.

---

## 📄 Dataset Requirements

The application accepts CSV files containing website traffic or event data.

The following columns are recognized when present:

| Category      | Supported Column Names                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------- |
| Country       | `country`, `countries`, `country_name`, `location_country`                                         |
| City          | `city`, `cities`, `city_name`, `location_city`                                                     |
| Date and Time | `date`, `datetime`, `date_time`, `timestamp`, `visit_datetime`, `event_date`, `created_at`, `time` |

Column names are normalized to lowercase, leading and trailing spaces are removed, and spaces and hyphens are replaced with underscores.

For example:

```csv
country,city,date
India,Chennai,2026-10-20
India,Madurai,2026-10-20
USA,New York,2026-10-21
India,Coimbatore,2026-10-21
UK,London,2026-10-22
```

The application can analyze country and city distributions independently when those columns exist. Daily traffic analysis requires a recognized date column containing parseable dates.

**Important:** The example dataset above is illustrative. The application does not require these exact records or this exact combination of columns.

---

## 🎯 Use Cases

This project can be used for:

* Website traffic data exploration.
* Geographic analysis of website activity.
* Daily website event monitoring.
* Exploratory Data Analysis (EDA).
* Learning Python-based data analytics and visualization.
* Developing lightweight analytics dashboards for CSV datasets.

---

## 🔮 Future Enhancements

Potential improvements include:

* Interactive charts using Plotly.
* Monthly and hourly traffic analysis.
* Traffic source and referral analysis.
* Device and browser usage analysis.
* Unique visitor and session analysis.
* Date-range and geographic filters.
* Exportable analytical reports.
* Improved validation and error handling for uploaded files.
* Database integration for storing historical traffic data.
* Deployment to a cloud platform.

---

## 👨‍💻 Author

**Tarunraj M.**

* GitHub: [Tarun-2006-Mdu](https://github.com/Tarun-2006-Mdu)
* Project Repository: [Website-Traffic-Analysis](https://github.com/Tarun-2006-Mdu/Website-Traffic-Analysis)

---

## 📜 License

This project can be distributed under the MIT License if an appropriate `LICENSE` file is added to the repository. Until then, no specific open-source license is declared.

---

## ⭐ Support

If you find this project useful for learning data analytics, Python, or Flask development, consider giving the repository a star!

**Built with Python, Flask, Pandas, Matplotlib, and Seaborn.**
