""" 
if string_list[[0]] == lower
    string_list[[0]].to_upper

elif string_list[[0]] == '#'
    string_list[[2]].to_upper #omdat 0 = '#' 1 = ' ' 2 = '(letter)'

elif string_list[[0]] == '-'
    string_list[[2]].to_upper

elif string_list[[0]] == upper
    do nothing

else
    print("error")


IDEA'S

with open(filename, 'r+') as f:
    text = f.read()
    text = re.sub('(letter)', '(letter.toupper)', text)
    f.seek(0)
    f.write(text)
    f.truncate()

    for i in txt_list:
    y = 0
    print("we are in the for each lus")
    while y < len(txt_list):
         txt_list[[y]].upper()
         y += 1


s = list("hello world")
print(s)

s[2] = 'E'
print(s)

print("".join(s))

"""
import re

file_place = "Capital-letter/files/testfile.txt"

with open(file_place, 'r+') as f:
    txt = f.read()
    txt_list = list(txt)
    


