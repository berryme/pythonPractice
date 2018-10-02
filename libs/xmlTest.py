'''
Created on Dec 20, 2017

@author: berryme@yahoo.com
'''


from lxml import etree


def xmlTest():
    root = etree.Element("root")
    print(root)
    
def print_events(parser):
    for action, element in parser.read_events():
        a = etree.tostring(action)
        print(a)
      
    
def xmlParse(f):
    parser = etree.XMLPullParser()  
    events = parser.read_events()

#   for line in f.readlines():
#       print(line)
    for line in f.readlines():
        parser.feed(line)
        print_events(parser)

    result = parser.close()
    f.close()

    
if __name__ == '__main__':
    xmlTest()
    file = open('c:/temp/FuelOpis_23.xml')
    xmlParse(file)