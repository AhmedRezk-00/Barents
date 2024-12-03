import tkinter as tk

class notification_popup:
    def __init__(self, root, title, message):
        self.frame = tk.Frame(root, bg="red", bd=2)
        self.frame.place(relx=0.5, rely=0.1, anchor="n", width=200, height=50)

        FONT = ("Helvetica", 10)
        BIGFONT = ("Helvetica", 10, "bold")
        tk.Label(self.frame, text=title, bg="red", fg="white", font=BIGFONT).pack()
        tk.Label(self.frame, text=message, bg="red", fg="white", font=FONT).pack()

        self.frame.after(2000, self.frame.destroy)