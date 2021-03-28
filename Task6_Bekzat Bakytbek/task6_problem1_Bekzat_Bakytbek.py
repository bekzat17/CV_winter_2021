#task6 problem 1 prepared by Bekzat Bakytbek
import numpy as np

def solution (N):
    maxZero = bin(N)
    maxZero = maxZero[2:]
    print("Binary value: ", maxZero)
    output = len(max(maxZero.strip('0').split('1')))
    return output

str_number = ""

while(str_number != "stop"):
    str_number = input("Enter positive integer (from 1 to 2 147 483 647) or stop:")
    try:
        number = int(str_number)
        if(number > 0):
            print("Decimal value: ", number)
            print("Binary tab within positive integer:", solution(number))
        else:
            print("Invalid input, enter positive integer")
    except:
        if str_number == "stop":
            print("you terminated the program")
        else:
            print("Invalid input")
