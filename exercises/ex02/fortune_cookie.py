"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730238066"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

number: int = (randint(1, 4))
print("Your fortune cookie says... ")
if number == 1:
    print("you will be lucky in love.")
if number == 2: 
    print("a great storm is coming your way ")
if number == 3:
    print("you are going to make a lot of money ")
if number == 4:
    print("don't make any rash decisions soon ")
print("Now, go spread positive vibes! ")