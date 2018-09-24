import os
import io, json
import sys
import boto3
import botocore
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from config import S3_BUCKET, S3_KEY, S3_SECRET
from boto.s3.connection import S3Connection


app = Flask(__name__)
app.secret_key = "secret"
app.config["MONGO_DBNAME"] = 'recipes-data-centric'
app.config["MONGO_URI"] = 'mongodb://root:s!evan101@ds233212.mlab.com:33212/recipes-data-centric'
app.config.from_object("config")


mongo = PyMongo(app)

 
#Creates a route that directs us to our sites home page. 
@app.route('/')
@app.route('/landing', methods=["GET","POST"])
def landing():
    return render_template('landing.html')
    
    
@app.route('/base')
def base():
    current_user=mongo.db.users.find_one()
    return render_template('base.html', current_user=current_user)


@app.route('/home', methods = ["GET","POST"])
def home():
    
    current_user=mongo.db.users.find_one()
    
    if request.method == 'POST':
        users_collection=mongo.db.users
        get_user=request.form['username']
        save_user = {"username": get_user}
        users_collection.insert(save_user)
    
    recipe_name=mongo.db.recipes.find()
    return render_template('home.html', recipe_name = recipe_name, current_user=current_user)
    
    
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    current_user=mongo.db.users.find_one()
    return render_template('add_recipe.html',current_user=current_user)
    
    
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
    
    
@app.route('/insert_username', methods=['GET', 'POST'])
def insert_username():
    if request.method == 'POST':
        item = mongo.db.users
        item.insert_one(request.form.to_dict())
    return redirect(url_for('home'))

    
@app.route('/about')
def about():
    current_user=mongo.db.users.find_one()
    return render_template('about.html', current_user=current_user)
    
    
@app.route('/categories')
def categories():
    current_user=mongo.db.users.find_one()
    return render_template('categories.html',current_user=current_user)
    
    
@app.route('/view_recipe/<recipe_name>', methods=['GET', 'POST'])
def view_recipe(recipe_name):
    find_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_name)})
    recipe_image = mongo.db.recipe_images.find_one()
    return render_template('view_recipe.html', recipe = find_recipe, recipe_image = recipe_image )
    
    
@app.route('/view_image/<image_name>', methods=['GET', 'POST'])
def view_image(image_name):
    find_image = mongo.db.images.find_one({"_id": ObjectId(image_name)})
    return redirect(url_for('home', image = find_image))
    

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket.Object(file.filename).put(Body=file)

    return redirect(url_for('files'))
       
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)

