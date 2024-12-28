from flask import Flask, render_template, jsonify
from database import save_trends, get_latest_trends, get_all_trends
import random

app = Flask(__name__)

with open("valid_proxies.txt", "r") as file:
    proxies = [line.strip() for line in file.readlines()]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/scrape')
def scrape():
    try:
        # Perform scraping logic
        get_latest_trends(random.choice(proxies))

        # Fetch all trends
        trends = get_all_trends()
        return jsonify({'message': 'Scraping done!', 'trends': trends})
    except Exception as e:
        return jsonify({'message': f'An error occurred: {str(e)}'})


if __name__ == '__main__':
    app.run(debug=True)
