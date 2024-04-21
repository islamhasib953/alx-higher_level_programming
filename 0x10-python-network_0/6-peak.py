
#!/usr/bin/python3
"""
    The function `find_peak` takes in a list of numbers
    and returns the peak element, which is an
    element that is greater than its adjacent elements.
    :param list_of_integers: The parameter `list_of_integers`
    is a list of numbers
    :return: the peak element from the given list.
"""


def find_peak(list_of_integers):
    """BRUTE force implementation for question
    """
    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers[0], list_of_integers[1])
    elif n == 0:
        return None
    mid = n // 2
    if list_of_integers[mid] > list_of_integers[mid - 1] and \
            list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    elif list_of_integers[mid] <= list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid+1:])
