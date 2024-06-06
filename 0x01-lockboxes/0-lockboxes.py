#!/usr/bin/python3
"""Complete the Lockboxes Interview Challenge"""


def canUnlockAll(boxes):
    """Method that determines if all boxes can be opened
        boxes: a list of lists
    """
    # Get the number of lists(indexes) in boxes
    numBoxes = len(boxes)
    # Variable to track the index of a box
    i = 0
    # List that will contain the key of all boxex that can be unlocked
    unlocked = []

    for obj in boxes:
        if type(obj) != list:  # Check if object is a list
            pass
        else:
            for num in obj:  # Loop through all the numbers in a list
                if num in unlocked or num == 0:
                    pass
                else:
                    if i >= 0 and i <= 1:
                        if num in range(i+1, numBoxes):
                            unlocked.append(num)
                    else:
                        if num in range(0, i) or num in range(i+1, numBoxes):
                            unlocked.append(num)
                i = i + 1

    # Check the list of unlocked boxes
    for number in range(1, numBoxes):
        if number in unlocked:
            pass
        else:
            return False

    return True
