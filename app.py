import os
import sys
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import boto3
from config import S3_BUCKET, S3_KEY, S3_SECRET

s3_resource = boto3.resource(
   "s3",
   aws_access_key_id=S3_KEY,
   aws_secret_access_key=S3_SECRET
)

app = Flask(__name__)
app.secret_key = "secret"
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://root:s!evan101@ds233212.mlab.com:33212/recipes-data-centric'


mongo = PyMongo(app)

 
#Creates a route that directs us to our sites home page. 
@app.route('/')
@app.route('/landing', methods=["GET","POST"])
def landing():
    return render_template("landing.html")
    

@app.route("/home", methods = ["GET","POST"])
def home():
    
    recipe_name=mongo.db.recipes.find()
    find_user =  mongo.db.users.find_one({"_id": ObjectId()})
    image = mongo.db.images.find()
    return render_template('home.html', recipe_name = recipe_name, find_user = find_user, image = image)
    
    
@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    return render_template('add_recipe.html')
    
    
@app.route('/insert_record', methods=['GET', 'POST'])
def insert_record():
    item = mongo.db.recipes
    item.insert_one(request.form.to_dict())
    file = request.files['file']
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket.Object(file.filename).put(Body=file)
    return redirect(url_for('add_recipe'))
    
    
@app.route('/insert_username', methods=['GET', 'POST'])
def insert_username():
    if request.method == 'POST':
        item = mongo.db.users
        item.insert_one(request.form.to_dict())
    return redirect(url_for('home'))

    
@app.route('/about')
def about():
    return render_template('about.html')
    
    
@app.route('/categories')
def categories():
    return render_template('categories.html')
    
    
@app.route('/view_recipe/<recipe_name>', methods=['GET', 'POST'])
def view_recipe(recipe_name):
    find_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_name)})
    return render_template('view_recipe.html', recipe = find_recipe )
    
    
@app.route('/view_image/<image_name>', methods=['GET', 'POST'])
def view_image(image_name):
    find_image = mongo.db.images.find_one({"_id": ObjectId(image_name)})
    return redirect(url_for('home', image = find_image))
    

@app.route('/testing')
def testing():
    
    return render_template('testing.html')
    
    
@app.route('/files')
def files():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    summaries = my_bucket.objects.all()
    return render_template('files.html', my_bucket=my_bucket, summaries=summaries)


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

