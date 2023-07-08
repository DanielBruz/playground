import tkinter
canvas_width = 640
canvas_height = 480
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

# canvas.create_line(10,10, 200, 200, 10, 200, 10, 10, width=10, fill="red")
# canvas.create_rectangle(250, 50, 600, 400, width=10, fill="yellow", outline="blue")
canvas.create_oval(320, 240, 200, 200, width=5, fill="grey", outline="blue")
# canvas.create_text(200, 100, text="Ahoj Danieli", font="Ariel 30", fill="red", angle=0)

# obrazek = tkinter.PhotoImage(file="img/python.png")
# canvas.create_image(100, 150, image="obrazek")


# rect_id = canvas.create_rectangle(250, 50, 600, 400)
# canvas.itemconfig(rect_id, fill="forestgreen")

canvas.mainloop()       # spustím hlavnú slučku - aplikácia beží pokým ju nevypnem
