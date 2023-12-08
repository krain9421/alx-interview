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
    # List of unlocked boxes
    unlocked = []
    for listt in boxes:
        if i == 0:
            pass
        else:
            i = i + 1
            for number in listt:
                if i == 1:
                    if number in range(i+1, numBoxes):
                        unlocked.append(number)
                else:
                    if number in range(0, i) or number in range(i, numBoxes):
                        unlocked.append(number)

    # Check the list of unlocked boxes
    for number in range(0, numBoxes):
        if number in unlocked:
            pass
        else:
            return False

    return True

