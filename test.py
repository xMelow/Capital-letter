""" 
TODO TAB?

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

"""
import re

file_place = "files/testfile.txt"

f = open(file_place, 'r+')
txt = f.read()

txt_list = list(txt)

txt[3] = "E"


print(txt)

""" s = list("hello world")
print(s)

s[2] = 'E'
print(s)

print("".join(s)) """
