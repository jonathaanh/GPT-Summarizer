import os

import openai
import textwrap
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        text = request.form["text"]
        response = recursiveSummary(text)
        print(response)
        return redirect(url_for("index", result=response))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(text):
    return """Write a concise detailed summary of the following:{}
    CONCISE DETAILED SUMMARY:""".format(text)

def recursiveSummary(text):
    chunks = textwrap.wrap(text,2000)
    output = list()
    for chunk in chunks:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(chunk),
            temperature=0.6,
            max_tokens=2000,
            top_p=1.0,
            frequency_penalty=0.25,
            presence_penalty=0.0,
            stop=['<<END>>']
        )
        output.append(response.choices[0].text)
    return output
    

def open_file(filepath):
	with open(filepath, 'r', encoding='utf-8') as infile:
		return infile.read()

def save_file(content, filepath):
	with open(filepath, 'w', encoding='utf-8') as outfile:
		outfile.write(content)


