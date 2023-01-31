# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
i = 0
j = 1
for i in range(0, len(student_scores)):
    for j in range(0, len(student_scores)):
        if student_scores[i] > student_scores[j]:
            student_scores[j] = student_scores[i]
            j += 1
        else:
            j += 1
    i += 1
print(f"The highest score in the class is: {student_scores[i-1]}")
