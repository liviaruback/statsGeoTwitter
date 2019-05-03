import pandas as pd
import ijson
import json
from urllib.request import urlopen
import time

def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)
 
filename = "FILENAME"
    
tweets = []
count = 0
countgeo = 0
countplaces = 0
countcoordinates = 0
countuserLocation = 0
file = open(filename, 'r')
#Total de linhas: 259134. 
# Tempo total para varrer todos: 16 minutos
# Tempo total para varrer todos, sem o append no dict: 1 minuto
# Tempo total para varrer todos, testando o geo:  minutos
for line in file:
    count += 1
    if (count % 50000 == 0): print(count, time.strftime("%Y_%m_%d %H_%M"))
    tweet = json.loads(line)
    #tweets.append(tweet)
    if tweet['geo']:
        countgeo += 1
    if tweet['place']:
        countplaces += 1
    if tweet['coordinates']:
        countcoordinates += 1
    if tweet['user']['location']:
        countuserLocation =+= 1
    if count < 100:
        print(tweet['user']['location']) 
        print('---------------------')
        

# Estatísticas:
# Total tweets: 259134
# com geo: 214 (0,08%)
# com coordinates: 214 (0,08%)
# com place : 2650 (1%)
# com userLocation: 187273 (72%)
   
print(count)
print('geo:', countgeo)
print('place:', countplaces)
print('coordinates:', countcoordinates)
print('userLocation:', countuserLocation)

