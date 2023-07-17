import tkinter as tk
from datetime import datetime

# Vytvoření hlavního okna
root = tk.Tk()

# Vytvoření plátna
canvas = tk.Canvas(root, width=300, height=100)
canvas.pack()

# Vytvoření textového objektu pro zobrazení času
text = canvas.create_text(150, 50, text="00:00:00.0", font=("Arial", 40), fill="black")

# Funkce pro aktualizaci času
def update_time():
    current_time = datetime.now().strftime("%H:%M:%S.%f")[:11]  # Získání aktuálního času s desetinnou částí sekundy
    canvas.itemconfig(text, text=current_time)  # Změna zobrazeného času v textovém objektu
    canvas.after(100, update_time)  # Spuštění funkce opět po 0.1 sekundy

# Spuštění funkce pro aktualizaci času
update_time()

# Spuštění hlavní smyčky událostí
root.mainloop()
