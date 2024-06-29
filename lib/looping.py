#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print (counter)
        counter -= 1
    print ("Happy New Year!")

def square_integers(int_list):
    squared_ints= [list*list for list in int_list]
    return squared_ints

def fizzbuzz():
    for i in range(1, 101):  
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(f'{i}')