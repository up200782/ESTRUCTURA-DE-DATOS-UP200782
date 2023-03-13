import tkinter as tk

WIDTH = 400
HEIGHT = 400
BALL_SIZE = 20
STEP_SIZE = 5

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(WIDTH/2-BALL_SIZE/2, HEIGHT/2-BALL_SIZE/2, WIDTH/2+BALL_SIZE/2, HEIGHT/2+BALL_SIZE/2, fill=color)
        self.canvas.bind_all("<Button-1>", self.jump)

    def jump(self, event):
        self.canvas.move(self.id, 0, -BALL_SIZE*2)

    def move(self):
        pass

def main():
    root = tk.Tk()
    root.title("Jumping Ball")

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    ball = Ball(canvas, "red")

    while True:
        ball.move()
        root.update()
        tk.time.sleep(0.01)

    root.mainloop()



if __name__ == "__main__":
    main()
canvas.mainloop()


