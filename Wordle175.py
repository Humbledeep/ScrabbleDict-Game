# Humbledeep Singh
# py file to run game


from ScrabbleDict import *     #importing of classes from modules created according to the tasks
from Clean import *
from main import *

class Wordle175(object):
     WordFile='word5Dict.txt'      #Initialisation of 'input file' name (corrupted file)   
     c=Clean(WordFile)         #calling Clean from Clean.py to convert corrupted file into uncorrupted/required file (one word per line)
     lw=c.getList()            
 
     file1=open("scrabble5.txt",'w') #name of required uncorrupted file initialised and file instance opened to carry out write operation on it.
     for i in range(len(lw)):
           file1.write(lw[i])        #writing in the file
           file1.write("\n")
     file1.close()                 #closing the instance of file
     w=main('scrabble5.txt')       #calling main.py to play the whole game as per the defined rules and regulations
     
     
     
    
    
