from guardarToken import token1
from errores import error

class lista():
    def __init__(self):
        self.listaTokens = [] #lista que guarda los tokens
        self.listaErrores = [] #lista que guarda los errores
    
    def insertarToken(self, token,valor,fila,columna):
        self.listaTokens.append(token1(token,valor,fila,columna))
    
    def insertError(self, caracter,fila,columna):
        self.listaErrores.append(error(caracter,fila,columna))
        
    def mostrarTokens(self): #Metodo de prueba para verificar el correcto guardado de los tokens
        i:token1
        for i in self.listaTokens:
            r =i.enviarTokens()
            print(r)

    def mostrarErrores(self): #Metodo de prueba para verificar el correcto guardado de los errores
        i:error
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                s = i.enviarErrores()
                print(s)
