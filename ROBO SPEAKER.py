import pyttsx3
print('\t\tRobot Speaker 2.0\n\t'
      'If you want to Quit then type q\n'
      )
var_py = pyttsx3.init()
while True:
    text = input('Enter text that what you want me speak: ')

    if text.lower() == 'q':
        break
    var_py.say(text)
    var_py.runAndWait()

# -----------------------------------------------------------
# If you want to write this code in macbook
"""
1 . import os
2 . n = input('Enter the text that you want me speak')
# say word use for macbook not in windows
# use loop before input if use speak again and again
# and inside loop use check to quit 
3 . command = f'say {n}' 
4 . os.system(command)
"""

