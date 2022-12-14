## Prueba técnica para la vacante de desarrollador Python JR.

### Sección 1

Para esta primera parte comencé por inspeccionar el archivo proporcionado, notando que era un archivo delimitado por comas y con la particularidad de tener una línea en blanco o vacía entre cada renglón, la solución para esto fue definir una función que abriera el archivo y lo recorra por completo, en cada iteración se retorna un objeto iterable con las columnas del archivo csv, por lo que la longitud de ese objeto debía ser mayor a 0 para consider que no está vacía y no es una línea en blanco, esto independiente de si alguna columna tiene algún valor nullo.
Una vez que se tiene el archivo sin esta particularidad procedí a inspeccionar los datos que contiene notando que había valores nullos y otros en un formato diferente al de los demás, por ejemplo la columna *amount*, la cual sus valores en su gran mayoria son numeros pequeños con dos decimales después del punto, pero en algunos renglones esto cambió a tenerlos en una gran magnitud, por lo que posteriormente al momento de diseñar el esquema de la base de datos modifiqué el tipo de dato propuesto en la guía para que al momento de insertar los datos no existiera alguna incompatibilidad.

#### Extracción

En este apartado de igual forma me apoyé en Python para realizar esta tarea, creando una función que tomaba ciertos párametros de entrada y de esta manera extraer las columnas deseadas del archivo csv original, exportando la información y diviendola en partes mas pequeñas, teniendo un archivo individual para las tablas del esquema de la base de datos, en el formato de las mismas para realizar la importación de manera eficaz.

![Diagrama de entidad relación](https://github.com/VivaldoGP/prueba-tecnica/blob/main/ER_diagram.png)

Los scripts para la extracción y transformación de los datos se encuentran en la carpeta [Seccion1](https://github.com/VivaldoGP/prueba-tecnica/tree/main/Seccion1) de este repositorio, de igual forma en esta carpeta se encuentran dos mas, [DB](https://github.com/VivaldoGP/prueba-tecnica/tree/main/Seccion1/DB) en el que se encuentra el esquema de la base de datos, su creción, una consulta simple para comprobar la relación entre las tablas, la importación de los archivos csv generados anteriormente y un backup de la base de datos por si se desea importar.

*Importante: para poder ejecutar la sentencia **COPY** los archivos deben estar en la carpeta pública del usuario, ya que esta cuenta con los permisos para realizar dicha acción.

### Requerimentos
Para este proyecto se hace uso de Python en su versión 3.11, la cual se puede descargar desde el siguiente [link](https://www.python.org/), como *DBMS* se optó por PostgreSQL en su versión 14, la elección de esta base de datos fue primordialmente por la experiencia previa, además de su practicidad y facilidad de uso, su interfaz gráfica(pgAdimn 4) es muy amigable para el usuario, su consola igualmente es fácil de usar y sus comandos básicos son sencillos. 

Se trabajó con un entorno virtual con la finalidad de poder replicar este repositorio:
Para instalarlo es suficiente con ejecutar lo siguiente:
```console
pip install virtualenv
```
Nos situamos en el directorio a trabajar y se ejecuta el comando siguiente:
```console
python -m virtualenv venv
```
Donde *venv* es el nombre del directorio del entorno virtual.

Veremos como se ha creado el directorio y para activarlo nos situamos en el directorio *venv*, entramos a la carpeta Scripts y ejecutamos el archivo *activate*.

Teniendo nuestro entorno activado procedemos a situarnos en la raíz de nuestro directorio y ejecutamos lo siguiente:

```console
pip install -r requirements.txt
```
Hasta este momento se tiene practicamente todo para la ejecución de los scripts contenidos en este repositorio.

*Es importante que todo esto se realiza desde la consola de su dispositivo.

## Seccion2
Creación API
Objetivo: Creación e implementación de una apliación.
Problema: Calcular el numero faltante de un conjunto de los primeros 100 números naturales del cual se extrajo uno.

### Especifiaciones
- Conjunto de los primeros 100 números naturale
- Un método Extract para extraer cierto número deseado
- Debe poder calcular que número se extrajo
- Validación del inpunt, que sea número y menor a 100
- Ejecutarse con un argumento introducido por el usuario

### Solución
Para esta tarea decidí crear una clase que tome como atributo de entrada un número que será el límite del rango de los números naturales, esto con la finalidad de que la clase no esté limitada a unicamente los primeros 100 números, se creó un arreglo espaciado con la cantidad de elementos establecidos en el atributo de la clase, después añadí atributos para poder realizar el cálculo de el elemento extraido, la lógica que seguí fue sumar todos los elementos del arreglo y asignarlo a un atributo de la clase, después a esa suma restar el número extraido por el usuario e igualmente asignarlo a un atributo de la clase, despúes realicé la resta de esas dos cantidades y el resultado es el valor que el usuario introdujo.

Este problema se podría ampliar aplicando un algoritmo que devuelva la posición del número extraido en el array, un ejemplo podría ser el algortimo de búsqueda binaria.

La validación del input del usuario la realicé de modo que no pudiera avanzar hasta que el tipo de dato de entrada cumpliera con las condiciones establecidas.

El script se encuentra en la carpeta [Seccion2](https://github.com/VivaldoGP/prueba-tecnica/tree/main/Seccion2)