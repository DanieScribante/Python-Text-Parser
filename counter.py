import matplotlib
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker 
import numpy as np
import copy

#----------------
# Parameters
movie = 'bee.txt'
percentage = 5
graph = False
#----------------

my_list = []
uniqueWords = []
uniqueWordsFrequency = []

# Function to find if the word is already in the list and return a corresponding boolean value
def inList(word):
    for i in range(len(uniqueWords)):
        if((uniqueWords[i] == word) and (len(uniqueWords) > 0)):
            return True
    
    return False    

# If a word is found to unique for the first time it is added new to the lists
def addNew(word):
    uniqueWordsFrequency.append(1)
    uniqueWords.append(word)
    
# If a word is found to be a reoccurence it is tallied    
def addFrequency(word):    
    place = -1
    
    for i in range(len(uniqueWords)):
        if(word == uniqueWords[i]):
            place = i

    if(place != -1):
        uniqueWordsFrequency[place] += 1
        
def bubbleSort():
    n = len(uniqueWordsFrequency)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if uniqueWordsFrequency[j] < uniqueWordsFrequency[j + 1] :
                uniqueWordsFrequency[j], uniqueWordsFrequency[j + 1] = uniqueWordsFrequency[j + 1], uniqueWordsFrequency[j]
                uniqueWords[j], uniqueWords[j + 1] = uniqueWords[j + 1], uniqueWords[j]      

def getFrequency(word):
    place = -1
    for i in range(len(uniqueWords)):
        if(uniqueWords[i] == word):
            place = i
            
    if(place != -1):
        print("The word is in the position: " + str(place) + ".")
        print("The word occurs: " + str(uniqueWordsFrequency[place]) + " times.")
        
    if(place == -1):
        print("Can't find word.")

lineNum = 0
# Change the text file to any text file you want to parse. Make sure it is in the same folder as the code!
with open(movie, encoding='utf8') as f: # This loop will go through all the line in the text file sequentially
    lines = f.readlines() # list containing lines of file
    textInLine = [] # To store all the sords in the line
    #print(lineNum)
    lineNum =+ 1
    for line in lines:
        line = line.strip() # remove leading/trailing white spaces
        if line:
            data = [item.strip() for item in line.split(' ')]

            my_list.append(data) # append dictionary to list

# code to clean up
for h in range(20):
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if(my_list[i][j] != ''):
                # End of word cleanup
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(44)): # ,
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new
                    
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(46)): # .
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new
                    #print("new word: " + new)
                    #print("new word lenght: " + str(len(new)))
                    
                #print(my_list[i][j])    
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(39)): # '
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new
                    
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(33)): # !
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new
                    
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(63)): # ?
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new
                    
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(59)): # ;
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new
                    
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(58)): # :
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new
                    
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(34)): # "
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new      
                    
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(125)): # }
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new        
                        
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(45)): # -
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new        
                        
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(8221)): # ”
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new 
                    
                if(my_list[i][j][len(my_list[i][j]) - 1] == chr(8230)): # …
                    new = ""
                    for k in range(len(my_list[i][j]) - 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new 
                    
                # Start of word cleanup
                if(my_list[i][j][0] == chr(39)): # '
                    new = ""
                    for k in range(1, len(my_list[i][j]), 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new 
                        
                if(my_list[i][j][0] == chr(34)): # ""
                    new = ""
                    for k in range(1, len(my_list[i][j]), 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new 
                        
                if(my_list[i][j][0] == chr(92)): # \
                    new = ""
                    for k in range(1, len(my_list[i][j]), 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new 
                    
                if(my_list[i][j][0] == chr(123)): # {
                    new = ""
                    for k in range(1, len(my_list[i][j]), 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new 
                    
                if(my_list[i][j][0] == chr(45)): # -
                    new = ""
                    for k in range(1, len(my_list[i][j]), 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new 
                    
                if(my_list[i][j][0] == chr(8220)): # “
                    new = ""
                    for k in range(1, len(my_list[i][j]), 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new 
                
                if(my_list[i][j][0] == chr(8230)): # …
                    new = ""
                    for k in range(1, len(my_list[i][j]), 1):
                        new = new + my_list[i][j][k]
                    if(len(new) > 0):
                        my_list[i][j] = new

#print(my_list)

# code to make all letters lower case
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        my_list[i][j] = my_list[i][j].lower()
        
#print(my_list)

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        if(inList(my_list[i][j])):
            addFrequency(my_list[i][j])            
        else:
            addNew(my_list[i][j])
    
tempUniqueWordsPart = []
tempUniqueWordsFrequencyPart = []
            
# Remove selected entries            
for i in range(len(uniqueWords)):
    if(uniqueWords[i] == ''):
        pass
    else:    
        tempUniqueWordsPart.append(uniqueWords[i])
        
        tempUniqueWordsFrequencyPart.append(uniqueWordsFrequency[i])

uniqueWords.clear()
uniqueWordsFrequency.clear()

uniqueWords = copy.deepcopy(tempUniqueWordsPart)
uniqueWordsFrequency = copy.deepcopy(tempUniqueWordsFrequencyPart)

bubbleSort() 

print(uniqueWords) #x
#print(uniqueWordsFrequency) #y

# Change this word to query for more info
getFrequency("captain")

uniqueWordsPart = []
uniqueWordsFrequencyPart = []

print(len(uniqueWords))

for i in range(int((len(uniqueWords)*(percentage/100)))):
    uniqueWordsPart.append(uniqueWords[i])
    uniqueWordsFrequencyPart.append(uniqueWordsFrequency[i])

if graph:
    plt.figure(figsize=(12,12)) 
    plt.bar(uniqueWordsPart, uniqueWordsFrequencyPart)
    #plt.pie(uniqueWordsFrequencyPart, labels=uniqueWordsPart, radius = 1.3, autopct='%1.1f%%', startangle=90)
    plt.xlabel('words',family='arial',size=1)
    plt.ylabel('frequency',family='arial',size=1)
    plt.gca().xaxis.set_tick_params(rotation=270)
    #plt.gca().xaxis.set_major_formatter(mticker.EngFormatter(unit='Hz',places=None,sep=" "))
    #plt.gca().yaxis.set_major_formatter(mticker.EngFormatter(unit='m',places=None,sep=" "))
    plt.show()

print(np.c_[uniqueWordsPart, uniqueWordsFrequencyPart])