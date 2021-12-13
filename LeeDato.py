import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import signal
import scipy.io.wavfile as waves
import scipy.fftpack as fourier
from time import *
import winsound
import sys
import 

class Microfono:

    def __init__(self) -> bool:
        pass

    def grabar(self):
       


class Audio():

    def __init__(self,ruta) -> None:
        self.frecuencia,self.datos=waves.read(ruta)
        #la frecuencia esta dado en un entero
        #los datos estan en un arreglo, dependiendo si es mono o estereo
        #vendra un arreglo,cada elemento es un vector 

        print("Frecuencia:",self.frecuencia,"Tam_Arreglo",len(self.datos)) #el tamalo de los datos es el shape[0]
        print(f"Numero de canales = {self.datos.shape[1]}") # si es estereo o mono
        self.length = self.datos.shape[0] / self.frecuencia,# cantidad de datos sobre la frecuencia, da el tiempo que dura la pista
        print(f"tamaño de audio = {self.length}s")

        self.izq=self.datos[:, 0]
        self.der=self.datos[:, 1]

    #se lee el audio y se muestra en una grafica
    def audio(self,ruta):

        time = np.linspace(0., self.length, self.datos.shape[0])
        plt.plot(time,self.izq, label="Left channel")
        plt.plot(time,self.der, label="Right channel")
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()

    


if __name__=='__main__':
    dato=Audio("Vocales.wav")


