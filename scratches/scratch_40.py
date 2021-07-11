import tkinter
from tkinter import messagebox
import time
from time import sleep
from threading import Thread
from tkinter.ttk import Progressbar
'''
def download():
    sleep(10)
    tkinter.messagebox.showwarning("Warning", "Download completed!")

'''
class Download(Thread):

    def run(self):
        time.sleep(2)
        tkinter.messagebox.showwarning("Warning", "Download completed!")


class Bar(Thread):
    def __init__(self,progress,top):
        super().__init__()
        self.progress = progress
        self.top = top
    def run(self):
        #top = tkinter.Tk()
        #progress = Progressbar(self, orient="horizontal", length=100, mode='determinate')
        self.progress['value'] = 20
        self.top.update_idletasks()
        sleep(1)

        self.progress['value'] = 40
        self.top.update_idletasks()
        sleep(1)

        self.progress['value'] = 50
        self.top.update_idletasks()
        sleep(1)

        self.progress['value'] = 60
        self.top.update_idletasks()
        sleep(1)

        self.progress['value'] = 80
        self.top.update_idletasks()
        sleep(1)
        self.progress['value'] = 100
        tkinter.messagebox.showwarning("JJJJ", "LINGZI!")



def download():
    Download(daemon=True).start()
    #Download().join()

def bar_bar(progress,top):
    Bar(progress,top).daemon = True
    Bar(progress,top).start()


def about():
    tkinter.messagebox.showinfo("Hello", "Lingzi is  slave!")

def main():


    top = tkinter.Tk()

    top.title("threading is good")

    top.geometry('500x300')


    # def bar():
    #
    #     progress['value'] = 20
    #     top.update_idletasks()
    #     time.sleep(1)
    #
    #     progress['value'] = 40
    #     top.update_idletasks()
    #     time.sleep(1)
    #
    #     progress['value'] = 50
    #     top.update_idletasks()
    #     time.sleep(1)
    #
    #     progress['value'] = 60
    #     top.update_idletasks()
    #     time.sleep(1)
    #
    #     progress['value'] = 80
    #     top.update_idletasks()
    #     time.sleep(1)
    #     progress['value'] = 100

    panel = tkinter.Frame(top)

    progress = Progressbar(panel, orient='horizontal',
                           length=100, mode='determinate')
    progress.pack(side ="bottom")

    #bar_bar =

    button1 = tkinter.Button(panel,text='Download',command=download)
    button1.pack(side="left")

    button2 = tkinter.Button(panel,text='About',command=bar_bar(progress,top))
    button2.pack(side='right')

    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ =="__main__":
    main()



