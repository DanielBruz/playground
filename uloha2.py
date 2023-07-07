## Úloha 2
#
# Nakresli olympíjske kruhy. Opýtaj sa používateľa na polomer kruhov a na
# súradnice prvého kruhu. pomocou výpočtov potom zisti súradnice všetkých
# ostatných kruhov. Všimni si, že kruhy sa na X-ovej osi nedotýkajú. Je tam
# istý offset. Offset nastav ako 2% z veľkosti polomeru.

import tkinter
canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

r = int(input("Zadej polomer kruznic: "))
x = int(input("Zadej souradnici X stredu prvmi kruznice: "))
y = int(input("Zadej souradnici Y stredu prvmi kruznice: "))

x1 = x - r
y1 = y - r
x2 = x + r
y2 = y + r

# offset 20%
offset = r * 0.2

canvas.create_oval(x1, y1, x2, y2, width=2, outline="blue")
canvas.create_oval(x1 + (2*r) + offset, y1, x2 + (2*r) + offset, y2, width=2, outline="blue")
canvas.create_oval(x1 + (4*r) + (2*offset), y1, x2 + (4*r) + (2*offset), y2, width=2, outline="blue")
canvas.create_oval(x1 + r + offset/2, y1 + r, x2 + r + offset/2, y2 + r, width=2, outline="blue")
canvas.create_oval(x1 + (3*r) + (1.5*offset), y1 + r, x2 + (3*r) + (1.5*offset), y2 + r, width=2, outline="blue")

canvas.mainloop()

