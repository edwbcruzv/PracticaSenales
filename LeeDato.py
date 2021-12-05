import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile



class Dato():

    def __init__(self,ruta) -> None:
        self.audio(ruta)

    #se lee el audio y se muestra en una grafica
    def audio(self,ruta):
        frecuencia,datos=wavfile.read(ruta)

        print(frecuencia,datos)
        print(f"Numero de canales = {datos.shape[1]}")
        length = datos.shape[0] / frecuencia
        print(f"tamaño de audio = {length}s")

        time = np.linspace(0., length, datos.shape[0])
        plt.plot(time, datos[:, 0], label="Left channel")
        plt.plot(time, datos[:, 1], label="Right channel")
        plt.legend()
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.show()