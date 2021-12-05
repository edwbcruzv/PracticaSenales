##conexion con la interfaz grafica comando>   pyuic5 -x Interfaz.ui -o Interfaz.py 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
import os
from Interfaz.Interfaz import Ui_Form
from Secuencia import Secuencia
from LeeDato import Dato


#audio=Dato("Vocales.wav")  #para leer un audio 

x=Secuencia([2,-1,4,0.5,2,-1,3],3)
h=Secuencia([1,4,6,0,-0.25,1],1)

class Ventana(QtWidgets.QWidget):
    

    def __init__(self,parent=None):
        super(Ventana,self).__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ruta_audio1=""
        self.ruta_audio2=""

        self.ui.pushButton_Calcular.clicked.connect(self.seleccionarOperacion)

        self.ui.pushButton_Audio1.clicked.connect(self.capturarAudio1)
        self.ui.pushButton_Audio2.clicked.connect(self.capturarAudio2)

    def seleccionarOperacion(self):

        if self.ui.radioButton_Suma.isChecked():
            #leer datos para calcular
            print("se selecciono suma")
            self.capturarDatos(2)

        elif self.ui.radioButton_Resta.isChecked():
            #leer datos para calcular
            print("se selecciono resta")
            self.capturarDatos(2)

        elif self.ui.radioButton_Multiplicacion.isChecked():
            #leer datos para calcular
            print("se selecciono multiplicacion")
            self.capturarDatos(2)

        elif self.ui.radioButton_Reflexion.isChecked():
            #leer datos para calcular
            print("se selecciono reflexion")
            self.capturarDatos(1)

        elif self.ui.radioButton_Desplazamiento.isChecked():
            #leer datos para calcular
            print("se selecciono desplazamiento")
            self.capturarDatos(1)

        elif self.ui.radioButton_Diezmacion.isChecked():
            #leer datos para calcular
            print("se selecciono diezmacion")
            self.capturarDatos(1)

        elif self.ui.radioButton_Interpolacion.isChecked():
            #leer datos para calcular
            print("se selecciono interpolacion")
            self.capturarDatos(1)

        elif self.ui.radioButton_Convolucion.isChecked():
            #leer datos para calcular
            print("se selecciono convolucion")
            self.capturarDatos(2)

        else:
            self.ui.label_Status.setText("No ha seleccionado la operacion")

    def capturarDatos(self,num_sec:int):
        cad=self.ui.textEdit_Secuencia1.toPlainText()
        if cad=="":
            if self.ruta_audio1!="":
                #procesar audio
                dato=Dato(self.ruta_audio1)
            else:
                self.ui.label_Status.setText("Ingrese los datos que faltan")
        else:
            #procesa la secuencia introducida
            pass

        if num_sec==2:
            cad=self.ui.textEdit_Secuencia2.toPlainText()
            if cad=="":
                if self.ruta_audio2!="":
                    #procesar audio
                    dato=Dato(self.ruta_audio2)
                else:
                    self.ui.label_Status.setText("Ingrese los datos que faltan")
            else:
                #procesa la secuencia introducida
                pass

    def capturarAudio1(self):
        self.cwd = os.getcwd()# ruta de la ejecucion del programa
        self.ruta_audio1, selected_filter=QFileDialog.getOpenFileName(self,"seleccionar audio",self.cwd,"Text Files (*.wav)")
        self.ui.label_RutaAudio1.setText(self.ruta_audio1)

    def capturarAudio2(self):
        self.cwd = os.getcwd()# ruta de la ejecucion del programa
        self.ruta_audio2, selected_filter=QFileDialog.getOpenFileName(self,"seleccionar audio",self.cwd,"Text Files (*.wav)")
        self.ui.label_RutaAudio2.setText(self.ruta_audio2)

    def validarSecuencia(self,cadena:str)->list:
        pass

##*****INICIO DE TODO EL PROGRAMA
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    myapp=Ventana()
    myapp.show()
    sys.exit(app.exec_())


