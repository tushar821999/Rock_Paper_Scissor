from tkinter import *
from random import randint
from PIL import ImageTk,Image

root = Tk()

# basic config of container
root.geometry('350x350')
root.title('ROCK PAPER SCISSOR')
root.config(bg='white')

# add image in the container
img = ImageTk.PhotoImage(Image.open('rocky.png'))
panel = Label(root,image=img,bg='white')
panel.place(x=145,y=3)

# set title of the container
lable_0 = Label(root,text="ROCK PAPER SCISSOR",width = 20,font=("bold",15),fg='brown',bg='white')
lable_0.place(x=70,y=83)

lable_1 = Label(root,text="Player 1 : ",width = 20,font=("bold",10),fg='brown',bg='white')
lable_1.place(x=20,y=130)
names = StringVar()
entry_1 = Entry(root,textvariable=names,bg='yellow')
entry_1.place(x=160,y=130)


def rock():
    name = entry_1.get()
    player = 'Rock'
    chosen = randint(1,3)
    if chosen == 1:
        computer = 'Rock'
    elif chosen == 2:
        computer ='Paper'
    else:
        computer = 'Scissor'
    lable_2.configure(text=name+": Rock")
    lable_3.configure(text="Forst : "+computer)

    if player == computer:
        lable_4.configure(text="Match Draw !")
    elif computer == 'Scissor':
        lable_4.configure(text=name+" Wins !")
    elif computer == 'Paper':
        lable_4.configure(text="Frost Wins !")


Button(root,text="Rock",width=10,bg='brown',fg='white',command=rock).place(x=50,y=180)


def paper():
    name = entry_1.get()
    player = 'Paper'
    chosen = randint(1,3)
    if chosen == 1:
        computer = 'Rock'
    elif chosen == 2:
        computer ='Paper'
    else:
        computer = 'Scissor'
    lable_2.configure(text=name+": Paper")
    lable_3.configure(text="Forst : "+computer)

    if player == computer:
        lable_4.configure(text="Match Draw !")
    elif computer == 'Rock':
        lable_4.configure(text=name+" Wins !")
    elif computer == 'Scissor':
        lable_4.configure(text="Frost Wins !")


Button(root,text="Paper",width=10,bg='brown',fg='white',command=paper).place(x=140,y=180)


def scissor():
    name = entry_1.get()
    player = 'Scissor'
    chosen = randint(1,3)
    if chosen == 1:
        computer = 'Rock'
    elif chosen == 2:
        computer ='Paper'
    else:
        computer = 'Scissor'
    lable_2.configure(text=name+": Scissor")
    lable_3.configure(text="Forst : "+computer)

    if player == computer:
        lable_4.configure(text="Match Draw !")
    elif computer == 'Paper':
        lable_4.configure(text=name+" Wins !")
    elif computer == 'Rock':
        lable_4.configure(text="Frost Wins !")


Button(root,text="Scissor",width=10,bg='brown',fg='white',command=scissor).place(x=230,y=180)

lable_2 = Label(root,text="...",width = 20,font=("bold",10),fg='brown',bg='white')
lable_2.place(x=100,y=210)

lable_3 = Label(root,text="...",width = 20,font=("bold",10),fg='brown',bg='white')
lable_3.place(x=100,y=250)

lable_4 = Label(root,text="Result Display Here",width = 20,font=("bold",10),fg='brown',bg='white')
lable_4.place(x=100,y=290)

mainloop()
