"""
    A fun coding exercise using a recursive function
"""


def pyramid_sum(lower, upper, margin=0):
    """A function that return values that form a side pyramid. Expects two values(low, high)"""

    blanks = (" " * margin)
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result

pyramid_sum(1, 4)