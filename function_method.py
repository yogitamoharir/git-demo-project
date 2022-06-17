# def tri_recursion(k):   ### ask to tush
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)



def calculator(a,b):
  # i=0
  # while (i<2):
  #   i+=1
  #  for i in range(6):

    user_info=input("enter your choice A,M,D,MOD:- ")

    if "A" in user_info:
      print(a+b)
    elif "M" in user_info:
      print(a*b)
    elif "D" in user_info:
      print(a/b)
    elif "MOD" in user_info:
      print(a%b)
    else:
      print("Please enter right choice")
    # continue

a=int(input("enter 1st number:-"))
b=int(input("enter 2nd number:-"))
calculator(a,b)