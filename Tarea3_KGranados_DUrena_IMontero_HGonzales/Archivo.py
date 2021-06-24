import msvcrt as ms
class Archivo:
    def __init__(self):
        self.Nombre=""
        self.Texto=""
        self.Direccion=""
    def Editar(self, texto):
        finish=False
        print(texto)
        while not finish:
            if ms.kbhit() :
                print("\033[2J\033[1;1f")
                if ord(ms.getch())==8:
                    texto=texto[0:len(texto)-1]
                if ord(ms.getch())==13:
                    texto= texto+"\n"
                else:
                    texto=texto+ms.getwch()
                    print(ms.getwch())
                print(texto)
                print(ms.getch())

a=Archivo()
a.Texto="Hola que tal mi nombre es dario"
a.Editar(a.Texto)