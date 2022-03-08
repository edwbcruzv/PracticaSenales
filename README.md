# PracticaSenales

MAteria de señales en ESCOM IPN

### *Este programa se creo en Python, usando los modulos princilapes como:*
- _[Scipy](https://scipy.org/)_
- _[Matplotlib](https://matplotlib.org/)_
- _~~[Numpy](https://numpy.org/)~~_ *Instalado pero no usado, por ahora :)*

## Interfaz Grafica

se uso pyqt5 y qt designer para crear la interfas y poder conectaros a los scrips creados
[Documentacionde Qt designer](https://doc.qt.io/) y [todas als clases](https://doc.qt.io/qt-5.15/classes.html).

[Descarga de qt designer](https://build-system.fman.io/qt-designer-download)


## Requerimientos para su descarga y correrlo

- **Tener instalado virtualenv y saber utilizarlo. aqui se encuentra la [guia de usuario](https://virtualenv.pypa.io/en/latest/user_guide.html)**

- **Despues del `git clone` entrar a la carpeta del proyecto y crear el entorno virtual con:**
```
virtualenv venv
```
- **Ahora debera haberse creado una carpeta llamada `venv`, ahora ejecutar el siguiente comando para entrar al entorno virtual**
    _En VS es un proceso diferente, por eso se recomienda hacerlo en el bash del GIT o en el CMD de windows directamente_
```
source venv/Scripts/activate
```
- **Ejemplo de como debera de verse**
```
(venv) 
Muerto@DESKTOP-8MA1RTD MINGW64 ~/Documents/VS/PracticaSenales (main)
$
```
- **esto se ejecuta el siguiente comando para instalar los modulos en el entorno virtual creado**
```
pip install -r requirements.txt
```

## Para salir den entorno virtual
- **Dentro de la misma carpeta del proyecto ejecutar**
```
deactivate
```
- **Ya no deveria de aparecer `(venv)`**

## Ejecutar el programa

**Para ello se necesita correr el `main.py` y se desplegara la interfaz grafica**




## Anexos

#### Proceso de reconocer si es la vos de Hombre o Mujer
    La frecuencia media de la voz masculina es de 106 Hz y con un rango de 77 Hz a 482 Hz.
    En cuanto a la voz femenina su frecuencia es de 193 Hz, con un rango de 137 Hz a 634 Hz. 

