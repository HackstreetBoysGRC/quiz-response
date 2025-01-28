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


from flask import Flask, render_template
from groq import Groq

import csv_reader

app = Flask(__name__, static_url_path='/static', static_folder='web')

# add csv reader to jinja template engine
# not permanent
@app.context_processor
def csvr():
    return dict(csvr=csv_reader.get_csv)

# base route, ask for rubric and such
@app.route('/')
def base_index():
    return render_template("quiz-results.html")

# potential solution, POST data to quiz?
# another option would be to have the data be ephemeral within the webpage itself
# @app.route('/quiz', methods=['POST'])

if __name__ == '__main__':
    app.run(port=8080)