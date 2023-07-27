import tkinter as tk
import random
from PIL import Image, ImageTk

# Konstanty pro čas hry (v sekundách)
GAME_DURATION = 30

# Počáteční hodnoty skóre a času
score = 0
time_remaining = GAME_DURATION

# Slovník pro uchovávání ptáků a jejich aktuálních snímků
birds_dict = {}

# Proměnné pro skutečnou velikost ptáka na plátně
frame_width = 0
frame_height = 0


# Funkce pro načtení obrázku pozadí a získání jeho rozměrů
def load_background_image(image_path):
    background_i = Image.open(image_path)
    background_w, background_h = background_i.size
    return ImageTk.PhotoImage(background_i), background_w, background_h


# Konstanta pro cestu k obrázku pozadí
BACKGROUND_IMAGE_PATH = "img/birds/background2.png"


# Funkce pro nastavení rozměrů okna na základě rozměrů obrázku pozadí
def set_window_size():
    root.geometry(f"{background_width}x{background_height}")


# Vytvoření hlavního okna
root = tk.Tk()
root.title("Bird Shooting Game")

# Načtení obrázku pozadí a jeho rozměrů
background_image = Image.open(BACKGROUND_IMAGE_PATH)
background_width, background_height = background_image.size
background_img = ImageTk.PhotoImage(background_image)

# Nastavení rozměrů okna na základě rozměrů obrázku pozadí
set_window_size()

# Vytvoření plátna s pozadím
canvas = tk.Canvas(root, width=background_width, height=background_height)
canvas.pack()
canvas.create_image(0, 0, image=background_img, anchor=tk.NW)


# Funkce pro vytvoření snímků ptáka z obrázku
def load_bird_frames(image_path):
    image = Image.open(image_path)
    image_frames = []
    global frame_width, frame_height
    frame_width = image.width // 4  # Očekáváme 4 sloupce v obrázku
    frame_height = image.height // 2  # Očekáváme 2 řádky v obrázku

    for row in range(2):
        for col in range(4):
            left = col * frame_width
            top = row * frame_height
            right = left + frame_width
            bottom = top + frame_height
            frame = image.crop((left, top, right, bottom))
            image_frames.append(ImageTk.PhotoImage(frame))

    return image_frames


# Funkce pro přidání nového ptáka
def add_bird():
    bird_y = random.randint(50, background_height - frame_height - 50)
    bird = canvas.create_image(background_width, bird_y, anchor=tk.W, image=bird_frames[0], tags="bird")
    birds_dict[bird] = 0  # Uchováváme ptáka a index aktuálního snímku ptáka v seznamu snímků
    root.after(1000, add_bird)  # Přidání nového ptáka po 1000 ms (1 sekunda)


# Funkce pro aktualizaci pohybu ptáků
def move_birds():
    birds_to_remove = []
    for bird in list(birds_dict.keys()):  # Používáme list() pro vytvoření kopie klíčů
        bird_coords = canvas.coords(bird)
        canvas.move(bird, -20, 0)  # Posun ptáka o 20 bodů doleva
        frame_idx = (birds_dict[bird] + 1) % len(bird_frames)
        canvas.itemconfig(bird, image=bird_frames[frame_idx])
        birds_dict[bird] = frame_idx  # Aktualizace indexu snímku ptáka v slovníku
        if bird_coords[0] + frame_width <= 0:  # Kontrola, zda je pták úplně mimo plátno
            birds_to_remove.append(bird)

    for bird in birds_to_remove:
        canvas.delete(bird)
        del birds_dict[bird]

    root.after(100, move_birds)  # Opakování funkce po 100 ms (0.1 sekundy)


# Funkce pro aktualizaci skóre
def update_score():
    global score
    score += 1
    canvas.itemconfig(score_label, text=f"Score: {score}", fill="red")


# Funkce pro aktualizaci zbývajícího času
def update_time():
    global time_remaining
    time_remaining -= 1
    canvas.itemconfig(time_label, text=f"Time: {time_remaining} sec", fill="red")
    if time_remaining > 0:
        root.after(1000, update_time)
    else:
        end_game()


# Funkce pro ukončení hry a zobrazení statistiky
def end_game():
    canvas.delete("all")
    canvas.create_image(0, 0, image=background_img, anchor=tk.NW)  # Obnovíme pozadí na prázdném canvasu
    canvas.create_text(background_width // 2, background_height // 2, text=f"Final Score: {score}", fill="red",
                       font=("Arial", 30))
    canvas.pack()  # Znovu zabalíme plátno, aby se zobrazila statistika


# Funkce pro kliknutí na ptáka
def shoot_bird(event):
    for bird in list(birds_dict.keys()):  # Používáme list() pro vytvoření kopie klíčů
        bird_coords = canvas.coords(bird)
        if bird_coords[0] <= event.x <= bird_coords[0] + frame_width and \
                bird_coords[1] <= event.y <= bird_coords[1] + frame_height:
            canvas.delete(bird)
            del birds_dict[bird]
            update_score()


# Funkce pro pohyb ukazatele myši a doplnění obrázku terče
def move_cursor(event):
    global cursor  # Musíme deklarovat, že používáme globální proměnnou cursor
    cursor_x, cursor_y = event.x, event.y
    if cursor is None:  # Pokud je cursor prázdný, vytvoříme nový plátnový objekt
        cursor = canvas.create_image(cursor_x, cursor_y, image=target_img, anchor=tk.CENTER)
    else:  # Jinak pouze aktualizujeme jeho pozici
        canvas.coords(cursor, cursor_x, cursor_y)


# Načtení snímků ptáka z obrázku
bird_frames = load_bird_frames("img/birds/spritesheet/yellow_flying_bird_3_flying.png")

# Vytvoření textového objektu pro skóre na plátno
score_label = canvas.create_text(100, 30, text="Score: 0", fill="white", font=("Arial", 20), anchor=tk.W)

# Vytvoření textového objektu pro zbývající čas na plátno
time_label = canvas.create_text(100, 60, text=f"Time: {time_remaining} sec", fill="white",
                                font=("Arial", 20), anchor=tk.W)

# Vytvoření textového objektu pro statistiku na plátno (prázdné canvas)
stats_label = canvas.create_text(background_width // 2, background_height // 2, text="",
                                 fill="red", font=("Arial", 30))

# Přidání události pro kliknutí myší
canvas.bind("<Button-1>", shoot_bird)

# Globální proměnná pro terč (ukazatel myši)
target_img = None
cursor = None  # Přidáme proměnnou cursor pro ukazatel myši


# Funkce pro načtení obrázku terče (target.png)
def load_target_image(image_path):
    global target_img
    target_image = Image.open(image_path)
    target_img = ImageTk.PhotoImage(target_image)


# Načtení obrázku terče
load_target_image("img/birds/target.png")

# Spuštění hry - přidání prvního ptáka, spuštění pohybu ptáků a spuštění časovače
add_bird()
move_birds()
update_time()
update_score()

# Přidání události pro pohyb myši a aktualizaci ukazatele
canvas.bind("<Motion>", move_cursor)

root.mainloop()
