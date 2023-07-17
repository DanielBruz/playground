import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


# V tomto pripade se volaji funkce na stridacku

def tik():
    print("tik")
    canvas.after(500, tok)  # timer - casovac, After naplanuje volani funkce, ale aplikace bezi mezitim dal.


def tok():
    print("tok")
    canvas.after(500, tik)


tik()
print("Ahoj")   # ukazka, ze po prvnim volani tik() bezi program k funkci print() a pak uz se funkce stridaji

canvas.mainloop()
