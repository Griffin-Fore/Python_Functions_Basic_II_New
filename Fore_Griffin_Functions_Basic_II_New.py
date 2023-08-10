# 1. Countdown - Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number 
# (as the 0th element) down to 0 (as the last element).

# def countdownFromNumber(number):
#     countdownList = []
#     for i in range(number, -1, -1):
#         countdownList.append(i)
#     return countdownList

# print(countdownFromNumber(5))


# 2. Print and Return - Create a function that will receive a list with two numbers.
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

# def print1Return2(list):
#     print(list[0])
#     return list[1]

# print(print1Return2([2,5]))


# 3. First Plus Length - Create a function that accepts a list and returns
# the sum of the first value in the list plus the list's length.

# def firstPlusLength(list):
#     return list[0] + len(list)

# a = [1,2,3,4,5]

# print(firstPlusLength(a))


# 4. Values Greater than Second - Write a function that accepts a list and creates a new list
# containing only the values from the original list that are greater than its 2nd value.
# Print how many values this is and then return the new list.
# If the list has less than 2 elements, have the function return False

# def valuesGreaterThanSecond(list):
#     new_list = []
#     for i in range(0,len(list)):
#         if(list[i] > list[1]):
#             new_list.append(list[i])
#     print(len(new_list))
#     return new_list

# b = [5,2,3,2,1,4]
# print(valuesGreaterThanSecond(b))


# This Length, That Value - Write a function that accepts two integers as parameters: size and value.
# The function should create and return a list whose length is equal to the given size,
# and whose values are all the given value.

# def length_and_value(x,y):
#     new_list = []
#     for i in range(x):
#         new_list.append(y)
#     return new_list

# print(length_and_value(4,7))
# print(length_and_value(6,2))