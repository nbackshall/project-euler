"""Problem 3: Largest Prime Factor"""


def largest_prime_factor(n: int = 13195):
    """The largest prime factor of n."""
    assert n > 0, "n must be > 0"
    prime_factors = set({2, 3})
    x = n / 2
    if x % 1 == 0:
        x = int(x)
        print(x)
        if is_prime(x):
            return x
    divisor = 3
    while True:
        x = n / divisor
        if x % 1 == 0:
            x = int(x)
            print(x)
            if is_prime(x):
                return x
        divisor += 2
    return None

def is_prime(x: int):
    """Check if x is prime."""
    if x <= 1:
        return False
    if x % 2 == 0:
        if x != 2:
            return False
    if x in [3, 4, 5]:
        return True
    for i in range(3, (x // 2) + 1):
        if x % i == 0:
            return False
    return True

n = 600851475143
print(f"The largest prime factor of {n} is {largest_prime_factor(n)}.")
