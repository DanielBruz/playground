# a = [1,2,3]
# b = a
# b[2] = "X"
# print(a)
# print(b)

list = ["A","H","O","J"]

list.append("X")           # (hodnota) pridá novú hodnotu na koniec pôvodného poľa
print(list)

list.insert(1,"Y")           # (index, hodnota) vloží hodnotu do pôvodného poľa pred zadaný index
print(list)

list2 = list.pop()              # odstráni posledný prvok pôvodného poľa a vráti tento prvok ako hodnotu
print(list2)
print()
print(list)

list3 = list.pop(0)             # odstráni prvý prvok pôvodného poľa a vráti tento prvok ako hodnotu
print(list3)
print()
print(list)

list4 = list.pop(2)         # odstráni prvok na zadanom indexe a vráti tento prvok ako hodnotu
print(list4)
print()
print(list)

list.remove("J")    # vyhodí z pôvodného poľa prvý výskyt hodnoty
print(list)

list5 = [5,4,3,2,1]
list5.sort()             # vzostupne utriedi pôvodné pole (priamo v pamäti), prvky poľa sa musia dať porovnávať
print(list5)

