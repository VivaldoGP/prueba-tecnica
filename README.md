## Prueba técnica para la vacante de desarrollador Python JR.
\i C:/Users/Vivaldo/Documents/personal-projects/prueba-tecnica-nt/Seccion1/DB/Schema.sql

### Sección 1

Para esta primera parte comencé por inspeccionar el archivo proporcionado, notando que era un archivo delimitado por comas y con la particularidad de tener una línea en blanco o vacía entre cada renglón, la solución para esto fue definir una función que abriera el archivo y lo recorra por completo, en cada iteración se retorna un objeto iterable con las columnas del archivo csv, por lo que la longitud de ese objeto debía ser mayor a 0 para consider que no está vacía y no es una línea en blanco, esto independiente de si alguna columna tiene algún valor nullo.