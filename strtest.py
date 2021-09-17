name="Rohit Raj"
namewithdollar="$$$ Rohit Raj $$$"

A = name.strip()
B = name.strip('$')

print(A)
print(B)

C = name.replace(" ", "MYSPACE")
print(C)
D = C.split("MYSPACE")
print(D)

E =  "**".join(D)
print(E)

F = "__".join(D)
print(F)

x = "cisco"
y = "switch"
z= x+x    #string with operand
print(z)
k= x*3    #string with operand
print(k)
if('r' in x):  #string with true/false check
    print("yes,its there")

#================================
print("my name is : %s and I am %d years old and my weight is %f" % (A,30,83.5))

print("my name is : {} and I am {} years old and my weight is {}".format(A,30,83.5))
#=================================

print(f"my name is {A} and I have {x} {y}")

print(f"my name is {A.lower()} and I have {x.upper()} {y.replace("switch","router")})