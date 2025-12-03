#question:https://www.geeksforgeeks.org/problems/the-fizzbuzz-program/1?page=1&category=python&sortBy=submissions
# User function Template for python3

def fizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)