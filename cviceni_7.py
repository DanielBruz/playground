def list_all_divisors(num):
	delitele = []
	delitele = [i+1 for i in range(num) if num % (i+1) == 0]
	return delitele
	
def is_perfect(num):
	pole = list_all_divisors(num)
	soucet = sum(pole[:-1])
	if soucet == num:
		perfect = "true"
	else:
		perfect = "false"
	return perfect

cislo = int(input("vlozte cislo: "))
print(list_all_divisors(cislo))
print(is_perfect(cislo))

# def is_perfect(number):
#    global delitele
#    delitele = list_all_divisors(number)
#    if (sum(delitele)-number) == number:
#        return True 
#    else:
#        return False

#print(is_perfect(int(cislo)))

def transform(A):
	for key, value in A.items():
		B = [A.items()]
	return B

A = {1 : "one", 2 : "two"}
list = transform(A)
print(list)



dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {}

for key, value in dict1.items():
    merged_dict.setdefault(key, {}).update({'dict1': value})

for key, value in dict2.items():
    merged_dict.setdefault(key, {}).update({'dict2': value})

print(merged_dict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)


print("Dalsi reseni\n")
print()
print("úloha_01\n")

cislo = input("napíš číslo: ")

def list_all_divisors(number):
    delitele = [(x+1)for x in range(number) if number % (x+1)==0]
    return delitele

print("delitele tvojho čísla: ")
print(list_all_divisors(int(cislo)))

print()

print("úloha_02\n")

def is_perfect(number):
    delitele = list_all_divisors(number)
    if (sum(delitele)-number) == number:
        return True
    else:
        return False

print(is_perfect(int(cislo)))



print()

print("úloha_03\n")

import tkinter

canvas = tkinter.Canvas(width = 640, height = 480, bg = "cyan")
canvas.pack()

def ball(x, y, r):
    canvas.create_oval(x-r, y-r, x+r, y+r, width = 0, fill = "white")

def snowman(x, y, r):
    ball(x, y, r)
    ball(x, y-5/3*r, 2/3*r)
    ball(x, y-17/6*r, 1/2*r)



snowman (640/2, 400, 90)

canvas.mainloop()

print()

print("uloha_04\n")

def transform(dictionary):
    return list(dictionary.items())

A = {1: "one", 2: "two"}
print(transform(A))


print()

print("úloha_05\n")

def merge(a, b):
    kopia = a.copy()
    kopia.update(b)
    for i in a.keys():
        if a[i] != kopia[i]:
            kopia[i] = [a[i], kopia[i]]
    return kopia

A = {1: "one", 2: "two"}
B = {2: "dva", 3: "three"}
print(merge(A, B))