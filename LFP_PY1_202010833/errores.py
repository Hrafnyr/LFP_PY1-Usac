
class error: #Guarda los tokens analizados
    def __init__(self, caracter,fila,columna):
        self.caracter = caracter
        self.fila = fila
        self.columna = columna

    def enviarErrores(self):
        return [self.caracter,self.fila, self.columna]