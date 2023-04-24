"""
File: largest_digit.py
Name: Anita
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
    print(find_largest_digit(12345))      # 5
    print(find_largest_digit(281))        # 8
    print(find_largest_digit(6))          # 6
    print(find_largest_digit(-111))       # 1
    print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
    """
    :param n: the number that will be checked
    :return: the largest digit in the number
    """
    if n < 0:
        n += -2 * n
    largest_digit = find_largest_digit_helper(-1, 1, n)
    return largest_digit


def find_largest_digit_helper(largest, digit, n):
    """
    :param largest: the largest digit recorded
    :param digit: the specific digit that will be checked
    :param n: the number that will be checked
    :return: the largest digit in the number
    """
    if digit > n:
        return largest
    else:
        digit_num = (n - n // (digit * 10) * digit * 10) // digit
        if digit_num > largest:
            largest = digit_num
        largest = find_largest_digit_helper(largest, digit * 10, n)
        return largest


if __name__ == '__main__':
    main()
