"""
Given the participants' score sheet for your University Sports Day,
you are required to find the runner-up score. You are given  scores. 
Store them in a list and find the score of the runner-up.

Sample Input 0

5
2 3 6 6 5

Sample Output 0

5

Explanation 0

Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. 
Hence, we print  as the runner-up score.

"""
num_input = int(input("Enter the number of input we want"))
new_arr = list(set(map(int, input().split())))
 

new_arr.sort()
print(new_arr[-2])