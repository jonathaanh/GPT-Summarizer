import os
import textwrap
import openai


openai.api_key=os.getenv("OPENAI_API_KEY")


def open_file(filepath):
	with open(filepath, 'r', encoding='utf-8') as infile:
		return infile.read()

def save_file(content, filepath):
	with open(filepath, 'w', encoding='utf-8') as outfile:
		outfile.write(content)


def gpt3_completion(prompt)

if __name__=='__main__':
	alltext = open_file('input.txt')
	chunks = textwrap.wrap(alltext, 4000)

	result = list()
	for chunk in chunks():

