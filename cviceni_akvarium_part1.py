import tkinter as tk


########################################### Trida Game #########################################
class Game(tk.Tk):  # dedi z hlavni aplikace (hlavniho okna) Tk
    def __init__(self):  # nepotrebuje zadne argumenty
        super().__init__()  # volam konstruktor Tk
        self.create_background()  # zavolam si metodu pro nacteni pozadi
        self.player = Player(self.canvas)

    def timer(self):
        self.player.tik()  # zavola mi casovaci metodu Tik, kterou jsme si pripravili v tride Player.
        #  a ted doplnim metodu canvas.after, doplnime 40ms a znovu zavolame Timer.
        #  A tak mame zakladni smyčku, ktera se bude vykonavat. A nakonec kodu doplnime game.timer()
        self.canvas.after(40, self.timer)

    def create_background(self):
        self.bg = tk.PhotoImage(file="img/akvarium/background.png")
        self.canvas = tk.Canvas(width=self.bg.width(), height=self.bg.height())
        self.canvas.pack()  # ummisti muj canvas do hlavniho okna
        self.canvas.create_image(self.bg.width() / 2, self.bg.height() / 2, image=self.bg)


########################################### Trida BaseSprite #########################################
class BaseSprite:  # trida reprezentuje muj zakladni obrazek (sprite)
    def __init__(self, canvas, x, y):  # dam mu canvas, kam se obrazek bude vykreslovat # a x, y souradnice
        self.canvas = canvas  # ukladam si to jako atributy objektu
        self.x, self.y = x, y
        self.id = self.canvas.create_image(x, y)  # zatim ma jen polohu a zadny obsah
        self.destroyed = False

    def load_sprite(self, file_path, rows, cols):  # jako argumenty davam cestu a radky a sloupce
        sprite_img = tk.PhotoImage(file=file_path)  # nedavam self, jen do konstruktoru
        sprites = []  # pole pro sprity
        width = sprite_img.width() // cols
        height = sprite_img.height() // rows
        for row in range(rows):
            for col in range(cols):
                l = col * width
                t = row * height
                r = (col + 1) * width
                b = (row + 1) * height
                subimage = self.create_subimage(sprite_img, l, t, r, b)  # zavolam si svoji funkci pro subimage
                sprites.append(subimage)
        return sprites  # vrati mi pole s polohami obrazku a muzeme indexovat atp.

    def create_subimage(self, img, left, top, right, bottom):
        subimage = tk.PhotoImage()  # vytvorim si prazdny obrazek
        # zavolam specialni metodu call a udelam vyrez:
        subimage.tk.call(subimage, "copy", img, "-from", left, top, right, bottom, "-to", 0, 0)
        return subimage

    # v kazde tride si definujeme tikaci funkci. Musime mit casovac. Tato nedela nic.
    # Prepiseme ji v kazde dalsi tride, ktera bude dedit z tridy BaseSprite.
    def tik(self):
        pass

    def destroy(self):  # metoda pro zniceni objektu = smazani
        self.destroyed = True
        self.canvas.delete(self.id)


########################################### Trida Player #########################################

class Player(BaseSprite):  # dedi z BaseSprite
    #  definuji si stringy "idle" atp. pro sprite_sheet jako konstanty - programátorsky lepší
    LEFT = "left"
    RIGHT = "right"
    IDLE = "idle"
    SWIM = "swim"

    def __init__(self, canvas, x=100, y=100):
        super().__init__(canvas, x, y)  # volam konstruktor me zakladni tridy BaseSprite
        self.sprite_sheet = self.load_all_sprites()  # funkce = nacitaji se mi vsechny polohy hrace
        #  definujeme si take stav pohybu a smer a nastavime startovaci hodnoty:
        self.movement = self.IDLE
        self.direction = self.LEFT
        self.sprite_idx = 0  # doplnili jsme po vyporadani se s indexem v next_animation_index. Na zacatku = 0.
        # A pak upravime tikani doplnenim self.sprite_idx = self.next_animation_index(self.sprite_idx)
        # tedy aktualni index.

    def load_all_sprites(self):
        #  nasekam si nase obrazky Player *.png na nejake casti
        #  a zvolim si datovou strukturu, do ktere je nasypu. Bude to dictionary:
        sprite_sheet = {
            self.IDLE: {
                self.LEFT: [],  # toto jsou pole spritů
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

    # Po pridani Timeru a game.timer() na konec kodu:
    # Pripravime si tedy indexovaci metodu next_animation_index v tride Player pomoci zbytku po celociselnem deleni.
    # Dame si ji pred Tik, ktery si nechavame na konci kodu tridy Player().
    # Jako argument dostane nejaky index idx.
    def next_animation_index(self, idx):
        idx += 1  # dalsi hodnota indexu
        # mam problem, ze v png souborech playeru je vzdy jiny pocet obrazku, tedy aby se mi index
        # tocil v nejakem rozmezi, musim si stanovit maximum indexu.
        # Vezmeme si delku aktualniho pole pomoci len() a vezmeme aktualni stav pohybu a smeru a vrati
        # mi to maximalni pocet hodnot toho pole a jeho delku. A pak pomoci % (zbytku po deleni) vypocitam dalsi
        # index. Do naseho Player/init pak doplnime self.sprite_idx = 0.
        max_idx = len(self.sprite_sheet[self.movement][self.direction])
        idx = idx % max_idx  # takto zarucim, ze se mi to bude tocit v indexech, ktere potrebuji.
        return idx

    #  zkusime neco nakreslit. Vezmeme tik ze zdedene BaseSprite a prepiseme ji.
    #  Mame zapamatovane IDčko naseho obrazku self.id = self.canvas.create_image(x, y)
    #  a s nim pracujeme.
    def tik(self):
        #  vyberu si prvni polohu hrace a
        #  do konstruktoru tridy Game() doplnim hrace a nejaky canvas self.player = Player(self.canvas)
        #  a pak si musim definovat v tride Game metodu Timer, ktery pouze zavola metodu Tik.
        #  protoze vykreslovani se deje v nasem casovani = tikani. Jinak se nic nenakresli.

        self.sprite_idx = self.next_animation_index(self.sprite_idx)  # doplneni o vzdy aktualni index obrazku.
        img = self.sprite_sheet[self.movement][self.direction][self.sprite_idx]   #  0 jsme zmenili na sprite_idx
        self.canvas.itemconfig(self.id, image=img)


game = Game()
game.timer()  # nastartuje moje tikani a rybicka se bude vykreslovat. Pak zacneme rybicku animovat.
# Pripravime si tedy indexovaci metodu next_animation_index v tride Player pomoci zbytku po celociselnem deleni.

game.mainloop()
