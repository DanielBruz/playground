# V tomto příkladu je vytvořeno okno s plátnem, ve kterém se zobrazuje kruh a skóre.
# Kruh se každou sekundu přesune na náhodnou pozici v ploše.
# Když hráč klikne do kruhu, jeho skóre se zvýší o 1 bod a kruh se přesune na novou pozici.
# Pokud hráč klikne vedle kruhu, skóre se sníží o 1 bod.
# Funkce update_score() aktualizuje zobrazené skóre na plátně na základě předané hodnoty.
# Funkce generate_position() generuje náhodnou pozici pro kruh uvnitř plochy.
# Funkce handle_click() se stará o obsluhu události kliknutí myší.
# Zjišťuje vzdálenost mezi pozicí kliknutí a středem kruhu.
# Pokud je kliknutí uvnitř kruhu, skóre se zvýší o 1 bod a kruh se přesune na novou pozici.
# Pokud je kliknutí mimo kruh, skóre se sníží o 1 bod.
# Funkce move_circle() se stará o pohyb kruhu na novou náhodnou pozici každou sekundu.
# Úprava: V tomto upraveném příkladu jsou přidána vstupní pole pro zadání poloměru kruhu a
# časového intervalu při spuštění hry.
# Hráč zadá hodnoty do těchto polí a poté stiskne tlačítko "Start" pro spuštění hry s danými parametry.
# Popisky "Radius" a "Interval (ms)" jsou přidány nad vstupními poli pro lepší orientaci.
# Při spuštění hry jsou hodnoty poloměru a intervalu načteny z vstupních polí a uloženy do příslušných proměnných.
# Skóre se resetuje na 0 a kruh se přesune na náhodnou pozici.
# Poté je spuštěna funkce move_circle() pro pohyb kruhu v daném intervalu.

import tkinter as tk
from random import randint

# Vytvoření hlavního okna
root = tk.Tk()

# Nastavení rozměrů okna
WIDTH = 600
HEIGHT = 400
root.geometry(f"{WIDTH}x{HEIGHT}")


# Funkce pro aktualizaci skóre
def update_score(value):
    global score
    score += value
    score_text = f"Score: {score}"
    canvas.itemconfig(score_label, text=score_text)


# Funkce pro generování náhodné pozice kruhu
def generate_position():
    x = randint(radius, WIDTH - radius)
    y = randint(radius, HEIGHT - radius)
    return x, y


# Funkce pro kliknutí myší
def handle_click(event):
    global radius
    x, y = event.x, event.y
    circle_x, circle_y = canvas.coords(circle)
    distance = ((circle_x - x) ** 2 + (circle_y - y) ** 2) ** 0.5
    if distance <= radius:
        update_score(1)
        canvas.coords(circle, generate_position())
    else:
        update_score(-1)


# Funkce pro pohyb kruhu
def move_circle():
    canvas.coords(circle, generate_position())
    root.after(interval, move_circle)


# Funkce pro spuštění hry
def start_game():
    global score, radius, interval
    score = 0
    radius = int(radius_entry.get())
    interval = int(interval_entry.get())
    update_score(0)
    canvas.coords(circle, generate_position())
    move_circle()


# Vytvoření plátna
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Vytvoření textového objektu pro skóre
score_text = "Score: 0"
score_label = canvas.create_text(50, 50, text=score_text, font=("Arial", 16), anchor="nw")

# Vytvoření popisku a vstupního pole pro poloměr kruhu
radius_label = tk.Label(root, text="Radius:")
radius_label.pack()
radius_entry = tk.Entry(root)
radius_entry.pack()

# Vytvoření popisku a vstupního pole pro časový interval
interval_label = tk.Label(root, text="Interval (ms):")
interval_label.pack()
interval_entry = tk.Entry(root)
interval_entry.pack()

# Vytvoření tlačítka pro spuštění hry
start_button = tk.Button(root, text="Start", command=start_game)
start_button.pack()

# Vytvoření kruhu
circle = canvas.create_oval(0, 0, 0, 0, fill="red")

# Přidání události pro kliknutí myší
canvas.bind("<Button-1>", handle_click)

# Spuštění hlavní smyčky událostí
root.mainloop()
