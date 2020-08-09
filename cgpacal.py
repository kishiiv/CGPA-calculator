from tkinter import *
import tkinter
import sqlite3
cal=tkinter.Tk()
cal.geometry("780x600")
cal.title("CGPA Calculator")

#++++++++++++++++++++++++++++++++++ Database +++++++++++++++++++++++++++++++++++++++


def database():
    
    Sub1_1=s1.get()
    Sub1_2=s2.get()
    Sub1_3=s3.get()
    Sub1_4=s4.get()
    Sub1_5=s5.get()
    Sub1_6=s6.get()

    Sub1_11=s11.get()
    Sub1_12=s12.get()
    Sub1_13=s13.get()
    Sub1_14=s14.get()
    Sub1_15=s15.get()
    Sub1_16=s16.get()
    
    tgpa1=s7.get()

    conn=sqlite3.connect("CGPA Calculator.db")
    with conn:
        cursor=conn.cursor()
    conn.execute("CREATE TABLE IF NOT EXISTS Student(s1 TEXT, s2 TEXT, s3 TEXT, s4 TEXT, s5 TEXT, s6 TEXT,s11 TEXT, s12 TEXT)")
    conn.execute("INSERT INTO Student(s1,s2,s3,s4,s5,s6) Values(?,?,?,?,?,?)",(Sub1_1,Sub1_2,Sub1_3,Sub1_4,Sub1_5,Sub1_6))
    
    conn.execute("CREATE TABLE IF NOT EXISTS Student(s11 TEXT, s12 TEXT, s13 TEXT, s14 TEXT, s15 TEXT, s16 TEXT,s17 TEXT)")
    conn.execute("INSERT INTO Student(s11,s12,s13,s14,s15,s16) Values(?,?,?,?,?,?)",(Sub1_11,Sub1_12,Sub1_13,Sub1_14,Sub1_15,Sub1_16))
    
    
    
    
    conn.commit()

    
#===================================================================================================================
#Button


#&&&&&&&&&&&&&&&&&&&&&&&& SEM 1 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def Tgpa1():

    S1=s1.get()

    if S1=="O":
        C1=10*3
    elif S1=="A+":
        C1=9*3
    elif S1=="A":
        C1=8*3
    elif S1=="B+":
        C1=7*3
    elif S1=="B":
        C1=6*3
    elif S1=="C":
        C1=5*3
    elif S1=="D":
        C1=4*3
    elif S1=="E":
        C1=3*3
    elif S1=="F":
        C1=0*3    
    else:
        C1=0*3 
        
    S2=s2.get()
    if S2=="O":
        C2=10*4
    elif S2=="A+":
        C2=9*4
    elif S2=="A":
        C2=8*4
    elif S2=="B+":
        C2=7*4
    elif S2=="B":
        C2=6*4
    elif S2=="C":
        C2=5*4
    elif S2=="D":
        C2=4*4
    elif S2=="E":
        C2=3*4
    elif S2=="F":
        C2=0*4   
    else:
        C2=0*4 
        
    S3=s3.get()
    if S3=="O":
        C3=10*4
    elif S3=="A+":
        C3=9*4
    elif S3=="A":
        C3=8*4
    elif S3=="B+":
        C3=7*4
    elif S3=="B":
        C3=6*4
    elif S3=="C":
        C3=5*4
    elif S3=="D":
        C3=4*4
    elif S3=="E":
        C3=3*4
    elif S3=="F":
        C3=0*4   
    else:
        C3=0*4 

        
    S4=s4.get()

    if S4=="O":
        C4=10*3
    elif S4=="A+":
        C4=9*3
    elif S4=="A":
        C4=8*3
    elif S4=="B+":
        C4=7*3
    elif S4=="B":
        C4=6*3
    elif S4=="C":
        C4=5*3
    elif S4=="D":
        C4=4*3
    elif S4=="E":
        C4=3*3
    elif S4=="F":
        C4=0*3    
    else:
        C4=0*3 

        
    S5=s5.get()

    if S5=="O":
        C5=10*3
    elif S5=="A+":
        C5=9*3
    elif S5=="A":
        C5=8*3
    elif S5=="B+":
        C5=7*3
    elif S5=="B":
        C5=6*3
    elif S5=="C":
        C5=5*3
    elif S5=="D":
        C5=4*3
    elif S5=="E":
        C5=3*3
    elif S5=="F":
        C5=0*3    
    else:
         C5=0*3 
        
    S6=s6.get()

    if S6=="O":
        C6=10*2
    elif S6=="A+":
        C6=9*2
    elif S6=="A":
        C6=8*2
    elif S6=="B+":
        C6=7*2
    elif S6=="B":
        C6=6*2
    elif S6=="C":
        C6=5*2
    elif S6=="D":
        C6=4*2
    elif S6=="E":
        C6=3*2
    elif S6=="F":
        C6=0*2   
    else:
        C6=0*2

    #grade={"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5,"D":4,"E":0,"F":0 }

   
        
        
   
     
    T1= ((C1 + C2 + C3 + C4 + C5 + C6)/190)*10

    s7.set(T1)
    return(T1)

#&&&&&&&&&&&&&&&&&&&&&&& SEM 2 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&    

def Tgpa2():

    
    S11=s11.get()

    if S11=="O":
        C11=10*3
    elif S11=="A+":
        C11=9*3
    elif S11=="A":
        C11=8*3
    elif S11=="B+":
        C1=7*3
    elif S11=="B":
        C11=6*3
    elif S11=="C":
        C11=5*3
    elif S11=="D":
        C11=4*3
    elif S11=="E":
        C11=3*3
    elif S11=="F":
        C11=0*3    
    else:
        C11=0*3 
   
    S12=s12.get()

    if S12=="O":
        C12=10*4
    elif S12=="A+":
        C12=9*4
    elif S12=="A":
        C12=8*4
    elif S12=="B+":
        C12=7*4
    elif S12=="B":
        C12=6*4
    elif S12=="C":
        C12=5*4
    elif S12=="D":
        C12=4*4
    elif S12=="E":
        C12=3*4
    elif S12=="F":
        C12=0*4    
    else:
        C12=0*4 
    
    S13=s13.get()

    if S13=="O":
        C13=10*4
    elif S13=="A+":
        C13=9*4
    elif S13=="A":
        C13=8*4
    elif S13=="B+":
        C13=7*4
    elif S13=="B":
        C13=6*4
    elif S13=="C":
        C13=5*4
    elif S13=="D":
        C13=4*4
    elif S13=="E":
        C13=3*4
    elif S13=="F":
        C13=0*4   
    else:
        C13=0*4 
    
    S14=s14.get()

    if S14=="O":
        C14=10*3
    elif S14=="A+":
        C14=9*3
    elif S14=="A":
        C14=8*3
    elif S14=="B+":
        C14=7*3
    elif S14=="B":
        C14=6*3
    elif S14=="C":
        C14=5*3
    elif S14=="D":
        C14=4*3
    elif S14=="E":
        C14=3*3
    elif S14=="F":
        C14=0*3    
    else:
        C14=0*3 
    
    S15=s15.get()

    if S15=="O":
        C15=10*3
    elif S15=="A+":
        C15=9*3
    elif S15=="A":
        C15=8*3
    elif S15=="B+":
        C15=7*3
    elif S15=="B":
        C15=6*3
    elif S15=="C":
        C15=5*3
    elif S15=="D":
        C15=4*3
    elif S15=="E":
        C15=3*3
    elif S15=="F":
        C15=0*3    
    else:
        C15=0*3 
    
    S16=s16.get()

    if S16=="O":
        C16=10*2
    elif S16=="A+":
        C16=9*2
    elif S16=="A":
        C16=8*2
    elif S16=="B+":
        C16=7*2
    elif S16=="B":
        C16=6*2
    elif S16=="C":
        C16=5*2
    elif S16=="D":
        C16=4*2
    elif S16=="E":
        C16=3*2
    elif S16=="F":
        C16=0*2   
    else:
        C16=0*2 

    

    

    
    T2= ((C11 + C12 + C13 + C14 + C15 + C16)/190)*10

    s37.set(T2)
    return(T2)    

#&&&&&&&&&&&&&&&&&&&&& CGPA &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


def Cgpa():

    C1 = (Tgpa1() + Tgpa2()) / 2
    s41.set(C1)
    
    S41=float(s41.get())
    
    if S41>=10:
       s42.set("Extra Ordinary")
    elif S41>=9:
       s42.set("Excellent")
    elif S41>=7:
       s42.set("Good")
    elif S41>=6:
       s42.set("Average")
    elif S41>=5:
       s42.set("Do Well")
    else:
        s42.set("Re-Appear")

    


def qExit():
    cal.destroy()


def Reset():
    s1.set("")
    s2.set("")
    s3.set("")
    s4.set("")
    s5.set("")
    s6.set("")
    s7.set("")
    s11.set("")
    s12.set("")
    s13.set("")
    s14.set("")
    s15.set("")
    s16.set("")
    s21.set("")
    s22.set("")
    s23.set("")
    s24.set("")
    s25.set("")
    s26.set("")
    s31.set("")
    s32.set("")
    s33.set("")
    s34.set("")
    s35.set("")
    s36.set("")
    s37.set("")
    s41.set("")
    s42.set("")
   


#===================================================================================================================



#la1 = Label(cal, text="CGPA Calculator", width=13, font=("Bold",15))
#la1.grid(row=0,column=3)
la2 = Label(cal, text = "Semester 1", width=20, font=("Bold"))
la2.grid(row=1, column=1, sticky="w")

la3 = Label(cal, text="Grade")
la3.grid(row=2, column=4,padx=24, pady=20)
la4 = Label(cal, text="Credit")
la4.grid(row=2, column=5, padx=24, pady=20)


#-----------------------------------------------------------------------------------------------------------

#SEMESTER-1


s1 = StringVar()
s2 = StringVar()
s3 = StringVar()
s4 = StringVar()
s5 = StringVar()
s6 = StringVar()
s7 = StringVar()
s21 = StringVar()
s22 = StringVar()
s23 = StringVar()
s24 = StringVar()
s25 = StringVar()
s26 = StringVar()

l1 = tkinter.Button(cal, text="TGPA-1", padx=25, command =Tgpa1, bg="powder blue")
l1.grid(row=5, column=7)
#l1.config(command=tgpa)
e01 = tkinter.Entry(cal, textvar=s7)
e01.grid(row=5, column=8)

l1 =tkinter.Label(cal, text="Dbms")
l1.grid(row=5, column=1, sticky="w")
e1 = tkinter.Entry(cal, textvar=s1)
e1.grid(row=5, column=4)
e2 = tkinter.Entry(cal, textvar=s21)
e2.grid(row=5, column=5)
s21.set("3")

l2 = tkinter.Label(cal, text="Cod")
l2.grid(row=6, column=1, sticky="w")
e3 = tkinter.Entry(cal, textvar=s2)
e3.grid(row=6, column=4)
e4 = tkinter.Entry(cal, textvar=s22)
e4.grid(row=6, column=5)
s22.set("4")

l3 = tkinter.Label(cal, text="Dsa")
l3.grid(row=7, column=1, sticky="w")
e5 = tkinter.Entry(cal, textvar=s3)
e5.grid(row=7, column=4)
e6 = tkinter.Entry(cal, textvar=s23)
e6.grid(row=7, column=5)
s23.set("4")

l4 = tkinter.Label(cal, text="Math")
l4.grid(row=8, column=1, sticky="w")
e7 = tkinter.Entry(cal, textvar=s4)
e7.grid(row=8, column=4)
e8 = tkinter.Entry(cal, textvar=s24)
e8.grid(row=8, column=5)
s24.set("3")

l5 = tkinter.Label(cal, text="SE")
l5.grid(row=9, column=1, sticky="w")
e9 = tkinter.Entry(cal, textvar=s5)
e9.grid(row=9, column=4)
e10 = tkinter.Entry(cal, textvar=s25)
e10.grid(row=9, column=5)
s25.set("3")

l6 = tkinter.Label(cal, text="Python")
l6.grid(row=10, column=1, sticky="w")
e11 = tkinter.Entry(cal, textvar=s6)
e11.grid(row=10, column=4)
e12 = tkinter.Entry(cal, textvar=s26)
e12.grid(row=10, column=5)
s26.set("2")






#------------------------------------------------------------------------------------------------------------#

#SEMESTER-2

s11=StringVar()
s12=StringVar()
s12=StringVar()
s13=StringVar()
s14=StringVar()
s15=StringVar()
s16=StringVar()
s31=StringVar()
s32=StringVar()
s32=StringVar()
s33=StringVar()
s34=StringVar()
s35=StringVar()
s36=StringVar()
s37=StringVar()


label=tkinter.Label(cal, text = "Semester 2", width=20, font=("Bold"))
label.grid(row=15, column=1, sticky="w", pady=20)
label1=tkinter.Label(cal, text="Grade")
label1.grid(row=16, column=4, padx=20, pady=20)
label2=tkinter.Label(cal, text="Credit")
label2.grid(row=16, column=5, padx=20, pady=20)


l21 = tkinter.Button(cal, text="TGPA-2", command = Tgpa2, padx=25, bg="powder blue")
l21.grid(row=17, column=7, sticky="w")
e21 = tkinter.Entry(cal, textvar=s37)
e21.grid(row=17, column=8)

l22 = tkinter.Label(cal, text="Dbms")
l22.grid(row=17, column=1, sticky="w")
e22 = tkinter.Entry(cal, textvar=s11)
e22.grid(row=17, column=4)
e23 = tkinter.Entry(cal, textvar=s31)
e23.grid(row=17, column=5)
s31.set("3")

l23 = tkinter.Label(cal, text="Cod")
l23.grid(row=18, column=1, sticky="w")
e24 = tkinter.Entry(cal, textvar=s12)
e24.grid(row=18, column=4)
e25 = tkinter.Entry(cal, textvar=s32)
e25.grid(row=18, column=5)
s32.set("4")

l24 = tkinter.Label(cal, text="Dsa")
l24.grid(row=19, column=1, sticky="w")
e26 = tkinter.Entry(cal, textvar=s13)
e26.grid(row=19, column=4)
e27 = tkinter.Entry(cal, textvar=s33)
e27.grid(row=19, column=5)
s33.set("4")

l25 = tkinter.Label(cal, text="Math")
l25.grid(row=20, column=1, sticky="w")
e28 = tkinter.Entry(cal, textvar=s14)
e28.grid(row=20, column=4)
e29 = tkinter.Entry(cal, textvar=s34)
e29.grid(row=20, column=5)
s34.set("3")

l26 = tkinter.Label(cal, text="SE")
l26.grid(row=21, column=1, sticky="w")
e30 = tkinter.Entry(cal, textvar=s15)
e30.grid(row=21, column=4)
e31 = tkinter.Entry(cal, textvar=s35)
e31.grid(row=21, column=5)
s35.set("3")

l27 = tkinter.Label(cal, text="Python")
l27.grid(row=22, column=1, sticky="w")
e32 = tkinter.Entry(cal, textvar=s16)
e32.grid(row=22, column=4)
e33 = tkinter.Entry(cal, textvar=s36)
e33.grid(row=22, column=5)
s36.set("2")



#--------------------------------------------------------------------------------------------------------------
#CGPA & REMARKS

s41=StringVar()
s42=StringVar()


l111 = tkinter.Button(cal, text="CGPA", command = Cgpa, height=1, padx=25, bg="powder blue")
l111.grid(row=28, column=4, sticky="w")
e111 = tkinter.Entry(cal, textvar=s41)
e111.grid(row=28, column=5)

l112 = tkinter.Label(cal, text="REMARKS", padx=25, pady=25)
l112.grid(row=26, column=4, sticky="w")
e112 = tkinter.Entry(cal, textvar=s42)
e112.grid(row=26, column=5)

#==================================================  Buttons  ==================================================

#btnreset = tkinter.Button(cal, text="Exit", height=1, padx=25)
#btnreset.grid(row=29, column=7, sticky="w")
btnexit=tkinter.Button(cal,text="Exit",bg="brown",fg="white",font=("bold",15),command=database)
btnexit.grid(row=29,column=9)

btnreset=tkinter.Button(cal,text="Reset",bg="brown",fg="white",font=("bold",15),command=database)
btnreset.grid(row=29,column=0)



cal.mainloop()
