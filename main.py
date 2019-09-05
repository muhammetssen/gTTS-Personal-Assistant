import os
import time 
import playsound
import speech_recognition as sr 
from gtts import gTTS
path = 'src/audio/'
def speak(text):
    print((text))
    file = path+str(text)+'.mp3'
    if os.path.exists(file):
        pass
    else:
        tts = gTTS(text=text,lang='en')
        tts.save(file)
    playsound.playsound(file)

'''def speak(sentence):
    if ' ' in sentence:
        words = sentence.split(' ')
        for word in words:
            check_file(word)
        for word in words:
            playsound.playsound((path + str(word) + '.mp3'))
    else:
        check_file(sentence)
        playsound.playsound((path + str(sentence) + '.mp3'))'''
    

def get_audio():
    print('ready')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said  = ''
        try:
            said = r.recognize_google(audio)
            print(str(said).capitalize())
        except Exception as e:
            print('Exception = No Input{}'.format(e))
    return said
    
def sentence_seperator(sentence_list):
    for sentence in sentence_list:
        speak(sentence)
        
from funcs.user import User
#can = User('can',18,'istanbul')
speak('Welcome, I\'m ready to listen')
while True:
    print('Loop has started')
    text_input = get_audio()
    if 'how are you' in text_input:
        speak('Thanks, I\'m fine. How are you?')
    if 'weather' in text_input:
        from funcs.weather import get_weather_info
        sentences = get_weather_info('istanbul')
        sentence_seperator(sentences)
    if 'exit' in text_input:
        speak('Okay, see you')
        break
    
