set2={"mango","bannaa","pineapple", "lemon"}
x=set2.add("mosambi")
print(set2)

set3={"red","yellow","green","orange"}
set2.update(set3)
print(set2)

y=set2.copy()
print(y)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
thisset.remove("apple")
print(thisset)

thisset.discard("apple")
print(thisset)


set_list={"28","yogo","vish","seja","varun"}
aa=set_list.add("mango")
xx=set_list.add("gasket")
bb=set_list.remove("28")
mm=["kjf","RRR"]
cc=set_list.update(mm)
dd=set_list.discard("varun")
print(set_list)

ee=set_list.copy()
ee.add("tushar")
print(ee)
f=ee.difference(set_list)
print(f)
g=ee.intersection(set_list)
print("this is g" , g)

h=set_list.isdisjoint(ee)   # true= if not any common element
i=set_list.issubset(ee)     #true= if a all common element of set_list in ee
j=set_list.issuperset(ee)
k=ee.issuperset(set_list)  #Return True if all items set ee are present in set_list
np=ee.pop()
print("ths is np",np)
print(ee)
z =ee.symmetric_difference(set_list)   ##Return a set that contains all items from both sets,except items that are present in both sets
print("this is uder z", z)
print(h)
print(i)
print(j)
print(k)
lk=set_list.union(ee)  #Return a set that contains all items from both sets, duplicates are excluded

# lk=ee.union(set_list)
print(set_list)
print(ee)
print("this is lk", lk)