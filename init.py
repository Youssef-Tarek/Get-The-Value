import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox
from tkinter import ttk, Tk
import statistics

def OpenGraphicsForm():
    main.destroy()
  #  Graphics.mainloop()

def OpenNumericalForm():
    main.destroy()
    root.mainloop()

def action():
    Label1.configure(text="Enter items Here: ")
    numValues.append(float(data.get()))
    numOfValues.delete(0,END)


def mode():
    numValues.sort()
    mode = statistics.mode(numValues)
    tkinter.messagebox.showinfo('mode window', 'the mode is equal to ' + str(mode))


def mean():
    numValues.sort()
    mean = statistics.mean(numValues)
    tkinter.messagebox.showinfo('mean window', 'the mean is equal to ' + str(mean))


def median():
    numValues.sort()
    median = statistics.median(numValues)
    tkinter.messagebox.showinfo('median window', 'the median is equal to ' + str(median))


def range():
    numValues.sort()
    range = numValues[len(numValues) - 1] - numValues[0]
    tkinter.messagebox.showinfo('range window', 'the range is equal to ' + str(range))


def IQR():
    numValues.sort()
    lenth = len(numValues)
    q1 = lenth * 0.25
    q2 = lenth * 0.5
    q3 = lenth * 0.75
    median = numValues[round(q2) - 1]
    realQ1 = numValues[round(q1) - 1]
    realQ3 = numValues[round(q3) - 1]
    IQRVar = realQ3 - realQ1
    tkinter.messagebox.showinfo('IQR window', 'the IQR is equal to ' + str(IQRVar))


def Var():
    numValues.sort()
    var = statistics.variance(numValues)
    tkinter.messagebox.showinfo('Variance window', 'the variance is equal to ' + str(var))

def Z_score():
    numValues.sort()
    mean = statistics.mean(numValues)
    SD = statistics.stdev(numValues)
    i = 0
    while i < len(numValues):
        tkinter.messagebox.showinfo('Variance window', ' i :     ' + str(i))
        tkinter.messagebox.showinfo('Z-scroe window', 'Z-score for ' + str(numValues[i]) + 'is equal to ' + str(
            (numValues[i] - mean) / SD))
        i += 1


def finished():
    Label1.configure(text="select what do you need")
    Label1.place(x=100, y=20)
    MODEButto = Button(root, text="the mode", command=mode)
    fnt = ('times', 11)
    MODEButto.config(background='lightgray', foreground='black', font=fnt)
    MODEButto.place(x=300, y=120)
    meanButto = Button(root, text="the mean", command=mean)
    meanButto.config(background='lightgray', foreground='black', font=fnt)
    meanButto.place(x=300, y=160)
    medianButto = Button(root, text="the median", command=median)
    medianButto.config(background='lightgray', foreground='black', font=fnt)
    medianButto.place(x=300, y=200)
    rangeButto = Button(root, text="the range", command=range)
    rangeButto.config(background='lightgray', foreground='black', font=fnt)
    rangeButto.place(x=300, y=240)
    IQRButto = Button(root, text="the IQR", command=IQR)
    IQRButto.config(background='lightgray', foreground='black', font=fnt)
    IQRButto.place(x=300, y=280)
    VarButto = Button(root, text="the variance", command=Var)
    VarButto.config(background='lightgray', foreground='black', font=fnt)
    VarButto.place(x=300, y=320)
    ZscoreButto = Button(root, text="the z-scroe", command=Z_score)
    ZscoreButto.config(background='lightgray', foreground='black', font=fnt)
    ZscoreButto.place(x=300, y=360)


main: Tk = Tk()
main.title('Statistics Project')
main.geometry('600x400+200+50')
GraphicsButton = Button(main ,text='Graphical',command=OpenGraphicsForm)
GraphicsButton.place(x=100,y=50)
GraphicsButton.pack()
main.mainloop()

root = Tk()
root.title('Numerical')
root.geometry('600x400+200+50')
root.config(background='lightblue')
Label1 = Label(root, text="Enter item number one by one ")
fnt =('times',13)
Label1 .config(background ='lightgray' ,foreground ='black',font =fnt  )
Label1.place(x =60,y=20)

data = StringVar()
numOfValues = Entry(root, textvariable=data, width=20)
numOfValues.place(x=300,y=25)
numValues = []
num = 0

Butto = Button(root, text="save your answer", command=action)
fnt =('times',13)
Butto .config(background ='lightgray' ,foreground ='black',font =fnt  )
Butto.place(x=70,y=70)

finishButto = Button(root, text="if you finisied", command=finished)
fnt =('times',13)
finishButto .config(background ='lightgray' ,foreground ='black',font =fnt  )
finishButto.place(x=330,y=70)
finishButto= ttk.Style()

root.mainloop()

Graphics=Tk()