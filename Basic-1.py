# Exercise 1: Given two integer numbers 
#return their product. If the product is greater than 1000, then return their sum
#
#
number1 = 30
number2 = 40

def multiply_nums(number1,number2):
    number3= number1*number2
    if number3 > 1000:
       return number1+number2
    else :
       return number3

print("Result",multiply_nums(number1,number2))