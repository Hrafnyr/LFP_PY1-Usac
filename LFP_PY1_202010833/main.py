

from listas import lista
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as stxt
from tkinter import filedialog
from tkinter import messagebox as MessageBox
import webbrowser


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
    txt.delete("1.0", "end") 
    txt.insert(INSERT,texto) #insertar texto en el scrolledtext
    data.botonEvento(texto)
    return texto

def analizarTexto(): 
    data.eliminarTodo()
    t = txt.get("1.0", tk.END)
    data.botonEvento(t)
    fila = 1
    columna = 1
    x = 0   #Indice
    estado = 0 #Estado inicial
    lexema = ""

    while x < len(t):
        if estado == 0:
            if t[x] == " ": #No se analiza espacio
                x+=1
                columna +=1
            elif t[x] == "\n": #No se analiza salto de línea 
                columna =1
                fila+=1
                x+=1
            elif t[x] == "\t": #No se analiza tabulación
                x+=1
                columna +=8
            elif t[x].isalpha(): #Si viene una letra se va al estado 1
                lexema = ""
                lexema+= t[x]
                x+=1
                estado = 1
                columna +=1
            elif t[x] == "~" or t[x]==">" or t[x]=="[" or t[x]=="<" or t[x]==":" or t[x]=="," or t[x]=="]": #Si viene un símbolo se va al estado 2
                lexema = t[x]
                estado = 2
            elif t[x] == "\"": #Si vienen comillas dobles  se va al estado 3
                columna +=1
                lexema=""
                x+=1
                estado = 3
            elif t[x] == "\'": #Si vienen comillas simples  se va al estado 4
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
            if t[x].isalpha() or t[x]=="_" or t[x].isdigit():
                lexema+= t[x]
                x+=1     
                columna +=1         
                estado = 1
            else:
                if lexema =="formulario":
                    data.insertarToken("Token palabra reservada",lexema,fila,columna)
                elif lexema =="tipo":
                    data.insertarToken("Token ID tipo",lexema,fila,columna)
                elif lexema =="valores":
                    data.insertarToken("Token ID valores",lexema,fila,columna)
                elif lexema =="fondo":
                    data.insertarToken("Token ID fondo",lexema,fila,columna)
                elif lexema =="valor":
                    data.insertarToken("Token ID valor",lexema,fila,columna)
                elif lexema =="evento":
                    data.insertarToken("Token ID evento",lexema,fila,columna)
                elif lexema =="info":
                    data.insertarToken("Token ID info",lexema,fila,columna)
                elif lexema =="entrada":
                    data.insertarToken("Token ID entrada",lexema,fila,columna)
                else:
                    data.insertarToken("Token ID",lexema,fila,columna)
                estado=0
        elif estado == 2: #Estado de símbolos
            if t[x] == "~":
                lexema=t[x]
                data.insertarToken("Token símbolo virgulilla",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 2
            elif t[x]==">":
                lexema=t[x]
                data.insertarToken("Token símbolo mayor que",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 2
            elif t[x]=="[":
                lexema=t[x]
                data.insertarToken("Token símbolo corchete abertura",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 2
            elif t[x]=="<":
                lexema=t[x]
                data.insertarToken("Token símbolo menor que",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 2
            elif t[x]==":":
                lexema=t[x]
                data.insertarToken("Token símbolo dos puntos",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 2
            elif t[x]==",":
                lexema=t[x]
                data.insertarToken("Token símbolo coma",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 2
            elif t[x]=="]":
                lexema=t[x]
                data.insertarToken("Token símbolo corchete cierre",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 2
            else:
                estado = 0
        elif estado == 3: #Estado para cadenas  " "
            if  t[x] != "\"":
                lexema+=t[x]
                x+=1
                columna +=1
                estado = 3       
            else:   
                if lexema =="etiqueta":
                    data.insertarToken("Token cadena etiqueta",lexema,fila,columna)
                elif lexema =="texto":
                    data.insertarToken("Token cadena texto",lexema,fila,columna)
                elif lexema =="grupo-radio":
                    data.insertarToken("Token cadena g-radio",lexema,fila,columna)
                elif lexema =="grupo-option":
                    data.insertarToken("Token cadena g-option",lexema,fila,columna)
                elif lexema =="boton" or lexema =="botón":
                    data.insertarToken("Token cadena boton",lexema,fila,columna)
                else: data.insertarToken("Token cadena comilla doble",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 0
        elif estado == 4: #Estado para cadenas con ''
            if  t[x] != "\'":
                lexema+=t[x]
                columna +=1
                x+=1
                estado = 4
            
            else:
                data.insertarToken("Token cadena simple",lexema,fila,columna)
                x+=1
                columna +=1
                estado = 0

    print('Errores:')
    data.mostrarErrores()
    print('Tokens:')
    data.mostrarTokens()

def verReportes():
    op = listaReportes.get()
    if op =="Reporte de tokens":
        data.reporteTokens()
    elif op =="Reporte de errores":
        data.reporteErrores()
    elif op =="Manual de usuario":
        path = r"D:\Moises\Documents\USAC\SEMESTRE 5\lenguajes formales 1\Proyecto 1\LFP_PY1_202010833\Documentación\Manual de usuario.pdf"
        webbrowser.open_new(path)
    elif op =="Manual técnico":
        path = r"D:\Moises\Documents\USAC\SEMESTRE 5\lenguajes formales 1\Proyecto 1\LFP_PY1_202010833\Documentación\Manual Técnico.pdf"
        webbrowser.open_new(path)
    else:
        print('NONE')
    
def verHtml():
    t = True
    if t:
        data.crearHtml()

#------------------------------------------------Interfaz gráfica
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

#Botón 4
botonEjecutar = tk.Button(text="Ejecutar",command=verHtml)
botonEjecutar.place(x=400, y=350)
botonEjecutar.config(font=("Courier", 12), bg="#0A1246",fg="white",width=10)

#Botón 5
botonEjecutar = tk.Button(text="Salir",command=exit)
botonEjecutar.place(x=550, y=350)
botonEjecutar.config(font=("Courier", 12), bg="#0A1246",fg="white",width=10)

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

