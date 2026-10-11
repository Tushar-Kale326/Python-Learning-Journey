
#If they can, determine whether the triangle is equilateral, isosceles, or scalene.

# The rules

# Type	         Rule	                  Example
# Equilateral	all 3 sides equal	     5, 5, 5
# Isosceles	    exactly 2 sides equal	 5, 5, 8
# Scalene	    no sides equal	         3, 4, 5


a=float(input("Enter size of first side: "))
b=float(input("Enter size of second side: "))
c=float(input("Enter size of third side: "))


if(a + b > c) and (a + c > b) and (b + c > a):
    if a==b==c:
        print("This triangle is Equilateral")
    elif (a==b or b==c or a==c):
        print("This triangle is Isosceles")  
    else:
        print("This triangle is Scalene")      
else:
    print("These three sides cant form a triangle") 