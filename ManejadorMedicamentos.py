import csv
from Medicamento import Medicamento
class ManejadorMedicamento:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def agregarMedicamentos(self,medicamento):
        if type(medicamento)==Medicamento:
            self.__lista.append(medicamento)
        else:
            print("No se puede agregar")
    def cargarArchivo(self):
        archivoMedicamentos=open("medicamentos.csv")
        reader=csv.reader(archivoMedicamentos,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                idCama=int(fila[0])
                idMedicamento=int(fila[1])
                nombreComercial=fila[2]
                monodroga=fila[3]
                presentacion=fila[4]
                cantidadAplicada=fila[5]
                precioTotal=float(fila[6])
                medicamento=(Medicamento(idCama,idMedicamento,nombreComercial,monodroga,presentacion,cantidadAplicada,precioTotal))
                self.agregarMedicamentos(medicamento)
        archivoMedicamentos.close()
    def mostrarDatos(self,idCama):
        acumPrecio=0
        print("{0:^30}  {1:^20} {2:^20}".format('Medicamentos'+'/'+'Monodroga','Cantidad','Precio'))
        for i in range(len(self.__lista)):
            if self.__lista[i].verificarIdCama(idCama):
                acumPrecio+=self.__lista[i].getPrecioTotal()
                print("{0:^30}  {1:^20} {2:^20.2f}".format(self.__lista[i].getNombreComercial()+'/'+self.__lista[i].getMonodroga(),self.__lista[i].getCantidadAplicada(),self.__lista[i].getPrecioTotal()))
        print(" Total adeudado                 {0:^60.2f}".format(acumPrecio))
    def funcionTestManejadorMedicamento(self):
        print("************Funcion Test ManejadorMedicamentos()**************")
        manejador=ManejadorMedicamento()
        medicamento=Medicamento(8,100,'Tafirol','Paracetamol','650mg',6,400)
        print("****Metodo agregarMedicamentos()****")
        manejador.agregarMedicamentos(medicamento)
        print("*****Metodo mostrarDatos()******")
        manejador.mostrarDatos(8)