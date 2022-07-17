from tkinter import *
from tkinter import messagebox
import time
import threading


time_speed= 0
#
def add_time(*args):
    global time_speed
    time_speed =15


def countdown(*args):

    global time_speed
    time_speed =15
    timer = True
    while timer:
        time.sleep(1)
        time_speed -= 1
        text_input.bind("<Key>", add_time)
        if time_speed == 0:
            timer= False

    messagebox.showinfo(title="Time Up", message=f"You stayed idle for 15 seconds, your text was cleared")
    text_input.delete("1.0", "end")

#
def restart():
    text_input.delete("1.0", "end")
    text_input.bind("<Key>", threading.Thread(target=countdown).start())

def start():
   window.withdraw()
   root.deiconify()
   text_input.bind("<Key>", threading.Thread(target=countdown).start())




root = Tk()
root.title("Disapearing Text App")
root.geometry("800x800")
root.config(padx=20, pady=20)
root.withdraw()

window = Tk()
window.title("Disapearing Text App")
window.geometry("700x600")
window.config(padx=20, pady=20)


#------------------------FIRST WINDOW-------------------------------------------------
window_frame = Frame(window,highlightbackground="#EDF6F9", highlightthickness=2, width=600,
             height=50,bg="#E3D5CA", relief=SUNKEN, padx=20, pady=20)
window_frame.pack(padx=20, pady=20)

text_label = Label(window_frame , text="Welcome to the Disappearing App!", font=("Ariel", 20, "bold"), bg="#F0EBE3")
text_label.grid(row=0,columnspan=3, pady=40, padx=40)

start_button= Button(window_frame ,text= "Start", bg="#FBC5C5",font=("Ariel", 15, "bold"),
                     width=15, command=start)
start_button.grid(row=2, column=1)

#------------------------SECOND WINDOW-------------------------------------------------

root_frame = Frame(root, highlightbackground="#EDF6F9", highlightthickness=2, width=500,
                     height=500, bg="#E3D5CA", relief=SUNKEN)
root_frame.grid(padx=50, pady=20)

title_label = Label(root_frame, text="Start Typing Below.",
                    font=("Times", 30), bg="#EDEDE9", fg="black",
                  padx=30, pady=30)
title_label.grid(row=0,column=0, columnspan=2, padx=10, pady=10)


text_input = Text(root_frame, font=("Ariel", 15), bg="#EDEDE9", height=15, width=50, fg="black",
                  padx=30, pady=30)
text_input.grid(row=7,column=0, columnspan=2, padx=10, pady=10)

restart_button = Button(root_frame, text="Restart", bg="#F5F0BB", activebackground="#F5F0BB",
                      foreground="blue",font=("Ariel", 10, "bold"),width=10, padx=10, pady=5, command=restart)
restart_button.grid(row=9, column=1,columnspan=2)





root.mainloop()




###TO-DOs:
## 1)Create a welcome page and a start button that takes user to the next page and starts the timer
# # 2)Create a time speed variable(secs)
# #3)Create a countdown function and bind your text input to any key ie if the user types a key
#    it triggers the add_time function which is 15 that will be deducted by 1 and if the user keeps
#    typing that 15 won't get to zero, but if the he stops typing for 15secs the text should disappear
#  4) Create a thread that makes the countdown function to run concurrently with the user text input
