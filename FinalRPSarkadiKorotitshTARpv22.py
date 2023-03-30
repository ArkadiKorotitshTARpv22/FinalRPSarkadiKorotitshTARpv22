
from operator import truediv
from tkinter import *
import random
import tkinter
import emoji
user = int
computer = int
win = 0
lose = 0
canvas = 1
def rps(win, lose, user):
    computer = random.randrange(1,6)
    if user == computer:
        var.set("It's a draw. \n No Points")  
    elif user == 1 and computer == 3:
        var.set(emoji.emojize(":gem_stone::right_arrow::scissors: \nYou win"))
        wins.set(wins.get() + 1)
        
    elif user == 1 and computer == 2:
        var.set(emoji.emojize(":gem_stone::left_arrow::newspaper: \nYou lose"))
        loses.set(loses.get() + 1)
          
    elif user == 2 and computer == 1:
        var.set(emoji.emojize(":newspaper::right_arrow::gem_stone: \nYou win"))
        wins.set(wins.get() + 1)
          
    elif user == 2 and computer == 3:
        var.set(emoji.emojize(":newspaper::left_arrow::scissors: \nYou lose"))
        loses.set(loses.get() + 1)
        
    elif user == 3 and computer == 1:
        var.set("You chose Scissors, I chose Rock. \nYou lose")
        loses.set(loses.get() + 1)
         
    elif user == 3 and computer == 2:
        var.set("You chose Scissors, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 3:
        var.set(emoji.emojize(":person_standing::right_arrow::scissors: \nYou win"))
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 1:
        var.set("You chose Spock, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 5:
        var.set("You chose Spock, I chose Lizard. \nYou lose")
        loses.set(loses.get() + 1)
        
    elif user == 4 and computer == 2:
        var.set("You chose Spock, I chose Paper. \nYou lose")
        loses.set(loses.get() + 1)
        
    elif user == 5 and computer == 1:
        var.set("You chose Lizard, I chose Rock. \nYou lose")
        loses.set(loses.get() + 1)
        
    elif user == 5 and computer == 2:
        var.set("You chose Lizard, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 5 and computer == 3:
        var.set("You chose Lizard, I chose Scissors. \nYou lose")
        loses.set(loses.get() + 1)
        
    elif user == 5 and computer == 4:
        var.set("You chose Lizard, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 1 and computer == 4:
        var.set("You chose Rock, I chose Spock. \nYou lose")
        loses.set(loses.get() + 1)
        
    elif user == 2 and computer == 4:
        var.set("You chose Paper, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 3 and computer == 4:
        var.set("You chose Scissors, I chose Spock. \nYou lose")
        loses.set(loses.get() + 1)
        
    elif user == 5 and computer == 4:
        var.set("You chose Lizard, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 1 and computer == 5:
        var.set("You chose Rock, I chose Lizard. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 2 and computer == 5:
        var.set("You chose Paper, I chose Lizard. \nYou lose")
        loses.set(loses.get() + 1)
        
    elif user == 3 and computer == 5:
        var.set("You chose Scissors, I chose Lizard. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 5:
        var.set("You chose Spock, I chose Lizard. \nYou lose")
        loses.set(loses.get() + 1)
        


    
top = tkinter.Tk()


top.wm_title("RPSLS")
top.minsize(width=400, height=200)
top.maxsize(width=400, height=200)
def change_color():
        top.configure(bg="white")
        B1.configure(bg="white",fg="grey20")
        B2.configure(bg="white",fg="grey20")
        B3.configure(bg="white",fg="grey20")
        B4.configure(bg="white",fg="grey20")
        B5.configure(bg="white",fg="grey20")
        l.configure(bg="white",fg="grey20")
        w.configure(bg="white",fg="grey20")
        w2.configure(bg="white",fg="grey20")
        labeled.configure(bg="white",fg="grey20")
        labeled2.configure(bg="white",fg="grey20")
def change_color2():
        top.configure(bg="grey14")
        B1.configure(bg="grey20",fg="white")
        B2.configure(bg="grey20",fg="white")
        B3.configure(bg="grey20",fg="white")
        B4.configure(bg="grey20",fg="white")
        B5.configure(bg="grey20",fg="white")
        l.configure(bg="grey14",fg="white")
        w.configure(bg="grey14",fg="white")
        w2.configure(bg="grey14",fg="white")
        labeled.configure(bg="grey14",fg="white")
        labeled2.configure(bg="grey14",fg="white")
button=Button(bg="white",fg="grey20",text= "Light", font=('Helvetica 10 bold'), command=change_color)
button.grid(row=0,column=0)
button=Button(bg="grey20",fg="white",text= "Dark", font=('Helvetica 10 bold'), command=change_color2)
button.grid(row=0,column=4)
def restartbtn():
    wins.set(wins.get() ==-1)
    loses.set(wins.get() ==-1)
B1 = tkinter.Button(top, text ="Rock", command = lambda: rps(win, lose, 1))
B1.grid(row=0, column=1)
B2 = tkinter.Button(top, text ="Paper", command = lambda: rps(win, lose, 2))
B2.grid(row=0, column=2)
B3 = tkinter.Button(top, text ="Scissors", command = lambda: rps(win, lose, 3))
B3.grid(row=0, column=3)
B4 = tkinter.Button(top, text ="Spock", command = lambda: rps(win, lose, 4))
B4.grid(row=1, column=1)
B5 = tkinter.Button(top, text ="Lizard", command = lambda: rps(win, lose, 5))
B5.grid(row=1, column=3)
Brestart = tkinter.Button(top,bg="red3",fg="white", text ="restart", command = lambda: restartbtn())
Brestart.grid(row=5, column=2)

var = StringVar()
var.set('Welcome!')
l = Label(top, textvariable = var)
l.grid(row=2, column=2)
wins = IntVar()
wins.set(win)
loses=IntVar()
loses.set(lose)
w = Label(top, textvariable = wins)
w.grid(row=4, column=1)
w2 = Label(top, textvariable = loses)
w2.grid(row=4, column=3)
labeled = Label(top, text = "Player Score:")
labeled.grid(row=3, column=1)
labeled2 = Label(top, text = "Robot Score:")
labeled2.grid(row=3, column=3)
top.configure(bg="white")
B1.configure(bg="white",fg="grey20")
B2.configure(bg="white",fg="grey20")
B3.configure(bg="white",fg="grey20")
B4.configure(bg="white",fg="grey20")
B5.configure(bg="white",fg="grey20")
l.configure(bg="white",fg="grey20")
w.configure(bg="white",fg="grey20")
w2.configure(bg="white",fg="grey20")
labeled.configure(bg="white",fg="grey20")
labeled2.configure(bg="white",fg="grey20")
top.mainloop()