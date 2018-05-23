from tkinter import *



def frame(root, side):
    w = Frame(root)
    w.pack(side = side, expand = YES, fill = BOTH)
    return w


def button_layout(btn_fame,word,command = None):
    w= Button(btn_fame,text=word,command =command)
    w.pack(side = LEFT, expand = YES, fill = BOTH)
    return w

def get_input(text,chr):
    #entry.insert(END, chr)
    #print(text.get())
    #print(chr)
    text.set(text.get()+chr)

def get_val(text,chr):
    val=text.get()
    output = str(eval(val.strip()))
    text.set(output)



if __name__ == "__main__":
    mainUI = Tk()
    mainUI.geometry('600x700+500+100')
    mainUI.title("calc")

    display = StringVar()
    #inp_f=Frame(mainUI)
    entry=Entry(mainUI,relief = SUNKEN,textvariable = display).pack(side = TOP, expand = YES,fill = BOTH)


    for st in ("012+","345-","678*","9C=/"):
        bf=frame(mainUI,TOP)
        for ch in st:
            if ch != '=':
                button_layout(bf,ch,command=lambda t=display,c=ch:get_input(t,c) )
            else:
                button_layout(bf,ch,command=lambda t=display,c=ch:get_val(t,c) )

    mainUI.mainloop()


