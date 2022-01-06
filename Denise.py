import os
import time
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def speak_assistent(output):

    print("Denise : ", output)

    toSpeak = gTTS(text=output, lang='de', slow=False)
    # saving the audio file given by google text to speech
    file = "Denise" + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound(file, True)
    os.remove(file)
    pass

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Höre zu...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="de_DE")
        print("Deine Anweisung: ", text)
        return text
    except sr.UnknownValueError:
        print()
    return ""

def process_text(abfrage):
    if "Wetter" in abfrage or "Temperatur" in abfrage:
        pass
    elif "Denise" in abfrage or "Wer bist du" in abfrage:
        speak_assistent("Hallo ich bin Denise dein persönlicher Home Assistent, zurzeit werde ich von Juljano Möller entwickelt.")
        return

    elif "Wetterwarnung" in abfrage or "Unwetter in Minden" in abfrage or "Unwetter" in abfrage:
        speak_assistent(
            "Hallo ich bin Denise dein persönlicher Home Assistent, zurzeit werde ich von Juljano Möller entwickelt.")

    elif "Licht aus Wohnzimmer" in abfrage or "Licht aus" in abfrage or "In Wohnzimmer licht aus":
        speak_assistent("Zurzeit kann ich das noch  nicht")

    elif "Uhrzeit" in abfrage or "Wie spät ist es" in abfrage:
        speak_assistent(time.strftime("%d.%m.%Y %H:%M:%S"))

    elif "Meine Youtube playlist abspielen" in abfrage or "Youtube Musik" in abfrage or "Musik" in abfrage:
        print()

    elif "Nacht" in abfrage or "Gute Nacht" in abfrage or "Schlaf gut" in abfrage:
        speak_assistent("Gute Nacht, Juljano Schlaf gut")

    else:
        speak_assistent("Tut mir leid das ich dich nicht verstehe! Juljano wird mich bald klüger machen")

def main():
    while True:
        #text = get_audio()
        process_text("gfg ")

if __name__ == "__main__":
    speak_assistent("Hallo")
    main()
