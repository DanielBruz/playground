import tkinter as tk

# Vytvoření hlavního okna
root = tk.Tk()

# Vytvoření plátna
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Vytvoření obdélníku
rectangle = canvas.create_rectangle(50, 50, 100, 100, fill="red")


# Pohyb obdélníku pomocí funkce canvas.coords()
def move_rectangle():
    coords = canvas.coords(rectangle)  # Získání aktuálních souřadnic obdélníku
    new_coords = [coords[0] + 10, coords[1] + 10, coords[2] + 10,
                  coords[3] + 10]  # Nové souřadnice posunuté o 10 jednotek
    canvas.coords(rectangle, *new_coords)  # Pohyb obdélníku na novou pozici


# Tlačítko pro pohyb obdélníku
button = tk.Button(root, text="Move Rectangle", command=move_rectangle, bg="yellow")
button.pack()

# Spuštění hlavní smyčky událostí
root.mainloop()
