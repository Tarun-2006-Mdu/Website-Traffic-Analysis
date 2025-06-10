from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Load dataset
    df = pd.read_csv(filepath, encoding='latin1')
    df.dropna(inplace=True)
    df.columns = df.columns.str.strip()

    # KPIs
    total_events = df.shape[0]
    unique_cities = df['city'].nunique()
    top_artist = df['artist'].mode().values[0] if 'artist' in df.columns else "N/A"

    # Traffic by country
    country_traffic = df['country'].value_counts().reset_index()
    country_traffic.columns = ['Country', 'Events']

    plt.figure(figsize=(8,5))
    sns.barplot(data=country_traffic.head(10), x='Country', y='Events', palette='rocket')
    plt.title('Top 10 Countries by Traffic')
    plt.xticks(rotation=45)
    plt.tight_layout()
    country_path = os.path.join(STATIC_FOLDER, 'traffic_by_country.png')
    plt.savefig(country_path)
    plt.close()

    # Daily events
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    daily = df.groupby(df['date'].dt.date)['event'].count().reset_index(name='Event Count')

    plt.figure(figsize=(10,5))
    sns.lineplot(data=daily, x='date', y='Event Count', marker='o')
    plt.title('Daily Website Events')
    plt.xticks(rotation=45)
    plt.tight_layout()
    events_path = os.path.join(STATIC_FOLDER, 'daily_events.png')
    plt.savefig(events_path)
    plt.close()

    return render_template('dashboard.html',
                           total_events=total_events,
                           unique_cities=unique_cities,
                           top_artist=top_artist,
                           country_img='static/traffic_by_country.png',
                           events_img='static/daily_events.png')

if __name__ == '__main__':
    app.run(debug=True)
