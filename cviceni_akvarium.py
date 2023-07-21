import tkinter as tk
import random
import time

class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_background()
        self.player = Player(self.canvas)
        self.food = self.add_food()
        self.bind_all_event()

        self.time = 20
        self.game_started = time.time()
        self.time_label = self.canvas.create_text(self.bg.width()-50, 30,
                               text="00:00", font="arial 30", fill="orangered")

    def display_game_time(self):
        t = self.time - int(time.time() - self.game_started)
        minutes = t // 60
        seconds = t % 60
        time_string = "{:02d}:{:02d}".format(minutes, seconds)
        self.canvas.itemconfig(self.time_label, text=time_string)
        return t

    def create_background(self):
        self.bg = tk.PhotoImage(file="background.png")
        self.canvas = tk.Canvas(width=self.bg.width(), height=self.bg.height())
        self.canvas.pack()
        self.canvas.create_image(self.bg.width()/2, self.bg.height()/2,
                                  image=self.bg)
    def bind_all_event(self):
        self.canvas.bind_all("<KeyPress-Right>", self.player.keypress_right)
        self.canvas.bind_all("<KeyRelease-Right>", self.player.keyrelease_right)
        self.canvas.bind_all("<KeyPress-Left>", self.player.keypress_left)
        self.canvas.bind_all("<KeyRelease-Left>", self.player.keyrelease_left)
        self.canvas.bind_all("<KeyPress-Up>", self.player.keypress_up)
        self.canvas.bind_all("<KeyRelease-Up>", self.player.keyrelease_up)
        self.canvas.bind_all("<KeyPress-Down>", self.player.keypress_down)
        self.canvas.bind_all("<KeyRelease-Down>", self.player.keyrelease_down)

    def add_food(self):
        food_list = [Flake, Flake, Flake, Flake, Flake, Flake, Flake, Flake,
                      Worm1, Worm1, Worm2, Pellet]
        food_type = random.choice(food_list)
        food = food_type(self.canvas)
        return food

    def timer(self):
        self.player.tik()
        self.food.tik()
        if self.food.destroyed:
            self.food = self.add_food()

        if self.player.eat(self.food):
            self.time += self.food.value
            self.food = self.add_food()

        t = self.display_game_time()
        if t <= 0:
            self.game_over()
        else:
            self.canvas.after(40, self.timer)

    def game_over(self):
        self.player.destroy()
        self.food.destroy()

        self.canvas.create_text(self.bg.width()/2, 100, text="GAME OVER",
                                font="arial 60", fill="orangered")

        f = w1 = w2 = p = 0
        for food in self.player.eaten_food:
            if isinstance(food, Flake):
                f += 1
            elif isinstance(food, Worm1):
                w1 += 1
            elif isinstance(food, Worm2):
                w2 += 1
            elif isinstance(food, Pellet):
                p += 1

        self.f = self.display_food_stats("food/flake_icon.png", f, 300)
        self.w1 = self.display_food_stats("food/worm1_icon.png", w1, 350)
        self.w2 = self.display_food_stats("food/worm2_icon.png", w2, 400)
        self.p = self.display_food_stats("food/pellet_icon.png", p, 450)

    def display_food_stats(self, file_path, count, position):
        img = tk.PhotoImage(file=file_path)
        self.canvas.create_image(self.bg.width()/2, position, image=img)
        self.canvas.create_text(self.bg.width()/2+50, position, text=str(count),
                                font="arial 20", fill="orangered")
        return img

class BaseSprite:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x, self.y = x, y
        self.id = self.canvas.create_image(x, y)
        self.destroyed = False

    def load_sprites(self, file_path, rows, cols):
        sprite_img = tk.PhotoImage(file=file_path)
        sprites = []
        height = sprite_img.height()//rows
        width = sprite_img.width()//cols
        for row in range(rows):
            for col in range(cols):
                l = col*width
                t = row*height
                r = (col+1)*width
                b = (row+1)*height
                subimage = self.create_subimage(sprite_img, l, t, r, b)
                sprites.append(subimage)
        return sprites

    def create_subimage(self, img, left, top, right, bottom):
        subimage = tk.PhotoImage()
        subimage.tk.call(subimage, "copy", img, "-from", left, top, right,
                          bottom, "-to", 0,0)
        return subimage

    def tik(self):
        pass

    def destroy(self):
        self.destroyed = True
        self.canvas.delete(self.id)

class Food(BaseSprite):
    value = 0
    speed = 0

    def __init__(self, canvas):
        x = random.randrange(100, 1100)
        y = 0
        super().__init__(canvas, x, y)

    def move(self):
        y = self.y + self.speed
        if y <= self.canvas.winfo_height()-20:
            self.y = y
        else:
            self.destroy()
        self.canvas.coords(self.id, self.x, self.y)

    def tik(self):
        self.move()

class Worm1(Food):
    value = 5
    speed = 5
    def __init__(self, canvas):
        super().__init__(canvas)
        self.sprites = self.load_sprites("food/worm1.png", 1, 1)
        self.canvas.itemconfig(self.id, image=self.sprites[0])

class Worm2(Food):
    value = 10
    speed = 6
    def __init__(self, canvas):
        super().__init__(canvas)
        self.sprites = self.load_sprites("food/worm2.png", 1, 1)
        self.canvas.itemconfig(self.id, image=self.sprites[0])

class Pellet(Food):
    value = 15
    speed = 7
    def __init__(self, canvas):
        super().__init__(canvas)
        self.sprites = self.load_sprites("food/pellet.png", 1, 1)
        self.canvas.itemconfig(self.id, image=self.sprites[0])

class Flake(Food):
    value = 2
    speed = 3
    flakes = ["food/flake1.png", "food/flake2.png", "food/flake3.png",
               "food/flake4.png", "food/flake5.png" ]
    def __init__(self, canvas):
        super().__init__(canvas)
        file_path = random.choice(self.flakes)
        self.sprites = self.load_sprites(file_path, 1, 1)
        self.canvas.itemconfig(self.id, image=self.sprites[0])

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
        self.dx = self.dy = 0
        self.keys_pressed = 0
        self.eaten_food = []

    def eat(self, food):
        dst = ((self.x - food.x)**2 + (self.y - food.y)**2)**0.5
        if dst < 50:
            self.eaten_food.append(food)
            food.destroy()
            return True
        return False

    def load_all_sprites(self):
        sprite_sheet = {
            self.IDLE : {
                self.LEFT : [],
                self.RIGHT : []
            },
            self.SWIM : {
                self.LEFT : [],
                self.RIGHT : []
            }
        }

        sprite_sheet[self.IDLE][self.LEFT] = self.load_sprites(
                                            "player/left_idle.png", 5, 4)
        sprite_sheet[self.IDLE][self.RIGHT] = self.load_sprites(
                                            "player/right_idle.png", 5, 4)
        sprite_sheet[self.SWIM][self.LEFT] = self.load_sprites(
                                            "player/left_swim.png", 3, 4)
        sprite_sheet[self.SWIM][self.RIGHT] = self.load_sprites(
                                            "player/right_swim.png", 3, 4)
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
        if self.movement == self.SWIM:
            self.move()

    def move(self):
        x = self.x + self.dx
        y = self.y + self.dy
        if x >= 55 and x <= self.canvas.winfo_width()-55:
            self.x = x
        if y >= 35 and y <= self.canvas.winfo_height()-35:
            self.y = y
        self.canvas.coords(self.id, x, y)

    

    def keypress_right(self, event):
        self.movement = self.SWIM
        self.direction = self.RIGHT
        self.keys_pressed += 1
        self.dx = 5

    def keyrelease_right(self, event):
        self.dx = 0
        self.keys_pressed -= 1
        if self.keys_pressed == 0:
            self.movement = self.IDLE

    def keypress_left(self, event):
        self.movement = self.SWIM
        self.direction = self.LEFT
        self.keys_pressed += 1
        self.dx = -5

    def keyrelease_left(self, event):
        self.dx = 0
        self.keys_pressed -= 1
        if self.keys_pressed == 0:
            self.movement = self.IDLE

    def keypress_up(self, event):
        self.movement = self.SWIM
        self.keys_pressed += 1
        self.dy = -5

    def keyrelease_up(self, event):
        self.dy = 0
        self.keys_pressed -= 1
        if self.keys_pressed == 0:
            self.movement = self.IDLE

    def keypress_down(self, event):
        self.movement = self.SWIM
        self.keys_pressed += 1
        self.dy = 5

    def keyrelease_down(self, event):
        self.dy = 0
        self.keys_pressed -= 1
        if self.keys_pressed == 0:
            self.movement = self.IDLE

game = Game()
game.timer()

game.mainloop()

