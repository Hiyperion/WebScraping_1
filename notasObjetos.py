class Casa:
    #metodo constructor
    def __init__(self,color):
        self.color=color
        self.consumoDeLuz=0
        self.consumoDeAgua=0
    def pintar(self,newColor):
        self.color=newColor
    def encenderLuz(self):
        self.consumoDeLuz += 10
    def abrirDucha(self):
        self.consumoDeAgua += 10
    def tocarTimbre(self):
        print("Ring Ring")
        self.consumoDeLuz +=2 


class Mansion(Casa):
    def encenderLuz(self):
        self.consumoDeLuz += 50
    def abrirDucha(self):
        self.consumoDeAgua += 50
    def tocarTimbre(self):
        print("ding dong")
        self.consumoDeLuz += 2


miCasa=Casa("Rojo")

# miCasa.tocarTimbre()
# miCasa.encenderLuz()
# miCasa.abrirDucha()
# miCasa.pintar("azul")
# print(miCasa.consumoDeLuz)
# print(miCasa.consumoDeAgua)
# print(miCasa.color)


miMansion=Mansion("Negro")
miMansion.tocarTimbre()
miMansion.pintar("Verde")

print(miMansion.color)