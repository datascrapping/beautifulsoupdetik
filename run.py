import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def home():
    return 'test'



if __name__=='_main_':
    app.run(debug=True)
