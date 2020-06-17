from tkinter import *
import math as m
root = Tk()

font = ("Verdana,20,bold")
root.title("Calculator")
root.geometry("350x400")
p1=PhotoImage(file="D:\\web dev\\calculator\\icon.png")
root.iconphoto(False,p1)
root.minsize(350,400)
root.maxsize(350,500)
root.wm_attributes('-alpha', 0.9)
root.config(bg="#404040")

#functio 
def click_event(event):
    b=event.widget
    text=b['text']
    ex=Entry1.get()
    if text=='X':
        Entry1.insert(END,'*')
        return 
    if text=='C':
        Entry1.delete(0,END) 
        return
    if text=='AC':
        Entry1.delete(0,END) 
        return    
    if text=='<--':
        ex=ex[0:len(ex)-1]
        Entry1.delete(0,END)
        Entry1.insert(0,ex)
        return
          
    if text=='=':
        try:
            ans=eval(ex)
            Entry1.delete(0,END)
            Entry1.insert(0,ans)
        except Exception as e:
            ex2 =e
            ex2 =Entry1.get()
            Entry1.delete(0,END)
            Entry1.insert(0,"Invalid syntax")  

        return 
    Entry1.insert(END,text)   
     
Entry1=Entry(root,font=font,relief=GROOVE)
Entry1.pack(side = 'top',padx=10,pady=20,fill='x',ipady=5)

Buttonframe=Frame(root)
Buttonframe.pack(side=TOP)
Buttonframe.config(bg="#404040")
temp=int(9)
for i in range(1,4):
    for j in range(1,4):
        Button1=Button(Buttonframe,text=str(temp),font=font,width=5,relief=RAISED,activebackground="Orange", activeforeground="White")
        Button1.grid(row=i,column=j,padx=2,pady=2,ipadx=5,ipady=5)
        
        temp-=1
        Button1.bind("<Button-1>",click_event)

Zerobut=Button(Buttonframe,text='0',font=font,width=5,relief=RAISED,activebackground="Orange", activeforeground="White")
Zerobut.grid(row=4,column=2,padx=2,pady=2,ipadx=5,ipady=5)  
pointbut=Button(Buttonframe,text=".",font=font,width=5,relief=RAISED,activebackground="orange", activeforeground="White")
pointbut.grid(row=4,column=3,padx=2,pady=2,ipadx=5,ipady=5)  
equalbut=Button(Buttonframe,text="=",font=font,width=5,relief=RAISED,activebackground="Orange", activeforeground="White",background="orange")
equalbut.grid(row=4,column=1,padx=2,pady=2,ipadx=5,ipady=5)       

divbut=Button(Buttonframe,text='/',font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
divbut.grid(row=1,column=4,padx=2,pady=2,ipadx=5,ipady=5)  
multiplybut=Button(Buttonframe,text="X",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
multiplybut.grid(row=2,column=4,padx=2,pady=2,ipadx=5,ipady=5)  
minusbut=Button(Buttonframe,text="-",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
minusbut.grid(row=3,column=4,padx=2,pady=2,ipadx=5,ipady=5)    
plusbut=Button(Buttonframe,text="+",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
plusbut.grid(row=4,column=4,padx=2,pady=2,ipadx=5,ipady=5)


clearbut=Button(Buttonframe,text='C',font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
clearbut.grid(row=0,column=3,padx=2,pady=2,ipadx=5,ipady=5)  
xbut=Button(Buttonframe,text="<--",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
xbut.grid(row=0,column=4,padx=2,pady=2,ipadx=5,ipady=5)  
prensetbut=Button(Buttonframe,text="%",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
prensetbut.grid(row=0,column=2,padx=2,pady=2,ipadx=5,ipady=5)    
Allclearbut=Button(Buttonframe,text="AC",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
Allclearbut.grid(row=0,column=1,padx=2,pady=2,ipadx=5,ipady=5)

#event_function:
Zerobut.bind("<Button-1>",click_event)
pointbut.bind("<Button-1>",click_event)
equalbut.bind("<Button-1>",click_event)
divbut.bind("<Button-1>",click_event)
multiplybut.bind("<Button-1>",click_event)
minusbut.bind("<Button-1>",click_event)
plusbut.bind("<Button-1>",click_event)
clearbut.bind("<Button-1>",click_event)
xbut.bind("<Button-1>",click_event)
prensetbut.bind("<Button-1>",click_event)
Allclearbut.bind("<Button-1>",click_event)
def enterClick(event):
    e=Event()
    e.widget = equalbut
    click_event(e)
root.bind('<Return>',enterClick)



#event_end:
####################################################################################################
Frame2=Frame(root)
Frame2.config(bg="#404040")
sinbut=Button(Frame2,text="sinθ",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
sinbut.grid(row=1,column=1,padx=2,pady=2,ipadx=5,ipady=5)
cosbut=Button(Frame2,text="cosθ",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
cosbut.grid(row=1,column=2,padx=2,pady=2,ipadx=5,ipady=5)
tanbut=Button(Frame2,text="tanθ",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
tanbut.grid(row=1,column=3,padx=2,pady=2,ipadx=5,ipady=5)
dtrbut=Button(Frame2,text="d->r",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
dtrbut.grid(row=1,column=4,padx=2,pady=2,ipadx=5,ipady=5)



sqrtbut=Button(Frame2,text="√",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
sqrtbut.grid(row=0,column=1,padx=2,pady=2,ipadx=5,ipady=5)
powbut=Button(Frame2,text="^",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
powbut.grid(row=0,column=2,padx=2,pady=2,ipadx=5,ipady=5)
factbut=Button(Frame2,text="x!",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
factbut.grid(row=0,column=3,padx=2,pady=2,ipadx=5,ipady=5)
radbut=Button(Frame2,text="r->d",font=font,width=5,relief=RAISED,background="orange",activebackground="Orange", activeforeground="White")
radbut.grid(row=0,column=4,padx=2,pady=2,ipadx=5,ipady=5)
#############################################################################################################################


normalcal = True
def sc_click():
    global normalcal
    if normalcal:
        Buttonframe.pack_forget()
        Frame2.pack(side=TOP)
        Buttonframe.pack(side=TOP,pady=10)
        root.geometry("350x500")
        root.title("Scientific calculator")
        normalcal=False
    else:
        Frame2.pack_forget()
        root.geometry("350x400")
        root.title("calculator")
        normalcal=True    

fontmenu=("verdana",10,"bold")
menubar=Menu(root)
mode=Menu(menubar,tearoff=0)
mode.add_checkbutton(label="Scientific Calculator",font=fontmenu,command=sc_click)
menubar.add_cascade(label="Mode",menu=mode,font=fontmenu)
root.config(menu=menubar)


##################################################################################################

def sc_calcul(event):
    b2=event.widget
    text=b2["text"]
    ex=Entry1.get()
    ans=''
    if text=='sinθ':
        ans=str(m.sin(m.radians(int(ex))))
    elif text=='cosθ':
        ans=str(m.cos(m.radians(int(ex))))
    elif text=='tanθ':
        ans=(m.tan(m.radians(int(ex))))
    elif text=='x!':
        ans=str(m.factorial(int(ex)))        
    elif text=='√' :
        ans=str(m.sqrt(float(ex)))
    elif text=='r->d':
        ans=str(m.degrees(float(ex)))
    elif text=='d->r':
        ans=str(m.radians(float(ex)))  
    elif text=='^':
        x,y=ex.split(',')
        ans=str(m.pow(int(x),int(y)))        

    Entry1.delete(0,END) 
    Entry1.insert(0,ans)


sqrtbut.bind("<Button-1>",sc_calcul)    
powbut.bind("<Button-1>",sc_calcul)
factbut.bind("<Button-1>",sc_calcul)
radbut.bind("<Button-1>",sc_calcul)
sinbut.bind("<Button-1>",sc_calcul)
cosbut.bind("<Button-1>",sc_calcul)
tanbut.bind("<Button-1>",sc_calcul)
dtrbut.bind("<Button-1>",sc_calcul)

root.mainloop()