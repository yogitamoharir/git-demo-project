'''
 Assignment numbers 1

'''
#10. Write a program to print every character of a string entered by the user in a new line using a loop
# user_input=input("enter your number:- ")
# for i in user_input:
#     print(i)

# 11. Write a program to find the length of the string "machine learning" with and without using len function.
# ml="machine learning"
#1) print(len(ml))

# 2)
# count=0
# for i in ml:
#     count=count+1
# print(count)

# 12.Write a program to check if the word 'orange' is present in the "This is orange juice".
# fruit="This is orange juice"
# if "orange" in fruit:
#     print("orange is present fruit")
# else:
#     print("not available")

#13.Write a program to find the number of vowels, consonants, digits, and white space characters in a string.
# my_str="apple is my fav fruit and its cost is 9004514488975 rs per piece    "
# vowels=0
# consonants=0
# digi=0
# space=0
# for i in my_str:
#     if  (i=='a' or i=="e" or i=="i" or i=="o" or i=="u" ):
#         vowels=vowels+1
#
#     # elif (my_str[i]>='0' and  my_str[i]<='9'):
#     elif (i>='0' and  i<='9'):
#
#         digi=digi+1
#
#     elif (i== ' '):
#         space=+1
#     else:
#         consonants=consonants+1
#
#
# print("vowels in my_str is" , vowels)
# print("consonats is ",consonants )
# print("Digits is ",digi )
# print("Space is ",space )

# que.14)Write a Python program to count Uppercase, Lowercase, special character,
# and numeric values in a given string.


# my_str="Apple Is My fav fruit and its cost  @#$%^*_+! is 9004514488975 per piece"
# upper=0
# lower=0
# digi=0
# special=0
# for i in my_str:
#     if  i.isupper()==True:
#      upper+=1
#     if  i.islower()==True:
#      lower+=1
#     elif (i>='0' and  i<='9'):
#        digi=digi+1
#     else:
#         special=special+1
# print("uppercase in my_str is" , upper)
# print("lower is ",lower )
# print("Digits is ",digi )
# print("Spacial char is ",special )

# Que.15. Write a program to make a new string with all the consonants deleted from the
# string "Hello, have a good day".

# str1="Hello, have a good day"
# new_str=" "
# for i in str1:
#     if i.islower()==True or i.isupper()==True:
#      new_str+=i
# print(new_str)

# 16. Write a Python program to remove the nth index character from a non-empty
# string.
# str2="my name is yogita moharir "
# user=int(input("Enter your index:-"))
# for i in range(len(str2)):
#     if i==user:
#         print(str2[i])
#         break
# else:
#     print("Out of range")

# 17. Write a Python program to change a given string to a new string where the
# first and last characters have been exchanged.

# str="my name is yogita moharir"
# # new_str=old.replace("m","r",1)
# new_str=str[-1]+str[1:-1]+str[0]
#
# print(new_str)

# 18. Write a Python program to count the occurrences of each word in a given sentence
# str3="my name is yogita moharir, and yogita is good girl"
# str4=str3.split()
# print(str4)
# a=input("enter your Word:- ")
# count=0
# for i in str4:
#     if i==a:
#      count+=1
# print(f"{a} and {count}")

# 19. How do you count the occurrence of a given character in a string?
# str3="my name is yogita moharir, and yogita is good girl"
# str4=str3.split()
# print(str4)
# a=input("enter your Word:- ")
# count=0
# for i in str3:
#     if i==a:
#      count+=1
# print(f"{a} and {count}")

# 20. Write a program to find last 10 characters of a string?
# str3="my name is yogita moharir, and yogita is good girl"
# print(str3[-10:])

# 21. WAP to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters.
# str3="myNAme is yogita moharir, and yogita is good girl"
# sort=str3[:5]
# count=0
# for i in sort:
#     if i.isupper()==True:
#         count+=1
#         if count==2:
#             print(str3.upper())

# 22. Write a Python program to remove a newline in Python.
# str4="myNAme is yogita moharir\n, and \n is good girl"
# print(str4)
# str5=str4.replace("\n", "")
# print(str5)

# 23. Write a Python program to swap commas and dots in a string
# ○ Sample string: "32.054,23"
# ○ Expected Output: "32,054.23"
# str6="32.054,23"
# x=str6.replace("," , "dot")
# y=x.replace(".",",")
# z=y.replace("dot",".")
# print(z)

# 24. Write a Python program to find the first repeated character in a given string
# repeted_words="Write a Python program to find the first repeated character in a given string"
# xx=repeted_words.lower()
# print(xx)
# for i in xx:
#     if xx.count(i)==2:
#         print(i)
#         break

# 25. Write a Python program to find the second most repeated word in a given string
# repeted_words="Write a  Python program to find the first repeated character in a given string"
# xx=repeted_words.lower().split()
# print(xx)
# l1=[]
# for i in xx:
#     if xx.count(i)==2:
#      l1.append(i)
# print(l1)
# print(l1[1])

# 26. Python program to Count Even and Odd numbers in a string

# str3 = "12 3 65 48 75 9 8 66 5 89"
# str2 = str3.split()
# print(str2)
# map_object = map(int, str2)
# str4=list(map_object)
# print(str4)
# def category(str4):
#     for i in str4:
#         if i%2==0:
#             print("this is even number:",i)
#         else:
#             print("this is odd number:",i)
# category(str4)

# a="1234567890"
# count=0
# odd=0
# for i in a:
#     if int(i)%2==0:
#         count+=1
#     elif int(i)%2!=0:
#         odd+=1
# print("Odd number count is ", odd)
# print("Even number count is ", count)

# 27. How do you check if a string contains only digits?
# b="1234567890"
# b="1256632"
# c=b.isnumeric()
# print(c)

# # x=b.split()
# # y=map(int,x)
# # z=list(y)
# # print(z)
# # for i in z:
# #     if int(i) !=0-9:
# #      break
# #     else:
# #         print("this is combination str")
# # print("This is  not digit only..")

# 28. How do you remove a given character/word from String?
# my_line="this is yogita moharir"
# x=my_line.replace("yogita","x")


# text = input('Enter a string: ')
# words = text. split()
# print(words)
# data = input('Enter a word to delete: ')
# status = False
# for word in words:
#     if word == data:
#         words. remove(word)
#         status = True
# if status:
#     text = ' '. join(words)
#     print('String after deletion:',text)
# else:
#     print("Word not present in string")

# 29. Write a Python program to remove the characters which have odd index values of a given string
# text = "my self yogita moharir"
# odd=""
# for i in text:
#     if (text.index(i))%2!=0 :
#         odd+=i
# print(odd)

# 30. Write a Python function to reverses a string if its length is a multiple of 5
# text1 = "my self yogit moharirmko, love to trave"
# xx=text1.split()
# print(xx)
# for i in xx:
#     if len(i)%5==0:
#         x1=i[::-1]
#         print(x1)

# 31. Write a Python program to format a number with a percentage(0.05 >> 5%)
# num=0.658
# percent="{:.0%}".format(num)
# print(percent)

# 32. Write a Python program to reverse words in a string
# ui=input("Enter your word:- ")
# x=ui[::-1]
# print(x)

# 33. Write a Python program to swap cases of a given string
# my_swap="Python Is My Favurite lANGUAGE"
# z=my_swap.swapcase()
# print(z)

# 34. Write a Python program to remove spaces from a given string
# space="   Python Is My Favurite lANGUAGE     bdw   "
# c=space.replace(" ","")
# print(c)

# 35. Write a Python program to remove duplicate characters of a given string
# dupli="Python Is My Favurite lANGUAGE Is My Favurite lANGUAGE"
# m=dupli.split()
# good= " "
# for i in m:
#     if i not in good:
#         good+=i
# print(good)

# 36. Write a Python Program to find the area of a circle
# pi=3.14
# data=float(input("enter your radius:- "))
# radius=pi*data*data
# print(radius)

# 37. Python Program to find Sum of squares of first n natural numbers
# x=int(input("enter your number: "))
# square=0
# for i in range(1,x+1):
#     if x>=1:
#         square+=(i**2)
# print(square)

# 38. Python Program to find cube sum of first n natural numbers
# x=int(input("enter your number: "))
# square=0
# for i in range(1,x+1):
#     if x>=1:
#         square+=(i**3)
# print(square)

# 39. Python Program to find simple interest and compound interest











# 40. Python program to check whether a number is Prime or not

# a number that is divisible only by itself and 1 (e.g. 2, 3, 5, 7, 11).

# num = 22
#
# # To take input from the user
# #num = int(input("Enter a number: "))
#
# # define a flag variable
# flag = False
#
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
#
# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")













