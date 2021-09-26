# Lists
list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]  # creating a list

len(list1)  # returns the number of elements in the list

list1[0]  # returns "Cisco" which is the first element in the list (index 0)

list1[0] = "HP"  # replacing the first element in the list with another value

# Lists - methods
list2 = [-11, 2, 12]

min(list2)  # returns the smallest element (value) in the list

max(list2)  # returns the largest element (value) in the list

list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]

list1.append(100)  # appending a new element to the list

del list1[4]  # removing an element from the list by index

list1.pop(0)  # removing an element from the list by index

list1.remove("Juniper")  # removing an element from the list by value

list1.insert(2, "Nortel")  # inserting an element at a particular index

list1.extend(list2)  # appending a list to another list

list1.index(-11)  # returns the index of element -11

list1.count(10)  # returns the number of times element 10 is in the list

list2 = [9, 99, 999, 1, 25, 500,9,10, 10.5, -11]

list2.sort()  # sorts the list elements in ascending order; modifies the list in place

list2.reverse()  # reverses the elements of the list

sorted(list2)  # sorts the elements of a list in ascending order and creates a new list at the same time

sorted(list2, reverse=True)  # sorts the elements of a list in descending order and creates a new list at the same time

list1 + list2  # concatenating two lists

list1 * 3  # repetition of a list
a_list = list2
# Lists - slicing (works the same as string slicing, but with list elements instead of string characters)
a_list[5:15]  # slice starting at index 5 up to, but NOT including, index 15; so index 14 represents the last element in the slice
a_list[5:]  # slice starting at index 5 up to the end of the list
a_list[:10]  # slice starting at the beginning of the list up to, but NOT including, index 10
a_list[:]  # returns the entire list
a_list[-1]  # returns the last element in the list
a_list[-2]  # returns the second to last element in the list
a_list[-9:-1]  # extracts a certain sublist using negative indexes
a_list[-5:]  # returns the last 5 elements in the list
a_list[:-5]  # returns the list minus its last 5 elements
a_list[::2]  # adds a third element called step; skips every second element of the list
a_list[::-1]  # returns a_list's elements in reverse order


#remove duplicate from list
print(set(list2))
print(set(list1).intersection(set(list2)))
print(set(list1).difference(set(list2)))
print(set(list1).union(set(list2))

#frozenset are immutable however sets are mutable

to make list immutable
f1 = frozenset(list1)
#now we can add or delete in f1


# Sets - unordered collections of unique elements
set1 = {"1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"}  # creating a set

list1 = [11, 12, 13, 14, 15, 15, 15, 11]
string1 = "aaabcdeeefgg"

set1 = set(list1)  # creating a set from a list; removing duplicate elements; returns {11, 12, 13, 14, 15}

set2 = set(
    string1)  # creating a set from a string; removing duplicate characters; returns {'b', 'a', 'g', 'f', 'c', 'd', 'e'}; remeber that sets are UNORDERED collections of elements

len(set1)  # returns the number of elements in the set

11 in set1  # returns True; checking if a value is an element of a set

10 not in set
1  # returns True; checking if a value is an element of a set

set1.add(16)  # adding an element to a set

set1.remove(16)  # removing an element from a set

# Frozensets - immutable sets. The elements of a frozenset remain the same after creation.
fs1 = frozenset(list1)  # defining a frozenset

fs1
frozenset({11, 12, 13, 14, 15})  # the result

type(fs1)
<


class 'frozenset'>  # the result

# proving that frozensets are indeed immutable


fs1.add(10)
AttributeError: 'frozenset'
object
has
no
attribute
'add'

fs1.remove(1)
AttributeError: 'frozenset'
object
has
no
attribute
'remove'

fs1.pop()
AttributeError: 'frozenset'
object
has
no
attribute
'pop'

fs1.clear()
AttributeError: 'frozenset'
object
has
no
attribute
'clear'

# Sets - methods
set1.intersection(set2)  # returns the common elements of the two sets

set1.difference(set2)  # returns the elements that set1 has and set2 doesn't

set1.union(
    set2)  # unifying two sets; the result is also a set, so there are no duplicate elements; not to be confused with concatenation

set1.pop()  # removes a random element from the set; set elements cannot be removed by index because sets are UNORDERED collections of elements, so there are no indexes to use

set1.clear()  # clearing a set; the result is an empty set
