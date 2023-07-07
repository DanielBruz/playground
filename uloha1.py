## Úloha 1
#
# Nakresli 9 pretínajúcich sa kruhov tak ako je to na obrázku spýtaj sa
# používateľa na veľkosť kruhu.  Definuj si najprv súradnice stredného kruhu
# a ostatné odvoď od týchto súradníc
#
# použi nasledujúcu konštrukciu

# import tkinter

# canvas = tkinter.Canvas(width=640, height=480)
# canvas.pack()

# r = int(input("Zadej polomer kruznic: "))
# x1 = 320 + r
# y1 = 240 + r
# x2 = 320 - r
# y2 = 240 - r

# canvas.create_oval(x1, y1, x2, y2, width=2, outline="blue")
# canvas.create_oval(x1, y1 + r, x2, y2 + r, width=2, outline="blue")
# canvas.create_oval(x1, y1 - r, x2, y2 - r, width=2, outline="blue")

# canvas.create_oval(x1 - r, y1, x2 - r, y2, width=2, outline="blue")
# canvas.create_oval(x1 - r, y1 + r, x2 - r, y2 + r, width=2, outline="blue")
# canvas.create_oval(x1 - r, y1 - r, x2 - r, y2 - r, width=2, outline="blue")

# canvas.create_oval(x1 + r, y1, x2 + r, y2, width=2, outline="blue")
# canvas.create_oval(x1 + r, y1 + r, x2 + r, y2 + r, width=2, outline="blue")
# canvas.create_oval(x1 + r, y1 - r, x2 + r, y2 - r, width=2, outline="blue")

# canvas.mainloop()

import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

r = int(input("Zadej polomer kruznic: "))
x1 = 320 - r
y1 = 240 - r
x2 = 320 + r
y2 = 240 + r

canvas.create_oval(x1, y1, x2, y2, width=2, outline="blue")
canvas.create_oval(x1, y1 + r, x2, y2 + r, width=2, outline="blue")
canvas.create_oval(x1, y1 - r, x2, y2 - r, width=2, outline="blue")

canvas.create_oval(x1 - r, y1, x2 - r, y2, width=2, outline="blue")
canvas.create_oval(x1 - r, y1 + r, x2 - r, y2 + r, width=2, outline="blue")
canvas.create_oval(x1 - r, y1 - r, x2 - r, y2 - r, width=2, outline="blue")

canvas.create_oval(x1 + r, y1, x2 + r, y2, width=2, outline="blue")
canvas.create_oval(x1 + r, y1 + r, x2 + r, y2 + r, width=2, outline="blue")
canvas.create_oval(x1 + r, y1 - r, x2 + r, y2 - r, width=2, outline="blue")

canvas.mainloop()
