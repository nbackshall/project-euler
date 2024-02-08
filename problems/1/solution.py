"""Problem 1: Multiples of 3 and 5"""


def sum_of_multiples_below(x: int, multiples: list):
    """Function to sum multiples under x."""
    assert x > 0, "Input must be > 0"
    l = set()
    for m in multiples:
        n = x // m
        if x % m == 0:
            n -= 1
        for i in range(n):
            l.add((i + 1) * m)
    return sum(l)

print(f"Sum of multiples below 10 is {sum_of_multiples_below(10, [3, 5])}.")
print(f"Sum of multiples below 1000 is {sum_of_multiples_below(1000, [3, 5])}.")
