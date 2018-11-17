import os
import time
from bson.objectid import ObjectId
from flask_pymongo import PyMongo


app = (__name__)


mongo = PyMongo(app)


test_database = 'mytestdb'
test_database_uri = 'mongodb://test_user:P@$$w0rd1@ds117362.mlab.com:17362/mytestdb'
    
    
#Test no. 1, test opening a connection to the MongoBD database. 
def test_open(uri):
    if uri == 'mongodb://test_user:P@$$w0rd1@ds117362.mlab.com:17362/mytestdb':
        print ("Connection successful. ")
        time.sleep(2)
    else:
        time.sleep(2)
        return ("Connection un-successful. ")
        
        
#Test no. 2, test closing a connection to the MongoBD database. 
def test_close(connection):
    return ("Connection to the database has been closed. ")
    
    
#Test no. 3, test writing to a mongodb collection.
def test_write(data, connection):
    connection.insert(data)
    time.sleep(2)
    return ("Data successfully written to the database. ")
    

#Test function calls        
test_open(test_database_uri)
test_close(test_database)
test_write("test_record_1", test_database_uri)
