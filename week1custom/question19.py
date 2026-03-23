grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]

count_A = 0
count_B = 0
count_C = 0
#count_D are the students whose marks are below 79
count_D = 0

for g in grades:
    if g >= 90:
        A += 1
    elif g >= 80:
        B += 1
    elif g >= 70:
        C += 1
    else:
        count_D += 1

print("Student who got A grade:", count_A)
print("Student who got B grade:", count_B)
print("Student who got C grade:",count_C)
print("Scored below 70:", count_D)
