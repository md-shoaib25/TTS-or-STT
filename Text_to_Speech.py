import pyttsx3
engine = pyttsx3.init()

# Set The Rate of Speech by User!!
speed = int(input("Enter The Speed You Need To Listen, Recommended-[120 to 150] : "))
engine.setProperty('rate', speed)

# Set The Volume of Speech by User!!
vol = float(input("Enter The Volume Level You Need To Listen, Recommended-[0.1 to 1] : "))
engine.setProperty('volume', vol)

# Set The Voice of Speech Male or Female by User!!
gender = str(input("Enter the Choice of The Voice You Like To Listen, Recommended-[Male or Female] : ")).lower()
if gender == 'male':
    gen = 0
else:
    gen = 1
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[gen].id)

# Main Speak & Save The Code!
text = str(input('Write Any Thing To Hear in Voice : '))
choose = str(input("Listen the Voice Type 'Speak', Save the Voice Type 'Save' & You Required Both Speak & Save Type 'Both' : ")).lower()

if choose == 'speak':
    engine.say(text)
    
elif choose == 'save':
    engine.save_to_file(text, 'voice.mp3')
    
elif choose == 'both':
    engine.say(text)
    engine.save_to_file(text, 'voice.mp3')

else:
    print('Choose Correct One Please!')
    
engine.runAndWait()
engine.stop()