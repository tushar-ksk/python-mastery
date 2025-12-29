def divisibleby5(n):
    """
    This function checks if a number is divisible by 5.
    :param n: The number to check.
    :return: True if n is divisible by 5, False otherwise.
    """
    if n % 5 == 0:
        return True
    return False

list1 = [5, 10, 15, 26, 34, 45, 56, 67, 35, 100, 1234243534982374,7298422985]
result = set(filter(divisibleby5, list1))
print(result)

# we can also use list, tuple, string formats for the output