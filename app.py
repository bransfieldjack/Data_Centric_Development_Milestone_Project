import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://root:s!evan101@ds233212.mlab.com:33212/recipes-data-centric'


mongo = PyMongo(app)

    
#Creates a route that directs us to our sites home page. 
@app.route('/')
@app.route('/home')
def home():
    images = os.listdir(os.path.join(app.static_folder, "images"))
    return render_template('home.html', images = images, recipe_name=mongo.db.recipe_name.find())
    
    
@app.route('/add_recipe', methods = ['POST', 'GET'])
def add_recipe():
    item = mongo.db.recipe_name
    item.insert_one(request.form.to_dict())
    return render_template('add_recipe.html')
    
    
@app.route('/about')
def about():
    return render_template('about.html')

       
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)