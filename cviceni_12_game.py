import tkinter as tk
import random
import time

# logika hry: pohybuji myší nad kachnami a levá klávesa myši je střelba.
# Mám omezený čas a počítám počet sestřelených kachen.


########################################### Trida Game #########################################
class Game(tk.Tk):
    def __init__(self):
        super().__init__()
        self.create_background()
        self.player = Player(self.canvas)
        self.food = self.add_food()
        self.bind_all_event()  # volam bindovani, ktere jsem si dal zvlast. Aby byl konstruktor citelny.

        self.time = 30  # herni cas bude 30 sekund
        self.game_started = time.time()  # musim si zapamatovat, kdy hra zacala, abych to mohl odpocitavat od 30s.
        # aby se mi vypisoval cas, musim si vytvorit placeholder v pravem hornim rohu:
        self.time_label = self.canvas.create_text(self.bg.width() - 50, 30,
                                                  text="00:00", font="ariel 30", fill="orangered")

    def display_game_time(self):  # vytvorim si funkci, ktera pocita cas
        t = self.time - int(time.time() - self.game_started)  # cas urceny na hru - (aktualni cas - kdy hra zacala)
        minutes = t // 60  # vypocitam si minuty celociselnym delenim
        seconds = t % 60  # vypocitam si sekundy zbytkem po celociselnem deleni
        time_string = "{:02d}:{:02d}".format(minutes, seconds)  # naformatuji si time_string
        self.canvas.itemconfig(self.time_label, text=time_string)  # menim text na time_string
        # a prechazim do casovace Game/Timer
        return t  # vraci mi, kolik sekund zbyva do konce hry.

    def bind_all_event(self):  # dal jsem si bindovani zvlast pro prehlednost.
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

        if self.player.eat(self.food):  # kdyz rybka opravdu sezrala jidlo.
            self.time += self.food.value  # kdyz rybka neco s ni, pripocita se k celkovemu casu hodnota toho jidla.
            self.food = self.add_food()  # dej mi dalsi jidlo.

        t = self.display_game_time()
        if t <= 0:  # dosel cas hry.
            self.game_over()  # volam ukonceni hry.
        else:  # kdyz cas hry nevyprsel.
            self.canvas.after(40, self.timer)

    def game_over(self):  # musim si definovat funkci pro konec hry.
        # a presouvame se k ukonceni hry a zobrazeni vysledku. Uklidim i herni plochu.
        self.player.destroy()  # znicim hrace, abych ho nevidel.
        self.food.destroy()  # znicim food, abych ho nevidel.
        self.canvas.create_text(self.bg.width() / 2, 100, text="GAME OVER", font="ariel 60", fill="orangered")
        #  a ted uz jen spocitat, kolik jsem toho sezral :-)
        f = w1 = w2 = p = 0  # zatim jsou 0
        for food in self.player.eaten_food:  # prochazim jidlo, ktere je snedene.
            if isinstance(food, Flake):  # jestli je muj objekt food instance tridy Flake.
                f += 1
            if isinstance(food, Worm1):
                w1 += 1
            if isinstance(food, Worm2):
                w2 += 1
            if isinstance(food, Pellet):
                p += 1
        self.f = self.display_food_stats("img/akvarium/food/flake_icon.png", f, 300)
        self.w1 = self.display_food_stats("img/akvarium/food/worm1_icon.png", w1, 350)
        self.w2 = self.display_food_stats("img/akvarium/food/worm2_icon.png", w2, 400)
        self.p = self.display_food_stats("img/akvarium/food/pellet_icon.png", p, 450)

    # a jdeme resit statistiky:
    # dam funkci cestu k moji ikonce jidla, mnozstvi sezraneho jidla, pozici vykresleni.
    def display_food_stats(self, file_path, count, position):
        img = tk.PhotoImage(file=file_path)
        self.canvas.create_image(self.bg.width() / 2, position, image=img)
        self.canvas.create_text(self.bg.width() / 2 + 50, position, text=str(count),
                                font="ariel 20", fill="orangered")
        return img      # vratim obrazek

    def create_background(self):
        self.bg = tk.PhotoImage(file="img/birds/background5.png")
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


########################################### Trida Food #########################################
class Food(BaseSprite):
    value = 0
    speed = 0

    def __init__(self, canvas):
        x = random.randrange(100, 1100)
        y = 0
        super().__init__(canvas, x, y)

    def move(self):
        y = self.y + self.speed
        if y <= self.canvas.winfo_height() - 20:
            self.y = y
        else:
            self.destroy()
        self.canvas.coords(self.id, self.x, self.y)

    def tik(self):
        self.move()


########################################### Tridy druhu jidla #########################################

class Worm1(Food):
    value = 5
    speed = 5

    def __init__(self, canvas):
        super().__init__(canvas)
        self.sprites = self.load_sprite("img/akvarium/food/worm1.png", 1, 1)
        self.canvas.itemconfig(self.id, image=self.sprites[0])


class Worm2(Food):
    value = 10
    speed = 6

    def __init__(self, canvas):
        super().__init__(canvas)
        self.sprites = self.load_sprite("img/akvarium/food/worm2.png", 1, 1)
        self.canvas.itemconfig(self.id, image=self.sprites[0])


class Pellet(Food):
    value = 15
    speed = 7

    def __init__(self, canvas):
        super().__init__(canvas)
        self.sprites = self.load_sprite("img/akvarium/food/pellet.png", 1, 1)
        self.canvas.itemconfig(self.id, image=self.sprites[0])


class Flake(Food):
    value = 3
    speed = 2
    flakes = ["img/akvarium/food/flake1.png", "img/akvarium/food/flake2.png", "img/akvarium/food/flake3.png",
              "img/akvarium/food/flake4.png", "img/akvarium/food/flake5.png"]

    def __init__(self, canvas):
        super().__init__(canvas)
        file_path = random.choice(self.flakes)
        self.sprites = self.load_sprite(file_path, 1, 1)
        self.canvas.itemconfig(self.id, image=self.sprites[0])


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
        self.dx = self.dy = 0
        self.keys_pressed = 0
        self.eaten_food = []  # musim si take nasizovat pole pro funkci eat.

    def eat(self, food):  # musim si definovat metodu pro pojidani jidla hracem. Argument je nejaky food,
        # ktery je k nemu blizko. Protoze trida Player dedi z tridy BaseSprite.
        dst = ((self.x - food.x) ** 2 + (self.y - food.y) ** 2) ** 0.5  # ryba dedi z tridy BaseSprite a food take,
        # tedy muzu adresovat x, y. Tedy ((x1 - x2)**2 + (y1 - y2)**2)**0.5.
        if dst < 50:
            self.eaten_food.append(food)
            # udelam si pole, co jsem snedl. A kdyz neco snim,
            # ulozim si to do pole, abych mohl delat nejake statistiky.
            # Pak v INIT definuji prazdne pole eaten_food. A prechazim do casovace Timer.
            food.destroy()  # kdyz to jidlo snim, musim ho take znicit.
            return True  # kdyz je ryba dostatecne blizko, vracim True
        return False  # Jinak vracim False.

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
        sprite_sheet[self.IDLE][self.LEFT] = self.load_sprite("img/birds/spritesheet/__red_flying_bird_3_flying.png", 2, 4)
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
        if self.movement == self.SWIM:
            self.move()

    def move(self):
        x = self.x + self.dx
        y = self.y + self.dy
        if x >= 55 and x <= self.canvas.winfo_width() - 55:
            self.x = x
        if y >= 35 and y <= self.canvas.winfo_height() - 35:
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


########################################## Hlavni kod ######################################################
game = Game()
game.timer()

game.mainloop()
