from tkinter import *

root=Tk()

root.title("Play with Strings")
root.geometry("600x600")

myFont = ("Courier",20)
Label_series = Label(root, text="fibonachi series: ")
Label_flower = Label(root)
Label_spiral = Label(root)
def fibonachi():
    
    first_number = 0
    second_number = 1
    sum = 0
    i = 0
    num = 10
    while i < num:
        i = i+1
        Label_series["text"] += str(sum) + " "
        first_number = second_number
        second_number = sum
        sum = first_number+second_number
    Label_flower["text"]="i guess the flower is blooming"
    Label_spiral["text"]="Spirals in the right direction are "+str(first_number)+" and spirals in the left direction is "+(second_number)+" total number of spirals is"+str(sum)

btn=Button(root,text="generate", command=fibonachi)
btn=Button(root,text="5", command=five)
btn=Button(root,text="10", command=ten)
btn=Button(root,text="15", command=fifteen)
def five():
    num = 5
    
def ten():
    num=10
    
def fifteen():
    num=15
    
btn.pack()
Label_series.pack()
Label_flower.pack()
Label_spiral.pack()
root.mainloop()