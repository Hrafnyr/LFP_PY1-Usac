
class error: #Guarda los tokens analizados
    def __init__(self, caracter,tipo,fila,columna):
        self.caracter = caracter
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def enviarErrores(self):
        return [self.caracter,self.tipo,self.fila, self.columna]