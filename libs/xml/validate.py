'''
Created on Mar 14, 2018

@author: berryme@yahoo.com
'''

from lxml import etree

class Validate:
    '''
    classdocs
    '''
    def __init__(self, xsd_path: str):
        etree.clear_error_log()
        xmlschema_doc = etree.parse(xsd_path)
        self.xmlschema = etree.XMLSchema(xmlschema_doc)

    def validate(self, xml_path: str) -> bool:
        xml_doc = etree.parse(xml_path)
        result = self.xmlschema.validate(xml_doc)

        return result