# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(USERNAME):
    USERNAME = "CourtneyN"
    print(USERNAME)
hello_name(' ')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    for num in range(1,101):
        if int(num) % 2 != 0:
            print(num, )
first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max = a_list[ 0 ]
    for num in a_list:
        if num > max:
            max = num
    return max
print(max_num_in_list([7,23,78,4,5]))
               

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
# but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

a_year = 2022
def is_leap_year(a_year):
    leap = False
    if (a_year % 4 == 0 and a_year % 100 != 0) or a_year % 400 == 0:
        leap = True
    return leap
print(is_leap_year(2023))


               
# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.


def checkConsecutive(a_list):
    if a_list == list(range(a_list[0], a_list[-1] + 1)):
        return True
    else:
        return False
a_list = [10,23,57,1,2]
a_list = [1,2,3,4,5]
print(checkConsecutive(a_list))