from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from rq import Queue
from rq.job import Job
from worker import conn

import os
import requests
import operator
import re
import nltk
import lxml
from bs4 import BeautifulSoup
from collections import Counter
from stop_words import stops

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

q = Queue(connection=conn)

from models import *


def count_save_words(url):
    errors = []
    try:
        r = requests.get(url)
    except:
        errors.append(
            "Unable to get URL. Please make sure it's valid and try again.")
        return {"error": errors}

        raw = BeautifulSoup(r.text, 'html.parser').get_text()
        nltk.data.path.append(os.path.join(os.getcwd(), "./nltk_data"))
        tokens = nltk.word_tokenize(raw)
        text = nltk.Text(tokens)

        #remove punctvations and raw count words
    nonPunc = re.compile(r'.*[A-Za-z].*')
    raw_words = [w for w in text if nonPunc.match(w)]
    raw_word_count = Counter(raw_words)
    no_stop_words = [w for w in raw_words if w.lower() not in stops]
    no_stop_words_count = Counter(no_stop_words)
    #saving results

    try:
        result = Result(
            url=url,
            result_all=raw_word_count,
            result_no_stop_words=no_stop_words_count)
        db.session.add(result)
        db.session.commit()

        return result.id

    except:
        errors.append("unable to add item to database")
        return {"error": errors}

@app.route('/', methods=["POST","GET"]
def index(args):
    result = {}
    pass




if __name__ == '__main__':
    app.run()
