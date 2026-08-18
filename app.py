from flask import Flask, render_template, request
import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "file" not in request.files:
        return "No file uploaded"

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # -----------------------------------------
    # LOAD DATASET
    # -----------------------------------------

    try:
        df = pd.read_csv(filepath, encoding="latin1")
    except Exception:
        try:
            df = pd.read_csv(filepath)
        except Exception as e:
            return f"Unable to read CSV: {e}"

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    df.dropna(how="all", inplace=True)

    # -----------------------------------------
    # DISPLAY DATASET INFORMATION
    # -----------------------------------------

    total_records = len(df)
    total_columns = len(df.columns)

    # -----------------------------------------
    # FIND COUNTRY COLUMN
    # -----------------------------------------

    country_column = None

    country_candidates = [
        "country",
        "countries",
        "country_name",
        "location_country"
    ]

    for column in country_candidates:
        if column in df.columns:
            country_column = column
            break

    # -----------------------------------------
    # FIND CITY COLUMN
    # -----------------------------------------

    city_column = None

    city_candidates = [
        "city",
        "cities",
        "city_name",
        "location_city"
    ]

    for column in city_candidates:
        if column in df.columns:
            city_column = column
            break

    # -----------------------------------------
    # FIND DATE COLUMN
    # -----------------------------------------

    date_column = None

    date_candidates = [
        "date",
        "datetime",
        "date_time",
        "timestamp",
        "visit_datetime",
        "event_date",
        "created_at",
        "time"
    ]

    for column in date_candidates:
        if column in df.columns:
            date_column = column
            break

    # -----------------------------------------
    # COUNTRY CHART
    # -----------------------------------------

    country_chart = False

    if country_column:

        country_data = (
            df[country_column]
            .dropna()
            .astype(str)
            .value_counts()
            .head(10)
            .reset_index()
        )

        country_data.columns = ["Country", "Events"]

        plt.figure(figsize=(10, 5))

        sns.barplot(
            data=country_data,
            x="Country",
            y="Events",
            hue="Country",
            legend=False
        )

        plt.title("Top 10 Countries by Website Traffic")
        plt.xlabel("Country")
        plt.ylabel("Number of Events")
        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                STATIC_FOLDER,
                "traffic_by_country.png"
            ),
            dpi=120
        )

        plt.close()

        country_chart = True

    # -----------------------------------------
    # CITY CHART
    # -----------------------------------------

    city_chart = False

    if city_column:

        city_data = (
            df[city_column]
            .dropna()
            .astype(str)
            .value_counts()
            .head(10)
            .reset_index()
        )

        city_data.columns = ["City", "Events"]

        plt.figure(figsize=(10, 5))

        sns.barplot(
            data=city_data,
            x="City",
            y="Events",
            hue="City",
            legend=False
        )

        plt.title("Top 10 Cities by Website Traffic")
        plt.xlabel("City")
        plt.ylabel("Number of Events")
        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig(
            os.path.join(
                STATIC_FOLDER,
                "traffic_by_city.png"
            ),
            dpi=120
        )

        plt.close()

        city_chart = True

    # -----------------------------------------
    # DAILY TRAFFIC CHART
    # -----------------------------------------

    daily_chart = False

    if date_column:

        df[date_column] = pd.to_datetime(
            df[date_column],
            errors="coerce"
        )

        date_data = df.dropna(subset=[date_column]).copy()

        if not date_data.empty:

            daily = (
                date_data
                .groupby(date_data[date_column].dt.date)
                .size()
                .reset_index(name="Events")
            )

            daily.columns = ["Date", "Events"]

            plt.figure(figsize=(10, 5))

            sns.lineplot(
                data=daily,
                x="Date",
                y="Events",
                marker="o"
            )

            plt.title("Daily Website Traffic")
            plt.xlabel("Date")
            plt.ylabel("Events")

            plt.xticks(rotation=45)

            plt.tight_layout()

            plt.savefig(
                os.path.join(
                    STATIC_FOLDER,
                    "daily_events.png"
                ),
                dpi=120
            )

            plt.close()

            daily_chart = True

    # -----------------------------------------
    # UNIQUE COUNTRIES
    # -----------------------------------------

    unique_countries = 0

    if country_column:
        unique_countries = df[country_column].nunique()

    # -----------------------------------------
    # UNIQUE CITIES
    # -----------------------------------------

    unique_cities = 0

    if city_column:
        unique_cities = df[city_column].nunique()

    # -----------------------------------------
    # RENDER DASHBOARD
    # -----------------------------------------

    return render_template(
        "dashboard.html",

        total_records=total_records,

        total_columns=total_columns,

        unique_countries=unique_countries,

        unique_cities=unique_cities,

        country_chart=country_chart,

        city_chart=city_chart,

        daily_chart=daily_chart,

        country_column=country_column,

        city_column=city_column,

        date_column=date_column
    )


if __name__ == "__main__":
    app.run(debug=True)