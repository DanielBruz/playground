import tkinter as tk
import random
from PIL import Image, ImageTk


class BirdShootingGame:
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

    def load_background_image(self, image_path):
        background_i = Image.open(image_path)
        background_w, background_h = background_i.size
        return ImageTk.PhotoImage(background_i), background_w, background_h

    def set_window_size(self):
        self.root.geometry(f"{self.background_width}x{self.background_height}")

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

    def add_bird(self):
        bird_y = random.randint(50, self.background_height - self.frame_height - 50)
        bird = self.canvas.create_image(self.background_width, bird_y, anchor=tk.W,
                                        image=self.bird_frames[0], tags="bird")
        self.birds_dict[bird] = 0  # Uchováváme ptáka a index aktuálního snímku ptáka v seznamu snímků
        root.after(1000, self.add_bird)  # Přidání nového ptáka po 1000 ms (1 sekunda)

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

    def is_game_over(self):
        return self.time_remaining <= 0

    def shoot_bird(self, event):
        for bird in list(self.birds_dict.keys()):
            bird_coords = self.canvas.coords(bird)
            if bird_coords and len(bird_coords) >= 2:  # Check if bird_coords is not empty and has at least 2 elements
                if bird_coords[0] <= event.x <= bird_coords[0] + self.frame_width and bird_coords[1] <= event.y <= \
                        bird_coords[1] + self.frame_height:
                    self.canvas.delete(bird)
                    del self.birds_dict[bird]
                    self.update_score()

    def move_cursor(self, event):
        cursor_x, cursor_y = event.x, event.y
        if self.cursor is None:
            self.cursor = self.canvas.create_image(cursor_x, cursor_y, image=self.target_img, anchor=tk.CENTER)
        else:
            self.canvas.coords(self.cursor, cursor_x, cursor_y)

    def update_score(self):
        self.score += 1  # Přístup k atributu self.score
        self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}", fill="red")

    def update_time(self):
        self.time_remaining -= 1  # Přístup k atributu self.time_remaining
        self.canvas.itemconfig(self.time_label, text=f"Time: {self.time_remaining} sec", fill="red")
        if self.time_remaining > 0:  # Přístup k atributu self.time_remaining
            self.root.after(1000, self.update_time)
        else:
            self.end_game()

    def end_game(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.background_img, anchor=tk.NW)  # Obnovíme pozadí na prázdném canvasu
        self.canvas.create_text(self.background_width // 2, self.background_height // 2,
                                text=f"Final Score: {self.score}", fill="red", font=("Arial", 30))
        self.canvas.pack()  # Znovu zabalíme plátno, aby se zobrazila statistika

    def load_target_image(self, image_path):  # Metoda pro načtení obrázku terče
        target_image = Image.open(image_path)
        self.target_img = ImageTk.PhotoImage(target_image)


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
