import tkinter as tk
import random
from playsound import playsound
import time


########################################### Trida Game #########################################
class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_background()
        self.birds = Birds(self.canvas)
        self.shooter = Shooter(self.canvas, x=0, y=0)

        self.canvas.bind("<Motion>", self.shooter.motion)
        self.canvas.bind("<ButtonPress-1>", self.shooter.press)
        self.canvas.bind("<ButtonRelease-1>", self.shooter.release)

        self.time = 30
        self.game_started = time.time()
        self.time_label = self.canvas.create_text(self.bg.width() - 50, 30,
                                                  text="00:00", font="ariel 30", fill="orangered")

    def display_game_time(self):
        t = self.time - int(time.time() - self.game_started)
        minutes = t // 60
        seconds = t % 60
        time_string = "{:02d}:{:02d}".format(minutes, seconds)
        self.canvas.itemconfig(self.time_label, text=time_string)
        return t

    def create_background(self):  # 1280 * 724
        self.bg = tk.PhotoImage(file="img/birds/background2.png")
        self.canvas = tk.Canvas(width=self.bg.width(), height=self.bg.height())
        self.canvas.pack()
        self.canvas.create_image(self.bg.width() / 2, self.bg.height() / 2, image=self.bg)

    def timer(self):
        self.birds.tik()
        t = self.display_game_time()
        if t <= 0:
            self.game_over()
        else:
            self.canvas.after(40, self.timer)

    def game_over(self):
        self.canvas.create_text(self.bg.width() - 200, 200,
                                text="GAME OVER", font="ariel 30", fill="orangered")


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

########################################### Trida Birds #########################################

class Birds(BaseSprite):

    def __init__(self, canvas, x=1700, y=200):
        super().__init__(canvas, x, y)
        self.idx = 0
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
        self.canvas.coords(self.id_target, event.x, event.y)

    def press(self, event):
        playsound("img/birds/shot.mp3")

    def release(self, event):
        pass


########################################## Hlavni kod ######################################################

game = Game()
game.timer()
game.mainloop()
