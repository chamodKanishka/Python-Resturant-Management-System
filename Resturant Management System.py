from tkinter import *
import random
import time
import datetime



root =Tk()
root.title("Resturant Management System")
root.configure(background="light green")

hry=Frame(root, width= 1000,height=500,relief=SUNKEN)
hry.pack(side=TOP)

frame1= Frame(root, width=800,height=100,relief=SUNKEN,bg="light green")
frame1.pack(side=LEFT)


labelinfo =Label(hry,font=('tahoma',45,'bold','italic'),text='Brooklyn Resturant',fg="dark blue",bg='yellow', anchor='w')
labelinfo.grid(row=0,column=0)
labelinfo.pack(side=LEFT,fill=Y)

def Rad():
    b=random.randint(10908,500876)
    randomRef=str(b)
    rand.set(randomRef)

    if(Cocacola.get()==""):
        coke=0
    else:
        coke=float(Cocacola.get())

    if(Burger.get()==""):
        bug=0
    else:
        bug=float(Burger.get())


    if(Spegatti.get()==""):
        spa=0
    else:
        spa=float(Spegatti.get())

    if(Pizza.get()==""):
        piz=0
    else:
        piz=float(Pizza.get())

    if(Sandwich.get()==""):
        san=0
    else:
        san=float(Sandwich.get())

    if(Macoroni.get()==""):
        mac=0
    else:
        mac=float(Macoroni.get())



    PriceofCoke=coke*50
    PriceofBug=bug*320
    PriceofSpa=spa*540
    PriceofPiz=piz*1100
    PriceofSan=san*80
    PriceofMac=mac*160

    PriceofMeal="RS",str('%.2f'%(PriceofCoke+PriceofBug+PriceofSpa+PriceofPiz+PriceofSan+PriceofMac))

    PayTax=((PriceofCoke+PriceofBug+PriceofSpa+PriceofPiz+PriceofSan+PriceofMac)*0.2)

    TotalPrice=(PriceofCoke+PriceofBug+PriceofSpa+PriceofPiz+PriceofSan+PriceofMac)

    Ser_Charge=((PriceofCoke+PriceofBug+PriceofSpa+PriceofPiz+PriceofSan+PriceofMac)/99)

    Service="Rs",str('%.2f'%Ser_Charge)

    OverAllCost = "Rs", str('%.2f'%(PayTax+TotalPrice+Ser_Charge))

    PaidTax = "Rs",str('%.2f'%PayTax)



    Service_Charge.set(Service)
    Price.set(PriceofMeal)
    Tax.set(PaidTax)
    SubTotal.set(PriceofMeal)
    Total.set(OverAllCost)

def exit():
    root.destroy()

def Reset():
    rand.set("")
    Cocacola.set("")
    Burger.set("")
    Spegatti.set("")
    Pizza.set("")
    Sandwich.set("")
    Macoroni.set("")
    Service_Charge.set("")
    Tax.set("")
    Price.set("")
    SubTotal.set("")
    Total.set("")


rand=StringVar()
Cocacola=StringVar()
Burger=StringVar()
Spegatti=StringVar()
Pizza=StringVar()
Sandwich=StringVar()
Macoroni=StringVar()
Service_Charge=StringVar()
Tax=StringVar()
Price=StringVar()
SubTotal=StringVar()
Total=StringVar()
PriceofMeal=StringVar()


lableReferenceNo=Label(frame1, font=('tahoma',14,'bold'), text='Reference No',bd=14,bg="light green")
lableReferenceNo.grid(row=0,column=0)
txtReference=Entry(frame1,font=('times new roman',14,'bold'),textvariable=rand,bd=5,insertwidth=4,bg="light gray",justify='right')
txtReference.grid(row=0,column=1)


lableCoke=Label(frame1, font=('tahoma',14,'bold'), text='Cocacola',bd=14,bg="light green")
lableCoke.grid(row=1,column=0)
txtCoke=Entry(frame1,font=('times new roman',14,'bold'),textvariable=Cocacola,bd=5,insertwidth=4,bg="light gray",justify='right')
txtCoke.grid(row=1,column=1)

lableBurger=Label(frame1, font=('tahoma',14,'bold'), text='Burger',bd=14,bg="light green")
lableBurger.grid(row=2,column=0)
txtBurger=Entry(frame1,font=('times new roman',14,'bold'),textvariable=Burger,bd=5,insertwidth=4,bg="light gray",justify='right')
txtBurger.grid(row=2,column=1)

lableSpegatti=Label(frame1, font=('tahoma',14,'bold'), text='Spegatti',bd=14,bg="light green")
lableSpegatti.grid(row=3,column=0)
txtSpegatti=Entry(frame1,font=('times new roman',14,'bold'),textvariable=Spegatti,bd=5,insertwidth=4,bg="light gray",justify='right')
txtSpegatti.grid(row=3,column=1)

lablePizza=Label(frame1, font=('tahoma',14,'bold'), text='Pizza',bd=14,bg="light green")
lablePizza.grid(row=4,column=0)
txtPizza=Entry(frame1,font=('times new roman',14,'bold'),textvariable=Pizza,bd=5,insertwidth=4,bg="light gray",justify='right')
txtPizza.grid(row=4,column=1)

lableSandwitch=Label(frame1, font=('tahoma',14,'bold'), text='Sandwitch',bd=14,bg="light green")
lableSandwitch.grid(row=5,column=0)
txtSandwitch=Entry(frame1,font=('times new roman',14,'bold'),textvariable=Sandwich,bd=5,insertwidth=4,bg="light gray",justify='right')
txtSandwitch.grid(row=5,column=1)

lableMacoroni=Label(frame1, font=('tahoma',14,'bold'), text='Macoroni',bd=14,bg="light green")
lableMacoroni.grid(row=0,column=2)
txtMacoroni=Entry(frame1,font=('times new roman',14,'bold'),textvariable=Macoroni,bd=5,insertwidth=4,bg="light gray",justify='right')
txtMacoroni.grid(row=0,column=3)

lableChickenBucket=Label(frame1, font=('tahoma',14,'bold'), text='Total Price',bd=14,bg="light green")
lableChickenBucket.grid(row=5,column=2)
txtChickenBucket=Entry(frame1,font=('times new roman',14,'bold'),textvariable=Total,bd=5,insertwidth=4,bg="light gray",justify='right')
txtChickenBucket.grid(row=5,column=3)

lableServiceCharge=Label(frame1, font=('tahoma',14,'bold'), text='Service Charge',bd=14,bg="light green")
lableServiceCharge.grid(row=2,column=2)
txtServiceCharge=Entry(frame1,font=('times new roman',14,'bold'),textvariable=Service_Charge,bd=5,insertwidth=4,bg="light gray",justify='right')
txtServiceCharge.grid(row=2,column=3)

lableTax=Label(frame1, font=('tahoma',14,'bold'), text='Tax count',bd=14,bg="light green")
lableTax.grid(row=3,column=2)
txtTax=Entry(frame1,font=('times new roman',14,'bold'),textvariable=Tax,bd=5,insertwidth=4,bg="light gray",justify='right')
txtTax.grid(row=3,column=3)

lablePriceofMeal=Label(frame1, font=('tahoma',14,'bold'), text='Price of Meal',bd=14,bg="light green")
lablePriceofMeal.grid(row=4,column=2)
txtPriceofMeal=Entry(frame1,font=('times new roman',14,'bold'),textvariable=PriceofMeal,bd=5,insertwidth=4,bg="light gray",justify='right')
txtPriceofMeal.grid(row=4,column=3)

lableSubTotal=Label(frame1, font=('tahoma',14,'bold'), text='Sub Total',bd=14,bg="light green")
lableSubTotal.grid(row=1,column=2)
txtSubTotal=Entry(frame1,font=('times new roman',14,'bold'),textvariable=SubTotal,bd=5,insertwidth=4,bg="light gray",justify='right')
txtSubTotal.grid(row=1,column=3)

btnTotal=Button(frame1,padx=6,pady=2,bd=1,fg="black",font=('tahoma',16,'bold'),width=8,text="Total",bg="blue",command=Rad).grid(row=7,column=1)

btnReset=Button(frame1,padx=6,pady=2,bd=1,fg="black",font=('tahoma',16,'bold'),width=8,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)

btnExit=Button(frame1,padx=6,pady=2,bd=1,fg="black",font=('tahoma',16,'bold'),width=8,text="Exit",bg="Red",command=exit).grid(row=7,column=3)

root.mainloop()




