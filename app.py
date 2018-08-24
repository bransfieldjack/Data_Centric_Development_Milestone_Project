import os
import pymysql


#Gets the username from the MySql database in the cloud9 workspace. 
username = os.getenv('C9_USER')


#Connect to the MySql database.
connection = pymysql.connect(host='localhost', user = username, password = '', db = 'Recipes')


try:
    #Query the database
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Recipes;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #Close the connection to the database.
    connection.close()
    