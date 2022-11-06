import tkinter as tk
from tkinter import ttk # FOR WIDGETS
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
########################## SET MAIN WINDOW ##################################
root = tk.Tk()
root.title('PDF_TOOLS')
root.iconbitmap('IMAGENES/ICONO.ico')
root.configure(bg='black')
#INITIAL SIZE##############################
window_width = 600
window_height = 400
root.minsize(window_width, window_height)
#GET SCREEN DIMENSION######################
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#FIND THE CENTER POINT#####################
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

#SET THE POSITION OF THE WINDOW TO THE CENTER OF THE SCREEN
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
########################## WIDGETS ##################################

label_up = tk.Label(
    root
    ,text="PDF'S-TOOLS"
    ,font=("Franklin Gothic", 14)
    ,background='#FF1C3B'
    ,foreground='white'
    ).place(relx=0.5, rely=0,relheight=0.15,relwidth=1, anchor=tk.N) 

label_down = tk.Label(
    root
    ,text="Created by Ivan Anzaldo \nPowered by python \t\t\t\t\t\t\t\tV1.0"
    ,font=("Franklin Gothic", 10)
    ,background='#FF1C3B'
    ,foreground='white'
    ).place(relx=0.5, rely=1,relheight=0.10,relwidth=1, anchor=tk.S) 

# Read the Image
image_merge = Image.open("imagenes/Merge_Vertical.png")
image_split = Image.open("imagenes/Split_Horizontal.png")
# Resize the image using resize() method

resize_image_merge = image_merge.resize((int(root.winfo_width()*.2), int(root.winfo_height()*.25)))
resize_image_split = image_split.resize((int(root.winfo_width()*.2), int(root.winfo_height()*.25)))
img_merge = ImageTk.PhotoImage(resize_image_merge)
img_split = ImageTk.PhotoImage(resize_image_split)

def merge_clicked():
    merge_window = tk.Tk()
    merge_window.mainloop()
    
merge_button = ttk.Button(
    root
    ,image = img_merge
    ,command=merge_clicked
).place(relx=0.4, rely=.5,relheight=0.25,relwidth=.2, anchor=tk.E)

label_merge_button = tk.Label(
    root
    ,text="MERGE"
    ,font=("Franklin Gothic bold", 12)
    ,background='black'
    ,foreground='#FF1C3B'
    ).place(relx=0.4, rely=.35,relheight=0.05,relwidth=.2, anchor=tk.E) 

def split_clicked():
    split_window = tk.Tk()
    split_window.mainloop()


split_button = ttk.Button(
    root
    ,image = img_split
    ,command=split_clicked
).place(relx=0.6, rely=.5,relheight=0.25,relwidth=.2, anchor=tk.W)

label_split_button = tk.Label(
    root
    ,text="SPLIT"
    ,font=("Franklin Gothic bold", 12)
    ,background='black'
    ,foreground='#FF1C3B'
    ).place(relx=0.6, rely=.35,relheight=0.05,relwidth=.2, anchor=tk.W) 

root.mainloop()

