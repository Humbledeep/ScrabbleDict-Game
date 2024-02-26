# hint.py for task 4 and 5

from Clean import *
from ScrabbleDict import *
class hint(object):
     def getMaskedWords(self,template):        
        #method to find the list of words according to validated template specified by user (including specified test cases) 
        self.template=template
        match_list=[]
       
        dict3=s1.getDict()
        list_words=list(dict3.keys())
        #print(list_words)
        for i in range(len(self.template)):
            if self.template[i]!='*':
                match_list.append(i)
        
        j=0
        print("List of words matching the template")
        for word in list_words:
             res=True
             for j in match_list:
                x=int(j) 
                if word[x]==self.template[x]:
                      res=res and True
                else: 
                      res=res and False
             if res==True:
                 print(word)
                 
      #method to find the list of words according to the template provided by user
      #and letters entered by user that may replace the wildcards in templat (as per the specified test cases)       
     def getConstrainedWords(self,template,letters):
           
           newlist=[]
           match=[]
           for i in range(len(template)):
            #print(self.template[i])
              if template[i]!='*':
                  match.append(i)
           
           dict4=s1.getDict()
           list1_words=list(dict4.keys())
           for word in list1_words:
               res=True
               for j in match:
                  y=int(j) 
                  if word[y]==template[y]:
                      res=res and True
                  else: 
                      res=res and False
               if res==True:
                  newlist.append(word)
           nmatch=[]
           r=False
           for i in range(len(template)):
                 if template[i]=='*':
                     nmatch.append(i)
           boool=[]
           print("List of constrained words matching the template and entered letters")
           for word in newlist:
                boool.clear()
                boool=[]
                for l in letters:
                     r=False
                     for k in nmatch:
                        z=int(k)
                        if word[z]==l:
                           r=r or True
                        else:
                           r=r or False
                     boool.append(str(r))
                resu=True
                for i in boool:
                    if i=='True':
                        resu=resu and True
                    else:
                        resu=resu and False
                if resu==True:
                     print(word)

if __name__=='__main__':
       # Test cases to check the class 
       h=hint()
       size=5
       temp_trials=0
       filename="scrabble5.txt"
       s1=ScrabbleDict(size,filename)
       #taking template input from user, validating it will all the specified conditions and invoking getMaskedWords(self,template) method
       print("To find list of words that match the template as well as entered letters")
       trial=False
       while temp_trials<5 and not trial:
           temp=input('Enter the template having size 5, write * at the place of letter which you do not know: ')
           if len(temp)!=s1.getWordSize():
               print("Template should be of size 5")
               temp_trials+=1
           else:
               trial=True
               h.getMaskedWords(temp)
          
       trial_new=False
       t=0
       temp1_trials=0
       count=0
       letr_list=[]
     
     #After the template matching, allowing the users to enter letters (if they want to) that may replace 
     #wildcards in the template, validating the input, then,invoking getConstraineddWords(self,template,letters) method
       trial_new=False
       v=input('Do you want to enter possible letters that may replace *, answer in 1 (for yes) or 0(for no) : ')
       if v==str(1):
            for i in range(len(temp)):
               if temp[i]=='*':
                   count+=1
               
            while temp1_trials<count and not trial_new:
               #letr_no=int(temp1_trials+1)
               l1=input("Enter letter: ")
               letr_list.append(l1)
               temp_trials+=1
               if temp_trials<count:
                  w=input('Do you want to enter more letter, answer in 1 (for yes) or 0 (for No): ')
                  if w==str(1):
                    # temp1_trials+=1
                     trial_new=False
                  else:
                     trial_new=True
               else:
                     trial_new=True
                   
               
            h.getConstrainedWords(temp,letr_list)
       else:
            print('Okay, go ahead with the above hits as per the template')
            
       print()
       print()
       #Code to calculate statistics for all the alphabets according to their respective frequency in allowed list of words
       #finding the appearance percentage of alphabets and making histogram as per the specification 
       print('Task 5: Statistics based')
       print()
       WordFile='word5Dict.txt'
       c=Clean(WordFile)
       lw=c.getList()

       word_string=""
      
       for i in lw:
           word_string=word_string+i.upper()
       alphabet_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
           #print(word_string)
       c=0
       s=0
       str_pattern=""
       total_count=len(word_string)
      
       for alphabet in alphabet_list:
           str_pattern=""
           c=word_string.count(alphabet)
           percent_alpha=(c/total_count)*100
           round_percent=round(percent_alpha)
           for i in range(round_percent):
               str_pattern=str_pattern+'*'
        
           decimal_percent = "{:.2f}".format(percent_alpha)
           if len(str(c))==2:
               print(alphabet,' :   ',str(c),"  ",str(decimal_percent).rjust(5,' '),'%','  ',str_pattern)
           elif len(str(c))==3:
               print(alphabet,' :  ',str(c),"  ",str(decimal_percent).rjust(5,' '),'%','  ',str_pattern)
           else:
               print(alphabet,' : ',str(c),"  ",str(decimal_percent).rjust(5,' '),'%','  ',str_pattern)
    
    
    
              
                    
               
    