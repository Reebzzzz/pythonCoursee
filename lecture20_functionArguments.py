# argument as a tuple
def average (*numbers):
    sum=0
    for i  in numbers:
        sum = sum+i
        
    return  sum/len(numbers)
        
        
ans = average(1,2,2,4,5,6,8,9)
print (ans)


# argument as a dictionary
# def name(**name):
#     print("hello" , name["fname"] , name["lname"] , name["mname"])
    
    
# name(mname="reebz" , fname =" areeba" , lname = " qadeer")

