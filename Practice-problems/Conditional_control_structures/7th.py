
#Check whether three sides can form a triangle.
#The triangle inequality rule: the sum of any two sides must be greater than the third side.

# For sides a, b, c, all three of these must be true:

# a + b > c
# a + c > b
# b + c > a

a=float(input("Enter size of first side: "))
b=float(input("Enter size of second side: "))
c=float(input("Enter size of third side: "))

if(a + b > c) and (a + c > b) and (b + c > a):
    print("These three sides can form a triangle")
else:
    print("These three sides cant form a triangle")    