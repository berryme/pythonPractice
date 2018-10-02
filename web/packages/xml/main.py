'''
Created on Mar 14, 2018

@author: berrym2
'''



def Run():
    return 'Yo'


class BerryClass:

    def __init__(self, str):
        self.name = str

    def setNum(self, num):
        if (('' + num).isnumeric()):
            self.number = num
        else:
            Exception('Not a number')

    @logit(logfile='func2.log')
    def getObjects(self):
        return {"python", "coding", "tips", "for", "beginners"}

    def getName(self):
        return self.name
