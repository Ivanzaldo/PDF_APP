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
#######################APP##########################
def window_root():
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
        root.destroy()
        window_merge()
        

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
        root.destroy()
        window_split()


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

def window_merge():
    ########################## SET MAIN WINDOW ##################################
    merge_window = tk.Tk()
    merge_window.title('PDF_MERGE')
    merge_window.iconbitmap('IMAGENES/ICONO.ico')
    merge_window.configure(bg='black')
    #INITIAL SIZE##############################
    window_width = 600
    window_height = 400
    merge_window.minsize(window_width, window_height)
    #GET SCREEN DIMENSION######################
    screen_width = merge_window.winfo_screenwidth()
    screen_height = merge_window.winfo_screenheight()

    #FIND THE CENTER POINT#####################
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    #SET THE POSITION OF THE WINDOW TO THE CENTER OF THE SCREEN
    merge_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    ########################## LABELS ##################################

    label_up = tk.Label(
        merge_window
        ,text="MERGE-TOOL"
        ,font=("Franklin Gothic", 14)
        ,background='#FF1C3B'
        ,foreground='white'
        ).place(relx=0.5, rely=0,relheight=0.15,relwidth=1, anchor=tk.N) 

    label_select = tk.Label(
        merge_window
        ,text="SELECTED FILES"
        ,font=("Franklin Gothic bond", 8)
        ,background='black'
        ,foreground='#FF1C3B'
        ).place(relx=0.55, rely=.2,relheight=0.05,relwidth=.3, anchor=tk.W)

    label_down = tk.Label(
        merge_window
        ,text="Created by Ivan Anzaldo \nPowered by python \t\t\t\t\t\t\t\tV1.0"
        ,font=("Franklin Gothic", 10)
        ,background='#FF1C3B'
        ,foreground='white'
        ).place(relx=0.5, rely=1,relheight=0.10,relwidth=1, anchor=tk.S) 

    ########################## FUNCIONALIDAD ##################################

    ########################## Scrollbar ##################################
    global filename_merge
    global filename_merge_list
    global filename_merge_dict
    filename_merge = ""
    filename_merge_list = []
    filename_merge_dict = {}

    scrollbar_v = ttk.Scrollbar(merge_window, orient=tk.VERTICAL)
    scrollbar_h = ttk.Scrollbar(merge_window, orient=tk.HORIZONTAL)
    # Vincularla con la lista.
    listbox = tk.Listbox(merge_window, yscrollcommand=scrollbar_v.set,xscrollcommand=scrollbar_h.set )
    scrollbar_v.config(command=listbox.yview)
    scrollbar_h.config(command=listbox.xview)
    # Ubicarla a la derecha.
    scrollbar_v.place(relx=0.95, rely=.5,relheight=0.5, anchor=tk.W)
    scrollbar_h.place(relx=0.45, rely=.77,relwidth=0.5, anchor=tk.W)

    ########################## listbox ##################################

    listbox.insert(0, *filename_merge_list)
    listbox.place(relx=0.45, rely=.5,relheight=0.5,relwidth=.5, anchor=tk.W)

    ########################## ENTRY ##################################

    def validate_entry(text):
        if text == "Initial Page" or text == "Final Page":
            return True
        else:
            return text.isdigit()

    initial_page = ttk.Entry(
        validate="key"
        ,validatecommand=(merge_window.register(validate_entry), "%S")
    )
    final_page = ttk.Entry(
        validate="key"
        ,validatecommand=(merge_window.register(validate_entry), "%S")
    )

    initial_page.insert(0,"Initial Page")
    final_page.insert(0,"Final Page")
    initial_page.place(relx=0.3, rely=.4,relheight=0.05,relwidth=.175, anchor=tk.E)
    Tip_initial = Hovertip(initial_page,'Add the number of the initial page from which you want to start selecting.')
    final_page.place(relx=0.3, rely=.45,relheight=0.05,relwidth=.175, anchor=tk.E)
    Tip_final = Hovertip(final_page,'Add the number of the final page from which you want to finish selecting.')
    ########################## BUTTONS ##################################
    # Read the Image
    image_return = Image.open("imagenes/return.png")
    # Resize the image using resize() method
    resize_image_return = image_return.resize((int(window_width*.05), int(window_height*.05)))
    img_return = ImageTk.PhotoImage(resize_image_return)

    def return_clicked():
        merge_window.destroy()
        window_root()
    
    return_button = tk.Button(
        merge_window
        ,image = img_return
        ,background='#FF1C3B'
        ,foreground='black'
        ,command=return_clicked
    )
    return_button.place(relx=0.065, rely=.05,relheight=.05,relwidth=.05, anchor=tk.N)

    check_all_file = tk.IntVar()
    check_but_all_file = tk.Checkbutton(merge_window, text = 'All pages', variable = check_all_file,background='#FF1C3B',foreground='black')
    check_but_all_file.place(relx=0.3, rely=.55,relheight=0.05,relwidth=.175, anchor=tk.E)

    def select_clicked():
        global filename_merge 
        filename_merge = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("pdf files", "*.pdf"), ("all files", "*.*")))
        print(filename_merge)
    
    select_button = tk.Button(
        merge_window
        ,text='SELECT FILE'
        ,font=("Franklin Gothic bond", 10)
        ,background='#FF1C3B'
        ,foreground='black'
        ,command=select_clicked
    )
    select_button.place(relx=0.3, rely=.3,relheight=0.075,relwidth=.175, anchor=tk.E)
    Tip_select = Hovertip(select_button,'Select a pdf file to merge.')


    def add_clicked():
        global filename_merge_list
        global filename_merge_dict
        global filename_merge 
        global error
        error = False
        
        try:
            print("Intentando entrar a "+filename_merge)
            pdfReader = PdfFileReader(filename_merge)
            count = pdfReader.numPages
            error = False
            print("Se logro entrar a "+filename_merge)
        except:
            print("No se logro entrar a "+filename_merge)
            tk.messagebox.showerror(title="ERROR", message="Archivo no valido o no seleccionado")
            count = 0
            error = True
        if check_all_file.get() == 0:
            if (initial_page.get().isdigit()):
                if int(initial_page.get()) == 0:
                    tk.messagebox.showerror(title="ERROR", message="Pagina inicial no puede empezar de 0")
                    error = True
                else:
                    if error != True :
                        error = False
                    pass
            else:
                tk.messagebox.showerror(title="ERROR", message="Ingresa una pagina inicial")
                error = True
            
            if (final_page.get().isdigit()):
                if error != True :
                        error = False
                pass
            else:
                tk.messagebox.showerror(title="ERROR", message="Ingresa una pagina final")

                error = True
            
            if (final_page.get().isdigit() and int(final_page.get())>count):
                tk.messagebox.showerror(title="ERROR", message="Sobrepasaste la pagina final")
                error = True
            else:
                if error != True :
                        error = False
                pass
            
            if(final_page.get().isdigit() and initial_page.get().isdigit() and int(final_page.get()) < int(initial_page.get()) ):
                tk.messagebox.showerror(title="ERROR", message="El # de la pagina inicial no puede ser mayor a el # de la pagina final")
                error = True
            else:
                if error != True :
                        error = False
                pass

        if error == False:
            listbox.delete(0, tk.END)
            filename_merge_list.append(filename_merge)
            listbox.insert(0, *filename_merge_list)
            if check_all_file.get() == 1:
                filename_merge_dict[filename_merge]=(0,count)
            else:
                filename_merge_dict[filename_merge]=(int(initial_page.get())-1,int(final_page.get()))
            
    add_button = tk.Button(
        merge_window
        ,text='ADD FILE'
        ,font=("Franklin Gothic bond", 10)
        ,background='#FF1C3B'
        ,foreground='black'
        ,command=add_clicked
    )

    add_button.place(relx=0.3, rely=.65,relheight=0.075,relwidth=.175, anchor=tk.E)
    Tip_add = Hovertip(add_button,'Click to confirm the adition to the merge.')

    def merge_clicked():
        global filename_merge_list
        global save_directory
        global filename_merge_dict
        global error

        if len(filename_merge_list)<=1:
            tk.messagebox.showerror(title="ERROR", message="No hay archivos seleccionados")
        else:
            save_directory = filedialog.asksaveasfile(initialdir = "/", title = "Select file", filetypes = (("pdf files", "*.pdf"), ("all files", "*.*")))
            merger = PdfMerger()
            for pdf,paginas in filename_merge_dict.items():
                input_temp = open(pdf, "rb")
                merger.append(fileobj=input_temp, pages=paginas)
                input_temp.close()

            merger.write(save_directory.name)
            merger.close()
            print(save_directory.name)

    
    merge_button = tk.Button(
        merge_window
        ,text='MERGE-SAVE FILES'
        ,font=("Franklin Gothic bond", 10)
        ,background='#FF1C3B'
        ,foreground='black'
        ,command=merge_clicked
    )
    merge_button.place(relx=0.3375, rely=.75,relheight=0.075,relwidth=.25, anchor=tk.E)
    Tip_merge = Hovertip(merge_button,'Click to merge and save the merged pdf.')

    def clear_clicked():
        global filename_merge_list
        global filename_merge_dict
        listbox.delete(0, tk.END)
        filename_merge_list = []
        filename_merge_dict = {}

    clear_button = tk.Button(
        merge_window
        ,text='CLEAR FILES'
        ,font=("Franklin Gothic bond", 10)
        ,background='#FF1C3B'
        ,foreground='black'
        ,command=clear_clicked
    )
    clear_button.place(relx=0.62, rely=.85,relheight=0.075,relwidth=.175, anchor=tk.W)

    Tip_clear = Hovertip(clear_button,'Click to clear all the selected files.')

    merge_window.mainloop()
    
def window_split():
    ########################## GET DOWNLOAD FOLDER ##################################
    with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
    ########################## SET MAIN WINDOW ##################################
    split_window = tk.Tk()
    split_window.title('PDF_SPLIT')
    split_window.iconbitmap('IMAGENES/ICONO.ico')
    split_window.configure(bg='black')
    #INITIAL SIZE##############################
    window_width = 600
    window_height = 400
    split_window.minsize(window_width, window_height)
    #GET SCREEN DIMENSION######################
    screen_width = split_window.winfo_screenwidth()
    screen_height = split_window.winfo_screenheight()

    #FIND THE CENTER POINT#####################
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    #SET THE POSITION OF THE WINDOW TO THE CENTER OF THE SCREEN
    split_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    ########################## LABELS ##################################

    label_up = tk.Label(
        split_window
        ,text="SPLIT-TOOL"
        ,font=("Franklin Gothic", 14)
        ,background='#FF1C3B'
        ,foreground='white'
        ).place(relx=0.5, rely=0,relheight=0.15,relwidth=1, anchor=tk.N) 

    label_select = tk.Label(
        split_window
        ,text="FILES SPLITED"
        ,font=("Franklin Gothic bond", 8)
        ,background='black'
        ,foreground='#FF1C3B'
        ).place(relx=0.55, rely=.2,relheight=0.05,relwidth=.3, anchor=tk.W)

    label_down = tk.Label(
        split_window
        ,text="Created by Ivan Anzaldo \nPowered by python \t\t\t\t\t\t\t\tV1.0"
        ,font=("Franklin Gothic", 10)
        ,background='#FF1C3B'
        ,foreground='white'
        ).place(relx=0.5, rely=1,relheight=0.10,relwidth=1, anchor=tk.S) 

    ########################## FUNCIONALIDAD ##################################

    ########################## Scrollbar ##################################
    global filename_split
    global filename_split_list
    global filename_split_dict
    filename_split = ""
    filename_split_list = []
    filename_split_dict = {}

    scrollbar_v = ttk.Scrollbar(split_window, orient=tk.VERTICAL)
    scrollbar_h = ttk.Scrollbar(split_window, orient=tk.HORIZONTAL)
    # Vincularla con la lista.
    listbox = tk.Listbox(split_window, yscrollcommand=scrollbar_v.set,xscrollcommand=scrollbar_h.set )
    scrollbar_v.config(command=listbox.yview)
    scrollbar_h.config(command=listbox.xview)
    # Ubicarla a la derecha.
    scrollbar_v.place(relx=0.95, rely=.5,relheight=0.5, anchor=tk.W)
    scrollbar_h.place(relx=0.45, rely=.77,relwidth=0.5, anchor=tk.W)

    ########################## listbox ##################################

    listbox.insert(0, *filename_split_list)
    listbox.place(relx=0.45, rely=.5,relheight=0.5,relwidth=.5, anchor=tk.W)

    ########################## ENTRY ##################################

    def validate_entry(text):
        if text == "Initial Page" or text == "Final Page":
            return True
        else:
            return text.isdigit()

    initial_page = ttk.Entry(
        validate="key"
        ,validatecommand=(split_window.register(validate_entry), "%S")
    )
    final_page = ttk.Entry(
        validate="key"
        ,validatecommand=(split_window.register(validate_entry), "%S")
    )

    initial_page.insert(0,"Initial Page")
    final_page.insert(0,"Final Page")
    initial_page.place(relx=0.3, rely=.4,relheight=0.05,relwidth=.175, anchor=tk.E)
    Tip_initial = Hovertip(initial_page,'Add the number of the initial page from which you want to start selecting.')
    final_page.place(relx=0.3, rely=.45,relheight=0.05,relwidth=.175, anchor=tk.E)
    Tip_final = Hovertip(final_page,'Add the number of the final page from which you want to finish selecting.')
    ########################## BUTTONS ##################################
    # Read the Image
    image_return = Image.open("imagenes/return.png")
    # Resize the image using resize() method
    resize_image_return = image_return.resize((int(window_width*.05), int(window_height*.05)))
    img_return = ImageTk.PhotoImage(resize_image_return)

    def return_clicked():
        split_window.destroy()
        window_root()
    
    return_button = tk.Button(
        split_window
        # ,text='RETURN'
        # ,font=("Franklin Gothic bond", 10)
        ,image = img_return
        ,background='#FF1C3B'
        ,foreground='black'
        ,command=return_clicked
    )
    return_button.place(relx=0.065, rely=.05,relheight=.05,relwidth=.05, anchor=tk.N)

    check_all_file = tk.IntVar()
    check_but_all_file = tk.Checkbutton(split_window, text = 'Join all the ranges into one pdf file', variable = check_all_file,background='#FF1C3B',foreground='black')
    check_but_all_file.place(relx=0.38, rely=.65,relheight=0.05,relwidth=.35, anchor=tk.E)

    def select_clicked():
        global filename_split 
        filename_split = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("pdf files", "*.pdf"), ("all files", "*.*")))
        print(filename_split)
    
    select_button = tk.Button(
        split_window
        ,text='SELECT FILE'
        ,font=("Franklin Gothic bond", 10)
        ,background='#FF1C3B'
        ,foreground='black'
        ,command=select_clicked
    )
    select_button.place(relx=0.3, rely=.3,relheight=0.075,relwidth=.175, anchor=tk.E)
    Tip_select = Hovertip(select_button,'Select a pdf file to split.')


    def add_clicked():
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
        if (initial_page.get().isdigit()):
            if int(initial_page.get()) == 0:
                tk.messagebox.showerror(title="ERROR", message="Pagina inicial no puede empezar de 0")
                error = True
            else:
                if error != True :
                    error = False
                pass
        else:
            tk.messagebox.showerror(title="ERROR", message="Ingresa una pagina inicial")
            error = True
            
        if (final_page.get().isdigit()):
            if error != True :
                    error = False
            pass
        else:
            tk.messagebox.showerror(title="ERROR", message="Ingresa una pagina final")
            error = True
            
        if (final_page.get().isdigit() and int(final_page.get())>count):
            tk.messagebox.showerror(title="ERROR", message="Sobrepasaste la pagina final")
            error = True
        else:
            if error != True :
                    error = False
            pass
            
        if(final_page.get().isdigit() and initial_page.get().isdigit() and int(final_page.get()) < int(initial_page.get()) ):
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
            listbox.delete(0, tk.END)
            size_temp = len(filename_split_list)
            filename_split_list.append("Split"+str(size_temp+1)+".pdf "+"page "+initial_page.get()+" to page "+final_page.get())
            listbox.insert(0, *filename_split_list)
            filename_split_dict["Split"+str(size_temp+1)+".pdf "]=(int(initial_page.get())-1,int(final_page.get()))
            
    add_button = tk.Button(
        split_window
        ,text='ADD RANGE'
        ,font=("Franklin Gothic bond", 10)
        ,background='#FF1C3B'
        ,foreground='black'
        ,command=add_clicked
    )

    add_button.place(relx=0.3, rely=.55,relheight=0.075,relwidth=.175, anchor=tk.E)
    Tip_add = Hovertip(add_button,'Click to confirm the split range.')

    def split_clicked():
        global filename_split_list
        global save_directory
        global filename_split_dict
        global filename_split 
        global error

        if len(filename_split_list)<1:
            tk.messagebox.showerror(title="ERROR", message="No hay archivos seleccionados")
        else:
            if (check_all_file.get() == 1):
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


    
    split_button = tk.Button(
        split_window
        ,text='SPLIT-SAVE FILES'
        ,font=("Franklin Gothic bond", 10)
        ,background='#FF1C3B'
        ,foreground='black'
        ,command=split_clicked
    )
    split_button.place(relx=0.3375, rely=.75,relheight=0.075,relwidth=.25, anchor=tk.E)
    Tip_merge = Hovertip(split_button,'Click to split and save the splited pdf´s.')

    def clear_clicked():
        global filename_split_list
        global filename_split_dict
        global filename_split

        listbox.delete(0, tk.END)
        filename_split_list = []
        filename_split_dict = {}
        filename_split = ""

    clear_button = tk.Button(
        split_window
        ,text='CLEAR FILES'
        ,font=("Franklin Gothic bond", 10)
        ,background='#FF1C3B'
        ,foreground='black'
        ,command=clear_clicked
    )
    clear_button.place(relx=0.62, rely=.85,relheight=0.075,relwidth=.175, anchor=tk.W)

    Tip_clear = Hovertip(clear_button,'Click to clear all the selected files.')

    split_window.mainloop()

window_root()