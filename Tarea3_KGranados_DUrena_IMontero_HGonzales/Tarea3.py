from Usuario import *
import os
from datetime import datetime
import shutil
import msvcrt as ms
import subprocess
import time

class   ControlVersiones:
    def __init__(self) :
        self.userslist=list()
        self.ActualUser=None
        self.doc=list()
        self.txt=list()
    def CrearCarpeta(self,nombre): #Crea por defecto las carpetas de cada usuario
        if os.path.isdir("Usuarios/")==False:
            os.mkdir("Usuarios")
        directorio="Usuarios/"+nombre
        try:
            
            os.mkdir(directorio)
            direccion=directorio+"/Archtemp.txt"
            registro= open(direccion, 'a')
            registro.close()
            direccion=directorio+"/Archperm.txt"
            registro= open(direccion, 'a')
            registro.close()

            os.mkdir(directorio+"/Temp")
            os.mkdir(directorio+"/Perm")
            os.mkdir(directorio+"/Documentos")
        except OSError:
            print("La creacion de la carpeta %s fallo" % directorio)
        else:
            print("Se ha creado la carpeta:%s"%directorio)


    def Registrar(self): # Registra un usuario
        print("\033[2J\033[1;1f")
        nombre=input("Introduzca el nombre: ")
        password=input("Introduzca la contraseña: ")
        registro= open("Usuarios.rg", 'a')
        if not self.Autenticar(nombre)and nombre != password:
            registro.write(nombre+" "+password+'\n')
            self.CrearCarpeta(nombre)
            print("%s se ha registrado de manera exitosa" %nombre)
            registro.close()
            self.userslist.clear()
            self.getUsuarios()
            time.sleep(3)
            print("\033[2J\033[1;1f")
        else:
            print("Los datos ya estan en el sistema, vuelva a intentarlo con otro nombre de usuario\n")
            registro.close()
            time.sleep(3)
            self.Registrar()


    def InicioSesion(self,name,passw):# Verifica si el usuario existe, si existe ingresa a la app sino lo envia a registrarse
        concat=str(name+" "+passw)
        usuario=False
        with open('Usuarios.rg') as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                if concat in line:
                    usuario=True
        if usuario:
            print("Inicio Sesion de forma Satisfactoria\n\n")
            for x in self.userslist:
                if x.Nombre == name:
                    self.ActualUser=x
            time.sleep(2)
            print("\033[2J\033[1;1f")
            print("0.Salir\n1.Crear Nuevo Documento\n2.Ver y Editar Documento\n3.Eliminar Documento\n4.Recuperar Archivo\n5.Crear Nueva Carpeta\n6.Ver Carpetas\n7.Ver otro Usuario\n\n")
            op=(input("Seleccione una opcion: "))
            print("\033[2J\033[1;1f")
            while int(op)!=0:
                if int(op)==1:
                    print("\t\tCreador de documentos\n\n")
                    nombre=str(input("Cual sera el nombre del documento: "))
                    self.ActualUser.CrearArchivo(nombre)
                    time.sleep(3)
                    self.Update(1,self.ActualUser.Nombre,self.ActualUser.NombreCarpeta,self.ActualUser.DatoActual)
                    self.ActualUser.DatoActual=""
                    # break
                if int(op)==2:
                    self.ActualUser.Editar()
                    self.Update(1,self.ActualUser.Nombre,self.ActualUser.NombreCarpeta,self.ActualUser.DatoActual)
                    self.ActualUser.DatoActual=""
                    # break
                if int(op)==3:
                    self.ActualUser.Eliminar()
                if int(op)==4:
                    self.ActualUser.RecuperarArchivo(1)
                if int(op)==5:
                    self.ActualUser.CrearCarpeta()
                    # break
                if int(op)==6:
                    self.ActualUser.VerCarpetas()
                if int(op)==7:
                    print("1.Si\t2.No\nDesea ingresar como administrador?\n\n")
                    option=input("Seleccione una opcion: ")
                    print("\033[2J\033[1;1f")
                    if int(option)==1:
                        nombre=str(input("Nombre de usuario: "))
                        contra=str(input("Contrasenia: "))
                        print("\033[2J\033[1;1f")
                        if nombre=="administrador" and contra=="administrador":
                            self.ActualUser.Permiso=3
                            self.VerUsuarios(self.ActualUser.Permiso)
                        else:
                            print("\033[2J\033[1;1f")
                            print("\n\n\t***No puede ingresar debido a que la contrasenia o usuario no son correctos***\n\n")
                    else:
                        self.ActualUser.Permiso=2   
                        self.VerUsuarios(self.ActualUser.Permiso)
                    # break
                print("\033[2J\033[1;1f")
                print("0.Salir\n1.Crear Nuevo Documento\n2.Ver y Editar Documento\n3.Eliminar Documento\n4.Recuperar Archivo\n5.Crear Nueva Carpeta\n6.Ver Carpetas\n7.Ver otro Usuario\n\n")
                op=(input("Seleccione una opcion: "))

        else:
            print("\033[2J\033[1;1f")
            print("\tNo Encontrado\n\tPor favor proceda a registrarse\n")
            # self.Registrar()

    def Autenticar(self,nombre): #Verifica si el usuario existe en la "bd"
        with open('Usuarios.rg') as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                if nombre in line:
                    # print("Encontrado %s" %line)
                    return True
                else:
                    # print("No Encontrado %s" %line)
                    return False


    def Update(self,tipo,nombre,carpname,dato): # Agrega archivos temporales o permanentes a sus respectivas carpetas
        now=datetime.now()
        
        filename=datetime.now().strftime("%d_%b_%Y_%H_%M_%S")
        if tipo==1:
            #Guardar el nombre del registro en el archivo
            direccionlist="Usuarios/"+nombre+"/Archtemp.txt"
            #Guardar el archivo en temp con el nombre de la fecha actual
            direccion="Usuarios/"+nombre+"/Temp/"+carpname+"/"+filename+".txt"
        if tipo==2:
            #Guardar el nombre del registro en el archivo
            direccionlist="Usuarios/"+nombre+"/Archperm.txt"
            #Guardar el archivo en temp con el nombre de la fecha actual
            direccion="Usuarios/"+nombre+"/Perm/"+carpname+"/"+filename+".txt"
        self.grabarArchivo(direccionlist,carpname+"/"+filename+".txt\n")
        self.grabarArchivo(direccion,dato)

    def grabarArchivo(self, direccion,dato):# Crea o modifica un archivo
        registro= open(direccion, 'a')
        registro.write(dato)
        registro.close()

    def RecuperarArchivo(self,nombre,tipo):#obtiene la ultima version guardada
        lista= list()
        if tipo==1:
            concat='Usuarios/'+nombre+'/Archtemp.txt'
        if tipo==2:
            concat='Usuarios/'+nombre+'/Archperm.txt'
        with open(concat) as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                lista.append(line)

        nombrearch=lista.pop(len(lista)-1)
        nombrearch=nombrearch[0:len(nombrearch)-1]
        print(lista)
        print(nombrearch)
        if tipo==1:
            filename= 'Usuarios/'+nombre+"/Temp/"+nombrearch
        if tipo==2:
            filename= 'Usuarios/'+nombre+"/Perm/"+nombrearch
        self.ObtenerArch(filename)
        os.remove(filename)
        registro= open(concat, 'w')
        for x in lista:
            registro.write(x)
        registro.close()

    def Commit(self, nombre): #Transfiere la ultima actualizacion de los archivos temporales a los Permanentes
        try:
            lista= list()
            concat='Usuarios/'+nombre+'/Archtemp.txt'
            concat2='Usuarios/'+nombre+'/Archperm.txt'
            with open(concat) as temp_f:
                archivo = temp_f.readlines()
                for line in archivo:
                    lista.append(line)
            nombrearch=lista.pop(len(lista)-1)
            nombrearch=nombrearch[0:len(nombrearch)-1]

            print(lista)
            print(nombrearch)
            filedir= 'Usuarios/'+nombre+"/Temp/"+nombrearch
            filedir2='Usuarios/'+nombre+"/Perm/"+nombrearch
            
            self.ObtenerArch(filedir)
            
            shutil.move(filedir,filedir2)
            self.grabarArchivo(concat2,nombrearch+"\n")
            # os.remove(concat)
            registro= open(concat, 'w')
            for x in lista:
                registro.write(x)
            registro.close()
        except:
            print("\n\nNo se encuentra ningun Backup\n\n")

    def ObtenerArch(self,direccion):

        registro= open(direccion, 'r')
        print(registro.read())
        registro.close()

    def Principal(self):
        
        print("\033[2J\033[1;1f")
        print(chr(27)+"[1;30;47m"+"\t\t***BIENVENIDO AL SISTEMA DE CONTROL DE VERSIONES***\n\n\n"+'\033[0;m')
        print(chr(27)+"[1;31m"+"\t0) Salir\n"+chr(27)+"[1;32m"+"\t1) Iniciar Sesion\n"+chr(27)+"[1;33m"+"\t2) Registrarse\n"+'\033[0;m'+'\033[0;m'+"\t3) Ver Usuarios\n"+'\035')
        print(chr(27)+"[1;30;47m"+"**Si no posee cuenta favor registrarse**\n"+'\033[0;m')
        op=int(input("Seleccione una opcion: "))
        print(op)
        while(op!=0):
            print("\033[2J\033[1;1f")
            if op==1:
                nombre=input("Introduzca el nombre: ")
                password=input("Introduzca la contraseña: ")
                self.InicioSesion(nombre,password)
            elif op==2:
                self.Registrar()
            elif op==3:
                self.VerUsuarios(1)
            print("\033[2J\033[1;1f")
            print(chr(27)+"[1;30;47m"+"\t\t***BIENVENIDO AL SISTEMA DE CONTROL DE VERSIONES***\n\n\n"+'\033[0;m')
            print(chr(27)+"[1;31m"+"\t0) Salir\n"+chr(27)+"[1;32m"+"\t1) Iniciar Sesion\n"+chr(27)+"[1;33m"+"\t2) Registrarse\n"+'\033[0;m'+'\033[0;m'+"\t3) Ver Usuarios\n"+'\033[0;m')
            print(chr(27)+"[1;30;47m"+"**Si no posee cuenta favor registrarse**\n"+'\033[0;m')
            op=int(input("Seleccione una opcion: "))
    def Eliminar(self,permiso):
        if permiso==3:
            opcion= int(input("Digite el numero de su eleccion: "))
            directorio=self.doc[opcion-1]
            if str(directorio).find(".txt") !=-1:
                os.remove(directorio)
                print("Se ha removido el siguiente archivo: "+directorio)
            else:
                contador=0
                print("\033[2J\033[1;1f") 
                print("Los archivos son: \n")
                with os.scandir(directorio) as ficheros:
                    for fichero in ficheros:
                        self.txt.append(directorio+"/"+fichero.name)
                        print(str(contador+1)+"."+fichero.name)
                        contador+=1
                opcion= int(input("Digite el numero de su eleccion: "))
                directorio=self.txt[opcion-1]
                if  str(directorio).find(".txt")!=-1:
                   os.remove(directorio)
                   print("Se ha removido el siguiente archivo: "+directorio)
        else:
            print("No posee los permisos para poder eliminar dicho archivo\n\n")
                       
            

    def VerUsuarios(self,permiso):
        print("Los usuarios existentes son: ")
        contador=0
        
        for x in self.userslist:
            print(str(contador+1)+"."+x.Nombre)
            contador+=1
        nombre=input("Porfavor escriba el nombre del usuario que desea observar: ")
        for x in self.userslist:
            if nombre == x.Nombre:
                print("\n\n1.Ver & Editar\n2.Eliminar\n")
                op=int(input("Seleccione una opcion: "))
                contador=0
                print("\033[2J\033[1;1f")        
                print("Los archivos del usuario "+x.Nombre+" son:")
                directorio="Usuarios/"+nombre
                with os.scandir(directorio) as ficheros:
                    for fichero in ficheros:
                        self.doc.append(directorio+"/"+fichero.name)
                        print(str(contador+1)+"."+fichero.name)
                        contador+=1
                
                if op==1:
                    self.Editar(permiso)
                elif op==2:
                    self.Eliminar(permiso)
            self.doc.clear()
            self.txt.clear()

    def Editar(self,permiso):# Abre un notepad para habilitar la edicion de un documento
        opcion= int(input("Digite el numero de su eleccion: "))
        directorio=self.doc[opcion-1]
        if str(directorio).find(".txt") !=-1:
            if permiso == 1:
                print("\033[2J\033[1;1f")  
                print("\n\nNo cuenta con los permisos necesarios para poder observar los documentos\nPorfavor Registrese o Inicie sesion para poder continuar\n\n")
            else:
                subprocess.run(["notepad.exe",directorio])
        else:
            contador=0
            print("\033[2J\033[1;1f") 
            print("Los archivos son: \n")
            with os.scandir(directorio) as ficheros:
                for fichero in ficheros:
                    self.txt.append(directorio+"/"+fichero.name)
                    print(str(contador+1)+"."+fichero.name)
                    contador+=1
            opcion= int(input("Digite el numero de su eleccion: "))
            directorio=self.txt[opcion-1]
            if  str(directorio).find(".txt")!=-1:
                if permiso == 1:
                    print("\033[2J\033[1;1f")  
                    print("\n\nNo cuenta con los permisos necesarios para poder observar los documentos\nPorfavor Registrese o Inicie sesion para poder continuar\n\n")
                else:
                    subprocess.run(["notepad.exe",directorio])

    def getUsuarios(self):# Llenar la lista de los usuarios registrados
        registro=open('Usuarios.rg','a')
        registro.write("")
        registro.close()
        with open('Usuarios.rg') as temp_f:
            archivo = temp_f.readlines()
            for line in archivo:
                user=Usuario(line[0:line.index(" ")],line[line.index(" "):line.index("\n")],1)
                self.userslist.append(user)

    def Carpetas(self, nombre):# Crea Una carpeta si el usuario asi lo desea
        for x in self.userslist:
            if x.Nombre==nombre:
                x.CrearCarpeta()

    
c=ControlVersiones()
def __main__():
    c.getUsuarios()
    c.Principal()

    
if __name__ =="__main__":
    __main__()