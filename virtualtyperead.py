import pyttsx3

vtf = pyttsx3.init()

""" RATE"""
rate = vtf.getProperty('rate')   # getting details of current speaking rate
vtf.setProperty('rate', 140)     # setting up new voice rate

def vtf_speak(text):
    print("speaking.....")
    print('')
    vtf.say(text)
    vtf.runAndWait()

txt = "hello boss. i am your virtual assistant"
vtf_speak(txt)

while txt != 'bye':
    txt = input("what should i say:")
    print('')
    txt = txt.lower()
    if txt != 'bye':
        vtf_speak(txt)
    else:
        vtf_speak('bye boss. you can call me when ever you needed boss')

