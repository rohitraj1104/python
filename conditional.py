# If / Elif / Else conditionals - executing code based on one or more conditions being evaluated as True or False; the "elif" and "else" clauses are optional
x = 5

if x > 5:  # if the "x > 5" expression is evaluated as True, the code indented under the "if" clause gets executed, otherwise the execution jumps to the "elif" clause...
    print("x is greater than 5")
elif x == 5:  # ...if the "x == 5" expression is evaluated as True, the code indented under the "elif" clause gets executed, otherwise the execution jumps to the "else" clause
    print("x IS 5")
else:  # this covers all situations not covered by the "if" and "elif" clauses; the "else" clause, if present, is always the last clause in the code block
    print("x is NOT greater than 5")

# result of the above "if" block
x IS 5

# For / For Else loops - executes a block of code a number of times, depending on the sequence it iterates on; the "else" clause is optional
vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

for element in vendors:  # interating over a sequence and executing the code indented under the "for" clause for each element in the sequence
    print(element)
else:  # the indented code below "else" will be executed when "for" has finished looping over the entire list
    print("The end of the list has been reached")

# result of the above "for" block
Cisco
HP
Nortel
Avaya
Juniper
The
end
of
the
list
has
been
reached

x = "Cisco"

if "i" in x:
    if len(x) > 3:  # if nesting
        print(x, len(x))

Cisco
5  # result of the above block

list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:
    for j in list2:  # for nesting
        print(i * j)

40
80
120
50
100
150
60
120
180  # result of the above block

x = 1
while x <= 10:
    z = 5
    x += 1
    while z <= 10:  # while nesting
        print(z)
        z += 1

5
6
7
8
9
10
5
6
7
8
9
10
5
6
7
8
9
10
5
6
7
8
9
10
5
6
7
8
9
10
5
6
7
8
9
10
5
6
7
8
9
10
5
6
7
8
9
10
5
6
7
8
9
10
5
6
7
8
9
10  # result of the above block

for number in range(10):
    if 5 <= number <= 9:  # mixed nesting
        print(number)

5
6
7
8
9  # result of the above block