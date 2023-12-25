def pow(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * pow(x, n - 1)
    return 1 / (x * pow(x, -n - 1))

print(f"Result: {pow(2, 3)}")
