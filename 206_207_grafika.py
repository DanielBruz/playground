import tkinter

canvas_width = 640
canvas_height = 480
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

line_id = canvas.create_line(10, 10, 200, 200, 10, 200, 10, 10, width=10, fill="red")
rect_id = canvas.create_rectangle(250, 50, 600, 400, width=10, fill="yellow", outline="blue")
oval_id = canvas.create_oval(320, 240, 200, 200, width=5, fill="grey", outline="blue")
text_id = canvas.create_text(200, 100, text="Ahoj Danieli", font="Ariel 30", fill="red", angle=0)

obrazek = tkinter.PhotoImage(file="img\python.png")
img_id = canvas.create_image(320, 240, image=obrazek)

canvas.itemconfig(rect_id, fill="forestgreen")

canvas.mainloop()
