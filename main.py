from tkinter import *
from tkinter import filedialog

from PIL import Image

#import os

game_height=800
game_width=900
boxsize=50
mouseX=0
mouseY=0
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
    canvas.delete("all")
    N=0
    for i1,j,z in add_to_list_word:
        N=N+1
        #print(add_to_list_word)
        i=0
        for wrd,xc,yc in z:
            if i1 == 'x':
                #for i in range(0, len(j)):

                    if i == 0:
                        #print(str(i))
                        canvas.create_rectangle(xc , yc ,xc + boxsize, yc + boxsize, width=1,fill="#FAF0E6")
                        if int(checkstate.get()) == 1:
                            canvas.create_text(xc + boxsize/2 , yc + boxsize/2, text=wrd,font=("Purisa", 36) )
                        canvas.create_text(xc + boxsize/8 , yc + boxsize/4, text=str(N),font=("Purisa", 14) )
                    else:
                        canvas.create_rectangle(xc , yc ,xc + boxsize, yc +boxsize, width=1)
                        if int(checkstate.get()) == 1:
                            canvas.create_text(xc + boxsize/2 , yc + boxsize/2, text=wrd,font=("Purisa", 36) )
            if i1 == 'y':
                #for i in range(0, len(j)):
                    if i == 0:
                        #print(str(i))
                        canvas.create_rectangle(xc , yc,xc + boxsize, yc + boxsize, width=1,fill="#FAF0E6")
                        if int(checkstate.get()) == 1:
                            canvas.create_text(xc + boxsize/2, yc+boxsize/2, text=wrd,font=("Purisa", 36) )
                        canvas.create_text(xc +boxsize/8, yc+boxsize/4, text=str(N),font=("Purisa", 14) )
                    else:
                        canvas.create_rectangle(xc , yc,xc+ boxsize, yc + boxsize, width=1)
                        if int(checkstate.get()) == 1:
                            canvas.create_text(xc +boxsize/2, yc+boxsize/2, text=wrd,font=("Purisa", 36) )
            i=i+1



def save_as_png():
    # save postscipt image

    filepath = filedialog.asksaveasfilename(title="Save files with Words")
    #canvas.postscript(file=filepath+".ps", colormode='color')
    canvas.postscript(file = filepath , colormode='color')
    # use PIL to convert to PNG
    img = Image.open(filepath)
    img.save(filepath + '.png', 'png')

def openfile():
    filepath = filedialog.askopenfilename(title="открыть список слов",filetypes=(("text files","*.txt"),("all files","*.*")))
    file = open(filepath,'r')
    for i in file.readlines():
        i = i.replace("\n","")
        listbox1.insert(END,i)
    file.close()

    #return filepath

def mouse_down(event):
    canvas.scan_mark(event.x, event.y)
    mx = event.x
    my = event.y
    print("clicked at: ", event.x, event.y)
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
                    canvas.create_text(xc + i*boxsize+boxsize/2, yc+boxsize/2, text=word_select[i],font=("Purisa", 36) )
                    canvas.create_text(xc + i*boxsize+boxsize/8, yc+boxsize/4, text=str(len(add_to_list_word)+1),font=("Purisa", 14) )
                    #word.append([word_select[i],xc + i*boxsize ,yc])
                    word.append([word_select[i],xc + i*boxsize ,yc])
                else:
                    canvas.create_rectangle(xc + i*boxsize, yc,xc+ i*boxsize + boxsize, yc + boxsize, width=1)
                    canvas.create_text(xc + i*boxsize+boxsize/2, yc+boxsize/2, text=word_select[i],font=("Purisa", 36) )
                    #word.append([word_select[i],xc + i*boxsize,yc])
                    word.append([word_select[i],xc + i*boxsize,yc])
            add_to_list_word.append(['x',word_select,word])
            #Ncount+=1
            listbox1.delete(listbox1.curselection())
        else:
            #word_select = listbox1.get(listbox1.curselection())
            print(add_to_list_word)
            for i,j,z in add_to_list_word:
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
            print(word_select)
            print(pressword)
            for i1 in word_select:
                word = []
                if i1 == pressword :
                    if xword == 'x':
                        print(add_to_list_word)
                        pressword_pos=word_select.find(pressword)
                        for i in range(0, len(word_select)):
                            if i == 0:
                                canvas.create_rectangle(xc , yc - pressword_pos*boxsize + i*boxsize,xc + boxsize, yc - pressword_pos*boxsize + i*boxsize +boxsize, width=1,fill="#FAF0E6")
                                canvas.create_text(xc + boxsize/2 , yc - pressword_pos*boxsize + i*boxsize + boxsize/2, text=word_select[i],font=("Purisa", 36) )
                                canvas.create_text(xc + boxsize/8 , yc - pressword_pos*boxsize + i*boxsize + boxsize/4, text=str(len(add_to_list_word)+1),font=("Purisa", 14) )
                                word.append([word_select[i],xc , yc - pressword_pos*boxsize + i*boxsize ])
                            else:
                                canvas.create_rectangle(xc , yc - pressword_pos*boxsize + i*boxsize,xc + boxsize, yc - pressword_pos*boxsize + i*boxsize +boxsize, width=1)
                                canvas.create_text(xc + boxsize/2 , yc - pressword_pos*boxsize + i*boxsize + boxsize/2, text=word_select[i],font=("Purisa", 36) )
                                word.append([word_select[i],xc , yc - pressword_pos*boxsize + i*boxsize ])
                        add_to_list_word.append(['y',word_select,word])
                        listbox1.delete(listbox1.curselection())
                        xword = ''
                    if yword == 'y':
                        print(add_to_list_word)
                        pressword_pos=word_select.find(pressword)
                        for i in range(0, len(word_select)):
                            if i == 0:
                                canvas.create_rectangle(xc - pressword_pos*boxsize + i*boxsize, yc,xc-pressword_pos*boxsize + i*boxsize + boxsize, yc + boxsize, width=1,fill="#FAF0E6")
                                canvas.create_text(xc - pressword_pos*boxsize + i*boxsize+boxsize/2, yc+boxsize/2, text=word_select[i],font=("Purisa", 36) )
                                canvas.create_text(xc - pressword_pos*boxsize + i*boxsize+boxsize/8, yc+boxsize/4, text=str(len(add_to_list_word)+1),font=("Purisa", 14) )
                                word.append([word_select[i],xc - pressword_pos*boxsize + i*boxsize , yc])
                            else:
                                canvas.create_rectangle(xc - pressword_pos*boxsize + i*boxsize, yc,xc-pressword_pos*boxsize + i*boxsize + boxsize, yc + boxsize, width=1)
                                canvas.create_text(xc - pressword_pos*boxsize + i*boxsize+boxsize/2, yc+boxsize/2, text=word_select[i],font=("Purisa", 36) )
                                word.append([word_select[i],xc - pressword_pos*boxsize + i*boxsize , yc])
                        add_to_list_word.append(['x',word_select,word])
                        listbox1.delete(listbox1.curselection())
                        yword = ''

window = Tk()
window.resizable(False,False)
frame = Frame(window)
frame.pack()
listbox1 = Listbox(frame,bg="#f7ffde",font=("Constantia",30),width=15,exportselection=0,height=15)
buttonopenfile = Button(frame,text="Вставить список слов",command=openfile,state=ACTIVE)
buttonsavefile = Button(frame,text="Сохранить фотографию",command=save_as_png,state=ACTIVE)
buttonReload = Button(frame,text="Обновить",command=reprint,state=ACTIVE)
checkstate=IntVar()
checkbox = Checkbutton(frame,text="Печатать букву",onvalue=1,offvalue=0,variable=checkstate,command=checkstates)
canvas = Canvas(frame,height=game_height,width=game_width,bg="#ffffe0")
listbox1.grid(row=0,column=0)
canvas.grid(row=0,column=1)
buttonopenfile.grid(row=1,column=0)
buttonReload.grid(row=1,column=1)
checkbox.grid(row=1,column=2)
buttonsavefile.grid(row=1,column=3)


canvas.bind("<ButtonPress-1>", mouse_down)

window.update()
windows_width = window.winfo_width()
window_heigth = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_heigth = window.winfo_screenheight()

x = int((screen_width/2) - (windows_width/2))
y = int((screen_heigth/2) - (window_heigth/2))

window.geometry(f"{windows_width}x{window_heigth}+{x}+{y}")



window.mainloop()