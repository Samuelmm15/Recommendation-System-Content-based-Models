# Sistemas de Recomendación. Modelos basados en el contenido.
Este repositorio continene la implementación de un sistema de recomendación que utiliza un modelo basado en el contenido. El sistema de recomendación se encuentra implementado en [Python 3.11.5](https://www.python.org/downloads/release/python-3110/).

##  🏷️ Descripción del sistema de recomendación.

La correspondiente aplicación se trata de un sistema que obtiene distintos documentos a partir de las líneas de un archivo de texto. A continuación, se realiza un preprocesamiento de los documentos, eliminando las puntuaciones, las stop words y aplicando un proceso de lematización. Una vez se han obtenido los documentos preprocesados, se realiza un proceso de vectorización de los mismos, obteniendo un vector de características para cada documento. Finalmente, se realiza un proceso de recomendación de documentos, en el que se obtienen los distintos valores de similitud entre los documentos. Para ello, se utiliza la similitud del coseno, que se calcula a partir de los vectores de características de los documentos.

En cuanto la ejecución del programa, se emplea el uso de un sistema [POSIX](https://nullprogram.com/blog/2020/08/01/), el cual permite el establecimiento de aquellos ficheros los cuales se quiere usar para poder obtener aquellas comparaciones entre los distintos documentos que han sido introducidos como parámetros para la aplicación.

### Primer parámetro: Fichero de entrada.

Para la primera opción del sistema POSIX, la opción `-t`,  se debe introducir el fichero de entrada, es decir, el fichero el cual contiene los distintos documentos que se van a utilizar para realizar las comparaciones entre ellos. El fichero de entrada debe contener una línea por cada documento, y cada línea debe contener el texto de un documento. El fichero de entrada debe ser un fichero de texto plano, con extensión .txt.

### Segundo parámetro: Fichero de Stop Words.

Para la segunda opción del sistema POSIX, la opción `-p`, se debe introducir el fichero de stop words, es decir, el fichero el cual contiene las distintas palabras que se van a eliminar de los documentos. Este, debe contener una palabra por cada línea. El fichero de stop words debe ser un fichero de texto plano, con extensión .txt.

### Tercer parámetro: Fichero de lematización.

Para la tercera opción del sistema POSIX, la opción `-l`, se debe de introducir el fichero de lematización, es decir, el fichero el cual contiene las distintas palabras que se van a lematizar. Este, debe contener una palabra por cada línea. El fichero de lematización debe ser un fichero de texto plano, con extensión .txt.

📌 Para más información sobre el funcionamiento del programa, el uso de argumentos y la ejecución del mismo, se puede consultar el apartado [Ejecución del programa](#-ejecución-del-programa).

##  🔨 Instalación de dependencias.

Para la instalación de las dependencias del programa, se debe de ejecutar el siguiente comando que permite la instalación de las distintas dependencias necesarias para la ejecución del programa:

```bash
$ pip install -r requirements.txt
```

## ⚡️ Ejecución del programa.

Para la ejecución del programa se debe de ejecutar el siguiente comando:

```bash
$ python main.py -t <fichero_entrada> -p <fichero_stop_words> -l <fichero_lematizacion>
```

Donde:

- `-t` es la ruta del fichero de entrada.
- `-p` es la ruta del fichero de stop words.
- `-l` es la ruta del fichero de lematización.

📌 Para más información sobre el uso del programa, se puede ejecutar el siguiente comando:

```bash
$ python main.py -h
```

## 🎨 Generación de la documentación del programa.

Para la generación de la documentación de la aplicación se ha hecho uso de [Doxygen](https://www.doxygen.nl/index.html), de manera que, para la visualización de dicha documentación en formato `html`, se debe de acceder a la siguiente ruta y realizar la siguiente ejecución:

```bash
$ cd docs/html
$ firefox index.html
```

Accediendo a dicho fichero, se ejecuta el navegador `Firefox` y se muestra la documentación de la aplicación.

En la siguiente imagen, se puede observar un ejemplo de la documentación generada por `Doxygen`:

<img width="1680" alt="Doxygen-documentation-GCO-P2" src="https://github.com/Samuelmm15/Recommendation-System-Content-based-Models/assets/72341631/d6e4a90a-ebf2-4442-8f1c-47c9c77a7a01">

## 🔧 Ejemplo de ejecución del programa.

A continuación, se muestra un ejemplo de ejecución del programa:

https://github.com/Samuelmm15/Recommendation-System-Content-based-Models/assets/72341631/2d627b71-1022-449f-8968-b930900cc7df

## 📝 Licencia

Este proyecto se encuentra bajo la licencia Creative Commons Legal Code, para más información consultar el fichero [LICENSE](./LICENSE).

## ✒️ Autores

- Samuel Martín Morales (alu0101359526@ull.edu.es)
- Aday Chocho Aisa (alu0101437538@ull.edu.es)
