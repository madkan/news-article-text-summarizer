from flask import Flask
from flask.templating import render_template
from scrape import *

app = Flask(__name__, static_folder='static')

@app.route('/index',methods=['GET'])
def home():
    
    return render_template('index.html')

@app.route('/awareness', methods=['GET'])
def aware():
    #res=getArticles()
    return render_template('awareness.html')

if __name__ == '__main__':
    app.run()