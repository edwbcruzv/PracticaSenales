# PracticaSenales

Materia de señales cursada con Jacqueline Arzate Gordillo en ESCOM IPN

Esta practica realiza las operaciones basicas de las secuencias y usando voces:
- Amplificacion.
- Suma.
- Resta.
- Multiplicacion.
- Reflexion.
- Desplazamiento.
- Diezmacion.
- interpolacion.
    - Cero.
    - Escalon.
    - Lineal.
- Convolucion
    - Finita.
    - Circular.
    - Periodica.

### *Este programa se creo en Python, usando los modulos princilapes como:*
- _[Scipy](https://scipy.org/)_
- _[Matplotlib](https://matplotlib.org/)_
- _~~[Numpy](https://numpy.org/)~~_ *Instalado pero no usado, por ahora :)*

## Interfaz Grafica
El Programa fue hecho y entregado en Windows 10.
Se uso pyqt5 y qt designer para crear la interfaz y poder conectarlos a los scrips creados
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
- **Ejemplo de como debe verse**
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


