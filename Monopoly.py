import tkinter
from tkinter import *
from PIL import ImageTk,Image
import random




def dice_roll():
    global jumps,canvas,dice,dice2,turn,Turn
    print("start")
    jumps =0
    temp = random.randint(1,6)
    dice = ImageTk.PhotoImage(Image.open("d{}.png".format(temp)))
    canvas.create_image(450,670, anchor=NW, image=dice)
    jumps+=temp
    temp = random.randint(1,6)
    dice2 = ImageTk.PhotoImage(Image.open("d{}.png".format(temp)))
    canvas.create_image(400, 670, anchor=NW, image=dice2)
    jumps+=temp
    
    if turn ==0:
        move()
        turn =1
        Turn.configure( text='Player 1')
    elif turn==3:
        Turn.configure( text='Press Board To Start')
        turn =0
    else:
        move()
        turn=0
        Turn.configure( text='Player 2')
    print("done")
    print(jumps)
def move():
    global jumps,canvas,hat,car,turn
    
    if turn == 0:
        car = ImageTk.PhotoImage(Image.open("car.png"))
        canvas.create_image(70,800, anchor=NW, image=car)
    else:
        hat = ImageTk.PhotoImage(Image.open("hat.png"))
        canvas.create_image(600,750, anchor=NW, image=hat)
jumps=0
root = Tk()
root.title("Monopoly")
root.minsize(width=1300, height=900)
root.attributes("-alpha", 0.90)
root.configure(background="#d0e7e0")
turn = 3




canvas = Canvas(root, width = 900, height = 900,background="#d0e7e0",bd=0, highlightthickness=0)  
canvas.place(relx=0.35, rely=0.5, anchor=CENTER)
blank = PhotoImage(file='blank.png')
roll = Button(canvas,width=450,height =450,command=dice_roll,borderwidth=0,image=blank)
roll.place(x=215, y=209)

img = ImageTk.PhotoImage(Image.open("1.jpg"))
canvas.create_image(20, 20, anchor=NW, image=img)


dice = ImageTk.PhotoImage(Image.open("d1.png"))
canvas.create_image(450,670, anchor=NW, image=dice)
dice2 = ImageTk.PhotoImage(Image.open("d1.png"))
canvas.create_image(400, 670, anchor=NW, image=dice2)



car = ImageTk.PhotoImage(Image.open("car.png"))
canvas.create_image(800,800, anchor=NW, image=car)
hat = ImageTk.PhotoImage(Image.open("hat.png"))
canvas.create_image(750,750, anchor=NW, image=hat)

tool = Canvas(root, width = 400, height = 900,background="#d0e7e0",bd=0, highlightthickness=0)  
tool.place(relx=0.85, rely=0.1, anchor=CENTER)

Turn = Label(tool, text='Player 1', fg="white",font="Geneva 30",bg="#d0e7e0")
Turn.pack()
bal = Label(tool, text='Balance', fg="white",font="Geneva 25",bg="#d0e7e0")
bal.pack()
bal = Label(tool, text='$500.00', fg="white",font="Geneva 25",bg="#d0e7e0")
bal.pack()
dice_roll()
root.mainloop()