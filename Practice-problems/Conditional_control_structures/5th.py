# # Create a simple calculator using +, -, *, /, %.

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter operator (+,-,*,/,%): ")

# if op == '+':
#     print("Addition: ",num1+num2)
# elif op == '-':
#     print("Subtraction: ",num1-num2) 
# elif op == '*':
#     print("Multiplication: ",num1*num2)
# elif (op == '/') and (num2 != 0):
#     print("Division: ",num1/num2)
# elif (op == '/' or op=='%') and (num2 == 0):
#     print("Error: Invalid operation. The second number cannot be 0.")    
# elif (op == '%') and (num2 != 0):
#     print("Modulo: ",num1%num2)  
# else:
#     print("Invalid Input")    
              
    
    # Create a simple calculator using +, -, *, /, %.

first = (input("Enter first number: ")) 
second = (input("Enter second number: "))
if (first.lstrip("-").replace(".", "", 1).isdigit()) and (second.lstrip("-").replace(".", "", 1).isdigit()):
    # print(first)
    # print(second)
    num1=float(first)
    num2=float(second)

 
    op = input("Enter operator (+,-,*,/,%): ")

    if op == '+':
        print("Addition: ",num1+num2)
    elif op == '-':
        print("Subtraction: ",num1-num2) 
    elif op == '*':
        print("Multiplication: ",num1*num2)
    elif (op == '/') and (num2 != 0):
        print("Division: ",num1/num2)
    elif (op == '/' or op=='%') and (num2 == 0):
        print("Error: Invalid operation. The second number cannot be 0.")    
    elif (op == '%') and (num2 != 0):
        print("Modulo: ",num1%num2)  
    else:
        print("Invalid Operator")    
else:
    print("Invalid Numbers")        
              
 
       

    
    