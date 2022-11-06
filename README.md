# PDF_APP


## PDF APP USING PYTHON


This is an app made with python, you can merge, and split pdf files. By cloning this repo you can run the file named "PDF_APP.exe" that is inside the folder "dist" If you want to take a look to the code you can look at the ".py" files.

## PDF APP SCOURCE CODE

This app was made with two approaches one using OOP paradigm and other using Functional programming, you can look at the ".py" files some says "POO" and others says "STR". Now each approach has four files: "TEST_1","TEST_2","TEST_3" and "GENERAL_TEST", each test have a layout of the app and the general test have the implementation of the three layouts. 

If you also want to run and make modifications to the code there is a file named "requierements.txt" just type on your terminal "pip install requirements.txt" and it will install all the librarys you need (before that install python).

If you made modifications to the source code and you want to recreate the ".exe" file, remember to do the following steps:

- Your final code save it on the ".py" file named "PDF_APP.py".
- Once you have it saved with that name, type on the terminal the following comand "pyinstaller PDF_APP.py --onefile -w", this is goin to create the "dist", "build" folder and the ".spec" file.
- Your already have the ".exe" file on the "dist" folder but you need to add the images you are going to use, for that inside the ".spec" file add the images like this:

        "a.datas += [('IMAGENES\\ICONO.ico','C:\\Users\\ivan_\\Escritorio\\Proyectos\\PDF_APP\\PDF_APP\\IMAGENES\\ICONO.ico', "DATA"),
            ('IMAGENES\\ICONO.png','C:\\Users\\ivan_\\Escritorio\\Proyectos\\PDF_APP\\PDF_APP\\IMAGENES\\ICONO.png', "DATA"),
            ('IMAGENES\\Merge_Vertical.png','C:\\Users\\ivan_\\Escritorio\\Proyectos\\PDF_APP\\PDF_APP\\IMAGENES\\Merge_Vertical.png', "DATA"),
            ('IMAGENES\\Split_Horizontal.png','C:\\Users\\ivan_\\Escritorio\\Proyectos\\PDF_APP\\PDF_APP\\IMAGENES\\Split_Horizontal.png', "DATA"),
            ('IMAGENES\\return.png','C:\\Users\\ivan_\\Escritorio\\Proyectos\\PDF_APP\\PDF_APP\\IMAGENES\\return.png', "DATA")
            ]"
- Now save the ".spec" file and type the followinf command "pyinstaller PDF_APP.spec".




