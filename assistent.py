import mappings as mappings
from neuralintents import GenericAssistant
import pyttsx3
import nltk
from google import google
import wikipediaapi

from playsound import playsound


#NLTK is a leading platform for building Python programs to work with human language data
nltk.download('omw-1.4')


#for the output
speaker = pyttsx3.init()
speaker.setProperty('rate',150)


def getInfoFromWikipedia():
    wiki_wiki = wikipediaapi.Wikipedia('de')

    info = wiki_wiki.page('Python_(programming_language)')

    if info.exists() == False:
        speaker.say("Die Seite existiert nicht oder ich habe es nicht verstanden!")
        speaker.runAndWait()

    print(info)

def getAquariumValues():
    pass

def sayGoodbye():
    pass

def getWeatherData():
    pass

def getStocksValues():
    pass


def googleSearch():
    search_results = google.search("This is my query", 1)
    for result in search_results:
        print(result.description)
        speaker.say(result.description)
        speaker.runAndWait()


mappings = {'aquarium' , getAquariumValues(),
            'wikipedia', getInfoFromWikipedia(),
            'abschied' , sayGoodbye(),
            'wetter' ,  getWeatherData(),
            'aktie', getStocksValues(),
            'internet', googleSearch()
            }


#the json file contains commands for the assistent
assistent = GenericAssistant('commands.json',intent_methods=mappings)
assistent.train_model()
assistent.train_model()


speaker.say("Ich bin bereit")
speaker.runAndWait()

googleSearch()

while True:
    pass


