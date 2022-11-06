###################TKINTER LIBS#####################
import tkinter as tk
from tkinter import ttk # FOR WIDGETS
from tkinter.messagebox import showinfo
from tkinter import filedialog
from idlelib.tooltip import Hovertip
###################IMAGE EDITING LIBS###############
from PIL import Image, ImageTk

from distutils.log import error

from PyPDF2 import PdfMerger
from PyPDF2 import PdfFileReader

from winreg import *
################################### APP #################################################

############################## SET MAIN WINDOW ##########################################

class root(tk.Tk):
    def __init__(self):
        super().__init__()
        ########################## WINDOW ############################
        self.root = self
        self.root.title('PDF_TOOLS')
        self.root.iconbitmap('IMAGENES/ICONO.ico')
        self.root.configure(bg='black')
        #INITIAL SIZE#####################
        window_width = 600
        window_height = 400
        self.root.minsize(window_width, window_height)
        #GET SCREEN DIMENSION#############
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        #FIND THE CENTER POINT############
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        #SET THE POSITION OF THE WINDOW TO THE CENTER OF THE SCREEN
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        ########################## LABELS ############################
        label_up = tk.Label(
                                self.root
                                ,text="PDF'S-TOOLS"
                                ,font=("Franklin Gothic", 14)
                                ,background='#FF1C3B'
                                ,foreground='white'
                            )
        label_up.place(relx=0.5, rely=0,relheight=0.15,relwidth=1, anchor=tk.N) 

        label_merge_button = tk.Label(
                                        self.root
                                        ,text="MERGE"
                                        ,font=("Franklin Gothic bold", 12)
                                        ,background='black'
                                        ,foreground='#FF1C3B'
                                    )
        label_merge_button.place(relx=0.4, rely=.35,relheight=0.05,relwidth=.2, anchor=tk.E) 

        label_split_button = tk.Label(
                                        self.root
                                        ,text="SPLIT"
                                        ,font=("Franklin Gothic bold", 12)
                                        ,background='black'
                                        ,foreground='#FF1C3B'
                                    )
        label_split_button.place(relx=0.6, rely=.35,relheight=0.05,relwidth=.2, anchor=tk.W)

        label_down = tk.Label(
                                self.root
                                ,text="Created by Ivan Anzaldo \nPowered by python \t\t\t\t\t\t\t\tV1.0"
                                ,font=("Franklin Gothic", 10)
                                ,background='#FF1C3B'
                                ,foreground='white'
                            )
        label_down.place(relx=0.5, rely=1,relheight=0.10,relwidth=1, anchor=tk.S)
        ########################## BUTTONS ###########################
        ######### Read the Image ##########
        image_merge = Image.open("IMAGENES/Merge_Vertical.png")
        image_split = Image.open("IMAGENES/Split_Horizontal.png")
        ######### Resize the image ########
        resize_image_merge = image_merge.resize((int(self.root.winfo_width()*.2), int(self.root.winfo_height()*.25)))
        resize_image_split = image_split.resize((int(self.root.winfo_width()*.2), int(self.root.winfo_height()*.25)))
        self.img_merge = ImageTk.PhotoImage(resize_image_merge)
        self.img_split = ImageTk.PhotoImage(resize_image_split)

        merge_button = ttk.Button(
                                    self.root
                                    ,image = self.img_merge
                                    ,command=self.merge_clicked
                                )
        merge_button.place(relx=0.4, rely=.5,relheight=0.25,relwidth=.2, anchor=tk.E)

        split_button = ttk.Button(
                                    self.root
                                    ,image = self.img_split
                                    ,command=self.split_clicked
                                )
        split_button.place(relx=0.6, rely=.5,relheight=0.25,relwidth=.2, anchor=tk.W)
        ########################## FUNCTIONS #########################
    def merge_clicked(self):
        print("merge")
    def split_clicked(self):
        print("split")

class GUI():
    def __init__(self):
        main = root()
        main.root.mainloop()

if __name__ == "__main__":
    app = GUI()

        