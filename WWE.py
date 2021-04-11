import json
from tkinter import *
from tkinter import ttk
import pprint
import random
import tkinter.messagebox
import time


root =Tk()
root.title("WWE CARDS")
root.geometry('1030x640+170+10')
root.iconbitmap("res\\images\\icon\\icon.ico")
ring = PhotoImage(file="res\\images\\ring\\ring.png")




w = ring.width()
h = ring.height()

cv = Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=ring, anchor='nw')


#create a menubar
menubar = Menu(root)
root.config(menu=menubar)

about = PhotoImage(file="res\\images\\about\\about.png")

def about_us():
    top = Toplevel()
    top.title("ABOUT")
    top.geometry("450x400+300+100")
    top.iconbitmap("res\\images\\icon\\icon.ico")
    w = about.width()
    h = about.height()
    

    aboutd = Label(top, image=about)
    aboutd.place(width=w, height=h)

    top.resizable(0,0)



submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About us", command=about_us)



intp=0
intpc=0
meturn=True
##Importing dictionaries
dictcards={}
dictresult=json.load(open('res\\data\\WrestlerData.json'))
for key in dictresult:
    dictcards[int(key)]=dictresult[key]

dictresult.clear()
for key in dictcards:
    dictcards[key]["img"]=PhotoImage(file=dictcards[key]["img"])
    dictcards[key]["stackimg"]=PhotoImage(file=dictcards[key]["stackimg"])
#global stack of players
listp=[]
listpc=[]

#pprint.pprint(dictcards)
print("***********************")
#a=random.randint(-1,3)
#print(dictcards[a]["Damage"]) 

strengthbtn = PhotoImage(file="res\\images\\buttons\\stren.png")
speedbtn = PhotoImage(file="res\\images\\buttons\\speed.png")
damagebtn = PhotoImage(file="res\\images\\buttons\\damage.png")
respectbtn = PhotoImage(file="res\\images\\buttons\\respect.png")

plywrestler = ["You got ","Welcome the ","This is "]

def card_show():
    global intp
    global intpc
    global Strength
    global Speed
    global Damage
    global Respect
    global challangestr
    global challangimm
    global challangfan

    if len(listp) == 0 or len(listpc) == 0:
        msg = tkinter.messagebox.showinfo("Shuffle","First Shuffle the cards")
    else:
        intp = listp[-1]
        intpc=listpc[-1]
        print("player got -> ",intp)
        print("Computer got -> ",intpc)
        print("Data of player card =======")
        pprint.pprint(dictcards[intp])
        print("=====================")

        plycardinfo.config(image=dictcards[intp]["img"])
        s1.config(image=dictcards[intp]["stackimg"])
        


        

        def challangestr():
            challangi("Strength")

        def challangimm():
            challangi("Speed")

        def challangfan():
            challangi("Damage")

        def challangres():
            challangi("Respect")


        Strength= Button(cv, image=strengthbtn, command=challangestr,bd=0,bg="grey",relief=FLAT)
        Strength.place(y=530, x= 750)

        Speed= Button(cv,image=speedbtn, command=challangimm,bd=0,bg="grey",relief=FLAT)
        Speed.place(y=530, x= 870)

        Damage= Button(cv,image=damagebtn ,command=challangfan,bd=0,bg="grey",relief=FLAT)
        Damage.place(y=585, x= 750)

        Respect= Button(cv, image=respectbtn, command=challangres,bd=0,bg="grey",relief=FLAT)
        Respect.place(y=585, x= 870)



def compare_Strength():
    realcheck("Strength")

def compare_Speed():
    realcheck("Speed")

def compare_Damage():
    realcheck("Damage")
    
def compare_Respect():
    realcheck("Respect")


def startalot(listmain):
    global intp
    global intpc
    mainsize=len(listmain)# mainsize is 8 now
    listp.clear()
    listpc.clear()#run
    for ele in range(0,mainsize):#this will run for 8 times
        if ele % 2== 0: #as loop is gonna run 8 times..values of ele will be 0,1,2,3,4,5,6,7..so every time the value is even it will be stored in lista else listcomp
            listp.append(listmain[ele]) #2,6,3,1 appended to lista 
        else:
            listpc.append(listmain[ele]) #4,5,7,0 appended to comp..
    #print("Player cards are=  ",lista)
    #print("Computer cards are=  ",listcomp)
    
totalcardply=StringVar()
totalcardcpu=StringVar()

def startshuffle():
    global intp
    global intpc
    size=len(dictcards)
    print(size)
    lista=[]
    for ele in range(0,size):
        lista.append(ele) #Appending numbers to the list till the size
    #print(lista)
    random.shuffle(lista)#that list is shuffled
    startalot(lista)
    stacki()
    tcard()
    

def tcard():
    totalplycards = len(listp)
    totalcpucards = len(listpc)

    totalcardply.set(f"Total cards = {totalplycards}")
    totalcardcpu.set(f"Total cards = {totalcpucards}")

textbg= PhotoImage(file="res\\images\\text\\textbg.png")

def stacki():
    global stacked
    global stackwrst
    global s1
    global sc1

    stacked.place_forget()
    sc1 = Button(cv,image=cardback, bd=0, text="card 1", bg="black",activebackground='black')
    sc1.place(y=250, x=320)  

    s1 = Button(cv,image=cardback2, text="Card 1", bd=0, bg="black",activebackground='black', command=card_show)
    s1.place(y=250, x=550)

    total_ply = Label(cv,textvariable=totalcardply, fg="white", bg="black",bd=0, font=("Times new roman", 20,"bold") ,image=textbg,compound=tkinter.CENTER)
    total_ply.place(y=78, x=760)

    total_cpu = Label(cv,textvariable=totalcardcpu, fg="white", bg="black",bd=0, font=("Times new roman", 20,"bold"),image=textbg,compound=tkinter.CENTER )
    total_cpu.place(y=78, x=40)

backcard = PhotoImage(file="res\\images\\cards\\stack.png")
backcard2 = PhotoImage(file="res\\images\\cards\\stack2.png")
cardinfo = PhotoImage(file="res\\images\\cards\\bg.png")

def forget_buttons():
    s1.place_forget()
    sc1.place_forget()
    Strength.place_forget()
    Speed.place_forget()
    Damage.place_forget()
    Respect.place_forget()

def match_comp():
    global s1
    global sc1
    global total_ply
    global total_cpu
    msg = tkinter.messagebox.showinfo("Match Ended","You Lost , Reshuffle to play again")
    listp.clear()
    listpc.clear()
    plycardinfo.config(image=cardinfo)
    cpucardinfo.config(image=cardinfo)
    forget_buttons()
    stacked.place(x=430, y=220)
    
def match_comp2():
    global s1
    global sc1
    global total_ply
    global total_cpu
    msg = tkinter.messagebox.showinfo("Match Ended","CPU Lost , Reshuffle to play again")
    listp.clear()
    listpc.clear()
    plycardinfo.config(image=cardinfo)
    cpucardinfo.config(image=cardinfo)
    forget_buttons()
    stacked.place(x=430, y=220)
    
    
def alot(): # listmain=[2,4,6,5,3,7,1,0]
    global intp
    global intpc
    if len(listp) == 0:
        match_comp()
    elif len(listpc) == 0:
        match_comp2()
    else:
        intp=listp[-1]
        intpc=listpc[-1]

pcwrestler = ["Computer got ","Beware from ","Here comes all power "]

def challangi(strpower):
    global intp
    global intpc
    global meturn
    global Strength
    global Speed
    global Damage
    global Respect
    global s1
    global cpuchose
    global compare_Strength
    global compare_Speed
    global compare_Damage
    global lista
    global listpc
    
    if meturn==True: #if it is player's turn
        if len(listp)==0 or len(listpc) == 0:
            if len(listp)==0:
                match_comp()
            elif len(listpc)==0:
                match_comp2()

        else:
            
            msg = tkinter.messagebox.showinfo("Your Turn",f"You chose {strpower} ! ")
            
            cpucardinfo.config(image=dictcards[intpc]["img"])
            sc1.config(image=dictcards[intpc]["stackimg"])
            



            if dictcards[intp][strpower]>dictcards[intpc][strpower]:
                strmsg = f"You win, as opponent {strpower} was just {str(dictcards[intpc][strpower])}"
                msg = tkinter.messagebox.showinfo("Cards",f"You win, as opponent {strpower} was just {str(dictcards[intpc][strpower])}")
           
                listp.insert(0,intpc)
                listp.insert(0,intp)
                listp.pop()
                listpc.pop()
                alot()
                meturn=True
                plycardinfo.config(image=cardinfo)
                s1.config(image=backcard2)
                cpucardinfo.config(image=cardinfo)
                sc1.config(image=backcard)
                tcard()

            
            elif dictcards[intp][strpower]<dictcards[intpc][strpower]:
                strmsg = f"You lost, as opponent {strpower} was {str(dictcards[intpc][strpower])}"
                msg = tkinter.messagebox.showinfo("Cards",f"You lost, as opponent {strpower} was {str(dictcards[intpc][strpower])}")
                
                listpc.insert(0,intp)
                listpc.insert(0,intpc)
                listp.pop()
                listpc.pop()
                alot() 
                meturn=False
                plycardinfo.config(image=cardinfo)
                s1.config(image=backcard2)

                cpucardinfo.config(image=cardinfo)
                sc1.config(image=backcard)
                tcard()
                    
            elif dictcards[intp][strpower]==dictcards[intpc][strpower]:
                strmsg = f"Your {strpower} match"
                msg = tkinter.messagebox.showinfo("Cards",f"Your {strpower} match")
               
                listp.insert(0,intp)
                listpc.insert(0,intpc)
                listp.pop()
                listpc.pop()
                alot()
                meturn=False
                plycardinfo.config(image=cardinfo)
                s1.config(image=backcard2)
                cpucardinfo.config(image=cardinfo)
                sc1.config(image=backcard)
                tcard()


            

            Strength.place_forget()
            Speed.place_forget()
            Damage.place_forget()
            Respect.place_forget()

    if meturn==False: #if it is pc turn

        if len(listp)==0 or len(listpc) == 0:
            if len(listp)==0:
                match_comp()
            elif len(listpc)==0:
                match_comp2()
        else:
            plycardinfo.config(image=cardinfo)
            s1.config(image=backcard2)
            cpucardinfo.config(image=cardinfo)
            sc1.config(image=backcard)
            tkinter.messagebox.showinfo("Turns", "Now computer will place cards")
        
            time.sleep(2)
            cpucardinfo.config(image=dictcards[intpc]["img"])
            sc1.config(image=dictcards[intpc]["stackimg"])

 

            criteria = [True,False] 
            criteria_larg = random.choice(criteria) 

            if criteria_larg == True:
                print("large done")
                if (dictcards[intpc]["Strength"] >= dictcards[intpc]["Speed"] ) and (dictcards[intpc]["Strength"]  >= dictcards[intpc]["Damage"]) and (dictcards[intpc]["Strength"]  >= dictcards[intpc]["Respect"]): #when Strength is largest
                    msg = tkinter.messagebox.showinfo("Cards","Computer Chose Strength")
             
                    cpuchose = dictcards[intpc]["Strength"]
                    s1.config(command=compare_Strength)

                elif (dictcards[intpc]["Speed"]  >= dictcards[intpc]["Strength"] ) and (dictcards[intpc]["Speed"]  >= dictcards[intpc]["Damage"]) and (dictcards[intpc]["Speed"]  >= dictcards[intpc]["Respect"]):#when Speed is largest
                    msg = tkinter.messagebox.showinfo("Cards","Computer chose Speed")
         
                    cpuchose = dictcards[intpc]["Speed"]
                    s1.config(command=compare_Speed)

                elif (dictcards[intpc]["Damage"]  >= dictcards[intpc]["Strength"] ) and (dictcards[intpc]["Damage"]  >= dictcards[intpc]["Speed"]) and (dictcards[intpc]["Damage"]  >= dictcards[intpc]["Respect"]): 
                    
                    msg = tkinter.messagebox.showinfo("Cards","Computer chose Damage")
              
                    cpuchose = dictcards[intpc]["Damage"]
                    s1.config(command=compare_Damage)

                else:
                    
                    msg = tkinter.messagebox.showinfo("Cards","Computer chose Respect")
            
                    cpuchose = dictcards[intpc]["Respect"]

                    s1.config(command=compare_Respect)

            else:# here starts the random criteria
                print("randomn done")
                stat = ["Strength","Speed","Damage","Respect"] #making a list of stats to randomly choose from
                statname= random.choice(stat)
                cpuchoice= dictcards[intpc][statname]#choosing randomnl
                msg = tkinter.messagebox.showinfo("Cards",f"Computer Chose {statname}")
                      
                
                if cpuchoice == dictcards[intpc]["Strength"]: 
                    s1.config(command=compare_Strength)

                elif cpuchoice == dictcards[intpc]["Speed"]:
                    s1.config(command=compare_Speed)
            
                elif cpuchoice == dictcards[intpc]["Damage"]:
                    s1.config(command=compare_Damage)
                else:
                    s1.config(command=compare_Respect)




def realcheck(strstat):
    global intp
    global intpc
    global meturn
    global Strength
    global Speed
    global Damage
    global s1
    global cpuchose
    global challangfan
    plycardinfo.config(image=dictcards[intp]["img"])
    s1.config(image=dictcards[intp]["stackimg"])

    if dictcards[intp][strstat]>cpuchose:
        msg = tkinter.messagebox.showinfo("Cards", f"[ {str(strstat)} ] CPU lost and You won!!!")
     
        listp.insert(0,intpc)
        listp.insert(0,intp)
        listp.pop()
        listpc.pop()
        alot()
        meturn=True
        s1.config(command=card_show)
        plycardinfo.config(image=cardinfo)
        s1.config(image=backcard2)
        cpucardinfo.config(image=cardinfo)
        sc1.config(image=backcard)
        tcard()
        
    elif dictcards[intp][strstat]<cpuchose:
        msg = tkinter.messagebox.showinfo("Cards",f"[ {str(strstat)} ] CPU won You lost !!!")
        
        listpc.insert(0,intp)
        listpc.insert(0,intpc)
        listp.pop()
        listpc.pop()
        alot()
        tcard()
        meturn=False
        challangi('#')

    else:
        msg = tkinter.messagebox.showinfo("Cards",f"[ {str(strstat)} ] This is a tie !!!")
      
        listp.insert(0,intp)
        listpc.insert(0,intpc)
        listp.pop()
        listpc.pop()
        alot()
        meturn=True
        s1.config(command=card_show)
        plycardinfo.config(image=cardinfo)
        s1.config(image=backcard2)
        cpucardinfo.config(image=cardinfo)
        sc1.config(image=backcard)
        tcard()

############### TKINTER GUI ###############

cardholder = Frame(cv, bg="black")
cardholder.config(height=80)
cardholder.pack(side=TOP, fill=X)

head = PhotoImage(file="res\\images\\head\\head.png")

title = Label(cardholder, image=head, bd=0,fg="white", bg="black", font=("Times new roman", 25))
title.place(x=400, y=0)

shuffler = Button(cardholder, text="Shuffle", font=("Times new roman", 20), command=startshuffle)
shuffler.place(y=10, x=700, height=40, width=100)

####################### STACK #####################
cardbackss = PhotoImage(file="res\\images\\cards\\stack.png")

stacked = Label(cv, image=cardbackss, bg="black")
stacked.place(x=430, y=220)

########  INFO ############
cpucardinfo = Label(cv, bg="grey1",image=cardinfo,bd=5, relief=FLAT)
cpucardinfo.place(y=120,height=400, x=20, width=250)

plycardinfo = Label(cv, bg="grey1",image=cardinfo,bd=5, relief=FLAT)
plycardinfo.place(y=120,height=400, x=735, width=250)



#### CPU #######################
cpu = Label(cv, text="CPU", fg="white", bg="black", font=("Times new roman", 20,"bold"))
cpu.place(y=180,x=330)

cardback = PhotoImage(file="res\\images\\cards\\stack.png")
#### PLAYER ######################

player = Label(cv, text="Player",  fg="white", bg="black", font=("Times new roman", 20,"bold"))
player.place(y=180,x=600)

cardback2 = PhotoImage(file="res\\images\\cards\\stack2.png")

def on_closing():
    Msg = tkinter.messagebox.askquestion ("Confirmation","Do you want to Close ? , All progress will be gone ! ",icon = 'warning')
    if Msg == 'yes':
        root.destroy()
    else:
        pass

root.protocol("WM_DELETE_WINDOW", on_closing)
root.resizable(0, 0)

root.mainloop()

