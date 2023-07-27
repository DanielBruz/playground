#     Třída Bird
#     Tato třída by reprezentovala jednotlivé ptáky, jejich pohyb a chování.
#     Může obsahovat metody pro načtení snímků animace ptáka a jeho pohyb po herním plátně.
#
#     Třída Game
#     Tato třída by řídila průběh celé hry, včetně přidávání nových ptáků, kontrolu střelby,
#     aktualizaci skóre a času hry. Může obsahovat metody pro zahájení hry, ukončení hry a aktualizaci herního stavu.
#
#     Třída Target
#     Tato třída by se starala o načtení obrázku terče a jeho pohyb podle polohy myši na herním plátně.
#
#     Třída GUI
#     Tato třída by se starala o vytvoření grafického uživatelského rozhraní, umístění herních prvků na plátno,
#     obsluhu událostí myši a klávesnice, zobrazení skóre, času a dalších informací na obrazovce.
#
#     Hlavní program
#     V hlavním programu by se vytvořily instance výše zmíněných tříd a spustila se
#     hlavní smyčka aplikace pomocí root.mainloop().

import tkinter as tk
import random
from PIL import Image, ImageTk


class Bird:
    def __init__(self, canvas, bird_frames, background_height):
        # Inicializace ptáka
        self.canvas = canvas
        self.bird_frames = bird_frames
        self.background_height = background_height
        self.frame_width = bird_frames[0].width()
        self.frame_height = bird_frames[0].height()

        bird_y = random.randint(50, self.background_height - self.frame_height - 50)
        self.bird = self.canvas.create_image(self.canvas.winfo_width(), bird_y, anchor=tk.W,
                                             image=self.bird_frames[0], tags="bird")
        self.frame_idx = 0

    def move(self):
        # Pohyb ptáka
        bird_coords = self.canvas.coords(self.bird)
        if bird_coords:
            self.canvas.move(self.bird, -20, 0)
            self.frame_idx = (self.frame_idx + 1) % len(self.bird_frames)
            self.canvas.itemconfig(self.bird, image=self.bird_frames[self.frame_idx])
            if bird_coords[0] + self.frame_width <= 0:
                self.canvas.delete(self.bird)


class Game:
    def __init__(self, canvas, w, h, game_duration):
        # Inicializace hry
        self.canvas = canvas
        self.target_img = None  # Inicializace atributu target_img
        self.root = root
        self.width = w  # přejmenováno, protože byl argument použit i mimo metodu
        self.height = h
        self.game_duration = game_duration
        self.time_remaining = game_duration
        self.is_game_running = False  # Nový atribut pro označení stavu hry (běží/není)
        self.birds_dict = {}  # Přidáme atribut pro uchování ptáků na plátně
        self.frame_width = 0
        self.frame_height = 0

        self.score = 0
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
        # Spuštění hry
        self.is_game_running = True  # Nastavíme, že hra běží
        self.root.after(1000, self.add_bird)
        self.root.after(100, self.move_birds)
        self.root.after(1000, self.update_time)

    def add_bird(self):
        # Přidání nového ptáka na plátno
        bird = Bird(self.canvas, self.bird_frames, self.background_height)
        self.birds.append(bird)
        self.root.after(1000, self.add_bird)

    def move_birds(self):
        if not self.is_game_over() and self.is_game_running:  # Přidáme podmínku, zda hra běží
            birds_to_remove = []
            for bird in self.birds:
                bird.move()
            for bird in list(self.birds_dict.keys()):
                bird_coords = self.canvas.coords(bird)
                if bird_coords:
                    self.canvas.move(bird, -20, 0)
                    frame_idx = (self.birds_dict[bird] + 1) % len(self.bird_frames)
                    self.canvas.itemconfig(bird, image=self.bird_frames[frame_idx])
                    self.birds_dict[bird] = frame_idx
                    if bird_coords[0] + self.frame_width <= 0:
                        birds_to_remove.append(bird)

            for bird in birds_to_remove:
                self.canvas.delete(bird)
                del self.birds_dict[bird]

            root.after(100, self.move_birds)
        else:
            self.end_game()  # Voláme end_game po skončení pohybu ptáků

    def shoot_bird(self, event):
        # Zpracování střelby na ptáka
        for bird in self.birds:
            bird_coords = self.canvas.coords(bird.bird)
            if bird_coords and len(bird_coords) >= 2:
                if bird_coords[0] <= event.x <= bird_coords[0] + bird.frame_width and bird_coords[1] <= event.y <= \
                        bird_coords[1] + bird.frame_height:
                    self.canvas.delete(bird.bird)
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
            self.root.after(1000, self.update_time)
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
        target_image = Image.open(image_path)
        self.target_img = ImageTk.PhotoImage(target_image)

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
