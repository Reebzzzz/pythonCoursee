print("*************** REEBZ CALCULATOR **************")

num1 = int(input("Enter number 1:"))
num2 = int(input ("Enter number 2 :"))
print ("options are :" "+" , "-" , "*" , "/" ," **"," %")
operation=input("Enter the operation you want to perform:")


if operation == "+" :
    print (num1 + num2)
    
elif operation == "-":
    print(num1 -  num2 )    
    
elif operation == "*":
    print(num1 * num2 )    
    
elif operation == "/":
    print(num1 / num2 )    


elif operation == "//":
    print(num1 // num2 )    
    
elif operation == "%":
    print(num1 % num2 )  
    
elif operation == "**":
    print(num1 ** num2 )    
    
else :
    print( "Kindly enter correct values" )    
    