from collections import deque
from typing import List
import Secuencia
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class Secuencia:

    def __init__(self,conjunto:list,origen:int) -> None:
        self.__conjunto=deque(conjunto)
        self.__origen=origen

    @property
    def conjunto(self):
        return self.__conjunto

    @property
    def origen(self):
        return self.__origen
    @origen.setter
    def origen(self,origen:int):
        self.__origen=origen

    def __alinear(self,secuencia:Secuencia):
        
        while self.origen > secuencia.origen:
            secuencia.conjunto.appendleft(0)
            secuencia.origen+=1
        
        while self.origen < secuencia.origen:
            self.conjunto.appendleft(0)
            self.origen+=1

        while len(self.conjunto) > len(secuencia.conjunto):
            secuencia.conjunto.append(0)
            secuencia.origen+=1
        
        while len(self.conjunto) < len(secuencia.conjunto):
            self.conjunto.append(0)
            self.origen+=1



    def suma(self,secuencia:Secuencia)->list:

        self.__alinear(secuencia)

        if len(self.conjunto)==len(secuencia.conjunto):
            print("son iguales")

        res=[]
        for elem1,elem2 in zip(self.conjunto,secuencia.conjunto):
            res.append(elem1+elem2)
        


    def resta(self,secuencia:Secuencia)->list:
        
        self.__alinear(secuencia)

        if len(self.conjunto)==len(secuencia.conjunto):
            print("son iguales")

        res=[]
        for elem1,elem2 in zip(self.conjunto,secuencia.conjunto):
            res.append(elem1-elem2)

    def multiplicar(self,secuencia:Secuencia)->list:
        
        self.__alinear(secuencia)

        if len(self.conjunto)==len(secuencia.conjunto):
            print("son iguales")

        res=[]
        for elem1,elem2 in zip(self.conjunto,secuencia.conjunto):
            res.append(elem1*elem2)

    def reflexion(self):
        pass



    def desplazamiento(self):
        pass

    def diezmacion(self):
        pass

    def interpolacion(self):
        pass

    def convolucion(self):
        pass

    def mostrar(self):
        x = np.arange(0,len(self.conjunto),1)
        y = self.conjunto

        plt.plot(x,y)
        plt.xlabel('n')
        plt.ylabel('f')
        plt.title('Secuencia')
        plt.show()