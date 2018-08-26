import os
import pymysql
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

    
#Creates a route that directs us to our sites home page. 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')

       
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)