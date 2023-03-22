from tkinter import *
from tkinter import messagebox
import ast

window=Tk()
window.title("SignUp")
window.geometry("925x500+300+200")
window.configure(bg='#fff')
window.resizable(False,False)

def signup():
    Username=user.get()
    Password=code.get()
    confprm_Password=conform_code.get()

    if Password==confprm_Password:
        try:
            file=open('data.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={Username:Password}
            r.update(dict2)
            file.truncate(0)
            file.close()


            file=open('data.txt','w')
            w=file.write(str(r))


            messagebox.showinfo('Signup','Sucessfully sign up')

        except:
            file=open('data.txt','w')
            pp=str({'Username':'Password'})
            file.write(pp)
            file.close()


    else:
        messagebox.showerror('Invalid',"Both Password should match")


def sign():
    window.destroy()
          


img = PhotoImage(file='login.png')
Label(window,image=img,border=0,bg='white').place(x=50,y=90)



frame=Frame(window,width=350,height=390,bg='#fff')
frame.place(x=480,y=50)


heading=Label(frame,text='Sign out', fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~user~~~~~~~~~~~~~~~~~~~~~#########~~~~~~~~~~~#

def no_enter(e):
    user.delete(0, 'end')

def no_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

    

user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',no_enter)
user.bind('<FocusOut>',no_leave)



Frame(frame,width=295,height=2,bg='black',).place(x=25,y=107)

#~~~~~~~~~~~~~~~~~~user~~~~~~~~~~~~~~~~~~~~~#########~~~~~~~~~~~#

def no_enter(e):
    code.delete(0, 'end')

def no_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')


code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',no_enter)
code.bind('<FocusOut>',no_leave)


Frame(frame,width=295,height=2,bg='black',).place(x=25,y=177)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def no_enter(e):
    conform_code.delete(0, 'end')

def no_leave(e):
    name=conform_code.get()
    if name=='':
        conform_code.insert(0,'Conform Password')


conform_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0,'Conform Password')
conform_code.bind('<FocusIn>',no_enter)
conform_code.bind('<FocusOut>',no_leave)


Frame(frame,width=295,height=2,bg='black',).place(x=25,y=247)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text="I have an account?",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=90,y=340)

sign_in= Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
sign_in.place(x=200,y=340)


window.mainloop()
