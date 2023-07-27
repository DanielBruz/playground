import tkinter as tk
import random
from PIL import Image, ImageTk


class GameObject:
    def __init__(self, canvas, image, x, y):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.object_id = self.canvas.create_image(self.x, self.y, image=self.image, anchor=tk.NW)

    def load_image(self, image_path):
        image = Image.open(image_path)
        return ImageTk.PhotoImage(image)

    def move(self, dx, dy):
        self.canvas.move(self.object_id, dx, dy)
        self.x += dx
        self.y += dy

    def delete(self):
        self.canvas.delete(self.object_id)


class Bird(GameObject):
    def __init__(self, canvas, bird_frames, background_height, frame_height):
        super().__init__(canvas, bird_frames[0], background_width, random.randint(50, background_height - frame_height - 50))
        self.bird_frames = bird_frames
        self.frame_idx = 0

    def animate(self):
        self.frame_idx = (self.frame_idx + 1) % len(self.bird_frames)
        self.canvas.itemconfig(self.object_id, image=self.bird_frames[self.frame_idx])


class Target(GameObject):
    def __init__(self, canvas, image_path, background_width, background_height):
        x = background_width // 2
        y = background_height // 2
        super().__init__(canvas, image_path, x, y)


class Game:
    def __init__(self, root, width, height, game_duration):
        self.root = root
        self.width = width
        self.height = height
        self.game_duration = game_duration
        self.time_remaining = game_duration
        self.frame_width = 0
        self.frame_height = 0
        self.background_width = 0
        self.frame_height = 0

        self.canvas = tk.Canvas(root, width=width, height=height)
        self.canvas.pack()

        self.score = 0
        self.birds = []
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

        self.target = Target(self.canvas, "img/birds/target.png", self.background_width, self.background_height)

        self.add_bird()
        self.move_birds()
        self.update_time()

        self.canvas.bind("<Button-1>", self.shoot_bird)
        self.canvas.bind("<Motion>", self.move_cursor)

    def load_background_image(self, image_path):
        background_i = Image.open(image_path)
        background_w, background_h = background_i.size
        return ImageTk.PhotoImage(background_i), background_w, background_h

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
        bird = Bird(self.canvas, self.bird_frames, self.background_height, self.background_width, self.frame_height)
        self.birds.append(bird)
        root.after(1000, self.add_bird)

    def move_birds(self):
        if not self.is_game_over():
            birds_to_remove = []
            for bird in self.birds:
                bird.move(-20, 0)
                bird.animate()
                bird_coords = (bird.x, bird.y)
                if bird_coords[0] + self.frame_width <= 0:
                    birds_to_remove.append(bird)

            for bird in birds_to_remove:
                bird.delete()
                self.birds.remove(bird)

            root.after(100, self.move_birds)

    def is_game_over(self):
        return self.time_remaining <= 0

    def shoot_bird(self, event):
        for bird in list(self.birds):
            bird_coords = (bird.x, bird.y)
            if bird_coords and bird_coords[0] <= event.x <= bird_coords[0] + self.frame_width\
                    and bird_coords[1] <= event.y <= bird_coords[1] + self.frame_height:
                bird.delete()
                self.birds.remove(bird)
                self.update_score()

    def move_cursor(self, event):
        self.target.move(event.x, event.y)

    def update_score(self):
        self.score += 1
        self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}", fill="red")

    def update_time(self):
        self.time_remaining -= 1
        self.canvas.itemconfig(self.time_label, text=f"Time: {self.time_remaining} sec", fill="red")
        if self.time_remaining > 0:
            self.root.after(1000, self.update_time)
        else:
            self.end_game()

    def end_game(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, image=self.background_img, anchor=tk.NW)
        self.canvas.create_text(self.background_width // 2, self.background_height // 2,
                                text=f"Final Score: {self.score}", fill="red", font=("Arial", 30))
        self.canvas.pack()


# Hlavní program
root = tk.Tk()
root.title("Bird Shooting Game")
width = 800
height = 600
GAME_DURATION = 30

game = Game(root, width, height, GAME_DURATION)

root.mainloop()
