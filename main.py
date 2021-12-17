import telegram
##conexion con la interfaz grafica comando>   pyuic5 -x Interfaz.ui -o Interfaz.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import os
from Interfaz.Interfaz import Ui_Form
from LeeDato import *
from Secuencia import Secuencia
from LeeDato import Microfono


class Ventana(QtWidgets.QWidget):


    def __init__(self,parent=None):
        super(Ventana,self).__init__(parent)
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        # Microfono
        self.microfono=Microfono()
        
        # Audios
        self.audio1=None
        self.audio2=None

        # Secuencias
        self.Sec_1=None
        self.Sec_2=None
        self.Res=None

        # Graficas
        self.fig_Sec1=FigureCanvas(Figure())
        self.fig_Sec2=FigureCanvas(Figure())
        self.fig_res=FigureCanvas(Figure())

        self.fig_Sec1.axes=self.fig_Sec1.figure.add_subplot(111)
        self.fig_Sec2.axes=self.fig_Sec2.figure.add_subplot(111)
        self.fig_res.axes=self.fig_res.figure.add_subplot(111)

        self.fig_Sec1.axes.clear()
        self.fig_Sec2.axes.clear()
        self.fig_res.axes.clear()

        self.fig_Sec1.axes.set_xlabel('Tiempo')
        self.fig_Sec1.axes.set_ylabel('Amplitud')
        self.fig_Sec1.axes.set_title('Secuencia 1')

        self.fig_Sec2.axes.set_xlabel('Tiempo')
        self.fig_Sec2.axes.set_ylabel('Amplitud')
        self.fig_Sec2.axes.set_title('Secuencia 2')

        self.fig_res.axes.set_xlabel('Tiempo')
        self.fig_res.axes.set_ylabel('Amplitud')
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
        self.ui.pushButton_ReproducirRespuesta.clicked.connect(self.reproduceRespuesta)

#dependiendo de lo que ingrese el usuario en la interfaz,el checked
#abrira la opcion correspondiente y antes de pasar a la operacion  realizara la
#lectura de los datos
    def seleccionarOperacion(self):
        self.fig_Sec1.axes.clear()
        self.fig_Sec2.axes.clear()
        self.fig_res.axes.clear()

        self.fig_Sec1.axes.set_xlabel('Tiempo')
        self.fig_Sec1.axes.set_ylabel('Amplitud')
        self.fig_Sec1.axes.set_title('Secuencia 1')

        self.fig_Sec2.axes.set_xlabel('Tiempo')
        self.fig_Sec2.axes.set_ylabel('Amplitud')
        self.fig_Sec2.axes.set_title('Secuencia 2')

        self.fig_res.axes.set_xlabel('Tiempo')
        self.fig_res.axes.set_ylabel('Amplitud')
        self.fig_res.axes.set_title('Respuesta')

        del self.Res
        self.Res=None

        if self.ui.radioButton_Suma.isChecked() and self.capturarDatos(2):
            print("se selecciono suma")
            #lectura de datos, el numero son la cantidad de secuencias a recibir
            x1,y1=self.Sec_1.coordenadas()
            x2,y2=self.Sec_2.coordenadas()
            self.fig_Sec1.axes.plot(x1,y1)
            self.fig_Sec2.axes.plot(x2,y2)
            self.Res=self.Sec_1.suma(self.Sec_2)
            x,y=self.Res.coordenadas()
            self.fig_res.axes.plot(x,y)


        elif self.ui.radioButton_Resta.isChecked() and self.capturarDatos(2):
            print("se selecciono resta")
            
            x1,y1=self.Sec_1.coordenadas()
            x2,y2=self.Sec_2.coordenadas()
            self.fig_Sec1.axes.plot(x1,y1)
            self.fig_Sec2.axes.plot(x2,y2)
            self.Res=self.Sec_1.resta(self.Sec_2)
            x,y=self.Res.coordenadas()
            self.fig_res.axes.plot(x,y)

        elif self.ui.radioButton_Multiplicacion.isChecked() and self.capturarDatos(2):
            print("se selecciono multiplicacion")
            x1,y1=self.Sec_1.coordenadas()
            x2,y2=self.Sec_2.coordenadas()
            self.fig_Sec1.axes.plot(x1,y1)
            self.fig_Sec2.axes.plot(x2,y2)
            self.Res=self.Sec_1.multiplicar(self.Sec_2)
            x,y=self.Res.coordenadas()
            self.fig_res.axes.plot(x,y)

        elif self.ui.radioButton_Reflexion.isChecked():
            print("se selecciono reflexion")
            self.capturarDatos(1)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x,y=self.Sec_1.coordenadas()
            self.fig_Sec1.axes.plot(x,y)
            self.Res=self.Sec_1.reflexion()
            x,y=self.Res.coordenadas()
            self.fig_res.axes.plot(x,y)

        elif self.ui.radioButton_Desplazamiento.isChecked():
            print("se selecciono desplazamiento")
            self.capturarDatos(1)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x,y=self.Sec_1.coordenadas()
            self.fig_Sec1.axes.plot(x,y)
            n0=self.ui.spinBox_n0.value()
            self.Res=self.Sec_1.desplazamiento(n0)
            print("n0:",n0)
            x,y=self.Res.coordenadas()
            self.fig_res.axes.plot(x,y)
            
        elif self.ui.radioButton_Diezmacion.isChecked():
            print("se selecciono diezmacion")
            self.capturarDatos(1)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x,y=self.Sec_1.coordenadas()
            self.fig_Sec1.axes.plot(x,y)
            k=self.ui.spinBox_KDiezm.value()
            print("k:",k)
            self.Res=self.Sec_1.diezmacion(k)
            x,y=self.Res.coordenadas()
            self.fig_res.axes.plot(x,y)
            

        elif self.ui.radioButton_Interpolacion.isChecked():
            print("se selecciono interpolacion")
            self.capturarDatos(1)#lectura de datos, el numero son la cantidad de secuencias a recibir
            x,y=self.Sec_1.coordenadas()
            self.fig_Sec1.axes.plot(x,y)
            tipo_inter=self.ui.comboBox_Interpolaciones.currentIndex()
            k=self.ui.spinBox_KInterp.value()
            print("k:",k)

            if tipo_inter==0:# A Cero
                self.Res=self.Sec_1.interpolacionCero(k)
                x,y=self.Res.coordenadas()
                self.fig_res.axes.plot(x,y)

            elif tipo_inter==1:# Escalon
                self.Res=self.Sec_1.interpolacionEscalon(k)
                x,y=self.Res.coordenadas()
                self.fig_res.axes.plot(x,y)

            elif tipo_inter==2:# Lineal
                self.Res=self.Sec_1.interpolacionLineal(k)
                x,y=self.Res.coordenadas()
                self.fig_res.axes.plot(x,y)

            else:
                print("No se a seleccionado el tipo de interpolacion")

        elif self.ui.radioButton_Convolucion.isChecked() and self.capturarDatos(2):
            print("se selecciono convolucion")
            
            x1,y1=self.Sec_1.coordenadas()
            x2,y2=self.Sec_2.coordenadas()
            self.fig_Sec1.axes.plot(x1,y1)
            self.fig_Sec2.axes.plot(x2,y2)
            tipo_conv=self.ui.comboBox_Convoluciones.currentIndex()

            if tipo_conv==0:
                self.Res=self.Sec_1.convolucionFinita(self.Sec_2)
                x,y=self.Res.coordenadas()
                self.fig_res.axes.plot(x,y)
            elif tipo_conv==1:
                self.Res=self.Sec_1.convolucionCircular(self.Sec_2)
                x,y=self.Res.coordenadas()
                self.fig_res.axes.plot(x,y)
            elif tipo_conv==2:
                self.Res=self.Sec_1.convolucionPeriodica(self.Sec_2)
                x,y=self.Res.coordenadas()
                self.fig_res.axes.plot(x,y)
            else:
                print("No se selecciono ningun tipo de convolucion.")

        else:
            self.ui.label_Status.setText(self.ui.label_Status.text()+" No ha seleccionado la operacion.")
            return

        self.fig_Sec1.draw()
        self.fig_Sec2.draw()
        self.fig_res.draw()

        self.ui.label_Status.setText("Operacion Exitosa.")
        print(self.Res)

#al escojer la operacion a realizar se capturan las secuencias o audios introducido,
#dando la prioridad a la secuencia en texto y si este no se ingreso se busca el archivo .wav
    def capturarDatos(self,num_sec:int)->tuple:
        #se almacenan las secuencias antes de crear el objeto
        list_Sec_1=None
        list_Sec_2=None
     

        cad1=self.ui.textEdit_Secuencia1.toPlainText() # entrada de secuencia por caracteres
        #cad1="1,0,-4*,3"
        #cad1="-10,4,0.25*,-1,0,2"
        #cad1="10,11,.5,-1,0,4*,1"
        #cad1="3,5,-6,*2,0,1"
        cad1="1,3,5,7*,9"
        #por defecto se leera la primera secuencia introducida----------------------------------------
        if cad1=="":
            #si no hay secuencia, entonces hay audio
            if self.Sec_1!=None:
                pass
            else:
                self.ui.label_Status.setText("Ingrese una secuencia o un audio.")
                return False
        else:
            #procesa verifica la sintaxis de la secuencia introducida y se crea el objeto Sentencia
            list_Sec_1,origen1=self.validarSecuencia(cad1)
            if origen1==-1:
                #se escribio mal la secuencia
                self.ui.label_Status.setText("No esta bien escrita la secuencia 1.")
                return False
            print("Sec1:",list_Sec_1,origen1)
            self.Sec_1=Secuencia(list_Sec_1,origen1)

        #en caso de que la operacion requiera dos secuencias se lee la segunda que falta----------------
        if num_sec==2:
            cad2=self.ui.textEdit_Secuencia2.toPlainText() # entrada de secuencia por caracteres
            #cad2="1*,2,3"
            #cad2="3,-7,11,*9,-5"
            #cad2="2,-3*,5"
            #cad2="-2*,1,5"
            if cad2=="":
                #si no hay secuencia, entonces hay audio
                if self.Sec_2!=None:
                    return True
                else:
                    self.ui.label_Status.setText("Falta ingresar el audio 2 o la secuencia 2.")
                    return False
            else:
                #procesa verifica la sintaxis la secuencia introducida y se crea el objeto Secuencia
                list_Sec_2,origen2=self.validarSecuencia(cad2)
                if origen2==-1:
                    #se escribio mal la secuencia
                    self.ui.label_Status.setText("No esta bien escrita la secuencia 2.")
                    return False

                print("Sec2:",list_Sec_2,origen2)
                self.Sec_2=Secuencia(list_Sec_2,origen2)

            #Existen 2 datos para trabajar
            return True
        #Existe 1 dato para trabajar
        return True

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
        origen=-1
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
    def capturarAudio1(self)->Audio:
        self.ruta_audio1=self.microfono.grabar() #se da por hecho que siempre se grabara un audio
        #self.ruta_audio1, selected_filter=QFileDialog.getOpenFileName(self,"seleccionar audio",self.cwd,"Text Files (*.wav)")
        self.ui.label_RutaAudio1.setText(self.ruta_audio1) #se mostrara la ruta del audio grabado
        #se procesara el audio intoducido para obtner la grafica y la secuencia
        try:
            # audio grabado
            self.fig_Sec1.axes.clear()
            self.fig_Sec1.axes.set_xlabel('Tiempo')
            self.fig_Sec1.axes.set_ylabel('Amplitud')
            self.fig_Sec1.axes.set_title('Secuencia 1')
            self.audio1=Audio(self.ruta_audio1)# ruta del audio
            self.Sec_1=Secuencia(self.audio1.der,0) # convirtiendolo a secuencia
            x1,y1=self.Sec_1.coordenadas()
            self.fig_Sec1.axes.plot(x1,y1) #datos para graficar
            self.fig_Sec1.draw()
        
        except Exception as e:
            self.audio1=None
            self.ui.label_RutaAudio1.setText("Error al grabar audio, "+str(e))


#Se Escoje el audio2 a analizar
    def capturarAudio2(self)->Audio:

        self.ruta_audio2=self.microfono.grabar() #se da por hecho que siempre se grabara un audio
        #self.ruta_audio2, selected_filter=QFileDialog.getOpenFileName(self,"seleccionar audio",self.cwd,"Text Files (*.wav)")
        self.ui.label_RutaAudio2.setText(self.ruta_audio2) #se mostrara la ruta del audio grabado
        #se procesara el audio intoducido para obtner la grafica y la secuencia
        try:#audio grabado
            self.fig_Sec2.axes.clear()
            self.fig_Sec2.axes.set_xlabel('Tiempo')
            self.fig_Sec2.axes.set_ylabel('Amplitud')
            self.fig_Sec2.axes.set_title('Secuencia 2')
            self.audio2=Audio(self.ruta_audio2)# ruta del audio
            self.Sec_2=Secuencia(self.audio2.der,0) # convirtiendolo a secuencia
            x2,y2=self.Sec_2.coordenadas()
            self.fig_Sec2.axes.plot(x2,y2) #datos para graficar
            self.fig_Sec2.draw()
        except Exception as e:
            self.audio2=None
            self.ui.label_RutaAudio2.setText("Error al grabar audio, "+str(e))

    def reproduceRespuesta(self):
        try:
            self.Res.reproduceAudio()
        except Exception as e:
            print("no hay respuesta,"+str(e))

##*****INICIO DE TODO EL PROGRAMA
if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    myapp=Ventana()
    myapp.show()
    sys.exit(app.exec_())


