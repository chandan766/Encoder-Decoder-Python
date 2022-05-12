from tkinter import *
from tkinter import ttk,messagebox
from encode_decode import *
import pyperclip as py
import string as st

def check_bin(a):
    p = set(a)
    s = {'0','1'}
    if s == p or p == {'0'} or p == {'1'}:
        return True
    else:
        return False
def check_oct(a):
    p = set(a)
    r = list(p)
    n = 0
    s = ['0','1','2','3','4','5','6','7']
    for i in range(0,len(r)):
        if r[i] in s:
            n = n+1
        else:
            n=0
    if n == len(r):
        return True
    else:
        return False

def btn_click(a):
    if a == "copy1":
        txt1_copy = txt_lbl1.get(1.0,"end-1c")
        py.copy(txt1_copy)
    elif a == "copy2":
        txt2_copy = txt_lbl2.get(1.0,"end-1c")
        py.copy(txt2_copy)
    elif a == "delete1":
        txt_lbl1.delete(1.0,END)
    elif a == "delete2":
        txt_lbl2.delete(1.0,END)
def frame_bind(e):
    global flag
    if str(e.widget) == ".!labelframe.!text":
        flag=0
    else:
        flag=1
    copy_btn1['text']="Copy"
    copy_btn1['bg']="#125ace"
    copy_btn2['text']="Copy"
    copy_btn2['bg']="#125ace"

def clear_all():
    btn_click("delete1")
    btn_click("delete2")
def click_copy1(e):
    win.focus()
    frame_bind(e)
    copy_btn1['text']="Copied!"
    copy_btn1['bg']="orange"
    win.after(2000,frame_bind,e)
def click_copy2(e):
    win.focus()
    frame_bind(e)
    copy_btn2['text']="Copied!"
    copy_btn2['bg']="orange"
    win.after(2000,frame_bind,e)

def click_option(e):
    global flag
    opt = option.get()
    if flag==0:
        encode()
    else:
        decode()
    return opt

def about():
    messagebox.showinfo("About","Hi,\nI am Chandan Maurya.I am a student of B.Tech(Cs).\nCurrently I working on python gui and many projects on it.\nIf you have interest to do some projects with me,mail me on\ncr3992@gmail.com")

def click_mail(e):
    about()
 
def encode():
    txt_lbl1.focus()
    opt = option.get()
    txt_lbl2.delete(1.0,END)
    txt = txt_lbl1.get(1.0,"end-1c")
    if txt == "":
        pass
    if opt == "Ascii":
            rslt=""
            for i in range(0, len(txt)):
                rslt = rslt+str(ord(txt[i]))+" "
            txt_lbl2.insert(END,rslt)
    elif opt == "Binary":
            if txt.isdigit()==True:
                rslt = str(bin(int(txt))).replace("0b","")
                txt_lbl2.insert(END,rslt+" ")
            else:
                for i in range(0,len(txt)):
                    rslt = str(bin(ord(txt[i]))).replace("0b","")
                    txt_lbl2.insert(END,rslt+" ")
    elif opt == "Hex":
            if txt.isdigit()==True:
                rslt = str(hex(int(txt))).replace("0x","")
                txt_lbl2.insert(END,rslt+" ")
            else:
                for i in range(0,len(txt)):
                    rslt = str(hex(ord(txt[i]))).replace("0x","")
                    txt_lbl2.insert(END,rslt+" ")
    elif opt == "Octal":
            if txt.isdigit()==True:
                rslt = str(oct(int(txt))).replace("0o","")
                txt_lbl2.insert(END,rslt+" ")
            else:
                for i in range(0,len(txt)):
                    rslt = str(oct(ord(txt[i]))).replace("0o","")
                    txt_lbl2.insert(END,rslt+" ")
    elif opt == "Reverse":
            rslt = ""
            for i in range(len(txt)-1,-1,-1):
                rslt = rslt+txt[i]
            txt_lbl2.insert(END,rslt)
    elif opt == "Upper case":
            rslt = txt.upper()
            txt_lbl2.insert(END,rslt)
    elif opt == "Lower case":
            rslt = txt.lower()
            txt_lbl2.insert(END,rslt)
    elif opt == "ROT-13":
            rslt = rot(txt)
            txt_lbl2.insert(END,rslt)
    elif opt == "Encode-6":
        if txt=="":
            pass 
        else:
            rslt = getEncode(txt)
            txt_lbl2.insert(END,rslt)

def decode():
    txt_lbl2.focus()
    opt = option.get()
    txt_lbl1.delete(1.0,END)
    txt = txt_lbl2.get(1.0,"end-1c")
    if txt == "":
        pass
    if opt == "Ascii":
            rslt=""
            store1 = txt
            rslt = rslt+str(chr(int(txt)))  
            txt_lbl1.insert(END,rslt+" ")
    elif opt == "Binary":
            if check_bin(txt)==True:
                rslt = str(int(txt,2))
            else:
                rslt = txt
            txt_lbl1.insert(END,rslt)
    elif opt == "Hex":
            if all(c in st.hexdigits for c in txt)==True:
                rslt = str(int(txt,16))
            else:
                rslt = txt
            txt_lbl1.insert(END,rslt)
    elif opt == "Octal":
            if check_oct(txt)==True:
                rslt = str(int(txt,8))
            else:
                rslt = txt
            txt_lbl1.insert(END,rslt)
    elif opt == "Reverse":
            rslt = ""
            for i in range(len(txt)-1,-1,-1):
                rslt = rslt+txt[i]
            txt_lbl1.insert(END,rslt)
    elif opt == "Upper case":
            rslt = txt.upper()
            txt_lbl1.insert(END,rslt)
    elif opt == "Lower case":
            rslt = txt.lower()
            txt_lbl1.insert(END,rslt)
    elif opt == "ROT-13":
            rslt = rot(txt)
            txt_lbl1.insert(END,rslt)
    elif opt == "Encode-6":
        if txt=="":
            pass 
        else:
            rslt = getDecode(txt)
            txt_lbl1.insert(END,rslt)
    

win = Tk()
option = StringVar()
rslt = ""
flag = 0
win.title("Encoder Decoder")
win.geometry("500x540+500+150")
win.config(bg="#ecc6a7",highlightbackground="yellow",highlightthickness=3)
lbl = Label(win,text="Encoder Decoder",font=("arial",20,"bold"),bg="yellow",fg="blue")
lbl.place(x=80,y=10)
lbl_frame1 = LabelFrame(win,text="Encode",bg="#a7d5ec")
lbl_frame1.place(x=10,y=70,width=400,height=150)
lbl_frame1.bind("<Button-1>",frame_bind)
txt_lbl1 = Text(lbl_frame1,font=("arial",10,"bold"),relief=RIDGE,bd=2,wrap=WORD)
txt_lbl1.place(x=0,y=0,width=380,height=131)
txt_lbl1.bind("<Button-1>",frame_bind)
txt_lbl1.focus()
scrollb = Scrollbar(lbl_frame1,command=txt_lbl1.yview,bg="lightgray")
scrollb.place(x=380,y=1,height=128,width=15)
txt_lbl1['yscrollcommand']=scrollb.set
copy_btn1 = Button(win,text="Copy",font=("arial",8,"bold"),bg="#125ace",fg="white",relief=GROOVE,command= lambda : btn_click("copy1"))
copy_btn1.place(x=430,y=90)
copy_btn1.bind("<Button-1>",click_copy1)
delete_btn1 = Button(win,text="X",font=("arial",8,"bold"),bg="#125ace",fg="white",relief=GROOVE,command= lambda : btn_click("delete1"))
delete_btn1.place(x=430,y=140,width=30)

encode_btn = Button(win,text="Encode",font=("arial",10,"bold"),bg="#69ff52",fg="white",command=encode)
encode_btn.place(x=12,y=250)
encode_btn = Button(win,text="Clear",font=("arial",10,"bold"),bg="#125ace",fg="white",command=clear_all)
encode_btn.place(x=130,y=250)
option_lbl= ttk.Combobox(win,textvariable=option,font=("Times New Roman",15),state='readonly',justify=CENTER)
option_lbl['values']=('Ascii','Binary','Hex','Octal','Reverse','Upper case','Lower case','ROT-13','Encode-6')
option_lbl.place(x=260,y=250,width=150)
option.set("Ascii")
option_lbl.bind("<<ComboboxSelected>>",click_option)

lbl_frame2 = LabelFrame(win,text="Decode",bg="#a7d5ec")
lbl_frame2.place(x=10,y=310,width=400,height=150)
lbl_frame2.bind("<Button-1>",frame_bind)
txt_lbl2 = Text(lbl_frame2,bd=2,relief=RIDGE,font=("arial",10,"bold"),wrap=WORD)
txt_lbl2.place(x=0,y=0,width=380,height=131)
txt_lbl2.bind("<Button-1>",frame_bind)
scrollb = Scrollbar(lbl_frame2,command=txt_lbl2.yview,bg="lightgray")
scrollb.place(x=380,y=1,height=128,width=15)
txt_lbl2['yscrollcommand']=scrollb.set
copy_btn2 = Button(win,text="Copy",font=("arial",8,"bold"),bg="#125ace",fg="white",relief=GROOVE,command= lambda : btn_click("copy2"))
copy_btn2.place(x=430,y=330)
copy_btn2.bind("<Button-1>",click_copy2)
delete_btn2 = Button(win,text="X",font=("arial",8,"bold"),bg="#125ace",fg="white",relief=GROOVE,command= lambda : btn_click("delete2"))
delete_btn2.place(x=430,y=380,width=30)

decode_btn = Button(win,text="Decode",font=("arial",10,"bold"),bg="#ff6652",fg="white",command=decode)
decode_btn.place(x=12,y=480)

about_btn = Button(win,text="About",font=("arial",10,"bold"),bg="#ecc6a7",fg="red",bd=0,command=about)
about_btn.place(x=430,y=15)
lbl1 = Label(win,text="cr3992@gmail.com",font=("arial",8,"italic"),bg="#ecc6a7",fg="black")
lbl1.place(x=380,y=490)
lbl1.bind("<Button-1>",click_mail)
win.mainloop()