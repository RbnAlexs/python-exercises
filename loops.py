# Input a Python list of student heights
student_heights = input().split()
print(student_heights)
for n in student_heights:
  print(n)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  print(n)
# Write your code below this row 👇