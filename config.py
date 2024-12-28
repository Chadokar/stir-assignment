from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
PROXYMESH_HOST = os.getenv('PROXYMESH_HOST')
PROXYMESH_PORT = os.getenv('PROXYMESH_PORT')