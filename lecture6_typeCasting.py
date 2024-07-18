#changning  datatype string to integer
value1 = " 30"
value2 = "20"

print (int(value1) + int(value2))

# integer to string 
int_num = 123
str_num = str(int_num)
print(str_num) 

# string to float
str_num = "123.45"
float_num = float(str_num)
print(float_num)



#IMPLICIT TYPECASTING
c = 19 
d = 50.3
print ("implicit typecast :" , c + d )
print (type(c+d))