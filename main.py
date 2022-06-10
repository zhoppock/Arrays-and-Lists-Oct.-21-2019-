print("\n==================Arrays==================\n")

print("-----------Array Function------------")

import array
arr = array.array('i', [1, 2, 3])
print(arr[1])

print("\n------------Normal Array-------------")

classmates = ("Alejandro", "Ed", "Kathryn", "Presila", "Sean", "Peter")
print(classmates[1])

print("\n===================Lists===================\n")

print("\n---------List from Scratch----------")

list_b=[None]*9
#print(list_b[1])
#now fill it with something
list_b[0]='!'
list_b[1]='a'
list_b[2]='b'
list_b[3]='c'
print(list_b[0])
print(list_b[1])
print(list_b[2])
print(list_b[8])

print("\n------------Normal List-------------")

#1a list one data types
years = [1979, 1999, 2019]
#a list of different datatypes
superList = ['a', "Hello world", 2.9, 78]

print(years[0])
print(years[1])
print(years[2])
print(superList[0])
print(superList[1])
print(superList[2])
print(superList[3])

print("\n===============Special Lists===============\n")

print("\n-----------List in a List------------")

uberList = ["not the taxi",[1,2,3,4],"whoo",4.4]
print(uberList[1][0])
#print items
print(uberList[0][0])
print(uberList[0][1])
print(uberList[0][2])
print(uberList[0][3])

#print the 2nd element of the nested list
print(uberList[2][1])
#print the 3rd element of the nested list
print(uberList[2][2])

print("\n-----------Inside the List------------")

superlist =["abc","123"]
print(superlist[0][0])
print(superlist[0][1])
print(superlist[0][2])

print("\n---------While Loop in a List----------")

#code to iterate over a list
loop_list = [12, 13, 54, 7, 91]

# Getting length of list
length = len(loop_list)
i = 0

# Iterating using while loop_list
while i < length:
  print(loop_list[i])
  i += 1

print("\n----------For Loop in a List-----------")

#code to iterate over a list
#using for loop
loop_list = [12, 13, 54, 7, 91]
for i, val in enumerate(loop_list):
  print(i, ",",val)

print("\n----------From Array to List-----------")

from array import *

def array_list(array_num):
  num_list = array_num.tolist()
  print(num_list)