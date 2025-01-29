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
    # Handle file uploads for rubric and quiz response CSVs
    rubric_file = request.files.get('rubric')  # Retrieve rubric CSV file
    quiz_response_file = request.files.get('quiz_response')  # Retrieve quiz response CSV file

    if rubric_file:
        rubric_data = csv_reader.get_csv_from_file(rubric_file)
    else:
        return "No rubric file uploaded!", 400

    if quiz_response_file:
        quiz_results = csv_reader.get_csv_from_file(quiz_response_file)
    else:
        return "No quiz response file uploaded!", 400

    # Load Groq API key
    with open("./groq_key.json", "r") as file:
        groq_key = json.load(file)["key"]
    
    # Initialize Groq client
    client = Groq(api_key=groq_key)

    # Prepare the AI prompt using rubric and quiz results
    rubric_str = json.dumps(rubric_data)  # Convert rubric data to string (JSON format)
    quiz_results_str = json.dumps(quiz_results)  # Convert quiz results to string (JSON format)

    prompt = f"Using the following rubric: {rubric_str}, provide feedback on these quiz results: {quiz_results_str}"

    # Send prompt to Groq AI
    chat = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": {prompt}, #changed still not working
        }],
        model="llama3-8b-8192",
    )

    # Get AI response
    response = chat.choices[0].message.content

    # Pass AI response to the template
    return render_template("quiz-results.html", ai_response=response)

if __name__ == '__main__':
    app.run(port=8080)