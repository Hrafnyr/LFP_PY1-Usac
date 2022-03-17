
from listas import lista
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as stxt
from tkinter import filedialog
from tkinter import messagebox as MessageBox

data = lista()

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
        ruta = archivo1.name #Obtener ruta
        t = open(ruta, 'r',encoding='utf-8')  #Si se seleccionó, leer el archivo y cerrarlo
        texto = t.read()
        mostrarDatos(texto)
        t.close()
        return texto

def mostrarDatos(texto):
    txt.insert(INSERT,texto) #insertar texto en el scrolledtext
    return texto

def analizarTexto():
    data.eliminarTodo()
    t = txt.get("1.0", tk.END)
    fila = 1
    columna = 1
    x = 0   #Indice
    estado = 0 #Estado inicial
    lexema = ""

    while x < len(t):
        if estado == 0:
            if t[x] == " ": #No se analiza espacio,salto de línea ni tabulación
                x+=1
                columna +=1
            elif t[x] == "\n":
                fila +=1
                columna =1
                x+=1
            elif t[x] == "\t":
                x+=1
                columna +=8
            elif t[x].isalpha(): #Estado que guarda caracteres del alfabeto y lo manda al estado 1
                lexema = ""
                lexema+= t[x]
                x+=1
                estado = 1
                columna +=1
            elif t[x] == "~" or t[x]==">" or t[x]=="[" or t[x]=="<" or t[x]==":" or t[x]=="," or t[x]=="]":
                lexema = t[x]
                estado = 2
                
            elif t[x] == "\"": #Cadenas con "" y ''
                columna +=1
                lexema=""
                x+=1
                estado = 3
            elif t[x] == "\'":
                columna +=1
                lexema=""
                x+=1
                estado = 4
            else:
                data.insertError(t[x],"Caracter desconocido",fila,columna)
                columna +=1
                x+=1
                estado = 0 
            
        elif estado == 1: #Termina de concatenar los caracteres de tipo alfabeto y guarda tokens de palabra reservada
            if t[x].isalpha():
                lexema+= t[x]
                x+=1     
                columna +=1         
                estado = 1
            else:
                if lexema =="formulario":
                    data.insertarToken("Token palabra reservada",lexema,fila,columna)
                elif lexema =="tipo":
                    data.insertarToken("Token palabra reservada",lexema,fila,columna)
                elif lexema =="valores":
                    data.insertarToken("Token palabra reservada",lexema,fila,columna)
                elif lexema =="fondo":
                    data.insertarToken("Token palabra reservada",lexema,fila,columna)
                elif lexema =="valor":
                    data.insertarToken("Token palabra reservada",lexema,fila,columna)
                elif lexema =="evento":
                    data.insertarToken("Token palabra reservada",lexema,fila,columna)
                else:
                    data.insertError(lexema,"Palabra mal escrita",fila,columna)
                estado=0
                
        elif estado == 2: #Estado de símbolos
            if t[x] == "~" or t[x]==">" or t[x]=="[" or t[x]=="<" or t[x]==":" or t[x]=="," or t[x]=="]":
                lexema=t[x]
                data.insertarToken("Token tipo símbolo",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 2
            else:
                estado = 0
        elif estado == 3: #Estado para cadenas e identificadores " "
            if  t[x] != "\"":
                lexema+=t[x]
                x+=1
                columna +=1
                estado = 3
            
            else:   
                if lexema =="etiqueta":
                    data.insertarToken("Token identificador",lexema,fila,columna)
                elif lexema =="texto":
                    data.insertarToken("Token identificador",lexema,fila,columna)
                elif lexema =="grupo-radio":
                    data.insertarToken("Token identificador",lexema,fila,columna)
                elif lexema =="grupo-option":
                    data.insertarToken("Token identificador",lexema,fila,columna)
                elif lexema =="boton" or lexema =="botón":
                    data.insertarToken("Token identificador",lexema,fila,columna)
                elif lexema =="evento":
                    data.insertarToken("Token identificador",lexema,fila,columna)
                else: data.insertarToken("Token cadena",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 0
        
        elif estado == 4: #Estado para cadenas e identificadores con ''
            if  t[x] != "\'":
                lexema+=t[x]
                columna +=1
                x+=1
                estado = 4
            
            else:
                data.insertarToken("Token cadena",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 0

    data.mostrarErrores()
    data.mostrarTokens()

def verReportes():
    op = listaReportes.get()
    if op =="Reporte de tokens":
        data.reporteTokens()
    

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
botonAnalizar = tk.Button(text="Analizar", command=analizarTexto)
botonAnalizar.place(x=25, y=350)
botonAnalizar.config(font=("Courier", 12), bg="#0A1246",fg="white",width=10)

#lista de Reportes
listaReportes = ttk.Combobox(root, width="17",state="readonly")
listaReportes.place(x=500, y=20)

reportes = ['Reporte de errores', 'Reporte de tokens','Manual de usuario','Manual técnico']
listaReportes['values'] = reportes

#Botón 3
botonAceptar = tk.Button(text="Aceptar", command=verReportes)
botonAceptar.place(x=630, y=18)
botonAceptar.config(font=("Courier", 10), bg="#0A1246",fg="white",width=6)

#Area de texto
txt = stxt.ScrolledText(root,width=78, height=15)
txt.place(x=25, y=75)

#Visualización
root.mainloop()

