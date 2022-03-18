from math import radians
from guardarToken import token1
from errores import error
from tkinter import messagebox as MessageBox
import webbrowser


class lista():
    def __init__(self):
        self.listaTokens = [] #lista que guarda los tokens
        self.listaErrores = [] #lista que guarda los errores
    
    def insertarToken(self, token,valor,fila,columna):
        self.listaTokens.append(token1(token,valor,fila,columna))
    
    def insertError(self, caracter,tipo,fila,columna):
        self.listaErrores.append(error(caracter,tipo,fila,columna))
        
    def mostrarTokens(self): #Metodo de prueba para verificar el correcto guardado de los tokens
        i:token1
        for i in self.listaTokens:
            r =i.enviarTokens()
            print(r)

    def mostrarErrores(self): #Metodo de prueba para verificar el correcto guardado de los errores
        i:error
        if len(self.listaErrores)==0:
            print('No hay errores')
            MessageBox.showinfo('Mensaje','No hay errores')
        else:
            MessageBox.showerror('Atención','Se encontraron errores')
            for i in self.listaErrores:
                s = i.enviarErrores()
                print(s)

    def eliminarTodo(self):
        del self.listaErrores[:]
        del self.listaTokens[:]
    
    def reporteTokens(self):
        if len(self.listaErrores)==0:
            print('No hay información')
            MessageBox.showinfo('Atención','No se ha analizado el texto')
        else:
            print('-------------------> Generando reporte, espere...')
            contadorReportes = 1
            name = "Reporte"+str(contadorReportes)+"Tokens.html"
            reporte = open(name, 'w')

            html_parte1 = '''
            <h2 style="text-align: center;">"Reporte de Tokens"</h2>
            <table style="width: 100%; border-collapse: collapse; border-style: solid;" border="1">
            <tbody>
            <tr>
            <td style="width: 7.56478%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">No.</span></strong></td>
            <td style="width: 7.56478%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Token</span></strong></td>
            <td style="width: 20%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Lexema</span></strong></td>
            <td style="width: 7.56478%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Fila</span></strong></td>
            <td style="width: 7.56478%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Columna</span></strong></td>
            </tr>'''
            
            html_parte2 = ''
            contador = 1
            i:token1
            for i in self.listaTokens:
                token = i.getToken()
                valor = i.getValor()
                fila =  i.getFila()
                columna = i.getColumna()

                html_parte2 += '''<tr>
            <td style="width: 7.56478%;">{}</td>
            <td style="width: 7.56478%;">{}</td>
            <td style="width: 20%;">{}</td>
            <td style="width: 7.56478%;">{}</td>
            <td style="width: 7.56478%;">{}</td>
            </tr>'''.format(contador,token,valor,fila,columna)
                contador+=1
        
            hmtl_fin = '''
            </tbody>
            </table>'''
            
            html_archivo = html_parte1 + html_parte2 + hmtl_fin

            reporte.write(html_archivo)
            reporte.close()

            print('Reporte creado con éxito')
            contadorReportes+=1
            webbrowser.open_new_tab(name)
    
    def reporteErrores(self):
        if len(self.listaErrores)==0:
            print('No hay información')
            MessageBox.showinfo('Atención','No ha analizado el texto')
        else:
            print('-------------------> Generando reporte, espere...')
            contadorReportes = 1
            name = "Reporte"+str(contadorReportes)+"Error.html"
            reporte = open(name, 'w')

            html_parte1 = '''
            <h2 style="text-align: center;">"Reporte de Errores"</h2>
            <table style="width: 100%; border-collapse: collapse; border-style: solid;" border="1">
            <tbody>
            <tr>
            <td style="width: 7.56478%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">No.</span></strong></td>
            <td style="width: 7.56478%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Caracter o token</span></strong></td>
            <td style="width: 20%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">tipo</span></strong></td>
            <td style="width: 7.56478%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Fila</span></strong></td>
            <td style="width: 7.56478%; text-align: center; border-style: solid; border-color: black; background-color: midnightblue;"><strong><span style="color: #ffffff;">Columna</span></strong></td>
            </tr>'''
            
            html_parte2 = ''
            contador = 1
            e:error
            for e in self.listaErrores:
                caracter = e.getCaracter()
                tipo = e.getTipo()
                fila = e.getFila()
                columna = e.getColumna()
                html_parte2 += '''<tr>
            <td style="width: 7.56478%;">{}</td>
            <td style="width: 7.56478%;">{}</td>
            <td style="width: 20%;">{}</td>
            <td style="width: 7.56478%;">{}</td>
            <td style="width: 7.56478%;">{}</td>
            </tr>'''.format(contador,caracter,tipo,fila,columna)
                contador+=1
        
            hmtl_fin = '''
            </tbody>
            </table>'''
            
            html_archivo = html_parte1 + html_parte2 + hmtl_fin

            reporte.write(html_archivo)
            reporte.close()

            print('Reporte creado con éxito')
            contadorReportes+=1
            webbrowser.open_new_tab(name)
    
    def crearHtml(self):


        cabecera = '''
        <!DOCTYPE html>
        <html>
        <body style="background-color:#C9FBC9;">
        <form action="ejemplo.php" method="get">
        <h1 style="text-align: center;"><strong>Formulario</strong></h1>'''

        txtEtiqueta = ""
        txtTexto = ""
        txtgRadio = ""
        txtgOption = ""
        txtBoton = ""
        htmlTxt = ""
    
        for i in range(len(self.listaTokens)): #Recorre tokens
            if self.listaTokens[i].getValor()=="<": #Abertura
                while self.listaTokens[i].getValor() !=">": #Guardará los datos dentro de <>
                    #print(self.listaTokens[i].getValor())
                    
                    if self.listaTokens[i].getValor() == "etiqueta": #Accede a etiqueta
                        e = i
                        while self.listaTokens[e].getValor() !=">": 
                            if self.listaTokens[e].getToken() == "Token cadena comilla doble":
                                htmlTxt+= '''<br><br><label><strong>{}</strong></label>'''.format(self.listaTokens[e].getValor())
                                #print('valor etiqueta:',self.listaTokens[i].getValor())
                            e+=1
                    
                    elif self.listaTokens[i].getValor() == "texto": #Accede a texto
                        contador = 0
                        e = i
                        while self.listaTokens[e].getValor() !=">"and contador<1:
                            if self.listaTokens[e].getToken() == "Token cadena comilla doble":
                                htmlTxt += '''<input type="text" name="{}" size="50" placeholder="{}">'''.format(self.listaTokens[e].getValor(),self.listaTokens[e+4].getValor())
                                #print('valor texto',self.listaTokens[i].getValor(),'-',self.listaTokens[i+4].getValor())
                                contador=2
                            e+=1

                    elif self.listaTokens[i].getValor() == "grupo-radio": #Accede a grupo radio
                        e = i
                        while self.listaTokens[e].getValor() !=">": #Guardará los datos dentro de <>
                            if self.listaTokens[e].getToken() == "Token cadena comilla doble":
                                htmlTxt+= '''  <p>{}</p>'''.format(self.listaTokens[e].getValor())
                            elif self.listaTokens[e].getToken() == "Token cadena simple":
                                htmlTxt+= '''<input type="radio" name="hm" value="h"> {}'''.format(self.listaTokens[e].getValor())
                            #print('valor:',self.listaTokens[i].getValor())
                            e+=1

                    elif self.listaTokens[i].getValor() == "grupo-option": #Accede a grupo option
                        e = i
                        while self.listaTokens[e].getValor() !=">": #Guardará los datos dentro de <>
                            if self.listaTokens[e].getToken() == "Token cadena comilla doble":
                                htmlTxt+= '''  <p>{}</p>'''.format(self.listaTokens[e].getValor())
                                htmlTxt+= '''<select name="select">'''
                            elif self.listaTokens[e].getToken() == "Token cadena simple":
                                htmlTxt+= '''<option value="value1">{}</option>'''.format(self.listaTokens[e].getValor())
                            
                            #print('valor:',self.listaTokens[i].getValor())
                            e+=1
                        htmlTxt+= '''</select>'''
                    i+=1

        final ='''</form>
        </body>
        </html>'''
        html = cabecera + htmlTxt +final

        name = "Formulario.html"
        reporte = open(name, 'w')
        reporte.write(html)
        reporte.close()
        print('Reporte creado con éxito')
        webbrowser.open_new_tab(name)

