import numpy as np
import csv
from Cama import Cama
from ManejadorMedicamentos import ManejadorMedicamento
class ManejadorCama:
    __cantidad=0
    __dimension=0
    __incremento=0
    __cama=None
    def __init__(self,dimension=0,incremento=5):
        self.__cama=np.empty(dimension,dtype=Cama)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
    def agregarCama(self,camas):
        if type(camas)==Cama:
            if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__cama.resize(self.__dimension)
            self.__cama[self.__cantidad]=camas
            self.__cantidad+=1
    def cargarArchivo(self):
        archivo=open("camas.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                idCama=int(fila[0])
                habitacion=int(fila[1])
                estado=bool(fila[2])
                apellidoNombre=fila[3]
                diagnostico=fila[4]
                fechaInternacion=fila[5]
                fechaAlta=fila[6]
                camas=Cama(idCama,habitacion,estado,apellidoNombre,diagnostico,fechaInternacion,fechaAlta)
                self.agregarCama(camas)
        archivo.close()
        
    def buscarNombre(self,apellido):
        i=0
        bandera=True
        resultado=0
        while i<self.__cantidad and bandera:
            if self.__cama[i].verificarApellidoNombre(apellido):
                bandera=not bandera
            else:
                i+=1
        if bandera:
            resultado=-1
        else:
            resultado=i
            
        return resultado
    def mostrarDatosPaciente(self,manejadorMedicamento,pos):
        fecha=input("Ingrese la fecha de Alta dd/mm/aaaa: ")
        self.__cama[pos].setFechaAlta(fecha)
        separador=fecha.split('/')
        dia=separador[0]
        mes=separador[1]
        año=separador[2]
        print("Paciente:{}       Cama:{}      Habitacion:{}".format(self.__cama[pos].getApellidoNombre(),self.__cama[pos].getIdCama(),self.__cama[pos].getHabitacion()))
        print("Diagnostico:{}   Fecha de Internacion:{}".format(self.__cama[pos].getDiagnostico(),self.__cama[pos].getFechaInternacion()))
        print("Fecha de Alta:{}/{}/{}".format(dia,mes,año))
        manejadorMedicamento.mostrarDatos(self.__cama[pos].getIdCama())
        self.__cama[pos].setEstado()
        
    def mostrarPacienteInternados(self,diag):
        for i in range(self.__cantidad):
            if(self.__cama[i].getEstado()):
                if self.__cama[i].verificarDiagnostico(diag):
                    print(self.__cama[i])
    def funcionTestMeanejadorCama(self,manejadorMedicamento):
        print("****************Funcion Test Manejador Cama***************")
        cama2=Cama(8,105,True,'Lopez, Paula','Covid','23/05/202')
        cama3=Cama(9,109,True,'Marcelo, Perez','Covid','10/09/2021')
        cama4=Cama(10,103,True,'Marcos Poblete','Covid','11/08/2021')
        print("*****Metodo agregarCama()*****")
        self.agregarCama(cama2)
        self.agregarCama(cama3)
        self.agregarCama(cama4)
        print("****Metodo buscarNombre()************")
        posicion=self.buscarNombre('Perez, Luis')
        print("*****Metodo mostrarDatosPaciente()*****")
        self.mostrarDatosPaciente(manejadorMedicamento,posicion)
        print("******Metodo mostrarPaientesInternados()******")
        self.mostrarPacienteInternados('Covid')