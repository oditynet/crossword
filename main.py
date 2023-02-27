#Author by odity

from tkinter import *
from tkinter import filedialog

from PIL import Image

#import os

game_height=600
game_width=1100
boxsize=30
mouseX=0
mouseY=0
ws=22
ws1=11

sel=0
add_to_list_word = []

def checkstates():
    if checkstate.get() == 1:
        return 1
    else:
        return 0
def reprint():

    #xword=None
    #yword=None
    #xc=None
    #yx=None
    #pressword = ""
    print(add_to_list_word)
    canvas.delete("all")
    #N=0
    for i1,j,z,cnt in add_to_list_word:
        #N=N+1
        #print(add_to_list_word)
        i=0
        for wrd,xc,yc in z:
            if i1 == 'x':
                #for i in range(0, len(j)):

                    if i == 0:
                        #print(str(i))
                        canvas.create_rectangle(xc , yc ,xc + boxsize, yc + boxsize, width=1,fill="#FAF0E6")
                        if int(checkstate.get()) == 1:
                            canvas.create_text(xc + boxsize/2 , yc + boxsize/2, text=wrd,font=("Purisa", ws) )
                        if (int(cnt) >= 10):
                            canvas.create_text(xc + boxsize/8 , yc + boxsize/4, text=cnt,font=("Purisa", ws1) -4 )
                        else:
                            canvas.create_text(xc + boxsize / 8, yc + boxsize / 4, text=cnt, font=("Purisa", ws1))
                    else:
                        canvas.create_rectangle(xc , yc ,xc + boxsize, yc +boxsize, width=1,fill="#FFFFF0")
                        if int(checkstate.get()) == 1:
                            canvas.create_text(xc + boxsize/2 , yc + boxsize/2, text=wrd,font=("Purisa", ws) )
            if i1 == 'y':
                #for i in range(0, len(j)):
                    if i == 0:
                        #print(str(i))
                        canvas.create_rectangle(xc , yc,xc + boxsize, yc + boxsize, width=1,fill="#FAF0E6")
                        if int(checkstate.get()) == 1:
                            canvas.create_text(xc + boxsize/2, yc+boxsize/2, text=wrd,font=("Purisa", ws) )
                        if (int(cnt) >= 9):
                            canvas.create_text(xc +boxsize/8, yc+boxsize/4, text=cnt,font=("Purisa", ws1 -4 ) )
                        else:
                            canvas.create_text(xc + boxsize / 8, yc + boxsize / 4, text=cnt, font=("Purisa", ws1))
                    else:
                        canvas.create_rectangle(xc , yc,xc+ boxsize, yc + boxsize, width=1,fill="#FFFFF0")
                        if int(checkstate.get()) == 1:
                            canvas.create_text(xc +boxsize/2, yc+boxsize/2, text=wrd,font=("Purisa", ws) )
            i=i+1



def save_as_png():
    # save postscipt image

    filepath = filedialog.asksaveasfilename(title="Save files with Words")
    #canvas.postscript(file=filepath+".ps", colormode='color')
    canvas.postscript(file = filepath , colormode='color')
    # use PIL to convert to PNG
    img = Image.open(filepath)
    img.save(filepath , 'png')
    file = open(filepath+"_out.txt", 'w')
    file.write("По горизонтали:\n")
    for i, j, z, cnt in add_to_list_word:
        if i == "x":
            file.write(cnt+": "+j+"\n")
    file.write("По вертикали:\n")
    for i, j, z, cnt in add_to_list_word:
        if i == "y":
            file.write(cnt+": "+j+"\n")
    file.close()

def move_up( pos):
    if pos == 0:
        return
    text = listbox1.get(pos)
    listbox1.delete(pos)
    listbox1.insert(pos-1, text)
def openfile():
    filepath = filedialog.askopenfilename(title="открыть список слов",filetypes=(("text files","*.txt"),("all files","*.*")))
    #filepath="w.txt"
    file = open(filepath,'r')
    for i in file.readlines():
        i = i.replace("\n","")
        listbox1.insert(END,i)
    file.close()
    for i1 in range(0, listbox1.size()): #Sord list
        for i in range(0,listbox1.size()-1):
            w=listbox1.get(i)
            w1=listbox1.get(i+1)
            if (w1[0]) < (w[0]):
                move_up(i+1)

def mouse_del(event):
    canvas.scan_mark(event.x, event.y)
    mx = event.x
    my = event.y
    xword=None
    yword=None
    xc=None
    yx=None
    count = 0
    print(add_to_list_word)
    for i,j,z,cnt in add_to_list_word:
                for wrd,zx,zy in z:
                    #print(zx,zy)
                    if (mx <= zx+boxsize and mx >= zx) and (my <= zy+boxsize and my >= zy):
                        #print("word="+j)
                        #print("X|Y x:y= '"+i+"' "+str(zx)+":"+str(zy)+" - "+wrd)
                        pressword=wrd
                        xc=zx
                        yc=zy
                        add_to_list_word.pop(count)
                        listbox1.insert(END,j)
                        reprint()
                        break
                count=count+1
                        

def mouse_down(event):
    canvas.scan_mark(event.x, event.y)
    mx = event.x
    my = event.y
    #print("clicked at: ", event.x, event.y)
    xword=None
    yword=None
    xc=None
    yx=None
    pressword = ""
    if listbox1.curselection():
        word_select = listbox1.get(listbox1.curselection())
        if not add_to_list_word:
            yc = my
            xc = mx
            word = []

            for i in range(0,len(word_select)):
                if i==0:
                    canvas.create_rectangle(xc + i * boxsize, yc, xc + i * boxsize + boxsize, yc + boxsize, width=1,fill="#FAF0E6")
                    canvas.create_text(xc + i*boxsize+boxsize/2, yc+boxsize/2, text=word_select[i],font=("Purisa", ws) )
                    if (len(add_to_list_word)+1 >= 9):
                        canvas.create_text(xc + i*boxsize+boxsize/8, yc+boxsize/4, text="1",font=("Purisa", ws1-4) )
                    else:
                        canvas.create_text(xc + i * boxsize + boxsize / 8, yc + boxsize / 4,text="1", font=("Purisa", ws1))
                    #word.append([word_select[i],xc + i*boxsize ,yc])
                    word.append([word_select[i],xc + i*boxsize ,yc])
                else:
                    canvas.create_rectangle(xc + i*boxsize, yc,xc+ i*boxsize + boxsize, yc + boxsize, width=1,fill="#FFFFF0")
                    canvas.create_text(xc + i*boxsize+boxsize/2, yc+boxsize/2, text=word_select[i],font=("Purisa", ws) )
                    #word.append([word_select[i],xc + i*boxsize,yc])
                    word.append([word_select[i],xc + i*boxsize,yc])
            add_to_list_word.append(['x',word_select,word,"1"])
            #Ncount+=1
            listbox1.delete(listbox1.curselection())
        else:
            #word_select = listbox1.get(listbox1.curselection())
            #print(add_to_list_word)
            for i,j,z,cnt in add_to_list_word:
                if j == word_select:
                    break
                #countword=0
                for wrd,zx,zy in z:
                    #print(zx,zy)
                    if (mx <= zx+boxsize and mx >= zx) and (my <= zy+boxsize and my >= zy):
                        #print("word="+j)
                        #print("X|Y x:y= '"+i+"' "+str(zx)+":"+str(zy)+" - "+wrd)
                        pressword=wrd
                        xc=zx
                        yc=zy
                        if i == 'x':
                            xword='x'
                        elif i == 'y':
                            yword='y'
                    #countword=countword + 1
            #print(word_select)
           # print(pressword)
            for i1 in word_select:
                word = []
                if i1 == pressword :
                    if xword == 'x':
                        #print(add_to_list_word)
                        pressword_pos=word_select.find(pressword)
                        p=0
                        for i in range(0, len(word_select)):
                            if i == 0:
                                for i2, j2, z2,cnt in add_to_list_word:
                                    print(z2)
                                    tmp_l=0
                                    for t in z2:
                                        if tmp_l == 0:
                                            if (mx <= t[1] + boxsize and mx >= t[1]) and ( my <= t[2] + boxsize and my >=t[2]):
                                                p=1
                                                print("cnt=",cnt)
                                        tmp_l = tmp_l+1
                                canvas.create_rectangle(xc , yc - pressword_pos*boxsize + i*boxsize,xc + boxsize, yc - pressword_pos*boxsize + i*boxsize +boxsize, width=1,fill="#FAF0E6")
                                canvas.create_text(xc + boxsize/2 , yc - pressword_pos*boxsize + i*boxsize + boxsize/2, text=word_select[i],font=("Purisa", ws) )
                                if(p!=0):
                                    if (int(cnt) >= 9):
                                        canvas.create_text(xc + boxsize / 8,
                                                           yc - pressword_pos * boxsize + i * boxsize + boxsize / 4,
                                                           text=cnt , font=("Purisa", ws1 - 4))
                                    else:
                                        canvas.create_text(xc + boxsize / 8,
                                                           yc - pressword_pos * boxsize + i * boxsize + boxsize / 4,
                                                           text=cnt, font=("Purisa", ws1))
                                else:
                                    if (int(cnt) >= 9):
                                        canvas.create_text(xc + boxsize/8 , yc - pressword_pos*boxsize + i*boxsize + boxsize/4, text=str(int(cnt)+1),font=("Purisa", ws1 - 4) )
                                    else:
                                        canvas.create_text(xc + boxsize / 8,yc - pressword_pos * boxsize + i * boxsize + boxsize / 4,text=str(int(cnt)+1), font=("Purisa", ws1))
                                word.append([word_select[i],xc , yc - pressword_pos*boxsize + i*boxsize ])
                            else:
                                canvas.create_rectangle(xc , yc - pressword_pos*boxsize + i*boxsize,xc + boxsize, yc - pressword_pos*boxsize + i*boxsize +boxsize, width=1,fill="#FFFFF0")
                                canvas.create_text(xc + boxsize/2 , yc - pressword_pos*boxsize + i*boxsize + boxsize/2, text=word_select[i],font=("Purisa", ws) )
                                word.append([word_select[i],xc , yc - pressword_pos*boxsize + i*boxsize ])
                        if p!=0:
                            add_to_list_word.append(['y', word_select, word, cnt])
                        else:
                            add_to_list_word.append(['y',word_select,word,str(int(cnt)+1)])
                        listbox1.delete(listbox1.curselection())
                        xword = ''
                    if yword == 'y':
                        #print(add_to_list_word)
                        p = 0
                        pressword_pos=word_select.find(pressword)
                        for i in range(0, len(word_select)):
                            if i == 0:
                                for i2, j2, z2,cnt in add_to_list_word:
                                    #print(add_to_list_word)
                                    tmp_l=0
                                    for t in z2:
                                        if tmp_l == 0:
                                            if (mx <= t[1] + boxsize and mx >= t[1]) and ( my <= t[2] + boxsize and my >=t[2]):
                                                p=1
                                                print("cnt=",cnt)
                                        tmp_l = tmp_l+1
                                canvas.create_rectangle(xc - pressword_pos*boxsize + i*boxsize, yc,xc-pressword_pos*boxsize + i*boxsize + boxsize, yc + boxsize, width=1,fill="#FAF0E6")
                                canvas.create_text(xc - pressword_pos*boxsize + i*boxsize+boxsize/2, yc+boxsize/2, text=word_select[i],font=("Purisa", ws) )
                                if (p != 0):
                                    if (int(cnt) >= 9):
                                        canvas.create_text(xc - pressword_pos * boxsize + i * boxsize + boxsize / 8,
                                                           yc + boxsize / 4, text=cnt , font=("Purisa", ws1 - 4))
                                    else:
                                        canvas.create_text(xc - pressword_pos * boxsize + i * boxsize + boxsize / 8,
                                                           yc + boxsize / 4, text=cnt, font=("Purisa", ws1))
                                else:
                                    if (int(cnt) >= 9):
                                        canvas.create_text(xc - pressword_pos * boxsize + i * boxsize + boxsize / 8,
                                                           yc + boxsize / 4, text=str(int(cnt)+1), font=("Purisa", ws1-4))
                                    else:
                                        canvas.create_text(xc - pressword_pos*boxsize + i*boxsize+boxsize/8, yc+boxsize/4, text=str(int(cnt)+1),font=("Purisa", ws1) )
                                word.append([word_select[i],xc - pressword_pos*boxsize + i*boxsize , yc])
                            else:
                                canvas.create_rectangle(xc - pressword_pos*boxsize + i*boxsize, yc,xc-pressword_pos*boxsize + i*boxsize + boxsize, yc + boxsize, width=1,fill="#FFFFF0")
                                canvas.create_text(xc - pressword_pos*boxsize + i*boxsize+boxsize/2, yc+boxsize/2, text=word_select[i],font=("Purisa", ws) )
                                word.append([word_select[i],xc - pressword_pos*boxsize + i*boxsize , yc])
                        #add_to_list_word.append(['x',word_select,word,len(add_to_list_word)+1])
                        if p!=0:
                            add_to_list_word.append(['x', word_select, word, cnt])
                        else:
                            add_to_list_word.append(['x',word_select,word,str(int(cnt)+1)])
                        listbox1.delete(listbox1.curselection())
                        yword = ''

def searchword():
    window.title("Tk")
    for i in range(0, listbox1.index("end")):
        word=listbox1.get(i)
        wb=text2.get()

        #print(word)
        #print(wb)
        k=0
        len_word=len(word)
        len_wb=len(wb)
        if len(word) < len(wb):
            continue
        for i1 in range(0, len(word)):
            if word[i1] == wb[0] :
                k=0
                if i1+len_wb <= len_word:
                    for j in range(0,len_wb):
                        if (word[i1+j] == wb[j] and wb[j] != "*" ) or (wb[j] == "*"):
                            k=k+1
                            print(wb[j])
        if k == len_wb:
            listbox1.select_set(i)
            sel=i
            window.title( word)
            #print("Found")
            break


window = Tk()
#window.resizable(False,False)
frame1 = Frame(window)
frame2= Frame(window)
frame1.pack()
frame2.pack()
listbox1 = Listbox(frame1,bg="#f7ffde",font=("Constantia",20),width=12,exportselection=0,height=18)


buttonopenfile = Button(frame1,text="Вставить список слов",command=openfile,state=ACTIVE)
buttonsavefile = Button(frame1,text="Сохранить фотографию",command=save_as_png,state=ACTIVE)
buttonReload = Button(frame1,text="Обновить",command=reprint,state=ACTIVE)
buttonsearch = Button(frame1,text="Поиск слова",command=searchword,state=ACTIVE)

checkstate=IntVar()
checkstate.set(1)
checkbox = Checkbutton(frame1,text="Печатать буквы",onvalue=1,offvalue=0,variable=checkstate,command=checkstates)
canvas = Canvas(frame1,height=game_height,width=game_width,bg="#ffffe0")
text2 = Entry(frame1,text="Поиск подходящих слов", width=20)
text2.insert(END, "о**д")


listbox1.grid(row=0,column=0)
canvas.grid(row=0,column=1)
buttonopenfile.grid(row=1,column=0)
buttonReload.grid(row=2,column=0)
checkbox.grid(row=3,column=0)
buttonsavefile.grid(row=4,column=0)
text2.grid(row=1,column=1)
buttonsearch.grid(row=2,column=1)
canvas.bind("<ButtonPress-1>", mouse_down)
canvas.bind("<ButtonPress-3>", mouse_del)


window.update()
windows_width = window.winfo_width()
window_heigth = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_heigth = window.winfo_screenheight()

x = int((screen_width/2) - (windows_width/2))
y = int((screen_heigth/2) - (window_heigth/2))

window.geometry(f"{windows_width}x{window_heigth}+{x}+{y}")



window.mainloop()
