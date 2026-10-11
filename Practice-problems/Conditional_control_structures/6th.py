# Given marks, print grade according to a grading system you define.
eng=float(input("Enter marks of english: "))
phy=float(input("Enter marks of physics: "))
che=float(input("Enter marks of chemistry: " ))
bio=float(input("Enter marks of biology: "))
maths=float(input("Enter marks of maths: "))
hindi=float(input("Enter marks of hindi: "))

if (0<=eng<=100 and 0<=phy<=100 and 0<=che<=100 and 0<=bio<=100 and 0<=maths<=100 and 0<=hindi<=100) :
    avg=(eng+phy+che+bio+maths+hindi)/6
    if 90<=avg:
        print("Grade: A")
    elif 80<=avg:
        print("Grade: B")   
    elif 70<=avg:
        print("Grade: C")   
    elif 60<=avg:
        print("Grade: D")   
    elif 50<=avg:
        print("Grade: E")
    else:
        print("Grade: F(Fail)")                            
else:
    print("Invalid Input")    