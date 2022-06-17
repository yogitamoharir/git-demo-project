"""
#uppercase(.upper)
#format()
Use the format() method to insert numbers into strings:

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#lowercase(.lower)
#whitespaces-strip

#.replace
.split- The split() method splits the string into substrings if it finds instances of the separator

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
"""
## All string methods returns new values. They do not change the original string.
#1)capitalize(1st letter upcase), casefold(all lower),

txt = "hello my Dear and, And WELCOME to my world."
#z=txt.center(100)
#print(z)
#b=txt.encode()
#print(b)
x = txt.capitalize()
y=txt.casefold()
a=txt.count("my")
c=txt.endswith(".")
d=txt.expandtabs(2)
e=txt.find("m", 10, 35)  ## if position not found it gives -1 as output
d=txt.index("m", 10, 35)  ## it find exact postion nd if not found give error
print(d)
print(e)
print(c)
print(a)
print(y)
print (x)

lis="I Am working in citiustech healthcare pvt ltd"
f=lis.isalnum()
g=lis.isnumeric()
h=lis.isspace()
i=lis.isalpha()
j=lis.islower()
k=lis.isprintable()
l = lis.istitle()
print("this is under l ",l)
print("this is under k ",k)
print("this is under j ",j)
print("this is under i ",i)
print("this is under f ",f)
print("this is under g ",g)
print("this is under h ",h)

my_list=["yog","tush","hritik","aish"]
m="#".join(my_list)

print(m)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

n = mySeparator.join(myDict)

print(n)

fruit = "I could eat bananas all day"
xx = fruit.partition("bananas")
yy=fruit.split()
print(yy)
print(xx)

txt1 = "Thank you for the music\nWelcome to\n the jungle"

x1 = txt1.splitlines()
x2 = txt1.swapcase()

print(x1)
print("this is x2", x2)

mm=txt1.replace('T','W')
print("this is mm" ,mm)



# a= "Yogita isgood girl, and she lik_to visit,new places, 125 and like,to see new sea"

# txt = "25656550"
#
# x = txt.zfill(10)
#
# print(x)

# txt = "Hello, welcome to my world."
#
# x = txt.rindex("e", 5, 10)
#
# print(x)

# b="hello my  beautiful dear"
# m1=b.title()
# print(m1)

# txt = "     banana     "
#
# x = txt.strip()
#
# print("of all fruits", x, "is my favorite")



# x14=a.expandtabs(4)
# print(x14)

###  "all "is" method in string return True and False only" ###
# x1=a.islower()
# print("This is unde x1", x1)
# x2=a.isalpha()
# print("This is unde x2", x2)
# x3=a.isalnum()
# print("This is unde x3", x3)
# x4=a.isspace()
# print("This is unde x4", x4)
# x5=a.isnumeric()
# print("This is unde x5", x5)
# x6=a.isprintable()
# print("This is unde x6", x6)
# x7=a.isdigit()
# print("This is unde x7", x7)
# x8=a.islower()
# print("This is unde x8", x8)
# x9=a.isupper()
# print("This is unde x9", x9)
# x10=a.isascii()
# print("This is unde x10", x10)
# x11=a.isdecimal()
# print("This is unde x11", x11)
# x12=a.isidentifier()
# print("This is unde x12", x12)
# x13=a.istitle()
# print("This is unde x13", x13)

# f=a.replace("and","und")
# print(f)


# e=a.split( ",")
# print(e)

# x=a.index("i",10,25)
# print(x)
#
# b=a.count("i",6,35)
# print(b)

# c=a.find("to", 35,66)
# print(c)

# d="#".join(b)
# print(d)


