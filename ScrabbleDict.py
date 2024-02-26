# Humbledeep Singh
# ScrabbleDict class for the game(py file) including test cases(Task 2)

#ScrabbleDict class including the methods that are to be used during the whole process of game playing Wordle 
class ScrabbleDict(object):
      #init method to initialise the dictionary with allowed 5 letter words (taken from each line of cleaned file)
       def __init__(self, size, filename):
            self._data=[]
            self.filename=filename
            self.size=size
            my_file=open(filename,'r') 
            wl=[] 
            wrds=my_file.read()
            wl=wrds.splitlines() 

            newlist=[]
            newlist=[string for string in wl if string!=""]
    
            self.dict1={}

            for i in newlist:
                if len(i)==int(size):
                   self.dict1[i]=""
           
       def getDict(self):
           return self.dict1
        
       def check(self,word):    # method to check whether the word is present in dictionary or not
            self.word=word
            if self.word in self.dict1.keys():
                return True
            else:
                return False
            
       def getSize(self):       #method to find the total number of words present in dictionary
           return len(self.dict1.keys())
       
       def getWords(self,letter):  #method to find the list of words (in sorted manner) starting from a specified letter  
           self.letter=letter
           list_words=[]
           for i in self.dict1.keys():
               if i.startswith(self.letter):
                   list_words.append(i)
           list_words.sort()
           return list_words
           
       def getWordSize(self):        #method to find the size of words present in dictionary
           return self.size
                         

# ScrabbleDict checking in isloation with all the specified test cases
if __name__=='__main__':
       # Test cases to check the class 
            s=ScrabbleDict('5', 'Scrabble5.txt')
            print()
            print('Checking for the presence of word in dictionary')
            #print()
            word_to_check=input("Enter a 5 letter word: ")
            b=s.check(word_to_check)
            if b==True:
                print("Present")
            else:
                print("Not Present")
            print() 
            print("Number of words in dictionary")
            no_of_words=s.getSize()
            print(no_of_words)
            print()
            print("Sorted list of words in the dictionary starting from a particular letter")
            start_letter=input("Enter starting letter: ")
            list4=s.getWords(start_letter)
            print(list4)
            print()
            print("Getting the size of words in dictionary")
            word_size=s.getWordSize()
            print(word_size)
            
