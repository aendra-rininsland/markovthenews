import yaml
import sqlite3
import feedparser
import os

def load_config():
  f = open('config.yml')
  return yaml.load(f.read())

config = load_config()

def poll_sources(config):
  con = sqlite3.connect('headlines.db')
  c = con.cursor()
  articles = []

  for source in config['sources']:
    feed = feedparser.parse(source['feed'])
    for item in feed['items']:
      if c.execute("SELECT * FROM headlines WHERE link=?", (item['link'],)).fetchone() == None:
        article = (item['title'], item['summary'], item['published'], source['name'], source['feed'], item['link'])
        print article
        articles.append(article)

  c.executemany("INSERT INTO headlines VALUES(?,?,?,?,?,?)", articles)
  con.commit()
  con.close()

poll_sources(config)
