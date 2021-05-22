# Average Height
# Don't change the code below 

student_heights = input("Input a list  of student Heights: ").split(" ")
# Don't change the code above  
total_ht = 0
for n in range(0, (len(student_heights))):
    student_heights[n] = int(student_heights[n])
    total_ht += student_heights[n]
print(student_heights)

student_heights_avg = total_ht / int(len(student_heights) - 1)

print(total_ht,len(student_heights))

print(student_heights_avg)