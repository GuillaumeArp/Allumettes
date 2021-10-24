import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Hello World!")
        self.button = tk.Button(self, text="Exit", command=self.quit)
        self.label.pack()
        self.button.pack()
        

if __name__ == "__main__":
    app = Application()
    app.title("Ma Première App :-)")
    app.mainloop()
