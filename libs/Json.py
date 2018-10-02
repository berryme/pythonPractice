'''
Created on Jul 18, 2016

@author: berryme@yahoo.com
'''


class JSONRead(object):
    parsed_json = None
    
    def __init__(self, f):
        matt = "Matt"
        
        global matt2  
        matt2 = matt.join(f.readlines())
        
        
        
      #  self.parsed_json = json.loads(''.join(f.readlines()))
        print("Yo1")
       
       
    def write(self):
        print(matt2)
       # print(json.dumps(self.parsed_json))
        
           
       
       
       

        