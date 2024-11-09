"""Problem 5: Sum Square Difference"""

n = 100

nums = [i for i in range(1, n+1)]
sq_nums = [i ** 2 for i in range(1, n+1)]

ans = sum(nums) ** 2 - sum(sq_nums)

print(f"The difference between the sum of the squares of the first {n} natural numbers and the square of the sum is {ans}.")

