from ManejadorCama import ManejadorCama
from Medicamento import Medicamento
from Cama import Cama
from Medicamento import Medicamento
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.salir
            }
    def lanzarMenu(self,manejadorCama,manejadorMedicamento):
        #Menu opciones
        if type(manejadorCama)==ManejadorCama:
            i=str(len(self.__opciones))
            opcion=0
            while(i!=opcion):
                print('Menu:')
                print('-Ingrese 1:Mostrar datos del paciente y monto adeudado.')
                print('-Ingrese 2:Mostrar datos de los pacientes internados')
                print('-Ingrese 3: Funcion Test.')
                print('-Ingrese 4: Salir.')
                opcion=input('Ingrese opcion:\n')
                ejecutar=self.__opciones.get(opcion,self.error)
                if (opcion=='1'or opcion=='3'):
                    ejecutar(manejadorCama,manejadorMedicamento)
                elif(opcion=='2'):
                    ejecutar(manejadorCama)
                else:
                    ejecutar()
    
    def opcion1(self,manejadorCama,manejadorMedicamento):
        apellido=input("Ingrese apellido y nombre del paciente: ")
        pos=manejadorCama.buscarNombre(apellido)
        if pos!=-1:
            manejadorCama.mostrarDatosPaciente(manejadorMedicamento,pos)
        else:
            print("No se encontro el paciente")
    def opcion2(self,manejadorCama):
        diag=str(input("Ingrese el diagnostico: "))
        manejadorCama.mostrarPacienteInternados(diag)
    def opcion3(self,manejadorCama,manejadorMedicamento):
        cama=Cama()
        medicamento=Medicamento()
        manejadorMedicamento.funcionTestManejadorMedicamento()
        manejadorCama.funcionTestMeanejadorCama(manejadorMedicamento)
        cama.funcionTestCama()
        medicamento.funcionTestMedicamento()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')