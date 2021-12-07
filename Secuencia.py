from collections import deque
from typing import List
import Secuencia
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class Secuencia:

    # conjunto: Lista de enteros
    # [2,1,-3,0.24,-8.3,0.7] los elementos deben de ser enteros o decimales

    #origen: entero

    def __init__(self,conjunto:list,origen:int) -> None|bool:
        if conjunto==[] or conjunto==None or origen==-1:
            return None
        self.__conjunto=deque(conjunto)
        self.__origen=origen
    #------Encapsulacion de los atributos
    @property
    def conjunto(self):
        return self.__conjunto

    @property
    def origen(self):
        return self.__origen
    @origen.setter
    def origen(self,origen:int):
        self.__origen=origen

    #Se encarga de emparejan las secuencias y que los origenes coincidan
    #no regresa nada porque la modificacion es profunda
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


    #realiza la operacion de suma con la secuencia que regrese como parametro
    def suma(self,secuencia:Secuencia)->list:

        self.__alinear(secuencia)

        if len(self.conjunto)==len(secuencia.conjunto):
            print("son iguales")

        res=[]
        for elem1,elem2 in zip(self.conjunto,secuencia.conjunto):
            res.append(elem1+elem2)
        print(res,self.origen)

    #realiza la operacion de resta con la secuencia que regrese como parametro
    def resta(self,secuencia:Secuencia)->list:
        
        self.__alinear(secuencia)

        if len(self.conjunto)==len(secuencia.conjunto):
            print("son iguales")

        res=[]
        for elem1,elem2 in zip(self.conjunto,secuencia.conjunto):
            res.append(elem1-elem2)
        print(res,self.origen)
    #realiza la operacion de multiplicacion con la secuencia que regrese como parametro
    def multiplicar(self,secuencia:Secuencia)->list:
        
        self.__alinear(secuencia)

        if len(self.conjunto)==len(secuencia.conjunto):
            print("son iguales")

        res=[]
        for elem1,elem2 in zip(self.conjunto,secuencia.conjunto):
            res.append(elem1*elem2)
        print(res,self.origen)

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
    #contiene la informacion de la Secuencia
    def __str__(self) -> str:
        return "{"+str(self.conjunto)+"},"+str(self.origen)

    #muestra la grafica de la secuencia
    def mostrar(self):
        x = np.arange(0,len(self.conjunto),1)
        y = self.conjunto

        plt.plot(x,y)
        plt.xlabel('n')
        plt.ylabel('f')
        plt.title('Secuencia')
        plt.show()