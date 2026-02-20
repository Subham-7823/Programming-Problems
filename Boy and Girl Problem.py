"""
Problem name : Boy or Girl
This is his method: if the number of distinct characters in one's user name is odd, then he is a male, 
otherwise she is a female. You are given the string that denotes the user name, 
please help our hero to determine the gender of this user by his method.

if user is male 
print : DON'T CHAT WITH HER

if user is female
print : CHAT WITH HER

#string input only consist lowercase lettrs

"""




user = input().lower()
distinct_user = set(user)
if len(distinct_user) % 2 == 0:
    print("CHAT WITH HER")
else:
    print("DON'T CHAT WITH HER")




