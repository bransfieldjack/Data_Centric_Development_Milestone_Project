# Data Centric Development - Milestone Project


## About: 
This is the third milestone project in the Code Institute Full Stack Software Development Course. 
The brief for this project required building a data-driven web application using the technologies learned throughout the Data Centric Development module.
The project required the storage and retrieval of easily accessible cooking recipes. 
The database technology I chose for this project, was MongoDB. 
I chose AWS S3 bucket storage to host the applications images.
As per the requirements outlined in the project brief, the assumption is that the app functionality will accomodate C(create) R(read) U(update) D(delete) operations.
The schema design incorporated for my app database was intended to provide functionality given the unstructured data set and the user requirements of the app.
Data fields ranged from the users credentials to the S3 bucket URL required for retrievel from AWS. 

The project can be accessed from the following link: [riddle-project](https://data-centric-milestone-project.herokuapp.com/)


## Site Navigation Description:
The user arrives at the apps login screen, where they will be prompted to input a username using form submission.
There is no option for the user to navigate through the app without first choosing a username. 
After selecting the approriate username, the user is directed to the home page where they are greeted by a scrolling list of all added recipes, and their corresponding summaries. 
The user can select any recipe in the list by clicking on the recipe image. 
This will direct the user to the view recipe page, where they can find detailed information such as allergy and nutritional information, as well as directions on how to prepare the meal. 
At the bottom of the view recipe page, the user will find an 'edit' and a 'delete' button. 
As the names suggest, these can be used to update information contained in the recipe, or remove the recipe from the site entirely.

The navbar is present on every page of this site. 
Contained in the navbar are options such as, 'about', 'categories', 'add a recipe' and 'home'.
The about page contains showcases information about the sites intentions, ethos and goal. 
This is meant as an informational supplement only. 

Navigating to the 'add a recipe' page will allow the user to input their own recipe from scratch. 
All relevant informational fields are catered for using form input, and there is image upload capability as well.

The categories page groups the sites existing recipes according to the food type selection, which is input during the form submission on the 'add a recipe' page. 
Food categroies will appear in accordance with the drop down meny set items. 

The users username can be viewed in the navbar at all times, using the flask session functionality. 

## Technologies used and functionality:
Technologies used in this project include:
    
* Bootstrap: Bootstrap was used for a basic HTML templating.
* HTML5/CSS: Used for the layout and styling of the application. 
* Python 3.0: The back-end functionality of the application was written entirely in python 3.0.
* Flask Microframework: Flask was used to extend pythons functionality to the front end and create RESTful functionality. 
* Amazon Web Service S3 (simple storage service) was used to store/host my images for this site.
* Python unit testing was used to conduct unit tests of backend functionality. 
* Selenium Web Driver with C# in Visual Studio was used to conduct browser based testing. 
* Balsamiq Cloud: Used for wireframes.


## Other Sources
The following supplementary learning resources were explored:

[Uploading images with flask and dropzone.](https://medium.com/@dustindavignon/upload-multiple-images-with-python-flask-and-flask-dropzone-d5b821829b1d)

[Storing Flask uploaded images and files on Amazon S3:](https://greenash.net.au/thoughts/2015/04/storing-flask-uploaded-images-and-files-on-amazon-s3/)

[Stack exchange article on image storage:](https://dba.stackexchange.com/questions/119271/storing-files-on-mongodb)

[Connecting to S3:](http://zabana.me/notes/upload-files-amazon-s3-flask.html)

[Installing Bower on Ubuntu:](https://tecadmin.net/install-bower-on-ubuntu/)

[How to upload a file to directory in S3 bucket using boto:](https://stackoverflow.com/questions/15085864/how-to-upload-a-file-to-directory-in-s3-bucket-using-boto)

[Upload directly to S3 from flask app. Updating IAM policy:](https://dyrynda.com.au/blog/uploading-files-to-amazon-s3-from-the-browser-part-one)

[Flask Integration with Amazon S3:](https://kishstats.com/python/2018/03/22/flask-amazon-s3-part-3.html)

[Get the most recently added record in a MongoDB collection:](https://community.exploratory.io/t/query-mongodb-for-the-n-most-recent-records/188/2)

[Flask Session Howto:](https://www.youtube.com/watch?v=eBwhBrNbrNI)

Images used for this project were taken from the pexels stock library:

[Pexels](https://www.pexels.com/)

* All of the python code written in this project is my own.

## Automated testing
This project was created using a TDD approach where possible.
Unit testing was conducted as much and as frequently as possible. 
For test cases where the unit test framework could not be applied to the work, a separate test_app.py file was used to test standalone python functions. 
The purpose of unit testing with python is to recognise bugs/issues with the code early in the development process. 

Selenium web driver with C# and Visual Studio was used to automate testing the sites behaviour in the web browser. 


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

!["I/O operation on a closed file."](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/input_output_operation_on_closed_file.PNG)


!["Read/Write permissions granted."](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/read_write_permissions_granted_text_file.PNG)


!["Value not expected."](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/value_not_expected.PNG)


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
 
 
## Manual Testing


### Linking/pages:

Checked all outgoing (page to page) and internal links.
Confirmed that no orphan pages exist as part of this project. (Un-used pages left over from the development process)

### Form Testing:

Tested form submission links.

### Cookies Testing:

Disabled cookies and confirmed that the site behaves as per normal.
No observable effect on application security after disabling cookies during or outside of a session.

### HTML Validation:

Validated all HTML code using: https://validator.w3.org/ (Fixed minor errors/warnings)

### Database Testing:

Not applicable.

### Ease of Learning:

The app is quite minimal. Everything the user needs in terms of information is clearly displayed. Clickable links are made obvious when appropriate.

### Navigation:

The site is relatively easy to navigate. 
The user cannot progress throughout the game without entering a username. 
The sites scoreboard can be accessed via the link provided. 

### Compatibility:

Cross browser compatibility testing has been conducted using Chrome, Firefox, Edge and Opera.
Mobile compatibility testing has been undertaken to ensure that the site works well on mobile devices. 


## Wireframe/Design:
Wireframing for this app was done using Balsamiq Mock-ups (Web-based).
Files were transferred to Cloud 9 from my local machine.


![](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/index_page.PNG)
![](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/riddle_page.PNG)
![](https://s3-ap-southeast-2.amazonaws.com/practical-python-milestone-project/game_over_page.PNG)


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
* You will also need to generate a "Procfile" before pushing your code. This acts as the entry point for your application. To generate this file, use the 'echo web: python app.py > Procfile' command from bash.
* Use git add. to save your work.
* Add your first commit (git commit -m "Initial Commit. "), then use 'git push heroku master' to push your code to Heroku. 
* To complete the process and ensure that your app will run, set the appropriate config variables from the heroku settings tab. 
* Create an 'IP' config var, with a corresponding value of: 0.0.0.0.
* Create a 'PORT' config var, with a corresponding value of: 5000.
* To access the application, click open on the heroku console (top right) and record the apps URL. 

## Examples of Code Refactoring:

### Changed condition on when the riddles are no longer displayed by removing:
    
    ```
    if request.method == "POST":
            if user_answer == "palmtree" and index >= 7:
                return redirect("game_over")
    ```
    
### Replacing with:
   
    ```
    if request.method == "POST":
            if index >= 8:
                return redirect("game_over")
    ```