# CREATE THE GIVEN LIST OF NUMBERS:
n = [12, 45, 3, 98, 7, 34, 21]

# a) TO PRINT EACH NUMBER:
print("Each number avaialble:")
for i in n:
    print(i)

# b) TO PRINT ONLY NUMBERS GREATER THAN 30:
print("Numbers greater than 30:")
for i in n:
    if i > 30:
        print(num)

# c) TO COUNT HOW MANY NUMBERS ARE GREATER THAN 30:
count = 0
for i in n:
    if i > 30:
        count = count + 1

print("Number of numbers present which are greater than 30 :  ", count)
