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
        self.birds_dict = {}
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
        self.is_game_running = True
        self.root.after(1000, self.add_bird)
        self.root.after(100, self.move_birds)
        self.root.after(1000, self.update_time)

    def add_bird(self):
        bird = Bird(self.canvas, self.bird_frames, self.background_height, self.width, self.height)
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
        for bird in self.birds:
            bird_coords = bird.get_coords()
            if bird_coords and len(bird_coords) >= 2:
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
