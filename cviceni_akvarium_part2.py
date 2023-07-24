import tkinter as tk


########################################### Trida Game #########################################
class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_background()
        self.player = Player(self.canvas)

    def timer(self):
        self.player.tik()
        self.canvas.after(40, self.timer)

    def create_background(self):
        self.bg = tk.PhotoImage(file="img/akvarium/background.png")
        self.canvas = tk.Canvas(width=self.bg.width(), height=self.bg.height())
        self.canvas.pack()
        self.canvas.create_image(self.bg.width() / 2, self.bg.height() / 2, image=self.bg)


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


########################################### Trida Player #########################################

class Player(BaseSprite):
    LEFT = "left"
    RIGHT = "right"
    IDLE = "idle"
    SWIM = "swim"

    def __init__(self, canvas, x=100, y=100):
        super().__init__(canvas, x, y)
        self.sprite_sheet = self.load_all_sprites()
        self.movement = self.IDLE
        self.direction = self.LEFT
        self.sprite_idx = 0

    def load_all_sprites(self):
        sprite_sheet = {
            self.IDLE: {
                self.LEFT: [],
                self.RIGHT: []
            },
            self.SWIM: {
                self.LEFT: [],
                self.RIGHT: []
            }
        }
        sprite_sheet[self.IDLE][self.LEFT] = self.load_sprite("img/akvarium/player/left_idle.png", 5, 4)
        sprite_sheet[self.IDLE][self.RIGHT] = self.load_sprite("img/akvarium/player/right_idle.png", 5, 4)
        sprite_sheet[self.SWIM][self.LEFT] = self.load_sprite("img/akvarium/player/left_swim.png", 3, 4)
        sprite_sheet[self.SWIM][self.RIGHT] = self.load_sprite("img/akvarium/player/right_swim.png", 3, 4)
        return sprite_sheet

    def next_animation_index(self, idx):
        idx += 1
        max_idx = len(self.sprite_sheet[self.movement][self.direction])
        idx = idx % max_idx
        return idx

    def tik(self):
        self.sprite_idx = self.next_animation_index(self.sprite_idx)
        img = self.sprite_sheet[self.movement][self.direction][self.sprite_idx]
        self.canvas.itemconfig(self.id, image=img)


game = Game()
game.timer()

game.mainloop()
