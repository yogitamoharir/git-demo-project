x=("y","o","g","i","t","a","y","o","y")
y=list(x)
y[2]="tushar"
x=tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(y)

z=x.count("y")
print(z)
w=x.index("tushar")
print("this is w", w)