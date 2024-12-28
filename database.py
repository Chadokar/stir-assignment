from pymongo import MongoClient
import config
from scraper import get_data
from bson import ObjectId


def get_db():
    client = MongoClient(config.MONGO_URI)
    return client.trends_db


def save_trends(trends_data):
    db = get_db()
    result = db.trends.insert_one(trends_data)
    return str(result.inserted_id)  # Convert ObjectId to string


def get_all_trends():
    db = get_db()
    trends = list(db.trends.find())
    for trend in trends:
        trend['_id'] = str(trend['_id'])  # Convert ObjectId to string
    return trends


def get_latest_trends(proxy):
    res = get_data(proxy)  # Scrape data (replace "" with your source URL)
    data = {
        'nameoftrend1': '',
        'nameoftrend2': '',
        'nameoftrend3': '',
        'nameoftrend4': ''
    }
    if isinstance(res, list):
        for i in range(len(res)):
            temp = res[i].split('\n')
            res[i] = {'category': temp[0],
                      'trending': temp[1], 'posts': temp[2]}
        data['nameoftrend1'] = res[0]
        data['nameoftrend2'] = res[1]
        data['nameoftrend3'] = res[2]
        data['nameoftrend4'] = res[3]
        save_trends(data)
    else:
        return "Error occurred while scraping"
