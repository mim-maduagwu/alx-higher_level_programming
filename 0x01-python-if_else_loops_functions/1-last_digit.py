#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num = str(number)
n = len(str_num) - 1
if str[0] == "-":
    print(f"Last digit of {number} is {str[n]} is less than 6 and not 0")
elif int(str_num[n]) < 6 and != 0:
    print(f"Last digit of {number} is {str[n]} is less than 6 and not 0")
elif int(str_num[n]) == 0:
	print(f"Last digit of {number} is {str[n]} is 0")
if int(str_num[n]) > 5:
	print(f"Last digit of {number} is {str[n]} is greater than 5")
