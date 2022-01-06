import mappings as mappings
from neuralintents import GenericAssistant
import pyttsx3
import nltk
import wikipediaapi

from playsound import playsound


#NLTK is a leading platform for building Python programs to work with human language data
nltk.download('omw-1.4')



#for the output
speaker = pyttsx3.init()
speaker.setProperty('rate',150)


def getInfoFromWikipedia():
    wiki_wiki = wikipediaapi.Wikipedia('en')

    info = wiki_wiki.page('Python_(programming_language)')

    if info.exists() == True:
        speaker.say("Die Seite existiert nicht oder ich habe es nicht verstanden!")
        speaker.runAndWait()

    print(info)

def getAquariumValues():
    pass




mappings = {'hi' , getAquariumValues(),
            'wikipedia', getInfoFromWikipedia(),
            }





#the json file contains commands for the assistent
assistent = GenericAssistant('commands.json',intent_methods=mappings)
assistent.train_model()
assistent.save_model()