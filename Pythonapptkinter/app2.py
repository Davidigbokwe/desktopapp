from tkinter import *

window=Tk()

def from_kg():
    gram_conv = float(e1_value.get())*1000
    pound_conv = float(e1_value.get())*2.20462
    ounces_conv = float(e1_value.get())*35.274
    grams.delete("1.0", END)
    grams.insert(END,gram_conv)
    pounds.delete("1.0", END)
    pounds.insert(END,pound_conv)
    ounces.delete("1.0", END)
    ounces.insert(END,  ounces_conv)



kg_text = Label(window, text= "Kg")
kg_text.grid(row = 0,column = 0)

e1_value=StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row =0, column =1)

b1 = Button(window,text = "Convert", command =from_kg)
b1.grid(row = 0, column =2)

grams = Text(window, height = 1, width = 20)
grams.grid(row = 1,column = 0)

pounds = Text(window, height = 1, width = 20)
pounds.grid(row = 1,column = 1)

ounces = Text(window, height = 1, width = 20)
ounces.grid(row = 1,column = 2)



window.mainloop()
