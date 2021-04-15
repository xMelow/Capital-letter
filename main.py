import re

file_place = "files/mdfile.md"

f = open(file_place, 'r+')

text = f.read() #de inhoud van de file in de variable text plaatsen
text = re.sub('fortnite', 'Games', text) #in de file de string "movies" veranderen naar "gamen"
f.seek(0)
f.write(text)
f.truncate()
