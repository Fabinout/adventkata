__author__ = 'fabienlamarque'


def calculatestairs(parameter):
    count = 0
    for char in list(parameter):
        if char == "(":
            count += 1
        else:
            count -= 1

    return count
