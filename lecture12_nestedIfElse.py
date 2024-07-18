marks = int(input("Enter your subject marks"))

if(marks>85):
    print("GPA : 4")
elif(marks>=80 and marks<=84):
    print("GPA:3.66")
elif(marks >=75 and marks<=79):
    print("GPA : 3.33")
elif(marks >=71 and marks<=74):
    print("GPA : 3.00")
elif(marks >=68 and marks<=70):
    print("GPA : 2.9")
elif(marks >=64 and marks<=67):
    print("GPA : 2.7")
elif(marks >= 61 and marks <=63):
    print("GPA : 2.3")
elif(marks>= 58 and marks <=60):
    print("GPA:2.00")
elif(marks>=54 and marks<=57):
    print("GPA:1.99")
elif(marks>=50 and marks<=53):
    print("GPA:1.66")
else:
    print("GPA:0.00")
