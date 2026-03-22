"""Utility functions for common operations."""


def is_palindrome(s):
    """Check if a string is a palindrome.

    Args:
        s: Input string.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def fizzbuzz(n):
    """Return FizzBuzz result for a number.

    Args:
        n: A positive integer.

    Returns:
        'FizzBuzz' if divisible by both 3 and 5,
        'Fizz' if divisible by 3,
        'Buzz' if divisible by 5,
        the number as a string otherwise.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    return str(n)


def flatten(lst):
    """Flatten a nested list into a single list.

    Args:
        lst: A potentially nested list.

    Returns:
        A flat list containing all elements.

    Example:
        >>> flatten([1, [2, [3, 4], 5], 6])
        [1, 2, 3, 4, 5, 6]
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
