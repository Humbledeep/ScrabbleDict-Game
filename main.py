# Humbledeep Singh

from ScrabbleDict import *       #importing ScrabbelDict already created by us (all methods in the class according to specifications)
import random                    #importing random to choose the target word
class main(object):
      def __init__(self,filename):
            size=5
            file_words=open(filename)
            s=ScrabbleDict(size, filename)  #instance of ScrabbleDict class to get the data from dictionary initialised with allowed 5 letter words (to play the game)
            dict2={}
            dict2=s.getDict()
            real_word=random.choice(list(dict2.keys()))       #target word to play the game
            #print(real_word)
            guesses=0
            guess_true=False
            guess_list=[]
            
    #taking the guesses as input from the user and validating it according to all the specified test cases
    #After validation, calling 'guess evaluate' method for checking the guess
            i=1
            while guesses<6 and not guess_true:
                guess=input('Attempt '+str(i)+": Please enter a 5 five-letter word: ")
                if len(guess)>s.getWordSize():
                    print(guess,' is too long')
                elif len(guess)<s.getWordSize():
                    print(guess,' is too short')
                else:    
                    if guess not in (list(dict2.keys())):
                           print("Not a recognised word")
                    else:    
                        if guess in guess_list:
                            print("Already guessed, Enter again")
                        else:
                           guesses=guesses+1     
                           guess_list.append(guess)
                           i=i+1
                           guess_true=main.guess_evaluate(real_word,guess)
    
            if guess_true:
                print("Found in",guesses,"attempts. Well done. The word is",guess.upper())
            else:
                print("Sorry you lose. The word is ", real_word.upper())
                
    #method to evaluate the guess, GREEN list to store the rightly positioned words in the guess
    #when compared to target word, ORANGE to store words that are in the word but not rightly positioned
    #and RED to store the words that are guessed but are not present in target word, all the things are done 
    #in alignment with specified rules and regulations of game in 'assignemnt'
      def guess_evaluate(org_word,guess_word):
               j=0
               l=0
               col=""
               GREEN=[]
               ORANGE=[]
               RED=[]
               x=0
               count=0
               for l in range(5):
                    count=0
                    lettr=guess_word[l]
                    count_guess=guess_word.count(lettr)
                    if lettr==org_word[l]:
                        if count_guess>1:
                             for x in range(l+1):
                                 if guess_word[x]==lettr:
                                    count+=1
                             GREEN.append(lettr.upper()+str(count))
                        else:
                             GREEN.append(lettr.upper())
                        col+="G"
                    elif lettr in org_word:
                         total=org_word.count(lettr)
                         #print(total)
                         correct_pos=0
                         occur=0
                         for j in range(5):
                              if guess_word[j]==lettr:
                                  if j<=l:
                                     occur+=1
                                  if lettr==org_word[j]:
                                     correct_pos+=1
                         if total-correct_pos-occur >=0:
                                if count_guess>1:
                                      for x in range(l+1):
                                            if guess_word[x]==lettr:
                                                count+=1
                                      ORANGE.append(lettr.upper()+str(count))
                                else:
                                      ORANGE.append(lettr.upper())                             
                                col+="O"
                         else:
                                if count_guess>1:
                                      for x in range(l+1):
                                            if guess_word[x]==lettr:
                                                count+=1
                                      RED.append(lettr.upper()+str(count))
                                else:
                                      RED.append(lettr.upper())                             
                                col+="R"
                    else:    
                         if count_guess>1:
                               for x in range(l+1):
                                   if guess_word[x]==lettr:
                                       count+=1
                               RED.append(lettr.upper()+str(count))
                         else:
                               RED.append(lettr.upper())  
                         col+="R"
            
               GREEN.sort()
               ORANGE.sort()
               RED.sort()
               print('GREEN= ',GREEN,'   ORANGE= ',ORANGE,'  RED= ',RED)
               print()
               return col=="GGGGG"
    
    
            
#to run this file independently        
if __name__=='__main__':
       w=main('scrabble5.txt')


