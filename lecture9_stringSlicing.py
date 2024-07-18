#SLICING(access some elemnts)
intro = ''' Hi , my name is Areeba Qadeer . I am from Rawalpindi,
Currently pursuing bs cybersecurity from comsats university Islamabad'''

print(intro[0:23])

print("The length of the string is :" , len(intro))
print("The length of the sliced sring is :" , len(intro[0:23]))

#negaitve slicing
print(intro[0:-3])
print(len(intro[0:-3]))

print(intro[-5:-3])
print(len(intro[-5:-3]))
