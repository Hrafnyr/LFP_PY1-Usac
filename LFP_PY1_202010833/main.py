
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as stxt
from tkinter import filedialog
from tkinter import messagebox as MessageBox



def abrirDocumentoForm():
    Tk().withdraw() #Remover ventana
    archivo1 = filedialog.askopenfile(       #Abrir ventana
        title = "Seleccione un archivo",   #Información solicitada
        initialdir = "./",
        filetypes = [
            ("Archivos .form", "*.form"),
            ("Archivos .lfp", "*.lfp"),
            ("Todos los archivos",  "*.*")
        ]
    )

    if archivo1 is None:  #Verifica que si existe selección de archivos
        MessageBox.showinfo('Atención','No se seleccionó ningún archivo')
        return None
    else:
        ruta = archivo1.name
        t = open(ruta, 'r',encoding='utf-8')  #Si se seleccionó, leer el archivo y cerrarlo
        texto = t.read()
        mostrarDatos(texto)
        t.close()
        return texto

def mostrarDatos(texto):
    txt.insert(INSERT,texto)

#Interfaz gráfica
root = tk.Tk()                 #Raiz           
#Configuración
root.title('Menú principal')      
root.geometry('700x400')
root.resizable(0,0)
root.config(bg="#87F7EC")  
root.eval('tk::PlaceWindow . center')

#Botón 1
botonCargar = tk.Button(text="Cargar archivo", command=abrirDocumentoForm)
botonCargar.place(x=25, y=20)
botonCargar.config(font=("Courier", 12), bg="#0A1246",fg="white",width=15)

#Botón 2
botonAnalizar = tk.Button(text="Analizar")
botonAnalizar.place(x=25, y=350)
botonAnalizar.config(font=("Courier", 12), bg="#0A1246",fg="white",width=10)

#lista de Reportes
listaReportes = ttk.Combobox(root, width="17",state="readonly")
listaReportes.place(x=500, y=20)

reportes = ['Reporte de errores', 'Reporte de tokens','Manual de usuario','Manual técnico']
listaReportes['values'] = reportes

#Botón 3
botonAceptar = tk.Button(text="Aceptar")
botonAceptar.place(x=630, y=18)
botonAceptar.config(font=("Courier", 10), bg="#0A1246",fg="white",width=6)

#Area de texto
txt = stxt.ScrolledText(root,width=78, height=15)
txt.place(x=25, y=75)

#Visualización
root.mainloop()