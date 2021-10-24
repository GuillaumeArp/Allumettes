import tkinter as tk
from tkinter import ttk

# class Application(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.create_widgets()

#     def create_widgets(self):
#         self.label = tk.Label(self, text="Hello World!")
#         self.button = tk.Button(self, text="Exit", command=self.quit)
#         self.label.pack()
#         self.button.pack()
        

# if __name__ == "__main__":
#     app = Application()
#     app.title("Ma Première App :-)")
#     app.mainloop()


root = tk.Tk()
root.title("Window Demo")

window_width = 600
window_height = 400

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
# Sets the alpha value for transparency
# root.attributes('-alpha', 0.5)
root.iconbitmap('./assets/match-head_39019.ico')

ttk.Label(root, text='Hello World').pack()

label = ttk.Label(root)
label['text'] = 'Hi, there'
label.pack()

label = ttk.Label(root)
label.config(text='I Love Python')
label.pack()

root.mainloop()