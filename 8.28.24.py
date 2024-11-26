# addition = 25

# def sum(a, b):
#     addition = a+b
#     print(addition)
# # here, addition is defined only locally, and can only be called as a variable inside this code block

# print(addition)

# # this print function will not work here because "addition" variable is not defined globally - only locally in the above function
# print("the sum of a and b is: ", addition)
# addition=3
# print(addition)

# # How you make a function in BASH:
# # function sum() {
#   #  addition = a+b
#    # echo $addition
# #}

# sum(10,20)

#import math   # We're learning about modules! This will install the module "Math" into our script. "Math" is a module that consists of a collection of formulas specifically about Math

# from math import sqrt
# print(sqrt(16))   # So in order to use the functions inherent in the Math module, we have to use the name of the module (Math in this instance), and then use a period and call the funciton. It looks like a method, but it's a function!
# import OurModule
# print(OurModule.sum(9,8))

def sum(a,b):
    addition = a+b
    return addition

answer = sum(1,10)
print(answer)