"""Counting letters in a string."""

__author__ = "730238066"


from typing import Counter


letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")

print(Counter(letter))