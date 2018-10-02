'''
Created on Jun 16, 2016

@author: berryme@yahoo.com
'''

import random

M = 50           # max size of integer
N = 80000               # number of ints in the stream

random.seed('test')
seen=set()

def dejaVu(n):          # the required function
    if n in seen:
        return True
    else:
        seen.add(n)     # not seen before so add to set
        return False

def tryit():            # generate another number & test it
    n = random.randint(0,M+1)
    if dejaVu(n): print ('Found : ', n)
    
                        # let's try it N times...
for _ in range(0,N): tryit()

print("Done")


def runMod():
    print ('Hello, world!')
    greet('Jack')
    greet('Jill')
    greet('Bob')
    tryit()

def greet(name):
    print ('Hello', name)











if __name__ == '__main__':
    runMod()


