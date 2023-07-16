def faktorial(n):
    if n < 2:
        return 1
    elif n == 2:
        return 2
    else:
        return n * faktorial(n - 1)


n = 10
print("Faktorial cisla '{}' je: {:,}".format(n, faktorial(n)))
