"""
TODO TAB?
TODO spaces?
TODO read string in list 
TODO change string to upper
TODO change letter to upper
TODO read index ('#', ' ', '-')
"""

import re

file_place = "Capital-letter/files/mainfile.txt"

f = open(file_place, 'r+')

text = f.read() #de inhoud van de file in de variable text plaatsen
text = re.sub('fortnite', 'Games', text) #in de file de string "movies" veranderen naar "gamen"
f.seek(0)
f.write(text)
f.truncate()
