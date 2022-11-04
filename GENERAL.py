import tkinter as tk
from idlelib.tooltip import Hovertip
    
app = tk.Tk()
myBtn = tk.Button(app,text='?')
myBtn.place(relx=0.3, rely=.3,relheight=0.075,relwidth=.175, anchor=tk.E)
myTip = Hovertip(myBtn,'This is \na multiline tooltip.')
app.mainloop()