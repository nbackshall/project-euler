"""Problem 3: Largest Palindromic Product"""


def largest_palindromic_product(n: int = 2):
    """The largest palindromic product of two n-digit numbers."""
    assert n > 0, "n must be > 0"
    max_num = int('9' * n)
    min_num = int('1' * n)
    largest_palindrome = 0
    pair = ()
    for i in range(max_num, min_num-1, -1):
        for j in range(i, min_num-1, -1):
            product = i * j
            if product < largest_palindrome:
                break
            if is_palindromic(product):
                largest_palindrome = product
                pair = (i, j)
    return pair

def is_palindromic(x: int):
    """Check if x is palindromic."""
    l = list(str(x))
    if l == l[::-1]:
        return True
    else:
        return False

n = 3
a, b = largest_palindromic_product(n)
print(f"The largest palindromic product of two {n}-digit numbers is {a}x{b}={a * b}.")
