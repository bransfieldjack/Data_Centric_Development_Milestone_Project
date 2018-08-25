import os
import pymysql
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)


#Gets the username from the MySql database in the cloud9 workspace. 
username = os.getenv('C9_USER')


#Connect to the MySql database.
connection = pymysql.connect(host='localhost', user = username, password = '', db = 'recipe')


try:
    #Query the database. Using DictCursor ensures that the rows returned include column names.
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = " select * from users; "
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    #Close the connection to the database.
    connection.close()

    
#Creates a route that directs us to our sites home page. 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

       
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)