# sprite = skupina obrazku zobrazujicich objekt v ruznych polohach.
# Nacitame obrazky, ulozime si je a budeme je rychle menit.

import tkinter

main = tkinter.Tk()
bg = tkinter.PhotoImage(file="img/animace/background.png")  # nacteni obrazku pozadi

canvas = tkinter.Canvas(width=bg.width(), height=bg.height())  # sirka a vyska obrazku pozadi
canvas.pack()

canvas.create_image(bg.width() / 2, bg.height() / 2, image=bg)  # umistime obrazek pozadi

braid = []
for i in range(27):  # do pole si nactu vsechny obrazky
    img = tkinter.PhotoImage(file="img/animace/braid/braid_{:02d}.png".format(i))
    braid.append(img)

braid_id = canvas.create_image(bg.width() / 2, bg.height() / 2)  # vytvorim si placeholder ve stredu plochy


# canvas.itemconfig(braid_id, image=braid[0])  # placeholderu zmenim obsah, pro ukazku zobrazi prvni obrazek

def animate():  # pomoci funkce casovace zprovoznime animaci
    global sprite_idx
    sprite_idx = (sprite_idx + 1) % 27  # zabezpeci mi, ze se index pohybuje od 0 do 26
    canvas.itemconfig(braid_id, image=braid[sprite_idx])
    canvas.after(50, animate)


sprite_idx = 0

animate()  # spustime animaci

canvas.mainloop()
