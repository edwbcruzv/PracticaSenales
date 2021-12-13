from collections import deque
from typing import List
import Secuencia
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Secuencia:

    # conjunto: Lista de enteros
    # [2,1,-3,0.24,-8.3,0.7] los elementos deben de ser enteros o decimales

    #origen: entero

    def __init__(self,conjunto:list,origen:int) -> None|bool:
        if conjunto==[] or conjunto==None or origen==-1:
            return None
        self.__conjunto=deque(conjunto)
        self.__origen=origen

#se encarga de validar y analizar la secuencia introducida
# y regresa la lista de la secuencia y la posicion de inicio que correspondera a la posicion de la lista
    def validarSecuencia(self,cadena:str)->tuple:
        #se filtran los caracteres de "0123456789,*"
        sec=''.join(x for x in cadena if x in "0123456789*-,.")
        aux_list=None
        aux_list=sec.split(',')

        if aux_list==[] or aux_list==None:
            return None,-1
        #print(aux_list)
        #hasta este punto suponemos que todos los elementos de la secuencia son numeros
        
        check_origen=False #verificar que solo tendremos un solo origen

        for s,i in zip(aux_list,range(len(aux_list))):

            index=s.find('*')#detecta el origen
            
            if index !=-1:#no es de todo un numero
                if len(s)>1 and check_origen==False:
                    #La secuencia y el origen estan correcto, el origen es la posicion de la lista
                    origen=aux_list.index(s)
                    #se quita el *
                    aux_list[i]=''.join(x for x in s if x in "0123456789-.")
                    s=aux_list[i]
                else:
                    #el origen no esta bien definido,o se puso mas de 2 veces
                    return None,-1
            #es un numero
            try:
                if s.find('.')>=0:#es un float
                    aux_list[i]=float(s)
                elif s.find('/')>=0:#es una fraccion
                    frac_list=s.split('/')
                    aux_list[i]=frac_list[0]/frac_list[1]
                    pass#por definir
                else:#es un entero
                    aux_list[i]=int(s)
            except:
                print("Error en la conversion de srt a numeros")
                return None,-1

        #la secuencia puede estar correcta 
        return aux_list, origen
    
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
            print("es mayor self.conjunto")
            secuencia.conjunto.appendleft(0)
            secuencia.origen+=1
        
        while self.origen < secuencia.origen:
            print("es mayor secuencia.conjunto")
            self.conjunto.appendleft(0)
            self.origen+=1

        while len(self.conjunto) > len(secuencia.conjunto):
            secuencia.conjunto.append(0)
        
        while len(self.conjunto) < len(secuencia.conjunto):
            self.conjunto.append(0)

        # print("Alineacion Final:")
        # print(self)
        # print(secuencia)        


    #realiza la operacion de suma con la secuencia que regrese como parametro
    def suma(self,secuencia:Secuencia)->Secuencia:
        self.__alinear(secuencia)
        res=[]
        for elem1,elem2 in zip(self.conjunto,secuencia.conjunto):
            res.append(elem1+elem2)
        #print(res)
        return Secuencia(list(res),self.origen)

    #realiza la operacion de resta con la secuencia que regrese como parametro
    def resta(self,secuencia:Secuencia)->Secuencia:
        self.__alinear(secuencia)
        res=[]
        for elem1,elem2 in zip(self.conjunto,secuencia.conjunto):
            res.append(elem1-elem2)
        #print(res)
        return Secuencia(list(res),self.origen)

    #realiza la operacion de multiplicacion con la secuencia que regrese como parametro
    def multiplicar(self,secuencia:Secuencia)->Secuencia:
        self.__alinear(secuencia)
        res=[]
        for elem1,elem2 in zip(self.conjunto,secuencia.conjunto):
            res.append(elem1*elem2)
        #print(res)
        return Secuencia(list(res),self.origen)

    def reflexion(self)->bool:
        self.conjunto.reverse()
        self.origen=len(self.conjunto)-self.origen-1
        #print(self)

    def desplazamiento(self,n0:int)->bool:
        nuevo_origen=self.origen-n0

        if nuevo_origen >= 0:
            self.origen=nuevo_origen

            if nuevo_origen < len(self.conjunto):
                return True
            else:
                #se agregan ceros faltantes a la derecha de la secuencia
                for i in range(nuevo_origen-len(self.conjunto)+1):
                    self.conjunto.append(0)
                return True
        else:
            #se agregan ceros faltantes a la Izquierda de la secuencia
            nuevo_origen=nuevo_origen*-1

            for i in range(nuevo_origen):
                self.conjunto.appendleft(0)
            self.origen=0
            return True

        return False
        

    def diezmacion(self,k:int)->Secuencia:

        # por defecto se agrega el origen
        res=deque([self.conjunto[self.origen]])

        nuevo_origen=0
        izq=der=self.origen
        izq-=k # se recorre a la izquierda k espacios
        der+=k # se recorre a la derecha k espacios
        
        while izq>=0:
            res.appendleft(self.conjunto[izq])
            izq-=k # se recorre a la izquierda k espacios
            nuevo_origen+=1 #nos ayudara a saber cual es el origen al final

        while der<len(self.conjunto):
            res.append(self.conjunto[der])
            der+=k # se recorre a la derecha k espacios

        return Secuencia(list(res),nuevo_origen)

    def interpolacionCero(self,k:int)->Secuencia:
        res=deque([])
        nuevo_origen=self.origen*k
        k=k-1
        for elem in self.conjunto:
            res.append(elem)
            for i in range(k): #k son los espacios que se agregan entre cada elemento
                res.append(0)
        return Secuencia(list(res),nuevo_origen)

    def interpolacionEscalon(self,k:int)->Secuencia:
        res=deque([])
        nuevo_origen=self.origen*k
        k=k-1
        for elem in self.conjunto:
            res.append(elem)
            for i in range(k): #k son los espacios que se agregan entre cada elemento
                res.append(elem)
        
        return Secuencia(list(res),nuevo_origen)

    def interpolacionLineal(self,k:int)->Secuencia:

        if k==1:
            return

        res=self.interpolacionCero(k)
        k=k-1
        tam=len(res)
        # ya se hizo una interpolacion a cero
        i=0
        while i<tam:
            i+=1 #se pasa al sig elemento del conjunto el cual debe de ser 0

            for j in range(k): #k son los espacios que se agregan entre cada elemento
                y1=res.conjunto[i+k]
                y0=res.conjunto[i]
                x1=i+1
                x0=i
                factor=y0+((y1-y0)/(x1-x0))
                for j in range(k):
                    res.append(factor)
                    factor+=factor
            i+=1

        return Secuencia(list(res),nuevo_origen)

    def convolucion(self)->Secuencia:
        pass
    #contiene la informacion de la Secuencia
    def __str__(self) -> str:
        return str(list(self.conjunto))+","+str(self.origen)

    #muestra la grafica de la secuencia
    def mostrarGrafica(self):
        x = np.arange(0,len(self.conjunto),1)
        y = self.conjunto

        plt.plot(x,y)
        plt.xlabel('n')
        plt.ylabel('f')
        plt.title('Secuencia')
        plt.show()

    def grafica(self):
        x = np.arange(0,len(self.conjunto),1)
        y = self.conjunto
        canvas=FigureCanvas(Figure())
        canvas.axes=canvas.figure.add_subplot(111)
        canvas.axes.clear()
        canvas.axes.plot(x,y)
        canvas.axes.set_xlabel('eje X')
        canvas.axes.set_ylabel('eje Y')
        canvas.axes.set_title('Secuencia')
        canvas.draw()
        return canvas

    def coordenadas(self):
        x = np.arange(0,len(self.conjunto),1)
        y = self.conjunto
        return x,y