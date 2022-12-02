import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker 
import textparser

# This file is just to test the code of the discord bot without the bot actually running

graph = False
# data_stream = io.BytesIO() # for apperant graph implementation

   
movieList = ["bee", "free", "shrek", "treasure"]

#----------------
# Parameters
#movie = 'treasure.txt'
movie = "bee.txt"
#percentage = 5
percentage = 10
graphType =  "bar"
#FreqWord = textArray[2]
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
    #Freqplace = -1
    for i in range(len(uniqueWords)):
        if(uniqueWords[i] == word):
            Freqplace = i
        else:
            Freqplace = -1
            
    

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

            my_list.append(data)

wordList = textparser.scriptParser(my_list)

for i in range(len(wordList)):
    if(inList(wordList[i])):
        addFrequency(wordList[i])            
    else:
        addNew(wordList[i])
    
tempUniqueWordsPart = []
tempUniqueWordsFrequencyPart = []
            
# Remove selected entries            
for i in range(len(uniqueWords)):
    if(uniqueWords[i] == ''):
        pass
    elif(uniqueWords[i] == '-'):
        pass
    else:    
        tempUniqueWordsPart.append(uniqueWords[i])
        
        tempUniqueWordsFrequencyPart.append(uniqueWordsFrequency[i])

uniqueWords.clear()
uniqueWordsFrequency.clear()

uniqueWords = tempUniqueWordsPart[:]
uniqueWordsFrequency = tempUniqueWordsFrequencyPart[:]

bubbleSort() 



#print(uniqueWords) #x
#print(uniqueWordsFrequency) #y

# Change this word to query for more info
#getFrequency(FreqWord)

uniqueWordsPart = []
uniqueWordsFrequencyPart = []

#print(len(uniqueWords))

for i in range(int((len(uniqueWords)*(percentage/100)))):
    uniqueWordsPart.append(uniqueWords[i])
    uniqueWordsFrequencyPart.append(uniqueWordsFrequency[i])
    
if graph:
    plt.figure(figsize=(12,12)) 
    if graphType == "bar":
        plt.bar(uniqueWordsPart, uniqueWordsFrequencyPart)
    elif graphType == "pie":    
        plt.pie(uniqueWordsFrequencyPart, labels=uniqueWordsPart, radius = 1.3, autopct='%1.1f%%', startangle=90)
    plt.xlabel('words',family='arial',size=1)
    plt.ylabel('frequency',family='arial',size=1)
    plt.gca().xaxis.set_tick_params(rotation=270)
    #plt.savefig(data_stream, format='png', bbox_inches="tight", dpi = 80)
    plt.close()
    #plt.show()

print(np.c_[uniqueWordsPart, uniqueWordsFrequencyPart])
    
    ## Create file
    # Reset point back to beginning of stream
    # data_stream.seek(0)
    # chart = discord.File(data_stream, filename="Word_Frequency.png")
    
    # embed = discord.Embed(title=movie, description="Frequency of every unique word in the chosen range.", color=0x00ff00)
    # embed.set_image(url="attachment://Word_Frequency.png")
    
    # await channel.send(embed=embed, file=chart)
    
#if(Freqplace != -1):
        #print("The word is in the position: " + str(place) + ".")
        #print("The word occurs: " + str(uniqueWordsFrequency[place]) + " times.")
        #await channel.send("The word is in the position: " + str(Freqplace) + ".")
        #await channel.send("The word occurs: " + str(uniqueWordsFrequency[Freqplace]) + " times.")
        
#if(Freqplace == -1):
    #print("Can't find word.")
    #await channel.send("Can't find word.")
    
#await channel.send(uniqueWords[0])
#await channel.send(uniqueWords[1])
# await channel.send("Amount of unique words:")
# await channel.send(len(uniqueWords))