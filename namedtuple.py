9# Enter your code here. Read input from STDIN. Print output to STDOUTfrom collections import namedtuple
from collections import namedtuple
n = int(input())
info = input()
total = 0
Student = namedtuple('Student', info)
for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)
print('{:.2f}'.format(total/n))
