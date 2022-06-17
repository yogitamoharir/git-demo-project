##A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.

##   lambda arguments : expression

# x=lambda a:a*5
# print(x(6))
#
# y=lambda a,b: a*b
# print(y(3,6))


def myfunc(n):            #### ASK TO heart
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))