'''
Created on Apr 30, 2018

@author: Sdxwo_000
'''
#I am a comment. For some reason my interpreter thinks that grey on white is a
#good idea. I guess I know what their Eclipse theme is.
from math import ceil
print('is items 5????')

items = 3
GPA = 2.9
dogs = "cute"

if items == 5 & items > 20:
    print (items)
    print ("yes")
else:
    print ("ACTUALLY IT ")
    print (items)

print ("I think dogs are: " + dogs)

    
''' Nevermind I went through some themes.
I'm darkest dark now. I guess thats the most popular. 
And this multiline comment is also dumb. Why is it
super visible like a string, but single line is 
nearly impossible to read?
'''

""" single multiline """

''' using single quotes! '''
vacation = False
weekday = True



def pork(v, w):
    if (v == False and w == True):
        return False
    else:
        return True
    
print(pork(vacation, weekday))

def dork (v,w):
    if not v and w:
        return False
    else:
        return True
    
print(dork(vacation, weekday))
print (ceil(GPA))