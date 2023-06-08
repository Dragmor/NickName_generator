import tkinter as tk
from tkinter import *
from lib.gen_nick_module import gen_nick
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.gen_nickname = tk.Button(self, text='Generate!', fg="blue", command= self.print_nick)       
        self.gen_nickname.pack(side="top")
        self.enter_lbl = Label(text = "Выберите язык генерации")
        self.enter_lbl.pack(side="top")
        self.select_lang = StringVar(window)
        self.select_lang.set("Eng")
        self.langlist = OptionMenu(window, self.select_lang, "Eng", "Ru")
        self.langlist.pack(side = "top")
        self.enter_lbl = Label(text = "Выберите длину никнейма")
        self.enter_lbl.pack(side="top")
        self.enter_lbl = Label(text = "(по умолчанию 6 символов)")
        self.enter_lbl.pack(side="top")
        self.enter_txt = Entry(text = 0)
        self.enter_txt.pack(side="top")
        self.enter_txt["justify"] = "center"
        self.enter_txt.focus()
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=exit)
        self.quit.pack(side="bottom")
    def print_nick(self):
        self.lang = self.select_lang.get()
        self.nick_len = self.enter_txt.get()
        try:
            self.label = Label(text = gen_nick(self.lang, int(self.nick_len))) 
        except:
            self.label = Label(text = gen_nick(self.lang, 6))
        self.label.place(x=85, y=170, width = 80, height = 30)
        self.label ["relief"] = "sunken"
window = tk.Tk()
window.title('NickGen')
window.geometry('250x205')
app = Application(master=window)
window.wm_iconbitmap("logo.ico")
# window.configure(background = "black")
app.mainloop()
