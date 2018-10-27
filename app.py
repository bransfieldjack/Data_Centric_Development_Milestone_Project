import os
import io, json
import sys
import boto3
import botocore
from flask import Flask, session, render_template, redirect, request, url_for
from bson.objectid import ObjectId
from config import S3_BUCKET, S3_KEY, S3_SECRET
from boto.s3.connection import S3Connection
from flask_pymongo import PyMongo


app = Flask(__name__)
app.secret_key = os.urandom(24) #Generates a random string which will encrypt the session cookie. 
app.config["MONGO_DBNAME"] = 'recipes-data-centric'
app.config["MONGO_URI"] = 'mongodb://root:s!evan101@ds233212.mlab.com:33212/recipes-data-centric'
app.config.from_object("config")


mongo = PyMongo(app)

 
#Creates a route that directs us to our sites landing page, then redirects to the homepage if the user login is correct. 
@app.route('/')
@app.route('/landing', methods=["GET","POST"])
def landing():
    if request.method == "POST":
        username = request.form["username"]
        session["user"] = username
        return redirect(url_for('home'))
    return render_template('landing.html')
    
    
@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/home', methods = ["GET","POST"])
def home():
    recipe_name=mongo.db.recipes.find()
    return render_template('home.html', recipe_name = recipe_name)
    
    
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    return render_template('add_recipe.html')
    
    
@app.route('/insert_record', methods=['GET', 'POST'])
def insert_record():
    
    """
    Declare variable for the recipe collection in the mongoDB
    """
    item = mongo.db.recipes 
    
    
    """
    Upload image to Amazon S3 Bucket, generate URL for the image and insert it into MongoDB
    """
    
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)

    file = request.files['file']    #grabbing the uploaded file from the input form.
    filename = file.filename    #gets the filename of the uploaded file, to be appended to the URL for the same file in S3
    my_bucket.Object(file.filename).put(Body=file)  #putting the file into our S3 bucket
    s3 = boto3.client('s3')
    connection = S3Connection(
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET)
    
    url = "https://s3.amazonaws.com/recipe-user-uploads/" + filename    #create a URL for the uploaded image in the bucket

    data = {"form_data": request.form, "image_url": url}    #store the form data and the image URL with Key Value pairs in MongoDB
    item.insert(data)

    return redirect(url_for('home'))
    
    
@app.route('/about')
def about():
    return render_template('about.html')
    
    
@app.route('/view_recipe/<recipe_name>', methods=['GET', 'POST'])
def view_recipe(recipe_name):
    find_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_name)})
    recipe_image = mongo.db.recipe_images.find_one()
    return render_template('view_recipe.html', recipe = find_recipe, recipe_image = recipe_image )
    
    
@app.route('/view_image/<image_name>', methods=['GET', 'POST'])
def view_image(image_name):
    find_image = mongo.db.images.find_one({"_id": ObjectId(image_name)})
    return redirect(url_for('home', image = find_image))


@app.route('/categories')
def categories():
    return render_template('categories.html')

    
@app.route('/meat_eaters', methods=['GET', 'POST'])
def meat_eaters():
    collection = mongo.db.recipes.find()
    return render_template('meat_eaters.html', collection=collection)
    
    
@app.route('/vegetarian', methods=['GET', 'POST'])
def vegetarian():
    collection = mongo.db.recipes.find()
    return render_template('vegetarian.html', collection=collection)
    
    
@app.route('/keto_friendly', methods=['GET', 'POST'])
def keto_friendly():
    collection = mongo.db.recipes.find()
    return render_template('keto_friendly.html', collection=collection)
    
    
@app.route('/paleo_friendly', methods=['GET', 'POST'])
def paleo_friendly():
    collection = mongo.db.recipes.find()
    return render_template('paleo_friendly.html', collection=collection)
    
    
@app.route('/asian_fusion', methods=['GET', 'POST'])
def asian_fusion():
    collection = mongo.db.recipes.find()
    return render_template('asian_fusion.html', collection=collection)
    
@app.route('/middle_eastern', methods=['GET', 'POST'])
def middle_eastern():
    collection = mongo.db.recipes.find()
    return render_template('middle_eastern.html', collection=collection)
    
    
@app.route('/european', methods=['GET', 'POST'])
def european():
    collection = mongo.db.recipes.find()
    return render_template('european.html', collection=collection)
    
    
@app.route('/desert', methods=['GET', 'POST'])
def desert():
    collection = mongo.db.recipes.find()
    return render_template('desert.html', collection=collection)

       
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)

