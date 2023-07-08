mocniny = [x**2 for x in range(10)]
print(mocniny)

delitelne_3_a_5 = [x for x in range(50) if x % 3 == 0 if x % 5 == 0]
print(delitelne_3_a_5)

delitelne_3_a_5 = []
for x in range(50):
    if x % 3 == 0 and x % 5 == 0:
        delitelne_3_a_5.append(x)
print(delitelne_3_a_5)

cisla = [y for x in range(5) for y in range(x+1)]
print(cisla)
