# Úloha 1
# vezmi riešenie z predchádzajúceho riešenia s formátovaním stringov a
# vykreslovaním kocky. Tentokrát použi modul random na získanie náhodného
# čísla. Vytvor podmienky typu "elif" a vykresli správnu stranu kocky. Na
# vykreslenie použi iba funkciu "format" a "print"

import random
cislo = random.randint(1, 6)
print("Na kostce padlo cislo: ", cislo)
print()

dice1 = "{: ^7}".format('0')
dice2 = "{: <7}".format('0')
dice3 = "{: >7}".format('0')
dice4 = "{: ^7}".format('0     0')
dice5 = "{: ^7}".format(' ')

if (cislo == 1):
    print("+" + 7*"-" + "+\n" + "|" + dice5 + "|\n" + "|" + dice1 + "|\n" + "|" + dice5 + "|\n" + "+" + 7*"-" + "+\n")
elif (cislo == 2):
    print("+" + 7*"-" + "+\n" + "|" + dice2 + "|\n" + "|" + dice5 + "|\n" + "|" + dice3 + "|\n" + "+" + 7*"-" + "+\n")
elif (cislo == 3):
    print("+" + 7*"-" + "+\n" + "|" + dice2 + "|\n" + "|" + dice1 + "|\n" + "|" + dice3 + "|\n" + "+" + 7*"-" + "+\n")
elif (cislo == 4):
    print("+" + 7*"-" + "+\n" + "|" + dice4 + "|\n" + "|" + dice5 + "|\n" + "|" + dice4 + "|\n" + "+" + 7*"-" + "+\n")
elif (cislo == 5):
    print("+" + 7*"-" + "+\n" + "|" + dice4 + "|\n" + "|" + dice1 + "|\n" + "|" + dice4 + "|\n" + "+" + 7*"-" + "+\n")
else:
    print("+" + 7*"-" + "+\n" + "|" + dice4 + "|\n" + "|" + dice4 + "|\n" + "|" + dice4 + "|\n" + "+" + 7*"-" + "+\n")