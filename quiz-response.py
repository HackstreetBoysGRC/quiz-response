#!/usr/bin/env python3

# initial commit.

# create venv
# python -m venv ./venv

# select venv:

    # on a POSIX machine:
    # source ./venv/bin/activate

    # on a Windows command shell:
    # ./venv/Scripts/activate

# install dependencies:

# pip install groq flask


# todo:
# import AI API
# serve a webpage

from flask import Flask, render_template
from groq import Groq

app = Flask(__name__, static_url_path='/static', static_folder='web')

#
@app.route('/')
def base_index():
    return render_template("quiz-results.html")

if __name__ == '__main__':
    app.run(port=8080)