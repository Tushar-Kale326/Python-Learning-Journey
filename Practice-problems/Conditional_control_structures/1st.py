    # Problem Statement:
    # You work in XYZ Corporation as a Data Analyst. Your company has told you to
    # work with the if-else condition.

    # Tasks To Be Performed:
    # 1. Input the values of a and b as 10 and 20 respectively. Now check if a is
    # greater or b is greater using if condition. Think about all the edge cases,
    # and print the statements accordingly.

a=10 
b=20
if a>b:
    print(a,"is greater than",b)
else:
    print(b,"is greater than",a)    
    

# same problem solved with 'match-case' conditional statement 
    
# The Workaround: The match-case Implementation

# match-case cannot directly compare two distinct variables like match a > b:. To make it work, you have to pass the variables as a tuple and use if guards inside the cases.

# a = 10
# b = 20

# match (a, b):
#     case (x, y) if x > y:
#         print(f"{x} is greater than {y}")
#     case (x, y) if y > x:
#         print(f"{y} is greater than {x}")
#     case _:
#         print(f"Both numbers are equal ({a} == {b})")