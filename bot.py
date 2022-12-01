import os
import random
import discord
import io
from dotenv import load_dotenv
            
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker 
import numpy as np
import copy

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    
    try:
    
        Freqplace = -1
        
        if message.author == client.user:
            return
        
        if message.content.startswith('??'):
            channel = message.channel
            await channel.send('watcha want')
            text = message.content
            text = text[2:] #This is to remove the identifier
            #await channel.send(text)
            
            if text == "Roll":
                dice = random.randint(1,6)
                await channel.send(str(dice))
                
        if message.content.startswith('//'):      
            movieList = ["bee", "free", "shrek", "treasure"]
            channel = message.channel
            text = message.content
            text = text[2:]
            if text == '':
                await channel.send("Incomplete command")
                return
            #await channel.send(text)
            textArray = []
            textArray = [item.strip() for item in text.split(' ')]
            
            #for s in textArray:
                #await channel.send(s) 
                
            if textArray[0] == "help":
                await channel.send("The format is a follows:")
                await channel.send("//movie Movie_Choice percentage_displayed graph_type")
                await channel.send("Example:")
                await channel.send("//movie shrek 2 pie")
                await channel.send("//movie shrek 2 bar")    
            
            elif textArray[0] == "options":
                await channel.send("The following movies/books can be chosen:")
                await channel.send("free")
                await channel.send("shrek")
                await channel.send("treasure")
                await channel.send("bee")
                
            elif textArray[0] != "movie":
                await channel.send("Incomplete command")  
                return
            
            elif textArray[0] == "movie":
                if textArray[1] not in movieList:
                    await channel.send("Movie is not available")
                    return
                
                graph = True
                data_stream = io.BytesIO()
                #----------------
                # Parameters
                #movie = 'treasure.txt'
                movie = textArray[1] + ".txt"
                #percentage = 5
                percentage = int(textArray[2])
                graphType =  textArray[3]
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
                    elif(uniqueWords[i] == '-'):
                        pass
                    else:    
                        tempUniqueWordsPart.append(uniqueWords[i])
                        
                        tempUniqueWordsFrequencyPart.append(uniqueWordsFrequency[i])

                uniqueWords.clear()
                uniqueWordsFrequency.clear()

                uniqueWords = copy.deepcopy(tempUniqueWordsPart)
                uniqueWordsFrequency = copy.deepcopy(tempUniqueWordsFrequencyPart)

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
                    #plt.gca().xaxis.set_major_formatter(mticker.EngFormatter(unit='Hz',places=None,sep=" "))
                    #plt.gca().yaxis.set_major_formatter(mticker.EngFormatter(unit='m',places=None,sep=" "))
                    plt.savefig(data_stream, format='png', bbox_inches="tight", dpi = 80)
                    plt.close()
                    #plt.show()

                    #print(np.c_[uniqueWordsPart, uniqueWordsFrequencyPart])
                    
                    ## Create file
                    # Reset point back to beginning of stream
                    data_stream.seek(0)
                    chart = discord.File(data_stream, filename="Word_Frequency.png")
                    
                    embed = discord.Embed(title=movie, description="Frequency of every unique word in the chosen range.", color=0x00ff00)
                    embed.set_image(url="attachment://Word_Frequency.png")
                    
                    await channel.send(embed=embed, file=chart)
                    
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
                await channel.send("Amount of unique words:")
                await channel.send(len(uniqueWords))
    except:
        await channel.send("Unexpected error. Don't send that message again. Use the proper message structure.")
        

client.run(TOKEN)