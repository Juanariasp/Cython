# Cython
<div> 
<img src="https://res-5.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1455514364/pim02bzqvgz0hibsra41.png" align="right"><br><br><FONT FACE="times new roman" SIZE=5>
<b> Cython </b>
<br>
<i><b>Autor:</b></i><br> Juan Esteban Arias Patron <br>
<i><b>Asignatura:</b></i> Parallel and Distributed Computing
<br>
<i><b>Docente:</b></i> John Corredor, PhD
<br>
01/11/22
<br><br><br>
</FONT>
</div>

Este programa tiene como objetivo demostrar los beneficios computacionales de utilizar Cython. Se realizan operaciones computacionales complejas y se comparan las versiones en Python y Cython para mostrar la diferencia en rendimiento.

## Descripción

Cython es un lenguaje que se escribe de forma muy similar a Python, pero permite la utilización de librerías y variables de tipo C. Combina la simplicidad de sintaxis de Python con la velocidad de C, lo que lo convierte en una herramienta poderosa para aplicaciones que requieren un alto rendimiento.

El programa utiliza Cython para aprovechar la velocidad de C y realizar operaciones computacionales complejas de manera eficiente. Además, se incluyen pruebas comparativas entre las versiones en Python y Cython para mostrar la diferencia en rendimiento y la mejora que se obtiene al utilizar Cython.

## Requisitos de instalación

- Cython
- Python
- make
- gcc

## Compilación y ejecución

El programa utiliza un Makefile para la compilación. Asegúrate de tener instalado `make` y `gcc` para compilar el código Cython. Sigue los siguientes pasos para compilar y ejecutar el programa:

1. Abre una terminal en el directorio del proyecto.
2. Ejecuta el siguiente comando para compilar el código Cython:
    ```shell
    $ make
    ```
3. Una vez compilado, ejecuta el programa con el siguiente comando:
    ```shell
    $ python main.py
    ```
## Limitaciones y consideraciones

Programar en Cython tiene sus ventajas en términos de rendimiento, pero también presenta algunas limitaciones y consideraciones:

- Es necesario compilar el código Cython por separado antes de ejecutar el programa.
- A diferencia de lenguajes como C o Fortran, Cython no tiene un soporte tan bueno para la paralelización de memoria.
