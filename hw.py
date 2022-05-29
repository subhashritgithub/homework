 Write a Python program to get the smallest number from a list.


from random import random


def smallest():
    small = 1
    a = [1, 2, 3, 4, 5, 6, 7]
    for i in a:
        if i < small:
            small = i
    return(small)


print(f"smallest number is {smallest()}")


# 2.  Write a Python function to check a list is empty or not.
def empty():
    c = 0
    a = [1, 2]
    for i in a:
        c = c+1
    if c > 0:
        print("not empty")
    else:
        print("empty")


empty()

# 3.  Write a Python program to select an item randomly from a list.
a = [1, 2, 3, 4, 5]
print(random.choice(a))

# 4.  Write a Python program to copy a list.
a = [1, 2, 3, 4]
b = []
b = a.copy()
print(a)
print(b)

# 5.  Write a Python program to find the 2nd largest number in a list.
# a = [1, 2, 3, 4, 5, 6, 7, 9, 40, 23]
# largest = 0
# secondL = 0
# for i in a:
#     if i > largest:
#         secondL = largest
#         largest = i
# print(f"second largest number is {secondL}")
a = [1, 2, 4, 55, 6, 7, 89, 12, 99, 1]
a.sort()
b = len(a)-2
print(f"Second largest number is {a[b]}")


# 6.  Write a Python program to print a specified list after removing the 3rd elements
a = [1, 2, 3, 4, 5, 6, 7, 9, 40, 23]
a.remove(3)
print(a)

# 7. Write a Python program to count the number of even and odd numbers from a series of numbers.
a = [1, 2, 3, 4, 5, 6, 7, 9, 40, 23]
even = 0
odd = 0
for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"Odd Number in series are {odd}")
print(f"even Number in series are {even}")


# 8. Write a Python program to add an item in a tuple
b = (1, 23, 4)
print(b)
b = list(b)
b.append(10)
b = tuple(b)
print(b)


# 9.  Write a Python program to convert tuple to list.
a = (1, 23, 4)
print(a)
a = list(a)
print(a)


# 10.  Write a Python program to convert a tuple to a string.
tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
a = ""
str = a.join(tup)
print(str)


# 11.  Write a Python program to convert a list to a tuple.
a = {1, 23, 4}
print(a)
a = tuple(a)
print(a)


# 12.  Write a Python Program to Convert List of Tuple into Dictionary
# l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
# dictionary = {}
# for tups in l:
#     if tups[0] not in dictionary:
#         dictionary[tups[0]] = [tups[1]]
#     else:
#         dictionary[tups[0]] = dictionary[tups[0]] + [tups[1]]
# print(dictionary)

l = [(1, "a"), (2, "b"), (3, "c")]
dictionary = {}
for z in l:
    dictionary[z[0]] = z[1]
    print(dictionary)


# 13.  Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
dictionary1 = {0: 10, 1: 20}
dictionary1[2] = "30"
print(dictionary1)


"""
14. Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)


# 15.  Write a Python script to check if a given key already exists in a dictionary.
a = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
b = a.keys()
print(b)
c = (int(input("Enter your key")))
for i in b:
    if i == c:
        print("The key is already in dictionary")
        exit()
print("The Key is not in dictionary")


# 16.  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
dic = {}
for i in range(1, 16):
    dic[(i)] = i**2
print(dic)


# 17. Write a Python script to merge two Python dictionaries.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic1.update(dic2)
print(dic1)

# 18. Write a Python program to find the 3nd largest number in a list.
a = [1, 2, 4, 55, 6, 7, 89, 12, 99, 1]
a.sort()
b = len(a)-3
print(f"Third largest number is {a[b]}")

# 19. Write a Python program to create a set.
a = set()
for i in range(10):
    a.add(i)
print(a)


# 20. Write a Python program to iteration over sets.
"""
malai fix solution tha bhayena kasai lai tha xa bhane pathau hai
"""


# 21. Write a Python program to add member(s) in a set.
set1 = {1, 2, 3, 45, 2}
a = int(input("Enter number of member you want to add in set"))
for i in range(a):
    b = input("Enter first member")
    set1.add(b)
print(set1)

# 22. Write a Python program to remove item(s) from set
set1 = {1, 2, 3, 45, 2}
a = int(input("Enter number of member you want to remove in set"))
for i in range(a):
    b = int(input("Enter first member"))
    set1.remove(b)
print(set1)


# 23. Write a Python program to remove an item from a set if it is present in the set.

set1 = {1, 2, 3, 45, 2}
a = int(input("Enter number of member you want to remove in set"))
for i in range(a):
    b = int(input("Enter first member"))
    set1.discard(b)
print(set1)


# 24. Write a Python program to create an intersection of sets.
a = {1, 2, 3}
b = {2, 43, 2}
c = a.intersection(b)
print(c)


# 25. Write a Python script to check if a given key exists in a dictionary.
a = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
b = a.keys()
print(b)
c = (int(input("Enter your key")))
for i in b:
    if i == c:
        print("The key is already in dictionary")
        exit()
print("The Key is not in dictionary")


# 26. Write a Python script to check if a given values exists in a dictionary.
a = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
b = a.values()
print(b)
c = (int(input("Enter your key")))
for i in b:
    if i == c:
        print("The value is already in dictionary")
        exit()
print("The value is not in dictionary")