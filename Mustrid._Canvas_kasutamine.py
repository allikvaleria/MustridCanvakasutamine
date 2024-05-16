from tkinter import * 
from turtle import width
import random 
from math import *


aken=Tk()      
aken.geometry("900x700")  
aken.iconbitmap('star.ico')
aken.title("Mustrid Canvas Kasutamine")
tekst="Mustrid Canvas Kasutamine\n"


pealkiri=Label(aken,
               text=tekst,
               fg="#000000",
               font=("Broadway 30"),
               height=2,width=len(tekst),
               cursor="watch")

pealkiri.grid(row=1, column=4, columnspan=5)

f=Frame(aken)


                                                   #MUSTER RING
def f1():
    aken=Tk()      
    aken.title("MUSTER RING")
    muster3_ring= Canvas(aken, width=600, height=600, background="#c0c0c0")
    muster3_ring.create_text(30, 500, anchor=NW)
    colors=["black",
                "cyan",
                "magenta",
                "red",
                "blue",
                "gray",
                "yellow",
                "green",
                "lightblue",
                "pink",
                "gold"]
    x0=0
    y0=0
    x1=600
    y1=600
    p=2
    for i in range(150):
            x0+=p
            y0+=p
            x1-=p
            y1-=p
            muster3_ring.create_oval(x0,y0,x1,y1,fill=random.choice(colors))
    muster3_ring.grid()


                                             #MUSTER RING SQUARE
def f2():
    aken=Tk()      
    aken.title("MUSTER RING SQUARE")
    muster_ring_square= Canvas(aken, width=300, height=300, background="#c0c0c0")
    colors=["pink","black"] 
    k=10
    x0=0
    y0=0
    x1=300
    y1=300
    a=150
    r=(a**2+a**2)**(1/2) 
    p=(a-r) 
    for i in range(k):
            x0+=p 
            y0+=p 
            x1-=p 
            y1-=p
            muster_ring_square.create_rectangle(x0,y0,x1,y1,width=1,outline="black", fill="pink")
            muster_ring_square.create_oval(x0,y0,x1,y1,width=1, outline="pink", fill="black")
            p=r-a
            r=r-p
            a=((r)*sqrt(2))/2
    muster_ring_square.grid()



                                                #EESTI LIPP
def f3():
    aken=Tk()      
    aken.title("EESTI LIPP")
    lipud_eesti=Canvas(aken, width=300, height=200, background="#c0c0c0")
    lipud_eesti.create_rectangle(0, 0, 300, 67, fill="blue")
    lipud_eesti.create_rectangle(0, 67, 300, 133, fill="black")
    lipud_eesti.create_rectangle(0, 133, 300, 200,fill="white")
    lipud_eesti.grid()
    lipud_eesti.grid()




                                                     #MALE
def f4():
    aken=Tk()      
    aken.title("MALE")
    male=Canvas(aken, width=200, height=200, background="#f8f8ff")
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                    color = "#f8f8ff"
            else:
                 color = "black" 
                 male.create_rectangle(j*25, i*25, (j+1)*25, (i+1)*25, fill=color)
                 male.grid()
    male.grid()



                                              #BAHAMA LIPP 

def f5():
    aken=Tk()      
    aken.title("BAHAMA LIPP")
    lipud_bahama=Canvas(aken, width=200, height=300, background="#c0c0c0")
    lipud_bahama.create_rectangle(0, 120, 200, 160, fill="#00827f")
    lipud_bahama.create_rectangle(0, 160, 200, 200, fill="#efcc00")
    lipud_bahama.create_rectangle(0, 200, 200, 240, fill="#00827f")
    lipud_bahama.create_polygon([0,120],[0,240],[100,180],fill="black")
    lipud_bahama.grid()
    lipud_bahama.grid()


                                                #OMA LIPP

def f6(): 
    aken=Tk()  
    aken.title("GERMAN LIPP")
    lipud_oma_lipp=Canvas(aken, width=300, height=200, background="#c0c0c0")
    lipud_oma_lipp.grid()
    def lipud_oma_lipp_():
        lipud_oma_lipp.delete("all")
        lipud_oma_lipp.create_rectangle(0, 0, 300, 67, fill="black")
        lipud_oma_lipp.create_rectangle(0, 67, 300, 133, fill="red")
        lipud_oma_lipp.create_rectangle(0, 133, 300, 200,fill="yellow")
        lipud_oma_lipp.grid()
    lipud_oma_lipp_()



                                                #VALGUSFOOR

def f7():
    aken=Tk()      
    aken.title("VALGUSFOOR")
    valgusfoor=Canvas(aken, width=450, height=500, background="#c0c0c0")
    valgusfoor.create_text(240, 0, text="VALGUSFOOR", font=("Impact", 20),anchor=N)
    valgusfoor.create_oval(210, 100, 260, 167,width=10,outline="black", fill="red")
    valgusfoor.create_oval(210, 167, 260, 233,width=10,outline="black", fill="yellow")
    valgusfoor.create_oval(210, 233, 260, 300,width=10,outline="black",fill="green")
    valgusfoor.create_rectangle(240, 300, 230, 367,width=1,outline="black",fill="black")
    valgusfoor.create_rectangle(180, 367, 295, 377,width=1,outline="black",fill="black")
    valgusfoor.grid()






var=IntVar()
def choice():
    figure = var.get()
    if figure == 1:
        f1()
    elif figure==2:
        f2()
    elif figure==3:
        f3()
    elif figure ==4:
        f4()
    elif figure == 5:
        f5()
    elif figure==6:
        f6()
    elif figure==7:
        f7()



figures1 = Radiobutton(aken, text="MUSTER RING", font=("Algerian 25"),variable=var, value=1, command=choice)
figures1.grid(row=3, column=5)

figures2 = Radiobutton(aken, text="MUSTER RING SQUARE", font=("Algerian 25"),variable=var, value=2, command=choice)
figures2.grid(row=4, column=5)

figures3 = Radiobutton(aken, text="EESTI LIPP", font=("Algerian 25"),variable=var, value=3, command=choice)
figures3.grid(row=5, column=5)

figures4 = Radiobutton(aken, text="MALE", font=("Algerian 25"),variable=var, value=4, command=choice)
figures4.grid(row=6, column=5) 

figures5 = Radiobutton(aken, text="BAHAMA LIPP", font=("Algerian 25"), variable=var, value=5, command=choice)
figures5.grid(row=7, column=5)

figures6 = Radiobutton(aken, text="OMA LIPP", font=("Algerian 25"),variable=var, value=6, command=choice)
figures6.grid(row=8, column=5)

figures7 = Radiobutton(aken, text="VALGUSFOOR", font=("Algerian 25"),variable=var, value=7, command=choice)
figures7.grid(row=9, column=5)

aken.mainloop() 

