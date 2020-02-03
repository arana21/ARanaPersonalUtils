"""
This file implements common search algorithms:

1. Linear search
2. Binary search
3.
"""


class SearchAlgorithms:
    """
    Common search algorithms
    """

    def __init__(self):
        pass

    def linear_search(self, arr, item_to_search):
        """Implements linear search algorithm.

        Args:
            arr (list)
            item_to_search

        Return:
            (int or None): Position of item in arr if present. Else None.
        """
        for i in range(len(arr)):

            if arr[i] == item_to_search:
                return i

        return None

    def binary_search(self, arr, item_to_search):
        """Implements linear search algorithm.

        Args:
            arr (list)
            item_to_search

        Return:
            (int or None): Position of item in arr if present. Else None.
        """
        pass
