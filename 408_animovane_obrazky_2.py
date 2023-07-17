# nacteni jednoho velkeho souboru misto spousty malych je rychlejsi

import tkinter as tk

main = tk.Tk()
bg = tk.PhotoImage(file="img/animace/background.png")  # nacteni obrazku pozadi

canvas = tk.Canvas(width=bg.width(), height=bg.height())  # sirka a vyska obrazku pozadi
canvas.pack()

canvas.create_image(bg.width() / 2, bg.height() / 2, image=bg)  # umistime obrazek pozadi
braid_id = canvas.create_image(bg.width() / 2, bg.height() / 2)  # vytvorim si placeholder ve stredu plochy


def load_sprites(file_path, rows, cols):
    sprite_img = tk.PhotoImage(file=file_path)
    sprites = []
    # zistím výšku a šírku jednotlivých častí
    height = sprite_img.height() // rows
    width = sprite_img.width() // cols
    for row in range(rows):
        for col in range(cols):
            l = col * width
            t = row * height
            r = (col + 1) * width
            b = (row + 1) * height
            subimage = create_sub_image(sprite_img, l, t, r, b)
            sprites.append(subimage)
    return sprites


def create_sub_image(img, left, top, right, bottom):
    subimage = tk.PhotoImage()
    subimage.tk.call(subimage, 'copy', img, '-from',
                     left, top, right, bottom, '-to', 0, 0)
    return subimage


def animate():  # pomoci funkce casovace zprovoznime animaci
    global sprite_idx
    sprite_idx = (sprite_idx + 1) % 27  # zabezpeci mi, ze se index pohybuje od 0 do 26
    canvas.itemconfig(braid_id, image=braid[sprite_idx])
    canvas.after(50, animate)


sprite_idx = 0

braid = load_sprites("img/animace/braid_sprite.png", 1, 27)
animate()

canvas.mainloop()
