import os
import random
import discord
import io
from dotenv import load_dotenv    
from matplotlib import pyplot as plt
import textparser

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    
    try:
        if message.author == client.user:
            return
        
        if message.content.startswith('??'):
            channel = message.channel
            # await channel.send('watcha want')
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
                await channel.send("If you want to find the frequency of a spedific word in the movie script then type:")
                await channel.send("//movie Movie_Choice word")
                await channel.send("Example:")
                await channel.send("//movie shrek donkey")
                await channel.send("//movie bee bee")    
            
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
                    Freqplace = -1
                    for i in range(len(uniqueWords)):
                        if(uniqueWords[i] == word):
                            Freqplace = i
                            
                    if Freqplace != -1:
                        return "This word appears in the script " + str(uniqueWordsFrequency[Freqplace]) + " times.\n" + "This word is number " + str(Freqplace + 1) + " in the list of occurences."
                    else:
                        return "This word is not in this script."
            
                data_stream = io.BytesIO()

                movie = "Scripts/" +textArray[1] + ".txt"

                my_list = []
                uniqueWords = []
                uniqueWordsFrequency = []

                with open(movie, encoding='utf8') as f: 
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip()
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
                
                percentage = -1
                
                try:
                    percentage = int(textArray[2])
                except:    
                    FreqWord = textArray[2]
                    

                if percentage == -1:
                    output = getFrequency(FreqWord)
                    await channel.send(output)
                else:
                    graphType =  textArray[3]
                    graph = True

                    uniqueWordsPart = []
                    uniqueWordsFrequencyPart = []

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
                        plt.savefig(data_stream, format='png', bbox_inches="tight", dpi = 80)
                        plt.close()

                        #print(np.c_[uniqueWordsPart, uniqueWordsFrequencyPart])
                        
                        ## Create file
                        # Reset point back to beginning of stream
                        data_stream.seek(0)
                        chart = discord.File(data_stream, filename="Word_Frequency.png")
                        
                        embed = discord.Embed(title=movie, description="Frequency of every unique word in the chosen range.", color=0x00ff00)
                        embed.set_image(url="attachment://Word_Frequency.png")
                        
                        await channel.send(embed=embed, file=chart)
                
                    await channel.send("Amount of unique words:")
                    await channel.send(len(uniqueWords))
    except:
        await channel.send("Unexpected error. Don't send that message again. Use the proper message structure.")
        

client.run(TOKEN)