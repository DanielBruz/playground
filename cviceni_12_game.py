import tkinter as tk
import random
import os


########################################### Trida Game #########################################
class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_background()
        self.duck = Duck(self.canvas)
        self.shooter = Shooter(self.canvas, x=0, y=0)
        self.canvas.bind("<Motion>", self.shooter.motion)
        self.canvas.bind("<ButtonPress-1>", self.shooter.press)
        self.canvas.bind("<ButtonRelease-1>", self.shooter.release)

    def create_background(self):  # 1280 * 724
        self.bg = tk.PhotoImage(file="img/birds/background2.png")
        self.canvas = tk.Canvas(width=self.bg.width(), height=self.bg.height())
        self.canvas.pack()
        self.canvas.create_image(self.bg.width() / 2, self.bg.height() / 2, image=self.bg)

    def timer(self):
        self.duck.tik()
        self.canvas.after(40, self.timer)


########################################### Trida BaseSprite #########################################
class BaseSprite:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x, self.y = x, y
        self.id = self.canvas.create_image(x, y)
        self.destroyed = False

    def load_sprite(self, file_path, rows, cols):
        sprite_img = tk.PhotoImage(file=file_path)
        sprites = []
        width = sprite_img.width() // cols
        height = sprite_img.height() // rows
        for row in range(rows):
            for col in range(cols):
                l = col * width
                t = row * height
                r = (col + 1) * width
                b = (row + 1) * height
                subimage = self.create_subimage(sprite_img, l, t, r, b)
                sprites.append(subimage)
        return sprites

    def create_subimage(self, img, left, top, right, bottom):
        subimage = tk.PhotoImage()
        subimage.tk.call(subimage, "copy", img, "-from", left, top, right, bottom, "-to", 0, 0)
        return subimage

    def tik(self):
        pass

    def destroy(self):
        self.destroyed = True
        self.canvas.delete(self.id)


########################################### Trida Duck #########################################

class Duck(BaseSprite):

    def __init__(self, canvas, x=1700, y=200):
        super().__init__(canvas, x, y)
        self.sprite_idx = 0
        self.sprite_sheet = self.load_all_sprites()
        self.dx = self.dy = 0
        self.x = 1280
        self.y = random.randrange(100, 500)

    def load_all_sprites(self):
        sprite_sheet = self.load_sprite("img/birds/spritesheet/__yellow_flying_bird_3_flying.png", 2, 4)
        return sprite_sheet

    def next_animation_index(self, idx):
        idx += 1
        max_idx = len(self.sprite_sheet)
        idx = idx % max_idx
        return idx

    def tik(self):
        self.sprite_idx = self.next_animation_index(self.sprite_idx)
        img = self.sprite_sheet[self.sprite_idx]
        self.canvas.itemconfig(self.id, image=img)
        self.move()

    def move(self):
        x = self.x - self.dx
        y = self.y
        if x >= -220:
            self.dx += 20
        else:
            self.destroy()
        self.canvas.coords(self.id, x, y)


########################################## Trida Shooter ######################################################
class Shooter(BaseSprite):
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y)
        self.canvas = canvas
        self.x, self.y = x, y
        self.target = tk.PhotoImage(file="img/birds/target.png")
        self.id_target = self.canvas.create_image(self.x, self.y, image=self.target)

    def motion(self, event):
        print("hybem sa na {},{}".format(event.x, event.y))
        self.canvas.coords(self.id_target, event.x, event.y)

    def press(self, event):
        print("stlačil som na {},{}".format(event.x, event.y))
        os.system("start img/birds/shot.mp3")

    def release(self, event):
        print("pustil som na {},{}".format(event.x, event.y))


########################################## Hlavni kod ######################################################

game = Game()
game.timer()
game.mainloop()
