###################TKINTER LIBS#####################
import tkinter as tk
from tkinter import ttk # FOR WIDGETS
from tkinter.messagebox import showinfo
from tkinter import filedialog
from idlelib.tooltip import Hovertip
###################IMAGE EDITING LIBS###############
import os
import sys
from PIL import Image, ImageTk

from distutils.log import error

from PyPDF2 import PdfMerger
from PyPDF2 import PdfFileReader

from winreg import *
################################### APP #################################################

############################## SET MAIN WINDOW ##########################################

class path_calc:
    @staticmethod
    def resource_path(relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

class root(tk.Tk):
    def __init__(self):
        super().__init__()
        ########################## WINDOW ############################
        self.root = self
        self.root.title('PDF_TOOLS')
        self.root.iconbitmap(path_calc.resource_path('IMAGENES\\ICONO.ico'))
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
        image_merge = Image.open(path_calc.resource_path('IMAGENES\\Merge_Vertical.png'))
        image_split = Image.open(path_calc.resource_path('IMAGENES\\Split_Horizontal.png'))
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
        self.root.destroy()
        sec = merge_window()
        sec.merge_window.mainloop()
    def split_clicked(self):
        self.root.destroy()
        sec = split_window()
        sec.split_window.mainloop()

############################## SET MERGE WINDOW #########################################

class merge_window(tk.Tk):
    def __init__(self):
        super().__init__()
        ########################## WINDOW ############################
        self.merge_window = self
        self.merge_window.title('PDF_MERGE')
        self.merge_window.iconbitmap(path_calc.resource_path('IMAGENES\\ICONO.ico'))
        self.merge_window.configure(bg='black')
        #INITIAL SIZE#####################
        window_width = 600
        window_height = 400
        self.merge_window.minsize(window_width, window_height)
        #GET SCREEN DIMENSION#############
        screen_width = self.merge_window.winfo_screenwidth()
        screen_height = self.merge_window.winfo_screenheight()
        #FIND THE CENTER POINT############
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        #SET THE POSITION OF THE WINDOW TO THE CENTER OF THE SCREEN
        self.merge_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        ########################## LABELS ############################
        label_up = tk.Label(
                                self.merge_window
                                ,text="MERGE-TOOL"
                                ,font=("Franklin Gothic", 14)
                                ,background='#FF1C3B'
                                ,foreground='white'
                            )
        label_up.place(relx=0.5, rely=0,relheight=0.15,relwidth=1, anchor=tk.N) 

        label_select = tk.Label(
                                    self.merge_window
                                    ,text="SELECTED FILES"
                                    ,font=("Franklin Gothic bond", 8)
                                    ,background='black'
                                    ,foreground='#FF1C3B'
                                )
        label_select.place(relx=0.55, rely=.2,relheight=0.05,relwidth=.3, anchor=tk.W)

        label_down = tk.Label(
                                    self.merge_window
                                    ,text="Created by Ivan Anzaldo \nPowered by python \t\t\t\t\t\t\t\tV1.0"
                                    ,font=("Franklin Gothic", 10)
                                    ,background='#FF1C3B'
                                    ,foreground='white'
                                )
        label_down.place(relx=0.5, rely=1,relheight=0.10,relwidth=1, anchor=tk.S)
        ######################### SCROLLBAR ##########################
        global filename_merge
        global filename_merge_list
        global filename_merge_dict
        filename_merge = ""
        filename_merge_list = []
        filename_merge_dict = {}

        scrollbar_v = ttk.Scrollbar(self.merge_window, orient=tk.VERTICAL)
        scrollbar_h = ttk.Scrollbar(self.merge_window, orient=tk.HORIZONTAL)
        # Vincularla con la lista.
        self.listbox = tk.Listbox(self.merge_window, yscrollcommand=scrollbar_v.set,xscrollcommand=scrollbar_h.set )
        scrollbar_v.config(command=self.listbox.yview)
        scrollbar_h.config(command=self.listbox.xview)
        # Ubicarla a la derecha.
        scrollbar_v.place(relx=0.95, rely=.5,relheight=0.5, anchor=tk.W)
        scrollbar_h.place(relx=0.45, rely=.77,relwidth=0.5, anchor=tk.W)
        ########################## LISTBOX ###########################
        self.listbox.insert(0, *filename_merge_list)
        self.listbox.place(relx=0.45, rely=.5,relheight=0.5,relwidth=.5, anchor=tk.W)
        ########################## ENTRYS ############################
        vcmd = (self.register(self.validate_entry), '%P')
        self.initial_page = ttk.Entry(self.merge_window)
        self.initial_page.config(validate='key', validatecommand=vcmd)
        self.final_page = ttk.Entry(self.merge_window)
        self.final_page.config(validate='key', validatecommand=vcmd)

        self.initial_page.insert(0,"Initial Page")
        self.initial_page.place(relx=0.3, rely=.4,relheight=0.05,relwidth=.175, anchor=tk.E)
        Tip_initial = Hovertip(self.initial_page,'Add the number of the initial page from which you want to start selecting.')
        self.final_page.insert(0,"Final Page")
        self.final_page.place(relx=0.3, rely=.45,relheight=0.05,relwidth=.175, anchor=tk.E)
        Tip_final = Hovertip(self.final_page,'Add the number of the final page from which you want to finish selecting.')
        ########################## BUTTONS ###########################
        # Read the Image
        self.image_return = Image.open(path_calc.resource_path('IMAGENES\\return.png'))
        # Resize the image using resize() method
        self.resize_image_return = self.image_return.resize((int(window_width*.05), int(window_height*.05)))
        self.img_return = ImageTk.PhotoImage(self.resize_image_return)
        #RETURN BUTTON ###############################
        return_button = tk.Button(
                                    self.merge_window
                                    ,image = self.img_return
                                    ,background='#FF1C3B'
                                    ,foreground='black'
                                    ,command=self.return_clicked
                                )
        return_button.place(relx=0.065, rely=.05,relheight=.05,relwidth=.05, anchor=tk.N)
        #CHECK BUTTON ################################
        self.check_all_file = tk.IntVar()
        self.check_but_all_file = tk.Checkbutton(self.merge_window, text = 'All pages', variable = self.check_all_file,background='#FF1C3B',foreground='black')
        self.check_but_all_file.place(relx=0.3, rely=.55,relheight=0.05,relwidth=.175, anchor=tk.E)
        #SELECT BUTTON ###############################
        select_button = tk.Button(
                                    self.merge_window
                                    ,text='SELECT FILE'
                                    ,font=("Franklin Gothic bond", 10)
                                    ,background='#FF1C3B'
                                    ,foreground='black'
                                    ,command=self.select_clicked
                                )
        select_button.place(relx=0.3, rely=.3,relheight=0.075,relwidth=.175, anchor=tk.E)
        Tip_select = Hovertip(select_button,'Select a pdf file to merge.')
        #ADD BUTTON #################################
        add_button = tk.Button(
                                    self.merge_window
                                    ,text='ADD FILE'
                                    ,font=("Franklin Gothic bond", 10)
                                    ,background='#FF1C3B'
                                    ,foreground='black'
                                    ,command=self.add_clicked
                                )
        add_button.place(relx=0.3, rely=.65,relheight=0.075,relwidth=.175, anchor=tk.E)
        Tip_add = Hovertip(add_button,'Click to confirm the adition to the merge.')
        #MERGE BUTTON ###############################
        merge_button = tk.Button(
                                    self.merge_window
                                    ,text='MERGE-SAVE FILES'
                                    ,font=("Franklin Gothic bond", 10)
                                    ,background='#FF1C3B'
                                    ,foreground='black'
                                    ,command=self.merge_clicked
                                )
        merge_button.place(relx=0.3375, rely=.75,relheight=0.075,relwidth=.25, anchor=tk.E)
        Tip_merge = Hovertip(merge_button,'Click to merge and save the merged pdf.')
        #CLEAR BUTTON ###############################
        clear_button = tk.Button(
                                    self.merge_window
                                    ,text='CLEAR FILES'
                                    ,font=("Franklin Gothic bond", 10)
                                    ,background='#FF1C3B'
                                    ,foreground='black'
                                    ,command=self.clear_clicked
                                )
        clear_button.place(relx=0.62, rely=.85,relheight=0.075,relwidth=.175, anchor=tk.W)
        Tip_clear = Hovertip(clear_button,'Click to clear all the selected files.')

        ########################## FUNCTIONS #########################
    def validate_entry(self,text):
        if text == "Initial Page" or text == "Final Page" or text == "":
            return True
        else:
            return text.isdigit()
    def return_clicked(self):
        self.merge_window.destroy()
        sec = root()
        sec.root.mainloop()
    def select_clicked(self):
        global filename_merge 
        filename_merge = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("pdf files", "*.pdf"), ("all files", "*.*")))
        print(filename_merge)
    def add_clicked(self):
            global filename_merge_list
            global filename_merge_dict
            global filename_merge 
            global error
            error = False
            
            try:
                pdfReader = PdfFileReader(filename_merge)
                count = pdfReader.numPages
                error = False
            except:
                tk.messagebox.showerror(title="ERROR", message="Archivo no valido o no seleccionado")
                count = 0
                error = True
            if self.check_all_file.get() == 0:
                if (self.initial_page.get().isdigit()):
                    if int(self.initial_page.get()) == 0:
                        tk.messagebox.showerror(title="ERROR", message="Pagina inicial no puede empezar de 0")
                        error = True
                    else:
                        if error != True :
                            error = False
                        pass
                else:
                    tk.messagebox.showerror(title="ERROR", message="Ingresa una pagina inicial")
                    error = True
                
                if (self.final_page.get().isdigit()):
                    if error != True :
                            error = False
                    pass
                else:
                    tk.messagebox.showerror(title="ERROR", message="Ingresa una pagina final")

                    error = True
                
                if (self.final_page.get().isdigit() and int(self.final_page.get())>count):
                    tk.messagebox.showerror(title="ERROR", message="Sobrepasaste la pagina final")
                    error = True
                else:
                    if error != True :
                            error = False
                    pass
                
                if(self.final_page.get().isdigit() and self.initial_page.get().isdigit() and int(self.final_page.get()) < int(self.initial_page.get()) ):
                    tk.messagebox.showerror(title="ERROR", message="El # de la pagina inicial no puede ser mayor a el # de la pagina final")
                    error = True
                else:
                    if error != True :
                            error = False
                    pass

            if error == False:
                self.listbox.delete(0, tk.END)
                filename_merge_list.append(filename_merge)
                self.listbox.insert(0, *filename_merge_list)
                if self.check_all_file.get() == 1:
                    
                    if filename_merge in filename_merge_dict.keys():
                        filename_merge_dict[filename_merge].append((0,count))
                    else:
                        filename_merge_dict[filename_merge]=[(0,count)]

                else:
                    if filename_merge in filename_merge_dict.keys():
                        filename_merge_dict[filename_merge].append(int(self.initial_page.get())-1,int(self.final_page.get()))
                    else:
                        filename_merge_dict[filename_merge]=[(int(self.initial_page.get())-1,int(self.final_page.get()))]

    def merge_clicked(self):
            global filename_merge_list
            global save_directory
            global filename_merge_dict
            global error

            if len(filename_merge_list)<=1:
                tk.messagebox.showerror(title="ERROR", message="No hay archivos seleccionados")
            else:
                save_directory = filedialog.asksaveasfile(initialdir = "/", title = "Select file", filetypes = (("pdf files", "*.pdf"), ("all files", "*.*")))
                merger = PdfMerger()
                for pdf,paginas_list in filename_merge_dict.items():
                    for paginas in paginas_list:
                        input_temp = open(pdf, "rb")
                        merger.append(fileobj=input_temp, pages=paginas)
                        input_temp.close()

                merger.write(save_directory.name)
                merger.close()
                print(save_directory.name)

    def clear_clicked(self):
            global filename_merge_list
            global filename_merge_dict
            self.listbox.delete(0, tk.END)
            filename_merge_list = []
            filename_merge_dict = {}

############################## SET SPLIT WINDOW #########################################

class split_window(tk.Tk):
    def __init__(self):
        super().__init__()
        ########################## GET DOWNLOAD FOLDER ##################################
        with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
            global Downloads
            Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
        ########################## WINDOW ############################
        self.split_window = self
        self.split_window.title('PDF_SPLIT')
        self.split_window.iconbitmap(path_calc.resource_path('IMAGENES\\ICONO.ico'))
        self.split_window.configure(bg='black')
        #INITIAL SIZE#####################
        window_width = 600
        window_height = 400
        self.split_window.minsize(window_width, window_height)
        #GET SCREEN DIMENSION#############
        screen_width = self.split_window.winfo_screenwidth()
        screen_height = self.split_window.winfo_screenheight()
        #FIND THE CENTER POINT############
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        #SET THE POSITION OF THE WINDOW TO THE CENTER OF THE SCREEN
        self.split_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        ########################## LABELS ############################
        label_up = tk.Label(
                                self.split_window
                                ,text="SPLIT-TOOL"
                                ,font=("Franklin Gothic", 14)
                                ,background='#FF1C3B'
                                ,foreground='white'
                            )
        label_up.place(relx=0.5, rely=0,relheight=0.15,relwidth=1, anchor=tk.N) 

        label_select = tk.Label(
                                    self.split_window
                                    ,text="FILES SPLITED"
                                    ,font=("Franklin Gothic bond", 8)
                                    ,background='black'
                                    ,foreground='#FF1C3B'
                                )
        label_select.place(relx=0.55, rely=.2,relheight=0.05,relwidth=.3, anchor=tk.W)

        label_down = tk.Label(
                                    self.split_window
                                    ,text="Created by Ivan Anzaldo \nPowered by python \t\t\t\t\t\t\t\tV1.0"
                                    ,font=("Franklin Gothic", 10)
                                    ,background='#FF1C3B'
                                    ,foreground='white'
                                )
        label_down.place(relx=0.5, rely=1,relheight=0.10,relwidth=1, anchor=tk.S) 
        ######################### SCROLLBAR ##########################
        global filename_split
        global filename_split_list
        global filename_split_dict
        filename_split = ""
        filename_split_list = []
        filename_split_dict = {}

        scrollbar_v = ttk.Scrollbar(self.split_window, orient=tk.VERTICAL)
        scrollbar_h = ttk.Scrollbar(self.split_window, orient=tk.HORIZONTAL)
        # Vincularla con la lista.
        self.listbox = tk.Listbox(self.split_window, yscrollcommand=scrollbar_v.set,xscrollcommand=scrollbar_h.set )
        scrollbar_v.config(command=self.listbox.yview)
        scrollbar_h.config(command=self.listbox.xview)
        # Ubicarla a la derecha.
        scrollbar_v.place(relx=0.95, rely=.5,relheight=0.5, anchor=tk.W)
        scrollbar_h.place(relx=0.45, rely=.77,relwidth=0.5, anchor=tk.W)
        ########################## LISTBOX ###########################
        self.listbox.insert(0, *filename_split_list)
        self.listbox.place(relx=0.45, rely=.5,relheight=0.5,relwidth=.5, anchor=tk.W)
        ########################## ENTRYS ############################
        vcmd = (self.register(self.validate_entry), '%P')
        self.initial_page = ttk.Entry(self.split_window)
        self.initial_page.config(validate='key', validatecommand=vcmd)
        self.final_page = ttk.Entry(self.split_window)
        self.final_page.config(validate='key', validatecommand=vcmd)

        self.initial_page.insert(0,"Initial Page")
        self.initial_page.place(relx=0.3, rely=.4,relheight=0.05,relwidth=.175, anchor=tk.E)
        Tip_initial = Hovertip(self.initial_page,'Add the number of the initial page from which you want to start selecting.')
        self.final_page.insert(0,"Final Page")
        self.final_page.place(relx=0.3, rely=.45,relheight=0.05,relwidth=.175, anchor=tk.E)
        Tip_final = Hovertip(self.final_page,'Add the number of the final page from which you want to finish selecting.')
        ########################## BUTTONS ###########################
        # Read the Image
        self.image_return = Image.open(path_calc.resource_path('IMAGENES\\return.png'))
        # Resize the image using resize() method
        self.resize_image_return = self.image_return.resize((int(window_width*.05), int(window_height*.05)))
        self.img_return = ImageTk.PhotoImage(self.resize_image_return)
        #RETURN BUTTON ###############################
        return_button = tk.Button(
                                    self.split_window
                                    ,image = self.img_return
                                    ,background='#FF1C3B'
                                    ,foreground='black'
                                    ,command=self.return_clicked
                                )
        return_button.place(relx=0.065, rely=.05,relheight=.05,relwidth=.05, anchor=tk.N)
        #CHECK BUTTON ################################
        self.check_all_file = tk.IntVar()
        self.check_but_all_file = tk.Checkbutton(self.split_window, text = 'Join all the ranges into one pdf file', variable = self.check_all_file,background='#FF1C3B',foreground='black')
        self.check_but_all_file.place(relx=0.38, rely=.65,relheight=0.05,relwidth=.35, anchor=tk.E)
        #SELECT BUTTON ###############################
        select_button = tk.Button(
                                    self.split_window
                                    ,text='SELECT FILE'
                                    ,font=("Franklin Gothic bond", 10)
                                    ,background='#FF1C3B'
                                    ,foreground='black'
                                    ,command=self.select_clicked
                                )
        select_button.place(relx=0.3, rely=.3,relheight=0.075,relwidth=.175, anchor=tk.E)
        Tip_select = Hovertip(select_button,'Select a pdf file to split.')
        #ADD BUTTON #################################    
        add_button = tk.Button(
                                    self.split_window
                                    ,text='ADD RANGE'
                                    ,font=("Franklin Gothic bond", 10)
                                    ,background='#FF1C3B'
                                    ,foreground='black'
                                    ,command=self.add_clicked
                                )

        add_button.place(relx=0.3, rely=.55,relheight=0.075,relwidth=.175, anchor=tk.E)
        Tip_add = Hovertip(add_button,'Click to confirm the split range.')
        #SPLIT BUTTON ###############################
        split_button = tk.Button(
                                    self.split_window
                                    ,text='SPLIT-SAVE FILES'
                                    ,font=("Franklin Gothic bond", 10)
                                    ,background='#FF1C3B'
                                    ,foreground='black'
                                    ,command=self.split_clicked
                                )
        split_button.place(relx=0.3375, rely=.75,relheight=0.075,relwidth=.25, anchor=tk.E)
        Tip_merge = Hovertip(split_button,'Click to split and save the splited pdf??s.')
        #CLEAR BUTTON ###############################
        clear_button = tk.Button(
                                    self.split_window
                                    ,text='CLEAR FILES'
                                    ,font=("Franklin Gothic bond", 10)
                                    ,background='#FF1C3B'
                                    ,foreground='black'
                                    ,command=self.clear_clicked
                                )
        clear_button.place(relx=0.62, rely=.85,relheight=0.075,relwidth=.175, anchor=tk.W)
        Tip_clear = Hovertip(clear_button,'Click to clear all the selected files.')

        ########################## FUNCTIONS #########################
    def validate_entry(self,text):
        if text == "Initial Page" or text == "Final Page" or text == "":
            return True
        else:
            return text.isdigit()

    def return_clicked(self):
        self.split_window.destroy()
        sec = root()
        sec.root.mainloop()

    def select_clicked(self):
        global filename_split 
        filename_split = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("pdf files", "*.pdf"), ("all files", "*.*")))
        print(filename_split)

    def add_clicked(self):
        global filename_split 
        global filename_split_list
        global filename_split_dict
        global error
        error = False
            
        try:
            pdfReader = PdfFileReader(filename_split)
            count = pdfReader.numPages
            error = False
        except:
            tk.messagebox.showerror(title="ERROR", message="Archivo no valido o no seleccionado")
            count = 0
            error = True
        if (self.initial_page.get().isdigit()):
            if int(self.initial_page.get()) == 0:
                tk.messagebox.showerror(title="ERROR", message="Pagina inicial no puede empezar de 0")
                error = True
            else:
                if error != True :
                    error = False
                pass
        else:
            tk.messagebox.showerror(title="ERROR", message="Ingresa una pagina inicial")
            error = True
                
        if (self.final_page.get().isdigit()):
            if error != True :
                error = False
            pass
        else:
            tk.messagebox.showerror(title="ERROR", message="Ingresa una pagina final")
            error = True
                
        if (self.final_page.get().isdigit() and int(self.final_page.get())>count):
            tk.messagebox.showerror(title="ERROR", message="Sobrepasaste la pagina final")
            error = True
        else:
            if error != True :
                error = False
            pass
                
        if(self.final_page.get().isdigit() and self.initial_page.get().isdigit() and int(self.final_page.get()) < int(self.initial_page.get()) ):
            tk.messagebox.showerror(title="ERROR", message="El # de la pagina inicial no puede ser mayor a el # de la pagina final")
            error = True
        else:
            if error != True :
                error = False
            pass

        if len(filename_split_list)<1 and filename_split == "":
            tk.messagebox.showerror(title="ERROR", message="No hay archivos seleccionados")
            error = True
        else:
            if error != True :
                error = False
            pass        

        if error == False:
            self.listbox.delete(0, tk.END)
            size_temp = len(filename_split_list)
            filename_split_list.append("Split"+str(size_temp+1)+".pdf "+"page "+self.initial_page.get()+" to page "+self.final_page.get())
            self.listbox.insert(0, *filename_split_list)
            filename_split_dict["Split"+str(size_temp+1)+".pdf "]=(int(self.initial_page.get())-1,int(self.final_page.get()))

    def split_clicked(self):
            global filename_split_list
            global save_directory
            global filename_split_dict
            global filename_split 
            global Downloads
            global error

            if len(filename_split_list)<1:
                tk.messagebox.showerror(title="ERROR", message="No hay archivos seleccionados")
            else:
                if (self.check_all_file.get() == 1):
                    merger = PdfMerger()
                    for pdf,paginas in filename_split_dict.items():
                        input_temp = open(filename_split, "rb")
                        merger.append(fileobj=filename_split, pages=paginas)
                        input_temp.close()
                    merger.write(Downloads+"\\"+pdf)
                    merger.close()
                else:
                    
                    for pdf,paginas in filename_split_dict.items():
                        merger = PdfMerger()
                        input_temp = open(filename_split, "rb")
                        merger.append(fileobj=filename_split, pages=paginas)
                        input_temp.close()
                        merger.write(Downloads+"\\"+pdf)
                        merger.close()
    def clear_clicked(self):
            global filename_split_list
            global filename_split_dict
            global filename_split

            self.listbox.delete(0, tk.END)
            filename_split_list = []
            filename_split_dict = {}
            filename_split = ""

class GUI():
    def __init__(self):
        main = root()
        main.root.mainloop()

if __name__ == "__main__":
    app = GUI()