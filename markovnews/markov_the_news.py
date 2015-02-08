import tokenise
import markovstate
from pymongo import MongoClient
import os

class MarkovTheNews():
  def __init__(self):
      super().__init__()
      self.savetxt()
      #self.markov = markovstate.MarkovState()
      #self.do_train()
      #self.markov.dump('generator')
      #return self.do_tokens()
      #print(self.do_sentences())
      #print(self.do_tokens())

  def charinput(self, lines):
    for line in lines:
      for char in line:
        yield char

  def savetxt(self):
    db = MongoClient(os.environ['MONGODB_URL'])
    articles = db.newspapers.articles
    article_results = articles.find(None, {'title': 1})
    headlines = []

    for story in article_results:
      headlines.append(story['title'])

    txt = "\n".join(headlines)
    f = open("headlines/data.txt", 'w')
    f.write(txt)

  def do_train(self):
    prefix_length = 3
    noparagraphs_arg = True
    db = MongoClient(os.environ['MONGODB_URL'])
    articles = db.newspapers.articles
    article_results = articles.find(None, {'title': 1})
    headlines = []

    for story in article_results:
      headlines.append(story['title'])

    print(self.charinput(headlines))

    self.markov.train(prefix_length, self.charinput(headlines), noparagraphs=noparagraphs_arg)

  def do_tokens(self):
    length = 350
    seed = None
    prob = 0
    offset = 0
    prefix = ()
    return self.markov.generate(length, seed, prob, offset,endchunkf=lambda t: t == '\n\n', kill=1, prefix=prefix)

  def do_sentences(self):
    length = 350
    seed = None
    prob = 0
    offset = 0
    prefix = ()
    sentence_token = lambda t: t[-1] in ".!?"
    return self.markov.generate(length, seed, prob, offset, startf=sentence_token, endchunkf=sentence_token, prefix=prefix)
