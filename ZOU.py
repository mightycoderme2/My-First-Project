from pathlib import Path
import tkinter as tk
from tkinter import ttk,PhotoImage
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import csv
import wolframalpha
import wikipedia
import wolframalpha
from nltk import word_tokenize, pos_tag, ne_chunk, conlltags2tree, tree2conlltags
import  google
import wikipedia
import collections
import csv
import  google
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
from datetime import datetime
import pandas as pd
from functools import*
import random

appId = 'APER4E-58XJGHAVAK'
client = wolframalpha.Client(appId)
def new_window(): 
    import tkinter as ttk
    from PIL import Image, ImageTk
    from pathlib import Path
    win= ttk.Toplevel()
    win.geometry("500x700")
    canvas4 =ttk.Canvas(
    win,
    height = 800,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
    def new_append():  
        ds2=[]
        x9=entry_1_1.get()
        y9=entry_1_2.get()
        with open ('poya.csv','a',encoding="utf-8") as file:
            writer = csv.writer(file)
            ds2.append([x9,y9])
            for i in ds2:
                writer.writerow(i)
        entry_1_1.delete(0,END)
        entry_1_2.delete(0,END)
    canvas4.place(x = 0, y = 0)
    img_win= (Image.open("pay.png"))
    resized_image_win= img_win.resize((800,900), Image.ANTIALIAS)
    new_image_win= ImageTk.PhotoImage(resized_image_win)
    t_1_1=canvas4.create_text(170,5,anchor="nw",font="consolas 20")
    canvas4.itemconfig(t_1_1,text="Custom Response")
    canvas4.create_image(200,250,  image=new_image_win)
    t1=canvas4.create_text(170,95,anchor="nw",font="consolas 20")
    canvas4.itemconfig(t1,text="User Response:")
    t3=canvas4.create_text(150,255,anchor="nw",font="consolas 20")
    canvas4.itemconfig(t3,text="Bot Response:")
    entry_image_1_2= PhotoImage(
    file="entry_1.png")
    entry_bg_1_2 = canvas4.create_image(
    240,
    179,
    image=entry_image_1_2
    )
    entry_image_1_3= PhotoImage(
    file="entry_1.png")
    entry_bg_1_2 = canvas4.create_image(
    250,
    340,
    image=entry_image_1_3
    )
    img__1= (Image.open("button12345.png"))

    resized_image__1= img__1.resize((180,75), Image.ANTIALIAS)    
    button_image_1__1= ImageTk.PhotoImage(resized_image__1)

    entry_1_1 =ttk.Entry(
    win,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font = "Consolas 20 "
    )
    entry_1_1.place(
    x=80.0,
    y=150.0,
    width=333.0,
    height=58.0,
    )
    entry_1_2 = ttk.Entry(
    win,
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font = "Consolas 20 "
    )
    entry_1_2.place(
    x=80.0,
    y=310.0,
    width=333.0,
    height=58.0,
    )
    
    button_123 = ttk.Button(
    win,
    image=button_image_1__1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=new_append
    )
    button_123.place(
    x=180.0,
    y=500.0,
    width=150.0,
    height=47.0,
    )
    win.resizable(False,False)
    win.mainloop()
   
self_pairs= []
self_pairs1=[]
df=pd.read_csv('maindataset.csv')
a=df["Question"]
b=df["Answer"]
g=['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',':',';','<',',','>','.','?','/',"'"]
global new_image123_
l=open('jokes.txt')
x=l.readlines()
for i in x:
    self_pairs.append(['tell me a joke',i])
global new_image123
l1=open('badwords.txt')
x=l1.readlines()
for i in x:
    self_pairs.append([i,'pls dont say that ... It makes me bad'])

def func(x):
    c=""    
    try:
        for i in x:
            if(i not in g):
                c=c+i
        return c
    except TypeError:
        print("hi")
for i in range(len(a)):
    d=[]
    f=[]
    d.append(str(func(a[i])).lower())
    d.append(b[i])
    self_pairs.append(d)
def new_train():
    with open ('poya.csv','r',encoding="utf-8") as d:
        wtr = csv.reader(d)
        wtr1=[]
        for i in wtr:
            wtr1.append(i)
        if(len(wtr1)>0):
            for i in range(1,len(wtr1),2):
                d1=[]
                d1.append(str(func(wtr1[i][0])).lower())
                d1.append(wtr1[i][1])
                self_pairs1.append(d1)
     
"""
self_pairs.append(['Bye' ,'Bye.....catch you later'])
self_pairs.append(['Bye bye!' ,'Bye.....catch you later'])
self_pairs.append(['See you later', 'Bye.....catch you later'])
self_pairs.append(['See you soon ','Bye.....catch you later'])
self_pairs.append(['Talk to you later','Bye.....catch you later'])
"""
def ans(p):
    new_train()
    x=func(p)
    x1=p
    y=x.split()
    q=[]
    if('time' in y or 'date' in y):
        return str(datetime.now())
    elif('bye' in y or 'goodbye' in y):
        container.destroy()
        window.destroy()
        exit()
    for i in self_pairs1:
        count=0
        z=i[0].split()
        for j in y:
            if(j in z):
                count+=1
        try:
            if((count/len(z))==1):
                q.append([i[1],count/len(z)])
        except ZeroDivisionError:
            continue
    if(len(q)==0):
        for i in self_pairs:
            count=0
            z=i[0].split()
            for j in y:
                if(j in z):
                    count+=1
            try:
                if(count/len(z)>=1):
                    q.append([i[1],count/len(z)])
            except ZeroDivisionError:
                continue
    try:
        h=[]
        for i in q:
            h.append(i[1])
        t=max(h)
        h=[]
        for i in q:
            if((i[1]==t)and (i[0] not in h)):
                h.append(i[0])
        x1=random.choice(h)
        return x1
    except ValueError:
        question=x1
        try:
                def classify_question(question):
                    q = question.lower().split()
                    if q[0] == 'where':
                        return 'Location'
                    elif 'year'  in question:
                        return 'Date'
                    elif 'country' in question:
                        return 'Country'
                    elif q[0] == 'who':
                        return 'Definition'
                    elif q[0] == 'what':
                        return 'Definition'
                    else:

                        return 'None'


                def google_search(question):
                    first_page = google.search(question,1)
                    top_three_result = []
                    i = 0
                    while i<5:
                        top_three_result.append(first_page[i].description)
                        i+=1

                    first_search = ''.join(top_three_result).encode('ascii','replace')
                    ne_tree = (ne_chunk(pos_tag(word_tokenize(first_search))))
                    iob_tagged = tree2conlltags(ne_tree)
                    ss = [tuple(map(str,eachTuple)) for eachTuple in iob_tagged]
                    question_type = classify_question(question)
  
                    if question_type == 'None':
                        ans = "Oops! I don't know."
                    else:
                        google_answer = []
                        if question_type == 'Person':
                            for i in range(len(ss)):
                                if ss[i][2] == 'B-PERSON'or ss[i][2] == 'I-PERSON':
                                    google_answer.append(ss[i][0])
                        elif question_type == 'Country':
      
                            for i in range(len(ss)):
                                if ss[i][2] == 'B-GPE'or ss[i][2] == 'I-GPE':
                                    google_answer.append(ss[i][0])
                        elif question_type == 'Location':
                            for i in range(len(ss)):
                                if ss[i][2] == 'B-LOCATION'or ss[i][2] == 'I-LOCATION':
                                    google_answer.append(ss[i][0])
                        elif question_type == 'Date':
                            for i in range(len(ss)):
                                if ss[i][2] == 'B-DATE'or ss[i][2] == 'I-DATE':
                                    google_answer.append(ss[i][0])
       
                        if not google_answer:
                            ans = "Oops, I don't know! "
                        else:
            
                            counts = collections.Counter(google_answer)
            
                            t = counts.most_common(4)
                            candidate_answer =  [ seq[0] for seq in t ]

                            for i in range(len(candidate_answer)):
                                candidate_answer[i] = 'Candidate Answer '+ str(i+1)+' '+ candidate_answer[i]
                                candidate_answer = '\n'.join(candidate_answer)
                                ans = candidate_answer
                    return ans
##################################################################################

                def wiki_search(question):
                    l = question.split(' ')
                    if len(l) > 2:
                        ques = " ".join(l[2:])
                    try:
      
                        ans = (wikipedia.summary(question, sentences=1))
                    except:
    
                        google_search(question)
                    return ans


                try:
                    app_id ='APER4E-58XJGHAVAK'   
                    client = wolframalpha.Client(app_id)
                    res = client.query(question)
                    ans = str(next(res.results).text).replace('.', '.\n')
                    if ans == 'None':

                        q_type = classify_question(question)
                    if q_type == 'Definition' or q_type == 'Location':
            
                        ans = wiki_search(question)
                    else:
               
                        ans = google_search(question)
          
                    return ans

                except:
                        try:
         
                            q_type = classify_question(question)
                            if q_type == 'Definition' or q_type == 'Location':
        
                                ans = wiki_search(question)
                            else:
                                ans = google_search(question)
    
                            return ans
                        except:
                            return "Oops! I don't know. Try something else"
        except:
            return "connect to the internet"

window212 = Tk()

window212.geometry("783x500")

def des():
    window212.destroy()

    
canvas = Canvas(
    window212,
    height = 500,
    width = 783,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
img= (Image.open("31.png"))
resized_image= img.resize((783,500), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
canvas.create_image(390,250,  image=new_image)

button_image_1 = PhotoImage(
    file="button_1.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=des,
    relief="flat"
)
button_1.place(
    x=220.0,
    y=400.0,
    width=343.0,
    height=52.0
)

text_1=canvas.create_text(150,130,anchor = "nw" )
canvas.itemconfig(text_1,text="-Created By S.S.Nitin Hariharan(1st year)",font="Consolas 20 ")
window212.resizable(False, False)
window212.mainloop()      
window = Tk()

window.geometry("500x700")

canvas = Canvas(
    
    window,
    height = 800,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

global i1
canvas.place(x = 0, y = 0)
img= (Image.open("pay.png"))
resized_image= img.resize((700,1000), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)


img1_= (Image.open('poya1.png'))
resized_image123_= img1_.resize((700,1000), Image.ANTIALIAS)
new_image123_= ImageTk.PhotoImage(resized_image123_)    
x=canvas.create_image(200,250,  image=new_image)
j=60

img= (Image.open("button123.png"))

resized_image= img.resize((180,75), Image.ANTIALIAS)
button_image_1= ImageTk.PhotoImage(resized_image)

img_4= (Image.open("clearcat.png"))

resized_image_4= img_4.resize((180,75), Image.ANTIALIAS)
button_image_2= ImageTk.PhotoImage(resized_image_4)




    
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=new_window
)
button_1.place(
    x=17.0,
    y=13.0,
    width=150.0,
    height=47.0
)

        
        
entry_image_1= (Image.open('entry_1.png'))
resized_image_1_2= entry_image_1.resize((450,59), Image.ANTIALIAS)
new_image_1_2= ImageTk.PhotoImage(resized_image_1_2)

entry_bg_1 = canvas.create_image(
    250,
    638.0,
    image=new_image_1_2
)


container = Frame(window,width=500,height=500)
container.grid(pady=80,padx=10)

    
canvas2 = Canvas(
    container,
    height = 500,
    width = 475,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",

)
canvas2.grid(pady=0,padx=0)
def new_canvas():
    canvas2 = tk.Canvas(
    container,
    height = 500,
    width =475,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",

    )
    canvas2.grid(pady=0,padx=0)
    canvas_2_elements()
    global tx
    global tt
    global ay
    global mn
    global ay1
    global tt1
    tx=500
    tt=750
    ay=1
    mn=2
    ay1=1
    tt1=1

global ay1
def canvas_2_elements():
    canvas2.yview_scroll(-1, "units")
    img123= (Image.open('pay.png'))
    resized_image123= img123.resize((500,500), Image.ANTIALIAS)
    global new_image123
    global i1
    new_image123= ImageTk.PhotoImage(resized_image123)
    canvas2.create_image(250,250,  image=new_image123)
    i1 = canvas2.create_rectangle(0,0,490,500, tags='rect')
    canvas2.configure(scrollregion = canvas2.bbox('rect'))
    text_canvas = canvas2.create_text(5,30, anchor = "nw",font = "Consolas 18 ")
    canvas2.itemconfig(text_canvas, text="Hi my name is ZoU-Bot")
    global j
    j=60
    

tx=500
tt=750
ay=1
mn=2
ay1=1
zxzx=1
zxzxy=1
global lee
def print_old_chats():
    global nit
    global new_image123
    global o
    global lee
    global ay1
    global zxzx
    tt=750
    dd=pd.read_csv('innovators.csv')
    a=dd['User']
    b=dd['Bot']
    lee=1
    for o in range(len(a)):
        if((a[o]=='' and b[o]=='') or (a[o]=='User' and b[o]=='Bot')):
            continue
        else:
            msg=a[o]
            ncount=0
            n1count=0
            global j
            bot=str(b[o])
            aasd=""
            xz=str(msg).split()
            mad=[]
            global ay1
            global zxzxy
            for i in range(len(xz)):
                if(i%3==0 and (i!=0 and i!=1 and i!=2)):
                    mad.append(aasd)
                    aasd=""
                aasd=aasd+xz[i]+" "
            mad.append(aasd)
            if(zxzxy==1):
                i1 = canvas2.create_rectangle(0,0,490,500, tags='rect')
                canvas2.configure(scrollregion = canvas2.bbox('rect'))
                zxzx=zxzx+1
            for i44 in mad:
                try:
                    i1234=len(i44)
                except TypeError:
                    continue
                i1234=i1234*13
                text_canvas = canvas2.create_text(460-i1234, j, anchor = "nw",font = "Consolas 18 ")
                ty=j
                canvas2.itemconfig(text_canvas,text=i44)
                if((ty/(tx*ay1)>=0.95)):
                    canvas2.create_image(250,tt,image=new_image123)
                    canvas2.delete(i1)
                    tt=tt+500
                    lee=lee+1
                    ay1=ay1+1
                    i1 = canvas2.create_rectangle(0,0,490,tt-250, tags='rect')
                    canvas2.configure(scrollregion = canvas2.bbox('rect'))
                    canvas2.bind(canvas2.yview_scroll(9, "units"))
                    j=j+60
                    canvas2.delete(text_canvas)
                    text_canvas = canvas2.create_text(460-i1234, j, anchor = "nw",font = "Consolas 18 ")
                    canvas2.itemconfig(text_canvas, text = i44)
                j=j+30
            j=j+30
            xz=[]
            xz=bot.split()
            aasd1=""
            k=1
            mad=[]
            global nx
            for i in range(len(xz)):
                if(i%3==0 and (i!=0 and i!=1 and i!=2)):
                    mad.append(aasd1)
                    aasd1=""
                aasd1=aasd1+xz[i]+" "
            mad.append(aasd1) 

            if(zxzx==1):
                i1 = canvas2.create_rectangle(0,0,490,500, tags='rect')
                canvas2.configure(scrollregion = canvas2.bbox('rect'))
                zxzx=zxzx+1
            for i44 in mad:
                text_canvas = canvas2.create_text(5, j, anchor = "nw",font = "Consolas 18 ")
                ty=j
                canvas2.itemconfig(text_canvas,text=i44)
                if((ty/(tx*ay1)>=0.95)):
                    canvas2.create_image(250,tt,image=new_image123)
                    canvas2.delete(i1)
                    tt=tt+500
                    lee=lee+1
                    ay1=ay1+1
                    i1 = canvas2.create_rectangle(0,0,490,tt-250, tags='rect')
                    canvas2.configure(scrollregion = canvas2.bbox('rect'))
                    canvas2.bind(canvas2.yview_scroll(9, "units"))
                    j=j+60
                    canvas2.delete(text_canvas)
                    text_canvas = canvas2.create_text(5, j, anchor = "nw",font = "Consolas 18 ")
                    canvas2.itemconfig(text_canvas, text = i44)
                j=j+30
        
    canvas2.bind(canvas2.yview_scroll(10000*lee, "units"))
                    
                                                                                                                                        
def clear_chat():
    global new_image123
    global container
    f = open("innovators.csv", "w")
    f.truncate()
    f.close()
    with open ('innovators.csv','a',encoding="utf-8") as f:
        wtr = csv.writer(f)
        wtr.writerow(['User','Bot'])
    global j
    canvas2.bind(canvas2.yview_scroll(mn*10000*(-1), "units"))  
    canvas2.delete('all')
    container = ttk.Frame(window,width=500,height=500)
    container.grid(pady=80,padx=10)
    global img
    new_canvas()
    j=10


button_2 = Button(window,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=clear_chat
)
button_2.place(
    x=337.0,
    y=13.0,
    width=150.0,
    height=47.0
)     

img123= (Image.open('pay.png'))
resized_image123= img123.resize((500,500), Image.ANTIALIAS)
new_image123= ImageTk.PhotoImage(resized_image123)
canvas2.create_image(250,250,  image=new_image123)
img123_123= (Image.open('zou8.png'))
resized_image123_123= img123_123.resize((150,45), Image.ANTIALIAS)
new_image123_123= ImageTk.PhotoImage(resized_image123_123)
canvas.create_image(250,38,  image=new_image123_123)
x=canvas2.create_image(250,750,  image=new_image123)
tt1=1

def down(event):
    canvas2.focus_force()
    canvas2.yview_scroll(1, "units")
def up(event):
    canvas2.focus_force()
    canvas2.yview_scroll(-1, "units")
print_old_chats()
tt=(500*lee)+250

def _on_enter_pressed(event):
    global tt1
    global ay1
    global tt
    ds2=[]
    tt1=1
    global new_image123
    msg =str(entry_1.get())  
    ds=msg  
    ncount=0
    n1count=0
    entry_1.delete(0, END)
    global j
    j=j+30
    bot=str(ans(msg)) 
    ds1=bot
    aasd=""
    xz=msg.split()
    mad=[]
    k1=1
    global ty
    for i in range(len(xz)):
        if(i%3==0 and (i!=0 and i!=1 and i!=2)):
            mad.append(aasd)
            k1=k1+1
            aasd=""
        aasd=aasd+xz[i]+" "
    mad.append(aasd)
    for i123 in mad:
            i56=len(i123)
            i56=i56*13
            text_canvas = canvas2.create_text(460-i56, j, anchor = "nw",font = "Consolas 18 ")
            canvas2.itemconfig(text_canvas, text=i123)
            ty=j
            global i1
            global ay 
            if((ty/(tx*ay1)>=0.95)):
                canvas2.create_image(250,tt,image=new_image123)
                ay1=ay1+1
                canvas2.delete(i1)
                tt=tt+500
                i1 = canvas2.create_rectangle(0,0,490,tt-250, tags='rect')
                canvas2.configure(scrollregion = canvas2.bbox('rect'))
                canvas2.bind(canvas2.yview_scroll(10, "units"))
                j=j+60
                canvas2.delete(text_canvas)
                text_canvas = canvas2.create_text(460-i56, j, anchor = "nw",font = "Consolas 18 ")
                canvas2.itemconfig(text_canvas,text=i123)
            j=j+30
    xz=[]
    xz=bot.split()
    aasd1=""
    k=1
    ds2.append([ds, ds1])
    with open('innovators.csv', 'a', encoding="utf-8") as file:
        writer = csv.writer(file)
        for i in ds2:
            writer.writerow(i)
    mad=[]
    global nx
    for i in range(len(xz)):
        if(i%3==0 and (i!=0 and i!=1 and i!=2)):
            mad.append(aasd1)
            aasd1=""
        aasd1=aasd1+xz[i]+" "
    mad.append(aasd1) 
    container.focus_force()
    canvas2.bind("<Up>", up)
    canvas2.bind("<Down>", down)
    entry_1.focus_force()
    for i44 in mad:
        text_canvas = canvas2.create_text(5, j, anchor = "nw",font = "Consolas 18 ")
        ty=j
        canvas2.itemconfig(text_canvas,text=i44)
        if((ty/(tx*ay1)>=0.95)):
            canvas2.create_image(250,tt,image=new_image123)
            canvas2.delete(i1)
            tt=tt+500
            tt1=2
            ay1=ay1+1
            i1 = canvas2.create_rectangle(0,0,490,tt-250, tags='rect')
            canvas2.configure(scrollregion = canvas2.bbox('rect'))
            canvas2.bind(canvas2.yview_scroll(10, "units"))
            j=j+60
            canvas2.delete(text_canvas)
            text_canvas = canvas2.create_text(5, j, anchor = "nw",font = "Consolas 18 ")
            canvas2.itemconfig(text_canvas, text = i44)
        j=j+30
    

i1 = canvas2.create_rectangle(0,0,490,500, tags='rect')
canvas2.configure(scrollregion = canvas2.bbox('rect'))   
text_canvas = canvas2.create_text(5,30, anchor = "nw",font = "Consolas 18 ")
canvas2.itemconfig(text_canvas, text="Hi my name is ZoU-Bot")
   
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    font = "Consolas 20  "
)
entry_1.place(
    x=31.0,
    y=610.0,
    width=413.0,
    height=58.0,
)

canvas2.focus_force()
canvas2.bind("<Button-3>", up)
canvas2.bind("<Up>", up)
canvas2.bind("<Down>", down)
canvas2.bind("<Button-1>",down)
canvas.bind("<Button-1>",down)
entry_1.bind("<Return>",_on_enter_pressed)
window.resizable(False,False)
window.mainloop()
