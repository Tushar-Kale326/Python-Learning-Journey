# Problem Statement:
# You work in XYZ Corporation as a Data Analyst. Your company has told you to
# work with the looping statements.
# Tasks To Be Performed:
# 1. Create an array that has user defined inputs and with the help of for loop,
# fetch all the prime numbers and print the numbers
user_input = input("Enter numbers separated by spaces: ")


numbers_list = []
for item in user_input.split():
    converted=int(item)
    numbers_list.append(converted)
    
# we can also write this in less lines    
# 1)
# numbers_list = []
# for item in user_input.split():
#     numbers_list.append(int(item))
    
# OR 

# 2) 
#    by using list comprehensions
#    numbers_list = [int(item) for item in user_input.split()]   

print("Your list:", numbers_list)
print("Prime numbers are:", end=" ")


for num in numbers_list:
    

    if num > 1:
        is_prime = True  
        
        
        for i in range(2, num):
            if num % i == 0:  
                is_prime = False  
                break  
                
        
        if is_prime == True:
            print(num, end=" ")
            
# above also could be done with less code 
# 1) using for-else
# for num in numbers_list:
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break  # If this hits, the 'else' block below is SKIPPED
#         else:
#             # This executes only if the loop ran completely without breaking
#             print(num, end=" ") 
            
# 2) if number is larger like 1010023 we cant check every single
#    so we use square root
# for num in numbers_list:
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break  # If this hits, the 'else' block below is SKIPPED
#         else:
#             # This executes only if the loop ran completely without breaking
#             print(num, end=" ") 
                 
                 
# 3) by using list comprehensions
# # Get all prime numbers in one elegant line
# prime_numbers = [num for num in numbers_list if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))]

# # Print the result
# print(*(prime_numbers))      

# In short all code can be written in 3 lines!!!