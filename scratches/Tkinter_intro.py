import tkinter
import tkinter.messagebox


def main():
    flag = True

    #modify the text on tag
    def change_label_text(text):
        nonlocal flag
        flag = not flag
        color,msg = ("red","hello world!")\
              if flag else ("blue","Goodbye world!")
        label.config(text=msg,fg=color)
        return text

    def confirm_to_exit():
        if tkinter.messagebox.askokcancel("Warning!","Are you sure to exit?"):
            top.quit()

    top= tkinter.Tk()

    top.geometry("240x160")

    top.title("Game")

    label = tkinter.Label(top,text =" Hello World!",font ="Arial -32",fg = "red")
    label.pack(expand=1)

    panel = tkinter.Frame(top)

    button1 = tkinter.Button(panel,text="Modify",command=change_label_text("A"))
    button1.pack(side="left")
    button2 = tkinter.Button(panel,text='Quit',command = confirm_to_exit)
    button2.pack(side="right")
    button3 = tkinter.Button(panel,text = "JUST TRY TRY!")
    button3.pack(side="top")



    panel.pack(side = "bottom")

    tkinter.mainloop()

if __name__ == "__main__":
    main()



'''
#from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("Welcome to ATT ANT Team")


window.geometry("300x200")

label = tkinter.Label(window,bg="red",bd=5,text="Hello i like Rou HU!",font=("Arial",50))

#Without calling the grid function for the label, it won’t show up.
#pack,grid,place three ways to place the label


label.grid(column=0,row =0)

button = tkinter.Button(window,bg="green",text="Yue Zhang is good boy!")
button.grid(row= 2, column = 6, pady =0)



def click_button():
    label.configure(text="Button is clicked!")




button.configure(command=click_button)


window.mainloop()


#get the whole tutorial here
'''