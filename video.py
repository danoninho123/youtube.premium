import pywhatkit
from webscraper import buscarVideo
link = buscarVideo(str(input('diz: ')))
pywhatkit.playonyt(link)
