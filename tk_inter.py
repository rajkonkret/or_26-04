import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Test")

        self.label1 = tkinter.Label(self.main_window, text="Witaj świecie")
        self.label2 = tkinter.Label(self.main_window, text="To jest program z GUI")
        self.label3 = tkinter.Label(self.main_window, text="Test z prawej")
        self.label4 = tkinter.Label(self.main_window, text="Koniec")

        self.label1.pack(side='left')
        self.label2.pack(side='bottom')
        self.label3.pack(side='right')
        self.label4.pack(side='top')
        tkinter.mainloop()


my_gui = MyGui()
