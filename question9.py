# Depicting the pass or fail criteria by input of marks
mark1 = int(input("Enter first exam score: "))
mark2 = int(input("Enter second exam score: "))

if mark1 >= 50 and mark2 >= 50:
    print("You passed")
else:
    print("You need to retake some exams")
