import pywhatkit
from webscraper import buscarVideo

def abrirYoutube(ENTRADA):
    link = buscarVideo(ENTRADA)
    pywhatkit.playonyt(link)
