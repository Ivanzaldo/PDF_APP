from distutils.log import error
import tkinter as tk
from tkinter import ttk # FOR WIDGETS
from tkinter.messagebox import showinfo
from tkinter import filedialog
from idlelib.tooltip import Hovertip


from PIL import Image, ImageTk
from PyPDF2 import PdfMerger
from PyPDF2 import PdfFileReader


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
        global filename_merge 
        print(filename_merge)
        # merge_window.destroy()
        # window_root()
    
    return_button = tk.Button(
        merge_window
        # ,text='RETURN'
        # ,font=("Franklin Gothic bond", 10)
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

window_merge()