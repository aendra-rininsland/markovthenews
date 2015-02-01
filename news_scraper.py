import yaml
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
import feedparser
import os

def load_config():
  f = open('config.yml')
  return yaml.load(f.read())

config = load_config()

def poll_sources(config):
  db = MongoClient(os.environ['MONGODB_URL'])
  articles = db.newspapers.articles

  for source in config['sources']:
    feed = feedparser.parse(source['feed'])
    for item in feed['items']:
      if (articles.find({"link": item['link']}).count() == 0):
        article = {
          'title': item['title'],
          'summary': item['summary'],
          'published': item['published'],
          'origin': source['name'],
          'feed': source['feed'],
          'link': item['link']
        }

        articles.insert(article)

  db.close()

poll_sources(config)
