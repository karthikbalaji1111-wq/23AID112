# mathematical operators in python
a = input("Enter the first number : ")
b = input("enter the second number : ")

aint = int(a)
bint = int(b)

add = aint+ bint
subtract = aint - bint
product = aint * bint

print("The sum is : " , add)
print("The difference is : " , subtract)
print("The product is : " , product)

if aint > bint:
    print("First number is bigger")
elif bint > aint:
    print("Second number is bigger")
else:
    print("Both numbers are equal")
