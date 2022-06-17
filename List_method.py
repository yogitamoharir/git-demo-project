list1 = ["apple", "banana", "cherry"]
list1.append("kiwi")
print(list1)
list1.insert(2,"grapes")
print(list1)

tropical = ["mango", "pineapple", "papaya"]
list1.extend(tropical)
print(list1)
list1.append(tropical)
print(list1)

list1.remove("papaya")
print(list1)
list1.pop()
print(list1)

del list1[0]
print(list1)

list1.clear()
print(list1)

list1.append("ram")
print(list1)
list2=["raja","shaym","daya","acp"]
list1.extend(list2)
print(list1)

name=["monu","rani", "sandip","nil"]
update_name=[]

for item in name:
    if 'i' in item:
        update_name.append(item)
print(update_name)

list2 = ["sona", "mone", "Kiyara", "chhaya", "chhaya", "mone", ]

list2.reverse()

print(list2)

list3=list2.copy()
print((list3))

list4=list(list3)
print(list4)
nm=list2.count("chhaya")
print(nm)
list2.index("Kiyara")

##################### List Method ############################

# a=["yog","pillo","mau","manu","don","yog","mau"]
# x1=a.count("pillo")
# print(x1)

# x2=a.index("mau",3,7)
# print(x2)
#
# a.append(["mira","aa"])  ## its add as a list or single element at last
# print(a)
#
# a.pop()
# print(a)
#
# a.extend(["m","g","w"])  ## its add as a element at last its extend at last
# print(a)
#
# a.remove("w")
# print(a)
#
# a.insert(2, "kal")
# print(a)
#
# b=a.copy()
# print(b)
#
# a.sort()
# print(a)
#
# a.reverse()
# print(a)
#
# a.clear()
# print(a)