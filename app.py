import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


app = Flask(__name__)
app.secret_key = "secret"
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://root:s!evan101@ds233212.mlab.com:33212/recipes-data-centric'


dropzone = Dropzone(app)


app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'add_recipe'
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'


photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


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
    
    # list to hold our uploaded image urls
    file_urls = []
    
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)
            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename    
            )
            # append image urls
            file_urls.append(photos.url(filename))

        return "uploading..."
    return render_template('add_recipe.html')
    
    
@app.route('/insert_record', methods=['GET', 'POST'])
def insert_record():
    item = mongo.db.recipes
    item.insert_one(request.form.to_dict())
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

       
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)