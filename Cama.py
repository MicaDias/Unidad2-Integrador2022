class Cama:
    __idCama=0
    __habitacion=''
    __estado=False
    __apellidoNombre=''
    __diagnostico=''
    __fechaInternacion=''
    __fechaAlta=''
    def __init__(self, idCama=0,habitacion='',estado=False,apellidoNombre='',diagnostico='',fechaInternacion='',fechaAlta=''):
        self.__idCama=idCama
        self.__habitacion=habitacion
        self.__estado=estado
        self.__apellidoNombre=apellidoNombre
        self.__diagnostico=diagnostico
        self.__fechaInternacion=fechaInternacion
        self.__fechaAlta=fechaAlta
    def verificarApellidoNombre(self,apellido):
        return self.__apellidoNombre==apellido
    def getIdCama(self):
        return self.__idCama
    def getHabitacion(self):
        return self.__habitacion
    def getApellidoNombre(self):
        return self.__apellidoNombre
    def getDiagnostico(self):
        return self.__diagnostico
    def getFechaInternacion(self):
        return self.__fechaInternacion
    def setFechaAlta(self,fecha):
        self.__fechaAlta=fecha
    def getFechaAlta(self):
        return self.__fechaAlta
    def setEstado(self):
        self.__estado=not self.__estado
    def getEstado(self):
        return self.__estado
    def verificarDiagnostico(self,diagnostico):
        return self.__diagnostico==diagnostico
    def __str__(self):
        return 'Apellido y Nombre:{}, Fecha de Internacion:{}, Diagnostico:{}'.format(self.__apellidoNombre,self.__fechaInternacion,self.__diagnostico)
    def funcionTestCama(self):
        print("***************Funcion Test Cama***************")
        cama1=Cama(8,'102',False,'Perez, Carlos','Covid','08/09/2021','19/08/2021')
        print("****Medetodo getIdCama()****")
        print("idCama:{}".format(cama1.getIdCama()))
        print("****Metodo getHabitacion()****") 
        print("Habitacion:{}".format(cama1.getHabitacion()))
        print("****Metodo getApellidoNombre()****")
        print("Apellido y Nombre:{}".format(cama1.getApellidoNombre()))    
        print("****Metodo getEstado()****")  
        print("Estado:{}".format(cama1.getEstado())) 
        print("****Metodo getFechaInternacion()****")
        print("Fecha de internacion:{}".format(cama1.getFechaInternacion()))