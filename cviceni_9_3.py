def urob(a, b):
    if a == 0:
        return 0
    return b + urob(a - 1, b)

print(urob(7, 17))
