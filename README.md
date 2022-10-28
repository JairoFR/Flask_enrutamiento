# **Comprender el enrutamiento en Flask**



## **Contenido**

 Servidor flask que tiene como finalidad comprender el enrutamiento y generar respuestas en el html de acuerdo a la informacion que se pasan a traves de ellas. 

    - Localhost:5000/ ==> "¡Hola Mundo!"
    - Localhost:5000/dojo  ==>  "¡Dojo!"
    - localhost:5000/say/flask ==>  "¡Hola, Flask!" 
    - localhost:5000/repeat/35/hello ==>  "hola" 35 veces

## **Instalacion y configuracion**

#### Instalar un entorno virtual con  pipenv en forma global (omitir si ya está instalado):      
#### Window:
    pip install pipenv

#### Mac:
    pip3 install pipenv



#### Clona el repositorio del proyecto: 


    $ git clone https://github.com/JairoFR/flask_enrutamiento.git  
    $ cd flask_enrutamiento

####  Instala desde Pipfile los paquetes que vienen configurados: 
    $ pipenv install

####  Activa el shell de Pipenv:
    $ pipenv shell

####  Detiene  el ambiente virtual en la terminal:
    $ exit


### Abrir proyecto en un editor de codigo fuente

    1.- Abrir proyecto en visual studio code.
    2.- Ir a Python: select interpreter ctrl+shift+p.
    3.- Seleccionar el ambiente virtual creado con el nombre de la carpeta.
    4.- Abrir nueva terminal y escribir python servidor.py
    5.- Escribir rutas especificadas en Seccion contenido.
