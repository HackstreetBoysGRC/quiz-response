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


from flask import Flask, render_template, request
from groq import Groq
import json
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
@app.route('/quizResults', methods=['POST'])
def quizResults():
    #save file to server
    # file = request.files['quiz-response']
    # file.save("./files/quiz-responses.csv")

    #load groq key from file
    with open("./groq_key.json", "r") as file:
        groq_key = json.load(file)["key"]
    
    #initialize groq client and pass message to AI
    client = Groq(
        api_key = groq_key,
    )
    chat = client.chat.completions.create(
        messages=
        [
            {
                "role": "user",
                "content": "What is the current population of Tokyo?"
            }
        ],
        model = "llama3-8b-8192",
    )

    #get response from AI and print to console
    response = chat.choices[0].message.content
    print(response)

    #refresh page
    return render_template("quiz-results.html")

if __name__ == '__main__':
    app.run(port=8080)