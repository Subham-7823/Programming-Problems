
"""
Problem name : Odd–Even Index String Rearrangement
Given a string, rearrange it so that all characters at odd positions come first, followed by all characters at even positions.

example
input : abcdef
output : bdface

"""




input_string = input()
oletters = ""
eletters = ""

for index, letter in enumerate(input_string):
    if index % 2 == 0:
        eletters = eletters + letter
    else:
        oletters =  oletters + letter

print(oletters + eletters)

# enumerate() is used when you want both the index (position) and the value while looping over something (like a list, string, tuple).