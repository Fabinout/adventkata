__author__ = 'fabienlamarque'


def calculatestairs(parameter):
    count = 0
    for char in list(parameter):
        if char == "(":
            count += 1
        else:
            count -= 1

    return count


def basemententrance(parameter):
    count = 0
    for index, char in enumerate(parameter):
        if char == "(":
            count += 1
        else:
            count -= 1
            if count < 0:
                return index + 1
    return index
