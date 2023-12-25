def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonachi(n - 1) + fibonachi(n - 2)


print(f"Input: n = 2\nOutput: {fibonachi(2)}")
print(f"Input: n = 3\nOutput: {fibonachi(3)}")
print(f"Input: n = 4\nOutput: {fibonachi(4)}")
