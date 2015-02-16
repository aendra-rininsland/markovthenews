import yaml
import sqlite3
import feedparser
import os
from time import strptime, strftime

def load_config():
  f = open('config.yml')
  return yaml.load(f.read())

config = load_config()

def poll_sources(config):
  con = sqlite3.connect('../../scraperwiki.sqlite')
  c = con.cursor()
  articles = []

  for source in config['sources']:
    feed = feedparser.parse(source['feed'])
    for item in feed['items']:
      try:
        publishedTS = strptime(item['published'], '%a, %d %b %Y %H:%M:%S %z')
        published = strftime('%Y-%m-%d %H:%M:%S', publishedTS)
      except:
        publishedTS = strptime(item['published'], '%a, %d %b %Y %H:%M:%S %Z')
        published = strftime('%Y-%m-%d %H:%M:%S', publishedTS)

      if c.execute("SELECT * FROM headlines WHERE link=?", (item['link'],)).fetchone() == None:
        article = (None, item['title'], item['summary'], published, source['name'], source['feed'], item['link'])
        #print article
        articles.append(article)

  c.executemany("INSERT INTO headlines VALUES(?,?,?,?,?,?,?)", articles)
  con.commit()
  con.close()

poll_sources(config)

def fix_dates():
  con = sqlite3.connect('../../scraperwiki.sqlite')
  c = con.cursor()
  rows = c.execute('select id, published from headlines').fetchall()

  for row in rows:
    try:
      newDate = strftime('%Y-%m-%d %H:%M:%S', strptime(row[1], '%a, %d %b %Y %H:%M:%S %Z'))
      c.execute('update headlines set published = ":date" where id = :id', {"date": newDate, "id": row[0]})
    except:
      newDate = row[1]
      c.execute('update headlines set published = ":date" where id = :id', {"date": newDate, "id": row[0]})
