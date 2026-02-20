"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] 
for a list of students. Print the average of the marks array for the student name provided, 
showing 2 places after the decimal.

Example

marks key:value pairs are

'alpha': [20, 30, 40]
'beta': [30, 50, 70]

query_name = 'beta'

The query_name is 'beta'. beta's average score is

(30 + 50 + 70)/3 = 50.0.



Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0

56.00

"""

total_students = int(input("Enter total number of students"))
student_marks = {}

for _ in range(total_students):

    key = input("Enter student name: ")
    values = list(map(int, input("Enter marks (space-separated): ").split()))
    student_marks[key] = values

query_name = input("Enter the student name")   
l=[]
for i in student_marks[query_name] :
    l.append(i)
res = 0
for i in l:
    res = res + i
output = res / len(l)
print(f"{output:.2f}")

