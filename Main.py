import numpy as np
import csv
from ManejadorCama import ManejadorCama
from ManejadorMedicamentos import ManejadorMedicamento
from Menu import Menu
if __name__=='__main__':
    manejadorMedicamento=ManejadorMedicamento()
    manejadorCama=ManejadorCama()
    manejadorMedicamento.cargarArchivo()
    manejadorCama.cargarArchivo()
    menu=Menu()
    menu.lanzarMenu(manejadorCama,manejadorMedicamento)