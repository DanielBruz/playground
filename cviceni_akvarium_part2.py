import tkinter as tk


########################################### Trida Game #########################################
class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_background()
        self.player = Player(self.canvas)
        # bindovani udalostí - tedy stisku a pusteni klaves. U klaves jde o bind_all.
        self.canvas.bind_all("<KeyPress-Right>", self.player.keypress_right)
        self.canvas.bind_all("<KeyRelease-Right>", self.player.keyrelease_right)
        self.canvas.bind_all("<KeyPress-Left>", self.player.keypress_left)
        self.canvas.bind_all("<KeyRelease-Left>", self.player.keyrelease_left)
        self.canvas.bind_all("<KeyPress-Up>", self.player.keypress_up)
        self.canvas.bind_all("<KeyRelease-Up>", self.player.keyrelease_up)
        self.canvas.bind_all("<KeyPress-Down>", self.player.keypress_down)
        self.canvas.bind_all("<KeyRelease-Down>", self.player.keyrelease_down)
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
        self.dx = self.dy = 0  # vynulovani vektoru pohybu

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
        #  v tikani se mi nemeni x a y, tedy rybicka by se pri stisku klavesy nepohybovala, udelam tedy funkci MOVE.
        #  A po jejim vytvoreni se vracim do Tiku a nastavim "kdyz je stav pohybu MOVE, pak volam funkci pohybu" :
        if self.movement == self.SWIM:
            self.move()

    def move(self):
        x = self.x + self.dx  # aktualni souradnice + vektor pohybu = nasledujici poloha rybicky
        y = self.y + self.dy
        # Kontrola, zdali se pohybuje v nasem okne, vlevo i vpravo 55 pixelu od kraje.
        # self.x a self.y jsou souradnice stredu rybicky, tedy musim nechat nejaky prostor, tedy 55 a 35 pro y.
        if x >= 55 and x <= self.canvas.winfo_width() - 55:
            self.x = x
        if y >= 35 and y <= self.canvas.winfo_height() - 35:
            self.y = y
        # a teď musim zmenit souradnioce meho objektu
        self.canvas.coords(self.id, x, y)

    # nadefinujeme si pohyb hrace pomoci stisku a pusteni klaves.
    # A pak v hlavnim GAME/INIT musim nastavit bindovani udalostí.
    def keypress_right(self, event):  # argument event je povinny
        self.movement = self.SWIM
        self.direction = self.RIGHT
        #  nastavim si vektor pohybu po ose x a jeho velikost a pak do INIT doplnim vektory dx a dy = 0.
        self.dx = 5

    # a udelam i protiudalost, tedy pusteni klavesy:
    def keyrelease_right(self, event):
        self.dx = 0
        self.movement = self.IDLE

    def keypress_left(self, event):
        self.movement = self.SWIM
        self.direction = self.LEFT
        self.dx = -5

    def keyrelease_left(self, event):
        self.dx = 0
        self.movement = self.IDLE

    def keypress_up(self, event):
        self.movement = self.SWIM
        self.dy = -5

    def keyrelease_up(self, event):
        self.dy = 0
        self.movement = self.IDLE

    def keypress_down(self, event):
        self.movement = self.SWIM
        self.dy = 5

    def keyrelease_down(self, event):
        self.dy = 0
        self.movement = self.IDLE

########################################## Hlavni kod ######################################################
game = Game()
game.timer()

game.mainloop()
