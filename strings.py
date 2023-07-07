hello = "ahoj svet"
print(hello)
print()
print(hello[5:])

spam = "the quick brown fox jumps over the lazy dog"
print(spam.count(" "))
print(spam.find("fox"))
print("fox" in spam)
print(spam.replace("the", "a"))
print(spam.replace("the", "a", 1))

cislo = input("zadaj cislo")
print(type(cislo))
if cislo.isdecimal():
    cislo = int(cislo)
print(cislo)
print(type(cislo))

spam = "    eggs  "
print(spam.strip())

spam = "***eggs**"
print(spam.strip("*"))

spam = "EGGS"
print(spam.lower())

spam = "eggs"
print(spam.upper())

spam = "the quick brown fox jumps over the lazy dog"
words = spam.split(" ")
print(words)
print(type(words))

words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
text = ("*".join(words))
print(text)
print(type(text))


