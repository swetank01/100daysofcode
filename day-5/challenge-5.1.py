# Average Height
# Don't change the code below 
student_heights = input("Input a list  of student Heights: ").split(" ")
for n in range(0, (len(student_heights))):
    student_heights[n] = int(student_heights[n])
# Don't change the code above  

total_height = 0
for students in student_heights:
    total_height += students

avg_height = total_height / len(student_heights)
print(round(avg_height))