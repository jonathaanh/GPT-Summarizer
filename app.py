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
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(text),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(text):
    return """Write a concise summary of the following:
    {}
    CONCISE SUMMARY:"""

def open_file(filepath):
	with open(filepath, 'r', encoding='utf-8') as infile:
		return infile.read()

def save_file(content, filepath):
	with open(filepath, 'w', encoding='utf-8') as outfile:
		outfile.write(content)
