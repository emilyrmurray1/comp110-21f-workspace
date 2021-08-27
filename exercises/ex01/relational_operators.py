"""On your own, relational operators."""

__author__ = "730238066"

left_hand_side: int = int(input("Left-Hand Side: "))
right_hand_side: int = int(input("Right-Hand Side: "))
less_than: int = bool(left_hand_side < right_hand_side)
print(str(left_hand_side) + " < " + str(right_hand_side) + " is " + str(less_than))
is_at_least: int = bool(left_hand_side >= right_hand_side)
print(str(left_hand_side) + " >= " + str(right_hand_side) + " is " + str(is_at_least))
equal: int = bool(left_hand_side == right_hand_side)
print(str(left_hand_side) + " == " + str(right_hand_side) + " is " + str(equal))
not_equal: int = bool(left_hand_side != right_hand_side)
print(str(left_hand_side) + " != " + str(right_hand_side) + " is " + str(not_equal))