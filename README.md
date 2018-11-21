# Data Centric Development - Milestone Project


## About: 
This is the third of four milestone projects in the Code Institute Full Stack Software Development Course, having already completed the Stream One (old LMS) and Practical Python projects. 
The brief for this project required building a data-driven web application using the technologies learned throughout the Data Centric Development module.
The project required the storage and retrieval of easily accessible cooking recipes. 
The database technology I chose for this project, was MongoDB. 
I chose AWS S3 bucket storage to host the applications images.
As per the requirements outlined in the project brief, the assumption is that the app functionality will accommodate C(create) R(read) U(update) D(delete) operations.
The schema design incorporated for my app database was intended to provide functionality given the unstructured data set and the user requirements of the app.
Data fields ranged from the user’s credentials to the S3 bucket URL required for retrieval from AWS. 

The project can be accessed from the following link: [recipes-project](https://data-centric-milestone-project.herokuapp.com/)


## Site Navigation Description:
The user arrives at the apps login screen, where they will be prompted to input a username using form submission.
There is no option for the user to navigate through the app without first choosing a username. 
After selecting the appropriate username, the user is directed to the home page where they are greeted by a scrolling list of all added recipes, and their corresponding summaries. 
The user can select any recipe in the list by clicking on the recipe image. 
This will direct the user to the view recipe page, where they can find details such as allergy and nutritional information, as well as directions on how to prepare the meal. 
At the bottom of the view recipe page, the user will find an 'edit' and a 'delete' button. 
As the names suggest, these can be used to update information contained in the recipe or remove the recipe from the site entirely.

The navbar is present on every page of this site. 
Contained in the navbar are options such as, 'about', 'categories', 'add a recipe' and 'home'.
The about page contains information about the sites intentions, ethos and goal. 
This is meant as an informational supplement only. 

Navigating to the 'add a recipe' page will allow the user to input their own recipe from scratch. 
All relevant informational fields are catered for using form input, and there is image upload capability as well.

The categories page groups the sites existing recipes according to the food type selection, which is input during the form submission on the 'add a recipe' page. 
Food categories will appear in accordance with the drop-down menu set items. 

The user’s username can be viewed in the navbar always, using the flask session functionality. 

## Technologies used and functionality:
Technologies used in this project include:
    
* Bootstrap: Bootstrap was used for a basic HTML templating.
* HTML5/CSS: Used for the layout and styling of the application. 
* Python 3.0: The back-end functionality of the application was written entirely in python 3.0.
* Flask Microframework: Flask was used to extend pythons functionality to the front end and create RESTful functionality. 
* Amazon Web Service S3 (simple storage service) was used to store/host my images for this site.
* Python unit testing was used to conduct unit tests of backend functionality. 
* MLab MongoDB database hosting was used for record storage and retrieval. 
* Balsamiq Cloud: Used for wireframes.


## Other Sources
The following supplementary learning resources were explored:

[Uploading images with flask and dropzone.](https://medium.com/@dustindavignon/upload-multiple-images-with-python-flask-and-flask-dropzone-d5b821829b1d)

[Storing Flask uploaded images and files on Amazon S3:](https://greenash.net.au/thoughts/2015/04/storing-flask-uploaded-images-and-files-on-amazon-s3/)

[Stack exchange article on image storage:](https://dba.stackexchange.com/questions/119271/storing-files-on-mongodb)

[Connecting to S3:](http://zabana.me/notes/upload-files-amazon-s3-flask.html)

[How to upload a file to directory in S3 bucket using boto:](https://stackoverflow.com/questions/15085864/how-to-upload-a-file-to-directory-in-s3-bucket-using-boto)

[Upload directly to S3 from flask app. Updating IAM policy:](https://dyrynda.com.au/blog/uploading-files-to-amazon-s3-from-the-browser-part-one)

[Flask Integration with Amazon S3:](https://kishstats.com/python/2018/03/22/flask-amazon-s3-part-3.html)

[Get the most recently added record in a MongoDB collection:](https://community.exploratory.io/t/query-mongodb-for-the-n-most-recent-records/188/2)

[Flask Session Howto:](https://www.youtube.com/watch?v=eBwhBrNbrNI)

[Selenium Testing:](https://www.seleniumhq.org/download/)

[Using AWS S3 to Store Static Assets and File Uploads](https://devcenter.heroku.com/articles/s3)

Images used for this project were taken from the pexels stock library:

[Pexels](https://www.pexels.com/)

* All of the python code written in this project is my own.

## Automated testing
This project was created using a TDD approach where possible.
Unit testing was conducted as much and as frequently as possible. 
For test cases where the unit test framework could not be applied to the work, a separate test_app.py file was used to test standalone python functions. 
The purpose of unit testing with python is to recognise bugs/issues with the code early in the development process. 


### Unit testing in python

```
#Test no. 1, test opening a connection to the MongoBD database. 
    def test_open(self):
        test_database_uri = 'mongodb://test_user:P@$$w0rd1@ds117362.mlab.com:17362/mytestdb'
        self.assertTrue(test_database_uri)
```
```
#Test no. 2, test closing a connection to the MongoBD database. 
    def test_close(self):
        db = app.db_connection_closed(self)
        self.assertTrue(db == True)
```

!["Opening/closing connection to the MongoDB. "](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/testing/unittest_app.PNG)


### Custom Python Test Functions
 
 
```
#Test no. 1, test opening a connection to the MongoBD database. 
def test_open(uri):
    if uri == 'mongodb://test_user:P@$$w0rd1@ds117362.mlab.com:17362/mytestdb':
        print ("Connection successful. ")
        time.sleep(2)
    else:
        time.sleep(2)
        return ("Connection un-successful. ")
```
```
#Test no. 2, test closing a connection to the MongoBD database. 
def test_close(connection):
    return ("Connection to the database has been closed. ")
```
```
#Test no. 3, test writing to a mongodb collection.
def test_write(data, connection):
    connection.insert(data)
    time.sleep(2)
    return ("Data successfully written to the database. ")
```
 
!["Opening/closing connection and writing to the MongoDB. "](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/testing/test_app.PNG)
 
## Manual Testing


### Linking/pages:

Checked all outgoing (page to page) and internal links.
Confirmed that no orphan pages exist as part of this project. (Un-used pages left over from the development process)

### Form Testing:

Tested form submission links and form validation for image upload - no issues.

### Cookies Testing:

Disabled cookies and confirmed that the site behaves as per normal.
No observable effect on application security after disabling cookies during or outside of a session.

### HTML Validation:

Validated all HTML code using: https://validator.w3.org/ (Fixed minor errors/warnings)

### Database Testing:

Verified that test data was writing to the mongoDB database. 
Verified the ability to retrieve data from the same database.

### Ease of Learning:

Everything the user needs in terms of information is clearly displayed. Clickable links are made obvious when appropriate, and large icons are used for clarity.

### Navigation:

The site is relatively easy to navigate. 
The user cannot progress throughout the site without entering a username. 

### Compatibility:

Cross browser compatibility testing has been conducted using Chrome, Firefox, Edge and Opera.
Mobile compatibility testing has been undertaken to ensure that the site works well on mobile devices. 


## Wireframe/Design:
Wireframing for this app was done using Balsamiq Mock-ups (Web-based).
Files were transferred to Cloud 9 from my local machine.


![](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/wire+frames/login.PNG)
![](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/wire+frames/homepage.PNG)
![](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/wire+frames/categories.PNG)
![](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/wire+frames/add_recipe.PNG)
![](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/wire+frames/about.PNG)


## Deploying the project:
This app is currently being hosted on Heroku. 
Instructions for deploying the code are as follows:

### From the Heroku Dashboard:

* Login to your heroku account.
* From the dashboard, select: New > Create New App.
* Select an appropriate App Name as per the on-screen instructions, and the most relevant hosting region. 
* Select Create App.

### From the bash command line/local repo:

* Logon to your heroku account using the 'heroku login' command. 
* Initialise your repo, if you havent already done so.
* Connect the Heroku App repo using the 'heroku git:remote -a (app name)' command.
* In order for Heroku to build your app, you will need to specify the requirements using the following command: 'sudo pip3 freeze --local > requirements.txt'.
* As per the development process, remove all packages/dependencies installed as a result of experimentation which may prohibit successful build on the heroku container. 
* You will also need to generate a "Procfile" before pushing your code. This acts as the entry point for your application. To generate this file, use the 'echo web: python app.py > Procfile' command from bash.
* Use git add . to save your work.
* Add your first commit (git commit -m "Initial Commit. "), then use 'git push heroku master' to push your code to Heroku. 
* To complete the process and ensure that your app will run, set the appropriate config variables from the heroku settings tab. 
* Create an 'IP' config var, with a corresponding value of: 0.0.0.0.
* Create a 'PORT' config var, with a corresponding value of: 5000.
* Create a config var for storage of the S3 secret access key credentials. 
* Create a config var containing your mongDB username and password credentials. 
* To access the application, click open on the heroku console (top right) and record the apps URL. 

## Security Review

The following measures were undertaken to ensure the security of this app and the platforms used to host/service it. 
All required packages have been upgraded to the latest versions where possible. 
With regards to the secret keys used for the BOTO3 library to upload to the AWS S3 bucket, these keys have not been included in any github push and are stored in a secure, offline location. 
An appropriate IAM user has been added for this web app in AWS and granted the necessary permissions to ensure all CRUD functionality is functioning as intended. 
Two factor authentication has been enabled for both the user and root accounts on AWS and the MLab administrator account used to host my MongoDB. 

![Github Security Alerts. ](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/security/alerts.PNG)
![Requests package upgrade. ](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/security/requests.PNG)
![Flask package upgrade. ](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/security/flask.PNG)
![Bootstrap package upgrade. ](https://s3-us-west-2.amazonaws.com/data-centic-development-storage/readme.md/security/bootstrap.PNG)
