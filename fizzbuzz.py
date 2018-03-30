'''
DCC: 3/22/2018
Goal: Write a program that prints the numbers from 1 to 100. But for multiples
        of three print “Fizz” instead of the number and for the multiples of
        five print “Buzz”. For numbers which are multiples of both three and
        five print “FizzBuzz”."
'''

def FizzBuzz(num):
    if (num % 3 == 0) and (num % 5 == 0):
        return 'FizzBuzz'
    elif (num % 3 == 0):
        return 'Fizz'
    elif (num % 5 == 0):
        return 'Buzz'
    else:
        return num

def main():
    for i in range(1, 100):
        print(str(FizzBuzz(i)) + '\n')

main()
