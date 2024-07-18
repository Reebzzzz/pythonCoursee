name = "reebzzzzzzzzzzzz"

# finding the length of the string
print("Length of the string is :"  , (len(name)))

#capitalize each word
print("MY NAME IS :"  , (name.upper()))

#stripting method
print(name.rstrip("z"))

#replacing method
print(name.replace("z" , "a"))

#split function
print(name.split(" "))

intro = ''' Hi , my name is Areeba Qadeer . I am from Rawalpindi,
Currently pursuing                  bs cybersecurity                                                from comsats university Islamabad'''
 
print(intro.split(" "))

print(name.capitalize())

#placing string in center
print(name.center(50))

#counting words occurence
print (name.count("z"))

#checking the ending character of the string
print(name.endswith("z"))
print(name.endswith("k"))

#checking value in between the string
print(name.endswith("z" , 3 , 7))

#using find functions
print (intro.find("from"))
print(intro.find("reebz"))

#using index method
print(intro.index("from"))


#checking alphanumeric numbers
print(intro.isalnum())

#checking printable characters
print(intro.isprintable())
print(name.isprintable())

#checking whitespaces
print("space:" ,intro.isspace())
print("space :" ,name.isspace())

#using title function
print(name.istitle())

print(name.title())