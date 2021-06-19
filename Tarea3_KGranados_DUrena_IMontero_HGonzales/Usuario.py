import datetime
import os
import subprocess
import shutil
class Usuario:
    def __init__(self) -> None:
        pass
    def __init__(self, Nombre, Contra,Permiso):
        self.Nombre=Nombre
        self.Contra=Contra
        self.Permiso=Permiso
        self.DatoActual=""
        self.Temporal=""
        self.Permanete=""
        self.NombreCarpeta=""
    def toString(self):
        sstream="Nombre: "+self.Nombre+"\nContraseña: "+self.Contra+"\nPermiso: "+str(self.Permiso)+"\n"
        return str(sstream)
    def CrearCarpeta(self):
        direccion="Usuarios/"+self.Nombre+"/"+input("Digite el nombre de la Carpeta: ")
        try:
            os.mkdir(direccion)
        except:
            print("No se pudo crear la carpeta en la direccion: "+direccion)
    def CrearArchivo(self, name):
        direccion="Usuarios/"+self.Nombre+"/Documentos/"+name+".txt"
        self.Temporal="Usuarios/"+self.Nombre+"/Temp/"+name
        self.Permanete="Usuarios/"+self.Nombre+"/Perm/"+name
        self.NombreCarpeta=name
        registro= open(direccion, 'w')
        registro.write('')
        registro.close()
        subprocess.run(["notepad.exe",direccion])
        
        os.mkdir(self.Temporal)#Crea una carpeta personal para los datos de cada archivo
        os.mkdir(self.Permanete) 

        with open(direccion) as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                self.DatoActual+=line
    def Editar(self):
        doc=list()
        txt=list()
        cont=0
        directorio="Usuarios/"+self.Nombre
        print("\t***Archivos***\n\n")
        with os.scandir(directorio) as ficheros:
            for fichero in ficheros:
                doc.append(directorio+"/"+fichero.name)
                print(str(cont+1)+"."+fichero.name)
                cont+=1
        opcion= int(input("\n\nDigite el numero de su eleccion: "))
        directorio=doc[opcion-1]
        
        if str(directorio).find(".txt") !=-1:
            slash=0
            carpeta=""
            subprocess.run(["notepad.exe",directorio])
            with open(directorio) as temp_f:
                archivo = temp_f.readlines()
                for line in archivo:
                    self.DatoActual+=line
                for x in directorio:
                    if slash >=3:
                        carpeta+=x
                    if x=="/":
                        slash+=1
                self.NombreCarpeta=carpeta[0:len(carpeta)-4]
                print (carpeta+"\n\n")
        else:
            cont=0
            slash=0
            carpeta=""
            print("\033[2J\033[1;1f")
            print("\t***Archivos***\n\n")
            print("Los archivos son: \n")
            with os.scandir(directorio) as ficheros:
                for fichero in ficheros:
                    txt.append(directorio+"/"+fichero.name)
                    print(str(cont+1)+"."+fichero.name)
                    cont+=1
            opcion= int(input("\n\nDigite el numero de su eleccion: "))
            directorio=txt[opcion-1]
            if  str(directorio).find(".txt")!=-1:
                subprocess.run(["notepad.exe",directorio])
                with open(directorio) as temp_f:
                    archivo = temp_f.readlines()
                    for line in archivo:
                        self.DatoActual+=line
                    for x in directorio:
                        if slash >=3:
                            carpeta+=x
                        if x=="/":
                            slash+=1
                    self.NombreCarpeta=carpeta[0:len(carpeta)-4]
                    print (carpeta+"\n\n")
    def Eliminar(self):
        doc=list()
        txt=list()
        cont=0
        directorio="Usuarios/"+self.Nombre
        print("\t***Archivos***\n\n")
        with os.scandir(directorio) as ficheros:
            for fichero in ficheros:
                doc.append(directorio+"/"+fichero.name)
                print(str(cont+1)+"."+fichero.name)
                cont+=1
        opcion= int(input("Digite el numero de su eleccion: "))
        directorio=doc[opcion-1]
        if str(directorio).find(".txt") !=-1:
            os.remove(directorio)
            print("Se ha removido el siguiente archivo: "+directorio)
        else:
            contador=0
            print("\033[2J\033[1;1f") 
            print("Los archivos son: \n")
            with os.scandir(directorio) as ficheros:
                for fichero in ficheros:
                    txt.append(directorio+"/"+fichero.name)
                    print(str(contador+1)+"."+fichero.name)
                    contador+=1
            opcion= int(input("Digite el numero de su eleccion: "))
            directorio=txt[opcion-1]
            if  str(directorio).find(".txt")!=-1:
                os.remove(directorio)
                print("Se ha removido el siguiente archivo: "+directorio)
        

            
    