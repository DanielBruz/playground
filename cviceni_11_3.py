import tkinter as tk
from random import randint

# Vytvoření hlavního okna
root = tk.Tk()

# Nastavení rozměrů okna
WIDTH = 600
HEIGHT = 400
root.geometry(f"{WIDTH}x{HEIGHT}")

# Počáteční hodnoty skóre a poloměru kruhu
score = 0
radius = int(input("Zadej poloměr kruhu: "))


# Funkce pro aktualizaci skóre
def update_score(value):
    global score
    score += value
    score_text = f"Score: {score}"
    canvas.itemconfig(score_label, text=score_text)


# Funkce pro generování náhodné pozice kruhu
def generate_position():
    x1 = randint(radius, WIDTH - radius)
    y1 = randint(radius, HEIGHT - radius)
    x2 = x1 + radius
    y2 = y1 + radius
    return x1, y1, x2, y2


# Funkce pro kliknutí myší
def handle_click(event):
    global radius
    x, y = event.x, event.y
    circle_x, circle_y, _, _ = canvas.coords(circle)
    distance = ((circle_x - x) ** 2 + (circle_y - y) ** 2) ** 0.5
    if score >= 0:
        if distance <= radius:
            update_score(1)
            canvas.coords(circle, generate_position())
        else:
            update_score(-1)


# Funkce pro pohyb kruhu
def move_circle():
    canvas.coords(circle, generate_position())
    if score >= 0:
        root.after(1000, move_circle)
    else:
        canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", font=("Arial", 16), fill="red", anchor="center")

# Vytvoření plátna
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Vytvoření kruhu
circle_x, circle_y, _, _ = generate_position()
circle = canvas.create_oval(circle_x - radius, circle_y - radius, circle_x + radius, circle_y + radius, fill="red")

# Vytvoření textového objektu pro skóre
score_text = f"Score: {score}"
score_label = canvas.create_text(50, 50, text=score_text, font=("Arial", 16), anchor="nw")

# Přidání události pro kliknutí myší
canvas.bind("<Button-1>", handle_click)

# Spuštění pohybu kruhu
root.after(1000, move_circle)

# Spuštění hlavní smyčky událostí
root.mainloop()
