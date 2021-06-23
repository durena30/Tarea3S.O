import datetime
import os
import subprocess
import shutil
import time
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
        directorio="Usuarios/"+self.Nombre+"/Documentos"
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

    def RecuperarArchivo(self,tipo):#obtiene la ultima version guardada
        cont=0
        finish=False
        if tipo==1:
            tipoCarp="Temp"
        if tipo==2:
            tipoCarp="Perm"
        path="Usuarios/"+self.Nombre+"/"+tipoCarp

        Ruta=list()
        Ruta.append(path)
        while(finish!=True):
            print("\033[2J\033[1;1f") 
            lista=os.listdir(path)
            if path=="Usuarios/"+self.Nombre+"/"+tipoCarp or path=="Usuarios/"+self.Nombre+"/"+tipoCarp+"/" :
                print("0.Salir")
            else:
                print("0.Atras")
            for x in lista:
                print(str(cont+1)+"."+x)
                cont+=1
            opcion= int(input("Digite el numero de su eleccion: "))
            if opcion==0:
                if path=="Usuarios/"+self.Nombre+"/"+tipoCarp or path=="Usuarios/"+self.Nombre+"/"+tipoCarp+"/":
                    finish=True
                    break
                pathaux=""
                Ruta.pop(len(Ruta)-1)
                for x in Ruta:
                    pathaux+=x+"/"
                path=pathaux
                print(path)
                
                # time.sleep(2)
                lista.clear()
                cont=0
            else:
                Ruta.append(lista[opcion-1])
                path+="/"+lista[opcion-1]
                lista.clear()
                cont=0
                
                if path.find(".txt")!=-1:
                    path1="Usuarios/"+self.Nombre+"/Documentos/"
                    OldFileName=Ruta[2]
                    NewFileName=Ruta[1]
                    if not os.path.isfile(path1+NewFileName+".txt"):
                        shutil.move(path,path1)
                        os.rename(path1+OldFileName,path1+NewFileName+".txt")
                    if os.path.isfile(path1+NewFileName+".txt"):
                        aactual=""
                        with open(path) as temp_f:
                            archivo = temp_f.readlines()
                            for line in archivo:
                                aactual+=line
                        reg= open(path1+NewFileName+".txt","w")
                        reg.write(aactual)
                        reg.close()
                        os.remove(path)
                        path="Usuarios/"+self.Nombre+"/"+tipoCarp

                    if tipo==1:
                        direccion="Usuarios/"+self.Nombre+"/Archtemp.txt"
                    if tipo==2:
                        direccion="Usuarios/"+self.Nombre+"/Archperm.txt"
                    registros= list()
                    with open(direccion) as temp_f:
                        archivo = temp_f.readlines()
                        for line in archivo:
                            registros.append(line)
                    for i in range(len(registros)-1):
                        if registros[i]==OldFileName+"/"+NewFileName:
                            registros.pop(i)

                    arch=open(direccion,"w")                      
                    for x in registros:
                        arch.write(x)
                    arch.close()

                    

    def VerCarpetas(self):
        cont=0
        finish=False
        path="Usuarios/"+self.Nombre
        Ruta=list()
        Ruta.append(path)
        while(finish!=True):
            print("\033[2J\033[1;1f") 
            lista=os.listdir(path)
            if path=="Usuarios/"+self.Nombre or path=="Usuarios/"+self.Nombre+"/":
                print("0.Salir")
            else:
                print("0.Atras")
            for x in lista:
                print(str(cont+1)+"."+x)
                cont+=1
            
            opcion= int(input("Digite el numero de su eleccion: "))
            
            if opcion==0 and (path =="Usuarios/"+self.Nombre or path =="Usuarios/"+self.Nombre+"/"):# si el path se devuelve hasta el inicio o esta en el inicio se sale del Ver Carpetas
                finish=True
                break
            if opcion==0:#El path se devuelve a la direccion anterior
                path=""
                Ruta.pop(len(Ruta)-1)
                for x in Ruta:
                    path+=x+"/"
                print(path)
                lista.clear()
                cont=0
            else:
                Ruta.append(lista[opcion-1])
                path+="/"+lista[opcion-1]
                lista.clear()
                cont=0
                if path.find(".txt")!=-1:
                    subprocess.run(["notepad.exe",path])
                    path="Usuarios/"+self.Nombre
            
    def Commit(self, op): #Transfiere la ultima actualizacion de los archivos temporales a los Permanentes
        lista= list()
        concat='Usuarios/'+self.Nombre+'/Archtemp.txt'
        concat2='Usuarios/'+self.Nombre+'/Archperm.txt'
        path="Usuarios/"+self.Nombre+"/Temp/"
        path1="Usuarios/"+self.Nombre+"/Perm/"
        lista=os.listdir(path)
        path+=lista[op]
        print(path)

        Carpeta=lista[op]
        lista.clear()
        lista=os.listdir(path)
        print(lista)
        path+="/"
        NombreArchivo=lista.pop(len(lista)-1)
        print(NombreArchivo)
        shutil.move(path+NombreArchivo,path1+Carpeta+"/"+NombreArchivo)

        registro= open(concat, 'w')
        for x in lista:
            registro.write(x)
        registro.close()
        registro= open(concat2, 'a')
        registro.write(Carpeta+"/"+NombreArchivo)
        registro.close()        
