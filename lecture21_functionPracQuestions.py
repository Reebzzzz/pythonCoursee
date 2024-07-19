# finding maxmium number from three numbers
# def findMaxOfThreeNumber (num1 , num2 , num3):
    
#     if(num1 > num2 and num1 > num3 ):
#         maxNum = num1
#     elif(num2 > num1 and num2 > num3):
#         maxNum = num2
#     else:
#         maxNum = num3
#     return maxNum
    
# ans =findMaxOfThreeNumber( 1 , 2 ,3)
# print(ans)


#  function to reverse a string

# def reverseString(str1):  
#     rstr = " "
#     index = len(str1)
#     while(index >0):
#         rstr+= str1[index - 1]
#         index = index -1
        
#     return rstr


# print (reverseString("areeba"))

# factorial of a number

# def calculateFactorial (n):
#     if n == 0:
#         return 1 
#     else :
#         return n*  calculateFactorial (n-1)
    
    
    
# n = int(input("Enter number"))
# print(calculateFactorial(n))
        
# checking prime number
# def checkPrime (n):
#     if(n == 1):
#         return False
#     elif( n == 2):
#         return True
#     else:
#         for i in range (2 , n ):
#             if ( n % i == 0 ):
#                 return False

#         return True
    
# print (checkPrime(9))

# check perfect number
# def perfectNumber(n):
#     sum = 0
#     for x in range(1, n):
#         if n % x == 0:
#             sum += x
#     return sum == n

# print(perfectNumber(5))

# check palindrome
def checkPakindrome (string):
    leftPos = 0 
    rightPos = len(string) -1 
    
    while rightPos >= leftPos:
        if not string[leftPos] == string[rightPos]:
            return False 
         
        leftPos+=1
        rightPos-=1
        
    return True

print(checkPakindrome("areeba"))