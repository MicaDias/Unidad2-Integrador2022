class Medicamento:
    __idCama=0
    __idMedicamento=0
    __nombreComercial=''
    __monodroga=''
    __presentacion=''
    __cantidadAplicada=''
    __precioTotal=0.0
    def __init__(self,idCama=0,idMedicamento=0,nombreComercial='',monodroga='',presentacion='',cantidadAplicada='',precioTotal=0.0):
        self.__idCama=idCama
        self.__idMedicamento=idMedicamento
        self.__nombreComercial=nombreComercial
        self.__monodroga=monodroga
        self.__presentacion=presentacion
        self.__cantidadAplicada=cantidadAplicada
        self.__precioTotal=precioTotal
    def getNombreComercial(self):
        return self.__nombreComercial
    def getMonodroga(self):
        return self.__monodroga
    def getPresentacion(self):
        return self.__presentacion
    def getCantidadAplicada(self):
        return self.__cantidadAplicada
    def getPrecioTotal(self):
        return self.__precioTotal
    def verificarIdCama(self,idCama):
        return self.__idCama==idCama
    def funcionTestMedicamento(self):
        print("********Funcion Test Medicamento**********")
        medicamento=Medicamento(8,100,'Pentotal','Penicilina','ampolla 10ml',4,3000)
        print("****Metodo getNonmbreComercial()****")
        print("Nombre comercial:{}".format(medicamento.getNombreComercial()))
        print("****Metodo getMonodroga()****")
        print("Monodroga:{}".format(medicamento.getMonodroga()))
        print("****Metodo getPresentacion()")
        print("Presentacion:{}".format(medicamento.getPresentacion()))
        print("****Metodo getCantiadAplicada()****")
        print("Cantidad:{}".format(medicamento.getCantidadAplicada()))
        print("****Metodo getPrecioTotal()****")
        print("Precio Total:{}".format(medicamento.getPrecioTotal()))