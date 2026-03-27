"""
Given an integer array Arr of size N, find the count of elements whose value is greater than all of its previous elements.

Note : 1st elemnt of the array should be considered in the count of the result.
for example , Arr=[7,4,8,2,9] At 7 is the first element,
it will consider in the result .
8 and 9 are also greater than  all of its previosu elemnts 
since total of 3 elemnts is presnet in the array that meets the condition

hence output is 3


"""

l=[1,3,5,2,6]
count=0
for i,j in zip(l,l[1:]):
    if i>j:
        count+=1
        
count+=1
print(count)