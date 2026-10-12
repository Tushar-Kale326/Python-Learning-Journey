
#Calculate electricity bill according to different unit slabs.

# Units consumed	                 Rate per unit
# First 100 units(1 to 100)	            ₹3
# Next 100 units (101 to 200)	        ₹5
# Next 100 units (201 to 300)	        ₹7
# Above 300 units	                    ₹10

units = int(input("Enter number of units consumed: "))

if units > 300:
    a = units - 300
    bill = (a * 10) + (100 * 7) + (100 * 5) + (100 * 3)
    print("Electricity bill:",bill)
elif units > 200:
    a = units - 200
    bill = (a * 7) + (100 * 5) + (100 * 3)
    print("Electricity bill:",bill)
elif units > 100:
    a = units - 100
    bill = (a * 5) + (100 * 3)
    print("Electricity bill:",bill) 
elif units >= 0:
    bill = units * 3
    print("Electricity bill:",bill) 
else:
    print("Invalid Input")    