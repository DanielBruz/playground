import tkinter as tk
import random
from PIL import Image, ImageTk


#   V této upravené verzi jsme vytvořili základní třídu GameObject, která obsahuje společné vlastnosti
#   a metody pro ptáky i hru. Třída Bird dědí od GameObject a využívá jeho konstruktor a metody, což umožňuje
#   snadné sdílení kódu a zjednodušení struktury. Tímto způsobem můžeme lépe organizovat váš kód a snižovat duplikaci.
class GameObject:
    def __init__(self, canvas, image_frames, background_height, x, y):
        self.canvas = canvas
        self.image_frames = image_frames
        self.background_height = background_height
        self.frame_width = image_frames[0].width()
        self.frame_height = image_frames[0].height()

        y = random.randint(50, self.background_height - self.frame_height - 50)
        self.object = self.canvas.create_image(x, y, anchor=tk.W, image=self.image_frames[0])
        self.frame_idx = 0

    def move(self):
        # Důvodem, proč existují metody move() a move_birds() v rámci tříd Bird a Game, je to,
        # že každá z těchto metod má odlišný účel a odpovědnost.
        # Metoda move() v třídě Bird:
        # Metoda move() je specifická pro jednoho ptáka. Každý pták na plátně má svou instanci třídy Bird,
        # a tato metoda řídí pohyb tohoto konkrétního ptáka. Metoda move() je volána v rámci smyčky pro každého
        # ptáka na plátně, aby se zajistilo, že se každý pták pohybuje samostatně.
        # Metoda move() může provádět jakýkoli specifický pohyb nebo animaci pro daného ptáka,
        # včetně změny obrázků ptáka, aby vypadalo, že pták létá.
        # Metoda move_birds() v třídě Game:
        # Metoda move_birds() je obecná metoda třídy Game, která řídí pohyb všech ptáků na plátně.
        # Tato metoda je volána v rámci smyčky, aby se zajistil pohyb všech ptáků najednou.
        # Metoda move_birds() přesouvá každého ptáka na plátně o určitou vzdálenost (například o -20 pixelů)
        # směrem doleva, což dává iluzi, že ptáci létají z pravé části plátna na levou.
        # Tato metoda také řídí animaci ptáků tím, že mění jejich obrázky (snímky) z animačního spritesheetu.
        # Závěr:
        # Metoda move() je určena pro jednotlivé instance ptáků a řídí jejich pohyb a animaci.
        # Metoda move_birds() je určena pro celou hru a řídí pohyb všech ptáků současně.
        # Tyto dvě metody pracují společně a umožňují, aby se ptáci na plátně pohybovali nezávisle na sobě
        # a vytvářeli celkový dojem letecké hry.
        coords = self.canvas.coords(self.object)
        if coords:
            self.canvas.move(self.object, -20, 0)
            self.frame_idx = (self.frame_idx + 1) % len(self.image_frames)
            self.canvas.itemconfig(self.object, image=self.image_frames[self.frame_idx])
            if coords[0] + self.frame_width <= 0:
                self.canvas.delete(self.object)


class Bird(GameObject):
    def __init__(self, canvas, bird_frames, background_height, x, y):
        super().__init__(canvas, bird_frames, background_height, x, y)

    def get_coords(self):
        return self.canvas.coords(self.object)


class Game:
    def __init__(self, canvas, w, h, game_duration):
        self.canvas = canvas
        self.target_img = None
        self.root = root
        self.width = w
        self.height = h
        self.game_duration = game_duration
        self.time_remaining = game_duration
        self.is_game_running = False
        self.frame_width = 0
        self.frame_height = 0
        self.score = 0

        # Slovník self.birds_dict a seznam self.birds mají významově různé použití:
        # self.birds_dict: Tento slovník slouží k uchování informací o momentálně viditelných ptácích na plátně
        # a jejich stavu animace. Klíčem ve slovníku je identifikátor (odkaz) grafického objektu (item) ptáka na plátně
        # (typicky vytvořený pomocí self.canvas.create_image()).
        # Hodnotou je pak index snímku (frame_idx) aktuálně používaného obrázku pro daného ptáka.
        # Tento slovník slouží zejména k tomu, aby se správně animovali ptáci a aby se mohli odstraňovat,
        # když doletí mimo obrazovku.
        # self.birds: Tento seznam slouží k uchování samotných objektů ptáků (instancí třídy Bird).
        # Každý prvek seznamu představuje jednoho ptáka, který je momentálně v hře. Seznam self.birds je tedy
        # zodpovědný za sledování, kolik ptáků se momentálně nachází na herním plátně.
        # V souhrnu lze říci, že slovník self.birds_dict se zaměřuje na animaci a manipulaci s grafickými objekty
        # ptáků na plátně, zatímco seznam self.birds slouží k uchování a sledování samotných instancí ptáků,
        # které jsou aktuálně ve hře.

        self.birds_dict = {}
        self.birds = []
        self.background_img, self.background_width, self.background_height = self.load_background_image(
            "img/birds/background2.png")
        self.canvas.create_image(0, 0, image=self.background_img, anchor=tk.NW)

        self.bird_frames = self.load_bird_frames("img/birds/spritesheet/yellow_flying_bird_3_flying.png")

        self.score_label = self.canvas.create_text(100, 30, text="Score: 0", fill="red", font=("Arial", 20),
                                                   anchor=tk.W)
        self.time_label = self.canvas.create_text(100, 60, text=f"Time: {self.time_remaining} sec", fill="red",
                                                  font=("Arial", 20), anchor=tk.W)
        self.stats_label = self.canvas.create_text(self.width // 2, self.height // 2, text="", fill="red",
                                                   font=("Arial", 30))

        self.load_target_image("img/birds/target.png")
        self.cursor = None

        self.canvas.bind("<Button-1>", self.shoot_bird)
        self.canvas.bind("<Motion>", self.move_cursor)

    def start(self):
        self.is_game_running = True
        self.root.after(1000, self.add_bird)
        self.root.after(100, self.move_birds)
        self.root.after(1000, self.update_time)

    def add_bird(self):
        # Nejprve se vytvoří nový objekt třídy Bird
        bird = Bird(self.canvas, self.bird_frames, self.background_height, self.width, self.height)
        # Potom je vytvořený pták (instance třídy Bird) přidán do seznamu self.birds, který uchovává všechny
        # aktuálně vytvořené ptáky v hře. Tím se zajišťuje, že ptáci budou správně pohybováni a aktualizováni.
        self.birds.append(bird)
        self.root.after(1000, self.add_bird)  # To způsobí, že se nový pták přidá do hry každou sekundu

    def move_birds(self):
        #     birds_to_remove = []: Vytváří prázdný seznam, do kterého budeme ukládat ptáky, kteří se nacházejí
        #     mimo herní plochu a budou následně odebráni ze hry.
        #     for bird in self.birds:: Projde všechny ptáky, kteří jsou momentálně ve hře.
        #     bird.move(): Pro každého ptáka zavolá metodu move(), která zajistí posunutí ptáka na herní ploše.
        #     for bird in list(self.birds_dict.keys()):: Projde všechny ptáky,
        #     kteří jsou momentálně ve slovníku self.birds_dict.
        #     bird_coords = self.canvas.coords(bird): Získá aktuální souřadnice ptáka na herní ploše.
        #     if bird_coords:: Pokud jsou souřadnice platné (tj. pták je stále na plátně, nebyl odstraněn):
        #     self.canvas.move(bird, -20, 0): Posune ptáka o -20 pixelů v horizontálním směru
        #     (tj. pták se posune doleva).
        #     frame_idx = (self.birds_dict[bird] + 1) % len(self.bird_frames):
        #     Aktualizuje index snímku pro animaci ptáka.
        #     self.canvas.itemconfig(bird, image=self.bird_frames[frame_idx]):
        #     Nastaví aktuální snímek ptáka na herní ploše na nový snímek podle aktuálního frame_idx.
        #     self.birds_dict[bird] = frame_idx: Aktualizuje index snímku pro ptáka ve slovníku self.birds_dict.
        #     if bird_coords[0] + self.frame_width <= 0:: Pokud je pták mimo herní plochu (jeho levá hrana je mimo hru):
        #     birds_to_remove.append(bird): Přidá ptáka do seznamu birds_to_remove, který bude následně odebrán ze hry.
        #     Po dokončení tohoto cyklu budou všechny ptáci posunuti doleva a aktualizována jejich animace.
        #     Pokud nějaký pták překročí levou hranici herní plochy (je mimo hru), bude přidán do
        #     seznamu birds_to_remove. Po dokončení tohoto cyklu budou z hry odebráni všichni ptáci, kteří
        #     jsou ve výše zmíněném seznamu, a tím budou odstraněni z herní plochy.

        # V slovníku self.birds_dict jsou uloženi ptáci, kteří jsou momentálně umístěni na plátně ve hře.
        # Klíčem ve slovníku je odkaz na grafický objekt (item) ptáka v plátně (tj. identifikátor vytvořený pomocí
        # self.canvas.create_image()), a hodnotou je index snímku (frame_idx) aktuálně
        # používaného obrázku pro daného ptáka. Když se pták pohybuje, probíhá animace, kdy se obrázky snímků
        # postupně mění. Abychom udrželi informaci o aktuálně používaném snímku pro každého ptáka, ukládáme tento index
        # snímku do slovníku self.birds_dict. Metoda move_birds() projde všechny ptáky ve slovníku self.birds_dict
        # a provede pro každého z nich krok pohybu (posun o -20 pixelů doleva) a aktualizuje použitý snímek na další
        # v animačním spritesheetu. Pokud je pták mimo obrazovku (jeho souřadnice X + šířka snímku jsou menší nebo
        # rovny nule), je označen ke smazání a bude odstraněn z plátna ve vhodném okamžiku. Celkově lze říci,
        # že slovník self.birds_dict je použit k uchování informací o všech momentálně viditelných ptácích na plátně
        # spolu s jejich aktuálním stavem animace (index použitého snímku).

        if not self.is_game_over() and self.is_game_running:  # Přidáme podmínku, zda hra běží
            birds_to_remove = []
            for bird in self.birds:
                bird.move()
            for bird in list(self.birds_dict.keys()):  # Klíčem je odkaz na grafický objekt (item) ptáka v plátně
                bird_coords = self.canvas.coords(bird)
                if bird_coords:  # jsou-li souřadnice platné.
                    self.canvas.move(bird, -20, 0)
                    frame_idx = (self.birds_dict[bird] + 1) % len(self.bird_frames)
                    self.canvas.itemconfig(bird, image=self.bird_frames[frame_idx])
                    self.birds_dict[bird] = frame_idx
                    # V podmínce if bird_coords[0] + self.frame_width <= 0: je bird_coords[0] nula,
                    # protože souřadnice bird_coords obsahují aktuální pozici ptáka na herní ploše
                    # jako (x, y). Hodnota bird_coords[0] představuje horizontální (x) souřadnici ptáka,
                    # což určuje jeho pozici na ose x (vodorovně). Pokud je tato hodnota menší nebo rovna nule,
                    # znamená to, že levá hrana ptáka je mimo herní plochu na levé straně.
                    # V tomto kontextu je znaménko + použito pro přidání šířky ptáka self.frame_width k jeho
                    # horizontální souřadnici. Tímto způsobem zjišťujeme, zda se pták dostal na levou stranu
                    # herní plochy.
                    # Pokud je výsledek výrazu bird_coords[0] + self.frame_width menší nebo roven nule, znamená to,
                    # že levá hrana ptáka je mimo herní plochu na levé straně.
                    # V tomto případě se pták nachází mimo herní plochu, a proto je přidán do seznamu birds_to_remove,
                    # který následně slouží k odstranění ptáků z herní plochy.
                    if bird_coords[0] + self.frame_width <= 0:
                        birds_to_remove.append(bird)

            for bird in birds_to_remove:
                self.canvas.delete(bird)
                del self.birds_dict[bird]

            root.after(100, self.move_birds)
        else:
            self.end_game()  # Voláme end_game po skončení pohybu ptáků

    def shoot_bird(self, event):
        for bird in self.birds:
            bird_coords = bird.get_coords()
            # bird_coords je výstupní hodnota z metody self.canvas.coords(bird.bird), která získá souřadnice (pozici)
            # objektu ptáka na plátně. Tato metoda vrátí seznam souřadnic, který obsahuje hodnoty
            # [x, y, width, height], kde x a y jsou souřadnice levého horního rohu ptáka a width a height
            # jsou jeho rozměry.
            # if bird_coords kontroluje, zda bird_coords obsahuje nějaké hodnoty (není prázdný seznam).
            # To zajišťuje, že pták ještě existuje na plátně a není již odstraněn.
            # len(bird_coords) >= 2 kontroluje, zda je délka seznamu bird_coords alespoň 2.
            # Pokud je to pravda, znamená to, že metoda self.canvas.coords(bird.bird) vrátila alespoň dvě
            # souřadnice x a y, což jsou minimálně souřadnice levého horního rohu ptáka.
            # Tím se ověřuje, že pták má platné souřadnice na plátně.
            # Celkově tato podmínka zajišťuje, že pták existuje na plátně a má platné souřadnice,
            # což je důležité předtím, než proběhne detekce, zda došlo ke střelbě na ptáka.
            if bird_coords and len(bird_coords) >= 2:
                # Jestliže je x myši mezi levou stranou ptáka na 0 a šíří ptáka a zároveň je y myši mezi horní
                # hranou ptáka a jeho výškou:
                if bird_coords[0] <= event.x <= bird_coords[0] + bird.frame_width and bird_coords[1] <= event.y <= \
                        bird_coords[1] + bird.frame_height:
                    self.canvas.delete(bird.object)
                    self.birds.remove(bird)
                    self.update_score()

    def update_score(self):
        # Aktualizace skóre
        self.score += 1
        self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}", fill="red")  # Změníme barvu na červenou

    def update_time(self):
        # Aktualizace zbývajícího času hry
        self.time_remaining -= 1
        self.canvas.itemconfig(self.time_label, text=f"Time: {self.time_remaining} sec", fill="red")  # červená barva
        if self.time_remaining > 0:
            self.root.after(1000, self.update_time)  # updatuje čas po jedné sekundě
        else:
            self.end_game()

    def is_game_over(self):
        # Kontrola, zda hra skončila
        return self.time_remaining <= 0

    def end_game(self):
        # Ukončení hry
        self.is_game_running = False  # Nastavíme, že hra není v provozu
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.background_img, anchor=tk.NW)
        self.canvas.create_text(self.background_width // 2, self.background_height // 2,
                                text=f"Final Score: {self.score}", fill="red", font=("Arial", 30))
        self.canvas.pack()

    def load_background_image(self, image_path):
        # Metoda pro načtení obrázku pozadí hry
        background_i = Image.open(image_path)
        background_w, background_h = background_i.size
        return ImageTk.PhotoImage(background_i), background_w, background_h

    def load_bird_frames(self, image_path):
        # Metoda pro načtení snímků animace ptáka z obrázku
        image = Image.open(image_path)
        image_frames = []
        self.frame_width = image.width // 4
        self.frame_height = image.height // 2

        for row in range(2):
            for col in range(4):
                left = col * self.frame_width
                top = row * self.frame_height
                right = left + self.frame_width
                bottom = top + self.frame_height

                if right <= image.width and bottom <= image.height:
                    frame = image.crop((left, top, right, bottom))
                    image_frames.append(ImageTk.PhotoImage(frame))

        return image_frames

    def load_target_image(self, image_path):
        # Metoda pro načtení obrázku terče
        target_image = Image.open(image_path)  # načtení objektu ve formátu Image
        self.target_img = ImageTk.PhotoImage(target_image)  # převedení na objekt PhotoImage pro zobrazení.

    def move_cursor(self, event):
        # Metoda pro pohyb kurzoru na plátně
        cursor_x, cursor_y = event.x, event.y
        if self.cursor is None:
            self.cursor = self.canvas.create_image(cursor_x, cursor_y, image=self.target_img, anchor=tk.CENTER)
        else:
            self.canvas.coords(self.cursor, cursor_x, cursor_y)


class GUI:
    def __init__(self, r, w, h):  # root, width, height jsem pojmenoval jinak, než je mimo metodu
        self.root = r
        self.width = w
        self.height = h
        self.canvas = self.create_game_elements()

    def create_game_elements(self):
        canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="white")
        canvas.pack()
        return canvas


# Hlavní program
root = tk.Tk()
root.title("Bird Shooting Game")
width = 800
height = 600
GAME_DURATION = 30

game_gui = GUI(root, width, height)
game = Game(game_gui.canvas, width, height, GAME_DURATION)
game.start()

root.mainloop()
