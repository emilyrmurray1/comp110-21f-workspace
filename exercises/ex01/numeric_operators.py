"""Numeric Operators Assignment."""

__author__ = "730238066"

left_hand_side: int = int(input("Left-Hand Side: "))
right_hand_side: int = int(input("Right-Hand Side: "))
exponent: int = left_hand_side ** right_hand_side
print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(exponent))
division: float = left_hand_side / right_hand_side
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(division))
int_division: int = left_hand_side // right_hand_side
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(int_division))
remainder: int = int(left_hand_side % right_hand_side)
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(remainder))