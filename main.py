from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.iconbitmap("piz.ico")
root.title('Pizza Vending machine') 
root.geometry('600x500')
root.resizable(width=False,height=False)

my_image=ImageTk.PhotoImage(Image.open("frame.png"))
img_label=Label(image=my_image)
img_label.pack()

capsi_Var=IntVar()
onion_Var=IntVar()
olives_Var=IntVar()
corn_Var=IntVar()
jalapeno_Var=IntVar()

Checkbutton(root,variable=capsi_Var,onvalue=1,offvalue=0,command= lambda :capsi_Var.get()).place(x=245,y=122)
Checkbutton(root,variable=onion_Var,onvalue=1,offvalue=0,command= lambda :onion_Var.get()).place(x=245,y=155)
Checkbutton(root,variable=olives_Var,onvalue=1,offvalue=0,command= lambda :olives_Var.get()).place(x=245,y=188)
Checkbutton(root,variable=corn_Var,onvalue=1,offvalue=0,command= lambda :corn_Var.get()).place(x=245,y=221)
Checkbutton(root,variable=jalapeno_Var,onvalue=1,offvalue=0,command= lambda :jalapeno_Var.get()).place(x=245,y=254)


def clear(): 
    Capsicum=capsi_Var.get()
    Onion=onion_Var.get()
    Corn=corn_Var.get()
    Olives=olives_Var.get()
    Jalapenos=jalapeno_Var.get()

    capsi_Var.set(0)
    onion_Var.set(0)
    olives_Var.set(0)
    corn_Var.set(0)
    jalapeno_Var.set(0)
    bill=generate_Bill(Capsicum,Onion,Corn,Olives,Jalapenos)
    bill=str(bill)+" $"

    Label(root,text=bill).place(x=261,y=438)
   

def generate_Bill(Capsicum=0,Onion=0,Corn=0,Olives=0,Jalapeno=0):
    topping={'Capsicum': 0.25, 'Onion': 0.39, 'Corn': 0.35, 'Black Olives': 0.63, 'Jalapeno': 0.68}
    total_price=10.00


    if Capsicum==1:
        total_price=total_price+topping["Capsicum"]

    if Onion==1:
        total_price=total_price+topping["Onion"]

    if Corn==1:
        total_price=total_price+topping['Corn']

    if Olives==1:
        total_price=total_price+topping['Black Olives']

    if Jalapeno==1:
        total_price=total_price+topping['Jalapeno']

    return round(total_price,2)


Button(root,text="Generate Bill",font="Georgia 10",command=clear,padx=5,pady=4).place(x=420,y=440)

Exit_button=Button(root,text="Exit",padx=16,pady=5,command=root.quit).place(x=520,y=440)
root.mainloop()

