#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


# Создано SotGE Ltd.
# Автор: Сорокин Максим Евгеньевич


import os
from flask import Flask, request, render_template
import requests


app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html");


@app.route('/handle_form', methods=['POST'])
def form():
	print("Posted file: {}".format(request.files['file']))
	file = request.files['file']
	files = {'file': file.read()}
	r = requests.post("http://127.0.0.1:8000/upload/", files=files)
	if r.ok:
		return "File uploaded!"
	else:
		return "Error uploading file!"


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, debug=True)
