from textwrap import shorten
from tkinter import Button, Tk,RAISED
from tkinker import * # import all the libraries from tkinter
import os
def restart():
    os.system("shutdown /r /t 1")
    
def restart_time():
   os.system("shutdown /r /t 20")
def log_out():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")
# tk class we have call
st=Tk()

st.title("ShutDown app")
st.geometry("500x500")
st.config(bg="blue")

# 4 buttons we are using
# restart variable
r_button=Button(st,text="Restart",font=("Time new roman",25,"bold"),fg="red",relief=RAISED,cursor="plus",command=restart)
r_button.place(x=120,y=80,height=50,width=160)




rt_button=Button(st,text="Restart time",font=("Time new roman",25,"bold"),fg="red",relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=120,y=160,height=50,width=160)

lg_button=Button(st,text="log-out",font=("Time new roman",25,"bold"),fg="red",relief=RAISED,cursor="plus",command=log_out)
lg_button.place(x=120,y=240,height=50,width=160)

st_button=Button(st,text="shutdown",font=("Time new roman",25,"bold"),fg="red",relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=120,y=320,height=50,width=160)


st.mainloop() # display window until we close it..!

