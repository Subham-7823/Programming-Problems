"""
At a fun fair, a street vendor is selling balloons of different colours. 
He sells N number of balloons, where each balloon has a colour represented in an array B[].
Your task is to find the colour of the balloon that appears an odd number of times in the given array.

⚠️ Conditions
1.If there is more than one colour occurring an odd number of times, print the first such colour in the array.
2.Balloon colours can be in uppercase or lowercase.
3.If all colours occur an even number of times, print:
All are even

Example 1:
7 -> value of n
[r,g,b,b,g,y,y] -> B[]
Elemnts B[0] to B[N-1], where each input elemnts is separated by space

output

"""

array = list(input().lower().split())
temp = set(array)
for i in temp:
    count=0
    for j in array:
        if i == j:
            count+=1
    if count % 2 !=0 :
        print(f"{i} is present odd number of times")
        break
else:
    print("All are even")

    
        