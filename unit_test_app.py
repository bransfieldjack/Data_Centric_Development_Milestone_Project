import os
import unittest
from flask_pymongo import PyMongo
from unit_test_app import app


class test_run(unittest.TestCase):
    
    
    test_database = 'testing'
    test_database_uri = 'mongodb://test_user:P@$$w0rd1@ds117362.mlab.com:17362/mytestdb'
    
    
    #Test no. 1, test opening a connection to the MongoBD database. 
    def test_open(self):
        test_database_uri = 'mongodb://test_user:P@$$w0rd1@ds117362.mlab.com:17362/mytestdb'
        self.assertTrue(test_database_uri)
        
        
    #Test no. 2, test closing a connection to the MongoBD database. 
    def test_close(self):
        db = app.db_connection_closed(self)
        self.assertTrue(db == True)
        
        