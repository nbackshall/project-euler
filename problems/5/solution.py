"""Problem 4: Smallest Multiple"""

n = 20
ans = 1
for i in (range(1, n+1)):
    if ans % i > 0:
        for j in range(1, n+1):
            if (ans*j) % i == 0:
                ans *= j
                break

print(f"The smallest multiple evenly divisible by 1-{n} is {ans}.")
