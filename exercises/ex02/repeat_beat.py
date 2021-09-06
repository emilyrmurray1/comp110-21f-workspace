"""Repeating a beat in a loop."""

__author__ = "730238066"


beat: str = input("What beat do you want to repeat? ")
counter: int = int(input("How many times do you want to repeat it? "))
blank: str = ""

if counter <= 0: 
    print("No beat...")

else:
    while counter > 0:
        blank = blank + beat 
        if counter > 1: 
            blank = blank + " "
        counter = counter - 1
    print(blank)
