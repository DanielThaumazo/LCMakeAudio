from gtts import gTTS 
import os

text = "Global warming is the long-term rise in the average temperature of the Earth’s climate system"
language = 'en'
speech = gTTS(text=text, lang=language, slow=False)
speech.save("text.mp3")

# For cross-platform compatibility, use the `os` module to play the saved audio file
if os.name == 'nt':  # For Windows
    os.system("start text.mp3")
elif os.name == 'posix':  # For Unix or MacOS
    os.system("open text.mp3")
