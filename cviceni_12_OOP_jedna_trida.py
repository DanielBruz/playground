import tkinter as tk
import random
from PIL import Image, ImageTk


########################################### Třída BirdShootingGame #########################################

# Tato třída reprezentuje hru a obsahuje metody a atributy potřebné pro její fungování.

class BirdShootingGame:
    #   Konstruktor třídy BirdShootingGame, který se volá při vytváření instance hry.
    #   root: Hlavní okno (Tk) aplikace.
    #   width: Šířka herního plátna.
    #   height: Výška herního plátna.
    #   game_duration: Délka trvání hry v sekundách.
    def __init__(self, root, width, height, game_duration):
        self.target_img = None
        self.root = root
        self.width = width
        self.height = height
        self.game_duration = game_duration
        self.time_remaining = game_duration  # Nový atribut pro zbývající čas
        # Přidáme atributy pro frame_width a frame_height
        self.frame_width = 0
        self.frame_height = 0

        self.canvas = tk.Canvas(root, width=width, height=height)
        self.canvas.pack()

        self.score = 0
        self.birds_dict = {}
        self.background_img, self.background_width, self.background_height = self.load_background_image(
            "img/birds/background2.png")
        self.canvas.create_image(0, 0, image=self.background_img, anchor=tk.NW)

        self.bird_frames = self.load_bird_frames("img/birds/spritesheet/yellow_flying_bird_3_flying.png")

        self.score_label = self.canvas.create_text(100, 30, text="Score: 0", fill="white", font=("Arial", 20),
                                                   anchor=tk.W)
        self.time_label = self.canvas.create_text(100, 60, text=f"Time: {self.time_remaining} sec", fill="white",
                                                  font=("Arial", 20), anchor=tk.W)
        self.stats_label = self.canvas.create_text(self.width // 2, self.height // 2, text="", fill="red",
                                                   font=("Arial", 30))

        # Před inicializací cursoru zavoláme metodu load_target_image
        self.load_target_image("img/birds/target.png")
        self.cursor = None

        self.add_bird()
        self.move_birds()
        self.update_time()

        self.canvas.bind("<Button-1>", self.shoot_bird)
        self.canvas.bind("<Motion>", self.move_cursor)

    #     Metoda pro načtení obrázku pozadí hry.
    #     image_path: Cesta k souboru s obrázkem pozadí.
    #     Návratová hodnota: Tuple obsahující (background_img, background_width, background_height).
    def load_background_image(self, image_path):
        background_i = Image.open(image_path)
        background_w, background_h = background_i.size
        return ImageTk.PhotoImage(background_i), background_w, background_h

    #   Metoda nastaví velikost okna na velikost pozadí hry.
    def set_window_size(self):
        self.root.geometry(f"{self.background_width}x{self.background_height}")

    #     Metoda pro načtení snímků animace ptáka z obrázku.
    #     image_path: Cesta k souboru s obrázkem ptáka.
    #     Návratová hodnota: List obsahující snímky animace ptáka (ImageTk.PhotoImage).
    def load_bird_frames(self, image_path):
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

    #     Metoda pro přidání nového ptáka na herní plátno.
    #     Generuje nového ptáka s náhodnou pozicí po pravé straně herního plátna a ukládá ho do slovníku birds_dict.
    #     Pták je přidán každou sekundu (po 1000 ms) zavoláním této metody.
    def add_bird(self):
        bird_y = random.randint(50, self.background_height - self.frame_height - 50)
        bird = self.canvas.create_image(self.background_width, bird_y, anchor=tk.W,
                                        image=self.bird_frames[0], tags="bird")
        self.birds_dict[bird] = 0  # Uchováváme ptáka a index aktuálního snímku ptáka v seznamu snímků
        root.after(1000, self.add_bird)  # Přidání nového ptáka po 1000 ms (1 sekunda)

    #     Metoda pro pohyb ptáků po herním plátně.
    #     Každých 100 ms se aktualizuje pozice a obrázek ptáka na plátně, a zároveň se kontroluje,
    #     jestli pták přeletěl plátno. Pokud ano, odstraní se.
    #     Metoda je zavolávána pravidelně, dokud hra neskončí.
    def move_birds(self):
        if not self.is_game_over():  # Kontrola, zda hra již neskončila
            birds_to_remove = []
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

    #     Metoda pro kontrolu, zda hra již skončila (když došel čas).
    #     Návratová hodnota: True, pokud hra skončila, jinak False.
    def is_game_over(self):
        return self.time_remaining <= 0

    #     Metoda pro zpracování střelby na ptáka.
    #     event: Informace o události stisku tlačítka myši.
    #     Metoda kontroluje, zda střela hráče zasáhla některého z ptáků na plátně.
    #     Pokud ano, odstraní ptáka a aktualizuje skóre.
    def shoot_bird(self, event):
        for bird in list(self.birds_dict.keys()):
            bird_coords = self.canvas.coords(bird)
            if bird_coords and len(bird_coords) >= 2:  # Check if bird_coords is not empty and has at least 2 elements
                if bird_coords[0] <= event.x <= bird_coords[0] + self.frame_width and bird_coords[1] <= event.y <= \
                        bird_coords[1] + self.frame_height:
                    self.canvas.delete(bird)
                    del self.birds_dict[bird]
                    self.update_score()

    #     Metoda pro pohyb kurzoru na plátně.
    #     event: Informace o události pohybu myši.
    #     Metoda nastavuje pozici obrázku kurzoru na pozici kurzoru myši.
    def move_cursor(self, event):
        cursor_x, cursor_y = event.x, event.y
        if self.cursor is None:
            self.cursor = self.canvas.create_image(cursor_x, cursor_y, image=self.target_img, anchor=tk.CENTER)
        else:
            self.canvas.coords(self.cursor, cursor_x, cursor_y)

    #     Metoda pro aktualizaci skóre (počtu zasažených ptáků).
    #     Inkrementuje atribut self.score a aktualizuje textový label na plátně s aktuálním skóre.
    def update_score(self):
        self.score += 1  # Přístup k atributu self.score
        self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}", fill="red")

    #     Metoda pro aktualizaci zbývajícího času hry.
    #     Sníží atribut self.time_remaining o 1, aktualizuje textový label na plátně s časem a
    #     zavolá sebe sama po 1000 ms, pokud zbývající čas není 0.
    def update_time(self):
        self.time_remaining -= 1  # Přístup k atributu self.time_remaining
        self.canvas.itemconfig(self.time_label, text=f"Time: {self.time_remaining} sec", fill="red")
        if self.time_remaining > 0:  # Přístup k atributu self.time_remaining
            self.root.after(1000, self.update_time)
        else:
            self.end_game()

    #     Metoda pro ukončení hry.
    #     Po skončení hry vymaže všechny prvky na plátně a zobrazí konečné skóre.
    def end_game(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.background_img, anchor=tk.NW)  # Obnovíme pozadí na prázdném canvasu
        self.canvas.create_text(self.background_width // 2, self.background_height // 2,
                                text=f"Final Score: {self.score}", fill="red", font=("Arial", 30))
        self.canvas.pack()  # Znovu zabalíme plátno, aby se zobrazila statistika

    #     Metoda pro načtení obrázku terče.
    #     image_path: Cesta k souboru s obrázkem terče.
    #     Načtený obrázek terče se uloží do atributu self.target_img.
    def load_target_image(self, image_path):  # Metoda pro načtení obrázku terče
        target_image = Image.open(image_path)
        self.target_img = ImageTk.PhotoImage(target_image)

    #   Vytvoříme hlavní okno pomocí tk.Tk() a nastavíme jeho titulek.
    #   Nastavíme rozměry okna a délku hry.
    #   Vytvoříme instanci hry (game) a spustíme hlavní smyčku aplikace pomocí root.mainloop().


# Vytvoření hlavního okna
root = tk.Tk()
root.title("Bird Shooting Game")

# Nastavení rozměrů okna
width = 800
height = 600

# Konstanta pro čas hry (v sekundách)
GAME_DURATION = 30

# Vytvoření instance hry BirdShootingGame
game = BirdShootingGame(root, width, height, GAME_DURATION)

root.mainloop()
