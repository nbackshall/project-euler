"""Problem 2: Even Fibonacci Numbers"""


def sum_of_even_fibonacci_under(max: int = 4e6):
    """Function to sum even fibonacci numbers under max."""
    assert max > 0, "Max must be > 0"
    total = 2
    f = [1, 2]
    i = 1
    while True:
        f.append(sum(f[-2:]))
        f.pop(0)
        if f[-1] > max:
            break
        if i % 3 == 0:
            total += f[-1]
        i += 1
    return total

max = 4e6
print(f"Sum of even fibonacci numbers below {max} is {sum_of_even_fibonacci_under(max)}.")
