'''
Created on Jul 18, 2016

@author: berryme@yahoo.com
'''

import Json

def execute( ):
    j = Json.JSONRead(open("test.json"))
    j.write() 
       
if __name__ == '__main__':
        execute()
