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


