#11. Given a person's age, income, and employment status,
# determine loan eligibility using multiple conditions.

# Eligibility rules

# A person is eligible only if all of these hold:

# Rule	           Condition
# Age	          21 to 60 (both included)
# Income	     at least ₹25,000 per month if salaried, at least ₹40,000 per month if self-employed
# Employment	 must be salaried or self-employed

# Students and unemployed applicants are always rejected, whatever their income.

# Optional extra tier

# If eligible, set a maximum loan amount based on income:

# Monthly income	               Maximum loan
# ₹1,00,000 or more	                ₹20 lakh
# ₹50,000 or more	                ₹10 lakh
# anything lower (but eligible)  	₹3 lakh

age = float(input("Enter your age: "))
Employment_status=input("Enter employment status(press A for salaried,B for self-employed,C for Unemployed): ")
income = float(input("Enter your monthly income: "))
Loan_Amount=float(input("Enter Loan amount: "))
if (21 <= age <= 60) and ((Employment_status == 'A' and income >= 25000) or (Employment_status=='B' and income >= 40000)) :
    if (income >= 100000 and Loan_Amount <= 2000000) or (income >= 50000 and Loan_Amount <= 1000000) or (income < 50000 and Loan_Amount <= 300000):
        print("You are eligible for loan")
    else:
        print("You are not eligible for loan")    
        
else:
    print("You are not eligible for loan")    