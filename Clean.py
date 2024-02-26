# Humbledeep Singh


#import ScrabbleDict
from ScrabbleDict import *
class Clean(object):
        #to clean the input coruupted file and converting it into the uncorrupted output file with one word per line to continue with the game
        def __init__(self,filename):
             my_file=open(filename,'r') 
             wlist=[] 
             words=my_file.read()

             words1=words.replace("\n","#")

             wlist=str(words1).split('#')
             self.new_wordlist1=[]
             for w in range(len(wlist)-1):
                 self.new_wordlist1.append(wlist[w])
     
        def getList(self):
            return self.new_wordlist1

            