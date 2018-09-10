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
    return render_template('home.html', images = images, recipe_name=mongo.db.recipes.find())
    
    
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    return render_template('add_recipe.html')
    
    
@app.route('/insert_record', methods=['GET', 'POST'])
def insert_record():
    item = mongo.db.recipes
    item.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe'))

    
@app.route('/about')
def about():
    return render_template('about.html')
    
    
@app.route('/view_recipe/<recipe_name>', methods=['GET', 'POST'])
def view_recipe(recipe_name):
    find_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_name)})
    return render_template('view_recipe.html', recipe = find_recipe )
    
    
@app.route('/view_image/<image_name>', methods=['GET', 'POST'])
def view_image(image_name):
    find_image = mongo.db.images.find_one({"_id": ObjectId(image_name)})
    return redirect(url_for('home'))

       
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)