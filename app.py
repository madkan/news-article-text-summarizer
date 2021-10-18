from flask import Flask
from flask.templating import render_template
from scrape import *
# import itertools

app = Flask(__name__, static_folder='static')

@app.route('/index',methods=['GET'])
def home():
    
    return render_template('index.html')

@app.route('/awareness', methods=['GET'])
def aware():
    res=getArticles()
    head=res[0]
    art=res[1]
    links=res[2]
    print(len(head),len(art),len(links))
    return render_template('awareness.html',head=head,art=art,links=links)

if __name__ == '__main__':
    app.run()