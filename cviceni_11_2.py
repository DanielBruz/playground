# V tomto příkladu je vytvořeno okno s plátnem, na kterém je umístěn čtverec.
# Po kliknutí myší se přepne stav pohybu čtverce.
# Pokud je pohyb zapnutý, čtverec se bude pohybovat nahoru a dolů na plátně.
# Funkce toggle_movement() se stará o přepnutí stavu pohybu čtverce (zapnutí nebo vypnutí).
# Pokud je pohyb zapnutý, volání move_square() zajistí plynulý pohyb čtverce.
# Funkce move_square() se stará o aktuální pohyb čtverce.
# Pokud je pohyb zapnutý, čtverec se pohybuje nahoru, dokud nenarazí na horní okraj plátna,
# a poté se pohybuje dolů, dokud nenarazí na dolní okraj plátna.
# Čtverec se pohybuje po malých krocích, což vytváří efekt plynulého pohybu.
# Funkce je volána opakovaně s krátkým časovým prodlevou pomocí canvas.after(10, move_square),
# aby se zajistil plynulý pohyb.

import tkinter as tk

# Konstanty pro velikost plátna
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

# Konstanty pro velikost čtverce
SQUARE_SIZE = 50

# Směr pohybu čtverce (0 = nahoru, 1 = dolů)
direction = 0

# Stav pohybu čtverce (True = pohyb zapnutý, False = pohyb vypnutý)
moving = False


def toggle_movement():
    global moving
    moving = not moving


def handle_click(event):
    global direction, moving
    toggle_movement()
    if moving:
        # Pohyb čtverce pokud je pohyb zapnutý
        move_square()


def move_square():
    global direction
    x1, y1, x2, y2 = canvas.coords(square)

    if moving:
        if direction == 0:  # Pohyb nahoru
            if y1 > 0:  # Pokud nenarazil na horní okraj
                y1 -= 5
                y2 -= 5
            else:  # Nastaví směr pohybu dolů
                direction = 1
        else:  # Pohyb dolů
            if y2 < CANVAS_HEIGHT:  # Pokud nenarazil na dolní okraj
                y1 += 5
                y2 += 5
            else:  # Nastaví směr pohybu nahoru
                direction = 0

        canvas.coords(square, x1, y1, x2, y2)  # Aktualizace pozice čtverce
        canvas.after(10, move_square)  # Opakované volání funkce pro plynulý pohyb


# Vytvoření hlavního okna
root = tk.Tk()

# Vytvoření plátna
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Vytvoření čtverce na plátně
square = canvas.create_rectangle(CANVAS_WIDTH/2, 0, SQUARE_SIZE+(CANVAS_WIDTH/2), SQUARE_SIZE, fill="red")

# Přidání události pro kliknutí myší
canvas.bind("<Button-1>", handle_click)

# Spuštění hlavní smyčky událostí
root.mainloop()
