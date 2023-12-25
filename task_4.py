def climb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return climb(n - 1) + climb(n - 2)


print(f"Input: n = 2\nOutput: {climb(2)}")
print(f"Input: n = 3\nOutput: {climb(3)}")
