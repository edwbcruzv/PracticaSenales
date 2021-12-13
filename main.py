##conexion con la interfaz grafica comando>   pyuic5 -x Interfaz.ui -o Interfaz.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
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

        ##Graficas
        self.fig_Sec1=FigureCanvas(Figure())
        self.fig_Sec2=FigureCanvas(Figure())
        self.fig_res=FigureCanvas(Figure())

        self.fig_Sec1.axes=self.fig_Sec1.figure.add_subplot(111)
        self.fig_Sec2.axes=self.fig_Sec2.figure.add_subplot(111)
        self.fig_res.axes=self.fig_res.figure.add_subplot(111)

        self.fig_Sec1.axes.clear()
        self.fig_Sec2.axes.clear()
        self.fig_res.axes.clear()

        self.fig_Sec1.axes.set_xlabel('eje X')
        self.fig_Sec1.axes.set_ylabel('eje Y')
        self.fig_Sec1.axes.set_title('Secuencia 1')

        self.fig_Sec2.axes.set_xlabel('eje X')
        self.fig_Sec2.axes.set_ylabel('eje Y')
        self.fig_Sec2.axes.set_title('Secuencia 2')

        self.fig_res.axes.set_xlabel('eje X')
        self.fig_res.axes.set_ylabel('eje Y')
        self.fig_res.axes.set_title('Respuesta')

        self.ui.verticalLayout_Sec1.addWidget(self.fig_Sec1)
        self.ui.verticalLayout_Sec2.addWidget(self.fig_Sec2)
        self.ui.verticalLayout_Respuesta.addWidget(self.fig_res)

        self.fig_Sec1.draw()
        self.fig_Sec2.draw()
        self.fig_res.draw()




        self.ui.pushButton_Calcular.clicked.connect(self.seleccionarOperacion)

        self.ui.pushButton_Audio1.clicked.connect(self.capturarAudio1)
        self.ui.pushButton_Audio2.clicked.connect(self.capturarAudio2)

#dependiendo de lo que ingrese el usuario en la interfaz,el checked
#abrira la opcion correspondiente y antes de pasar a la operacion  realizara la
#lectura de los datos
    def seleccionarOperacion(self):
        self.fig_Sec1.axes.clear()
        self.fig_Sec2.axes.clear()
        self.fig_res.axes.clear()

        self.fig_Sec1.axes.set_xlabel('eje X')
        self.fig_Sec1.axes.set_ylabel('eje Y')
        self.fig_Sec1.axes.set_title('Secuencia 1')

        self.fig_Sec2.axes.set_xlabel('eje X')
        self.fig_Sec2.axes.set_ylabel('eje Y')
        self.fig_Sec2.axes.set_title('Secuencia 2')

        self.fig_res.axes.set_xlabel('eje X')
        self.fig_res.axes.set_ylabel('eje Y')
        self.fig_res.axes.set_title('Respuesta')

        if self.ui.radioButton_Suma.isChecked():
            print("se selecciono suma")
            S1,S2=self.capturarDatos(2)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x1,y1=S1.coordenadas()
            x2,y2=S1.coordenadas()
            self.fig_Sec1.axes.plot(x1,y1)
            self.fig_Sec2.axes.plot(x2,y2)
            res=S1.suma(S2)
            print(res)
            x,y=res.coordenadas()
            self.fig_res.axes.plot(x,y)


        elif self.ui.radioButton_Resta.isChecked():
            print("se selecciono resta")
            S1,S2=self.capturarDatos(2)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x1,y1=S1.coordenadas()
            x2,y2=S1.coordenadas()
            self.fig_Sec1.axes.plot(x1,y1)
            self.fig_Sec2.axes.plot(x2,y2)
            res=S1.resta(S2)
            print(res)
            x,y=res.coordenadas()
            self.fig_res.axes.plot(x,y)

        elif self.ui.radioButton_Multiplicacion.isChecked():
            print("se selecciono multiplicacion")
            S1,S2=self.capturarDatos(2)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x1,y1=S1.coordenadas()
            x2,y2=S1.coordenadas()
            self.fig_Sec1.axes.plot(x1,y1)
            self.fig_Sec2.axes.plot(x2,y2)
            res=S1.multiplicar(S2)
            print(res)
            x,y=res.coordenadas()
            self.fig_res.axes.plot(x,y)

        elif self.ui.radioButton_Reflexion.isChecked():
            print("se selecciono reflexion")
            S=self.capturarDatos(1)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x,y=S.coordenadas()
            self.fig_Sec1.axes.plot(x,y)
            S.reflexion()
            print(S)
            x,y=S.coordenadas()
            self.fig_res.axes.plot(x,y)

        elif self.ui.radioButton_Desplazamiento.isChecked():
            print("se selecciono desplazamiento")
            S=self.capturarDatos(1)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x,y=S.coordenadas()
            self.fig_Sec1.axes.plot(x,y)
            n0=self.ui.spinBox_n0.value()
            S.desplazamiento(n0)
            print("n0:",n0)
            print(S)
            x,y=S.coordenadas()
            self.fig_res.axes.plot(x,y)

        elif self.ui.radioButton_Diezmacion.isChecked():
            print("se selecciono diezmacion")
            S=self.capturarDatos(1)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x,y=S.coordenadas()
            self.fig_Sec1.axes.plot(x,y)
            k=self.ui.spinBox_KDiezm.value()
            print("k:",k)
            res=S.diezmacion(k)
            print(res)
            x,y=res.coordenadas()
            self.fig_res.axes.plot(x,y)

        elif self.ui.radioButton_Interpolacion.isChecked():
            print("se selecciono interpolacion")
            S=self.capturarDatos(1)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x,y=S.coordenadas()
            self.fig_Sec1.axes.plot(x,y)
            tipo_inter=self.ui.comboBox_Interpolaciones.currentIndex()
            k=self.ui.spinBox_KInterp.value()
            print("k:",k)
            if tipo_inter==0:# A Cero
                res=S.interpolacionCero(k)
                print(res)
                x,y=res.coordenadas()
                self.fig_res.axes.plot(x,y)
            elif tipo_inter==1:# Escalon
                res=S.interpolacionEscalon(k)
                print(res)
                x,y=res.coordenadas()
                self.fig_res.axes.plot(x,y)
            elif tipo_inter==2:# Lineal, pendiente
                # res=S.interpolacionLineal(k)
                # print(res)
                # x,y=res.coordenadas()
                # self.fig_res.axes.plot(x,y)
                pass
            else:
                print("No se a seleccionado el tipo de interpolacion")




        elif self.ui.radioButton_Convolucion.isChecked():
            print("se selecciono convolucion")
            S1,S2=self.capturarDatos(2)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x1,y1=S1.coordenadas()
            x2,y2=S1.coordenadas()
            self.fig_Sec1.axes.plot(x1,y1)
            self.fig_Sec2.axes.plot(x2,y2)

        else:
            self.ui.label_Status.setText("No ha seleccionado la operacion")


        self.fig_Sec1.draw()
        self.fig_Sec2.draw()
        self.fig_res.draw()

#al escojer la operacion a realizar se capturan las secuencias o audios introducido,
#dando la prioridad a la secuencia en texto y si este no se ingreso se busca el archivo .wav
    def capturarDatos(self,num_sec:int)->tuple:
        list_Sec_1=None
        list_Sec_2=None

        cad1=self.ui.textEdit_Secuencia1.toPlainText()#Secuencia1 {2,6,4,7,9,2,1,4,8,3*,6,5,4,7,8,2,1}
        cad1="{1,4*,6,0,-0.25,1}"
        #cad1="{2,-1,4,*0.5,2,-1,3}"

        #por defecto se leera la primera secuencia introducida
        if cad1=="":
            #si no hay secuencia, entonces hay audio
            if self.ruta_audio1!="":
                #dato=Dato(self.ruta_audio1)#procesar audio a secuencia
                pass
            else:
                self.ui.label_Status.setText("Ingrese una secuencia o un audio")
        else:
            #procesa verifica la sintaxis de la secuencia introducida y se crea el objeto Sentencia
            list_Sec_1,origen1=self.validarSecuencia(cad1)
            if origen1==-1:
                self.ui.label_Status.setText("No esta definido la secuencia 1")
                return
            print("Sec1:",list_Sec_1,origen1)
            Sec_Obj_1=Secuencia(list_Sec_1,origen1)

        #en caso de que la operacion requiera dos secuencias se lee la segunda que falta
        if num_sec==2:
            cad2=self.ui.textEdit_Secuencia2.toPlainText()#Secuencia2 {5,8,4,9,*3,1,2,5,4,7,8}
            cad2="{2,-1,4,*0.5,2,-1,3}"
            if cad2=="":
                #si no hay secuencia, entonces hay audio
                if self.ruta_audio2!="":
                    #dato=Dato(self.ruta_audio2)#procesar audio a secuencia
                    pass
                else:
                    self.ui.label_Status.setText("Falta ingresar el audio o la secuencia 2")
            else:
                #procesa verifica la sintaxis la secuencia introducida y se crea el objeto Secuencia
                list_Sec_2,origen2=self.validarSecuencia(cad2)
                if origen1==-1:
                    self.ui.label_Status.setText("No esta bien definido la secuencia 2")
                    return
                print("Sec2:",list_Sec_2,origen2)
                Sec_Obj_2=Secuencia(list_Sec_2,origen2)
            #Regresan 2 Secuencias
            return Sec_Obj_1,Sec_Obj_2

        #Regresa 1 Secuencia
        return Sec_Obj_1

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


#Se Escoje el audio1 a analizar
    def capturarAudio1(self):
        self.cwd = os.getcwd()# ruta de la ejecucion del programa
        self.ruta_audio1, selected_filter=QFileDialog.getOpenFileName(self,"seleccionar audio",self.cwd,"Text Files (*.wav)")
        self.ui.label_RutaAudio1.setText(self.ruta_audio1)
#Se Escoje el audio2 a analizar
    def capturarAudio2(self):
        self.cwd = os.getcwd()# ruta de la ejecucion del programa
        self.ruta_audio2, selected_filter=QFileDialog.getOpenFileName(self,"seleccionar audio",self.cwd,"Text Files (*.wav)")
        self.ui.label_RutaAudio2.setText(self.ruta_audio2)



##*****INICIO DE TODO EL PROGRAMA
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    myapp=Ventana()
    myapp.show()
    sys.exit(app.exec_())


