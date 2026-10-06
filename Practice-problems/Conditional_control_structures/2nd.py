# Problem Statement:
# You work in XYZ Corporation as a Data Analyst. Your company has told you to
# work with the if-else condition.
# Tasks To Be Performed:
# 1. Take three user inputs and print the greatest number from those inputs
# using if-else condition. Edge cases, if any, should also be handled.

a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

c=float(input("Enter third number:"))

if(a>=b) and (a>=c):
    print(a,"is greatest number")
elif (b>=a) and (b>=c):
    print(b,"is greatest number")
else :
    print(c,"is greatest number")        

        

