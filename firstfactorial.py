'''
DCC: 3/19/2018
Goal: Using the Python language, have the function FirstFactorial(num) take
       the num parameter being passed and return the factorial of it (e.g. if
       num = 4, return (4 * 3 * 2 * 1)). For the test cases, the range will
       be between 1 and 18 and the input will always be an integer.
'''

import sys

def FirstFactorial(num):
    if num < 1:
        return 1
    else:
        return num * FirstFactorial(num - 1)

def main():
    num = int(input("Enter a number to get the factorial of: "))
    print("The factorial of " + str(num) + " is: " + str(FirstFactorial(num)))

main()
