import tkinter

window=tkinter.Tk()
window.title("hello world!")
window.geometry('400x400')

variable=tkinter.StringVar()

l=tkinter.Label(window,text='didn\'t hit',textvariable=variable,bg='violet',font=('Arial',14)
                ,width=16,height=4)
l.pack()

on_hit=False

def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        variable.set('you hit me')
    else:
        on_hit=False
        variable.set('')
    
    
b=tkinter.Button(window,text='hit me',width=16,height=3,command=hit_me)
b.pack()

window.mainloop()