__author__ = 'sexybaby'
import string
text = raw_input()

table = string.maketrans(string.ascii_lowercase,string.ascii_lowercase[2:]+string.ascii_lowercase[:2])

print(string.translate(text,table))