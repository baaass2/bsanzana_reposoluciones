# Graficador de cadenas polipeptídicas
A travès de la utilizaciòn Bash Script, se hace una descarga de una base de datos, que contienen archivos .pdb de una determinada proteina, de esta utilizando awk(manipulador de texto)
se puede filtrar la data, para obtener informacion indicada para procesarla y obtener un formato .svg, en cual se obtiene un grafica sencilla de como se conectan
atomos a un determinado aminoacido, y este como pertenece a una cadena X, y asi se puede vizualizar un orden.
En resumen el proyecto maneja estos conceptos, DESCARGA -> PROCESA -> FILTRA -> ANALIZA -> GRAFICA, una base de datos.
El proyecto esta alojado en el siguente repositorio:
	https://github.com/baaass2/bsanzana_reposoluciones/tree/master/proyecto1progaav
Ahì se encuentra la ùltima actualizaciòn del proyecto.
### Pre-requisitos.
Tener una conexion a internet.
Un vizualizador de imagenes, se recomienda sencillamante el mismo navegador.
Instalar el paquete graphviz:
	sudo apt-get install graphiz
Se recomienda tener el programa en una carpeta, ya que genera varios archivos.
### Instalación.
Ya que es un Script solo se necesita abrir una terminal y llamarlo, de la siguente manera:
	bash proyecto1.sh
### Anàlisis.
El programa consiste en que luego de ser ejecutado el Script, se solicita una ID de proteina, estas se pueden obtener en la primera ejecuciòn del programa, en la cual se descarga
la base de datos, luego de ingresar la ID, se verifica si realmente se esta solicitando graficar una proteina, dependiendo de la longitud de esta, o la informacion contenga,
el filtrado puede demorarse un tiempo considerable (1 min), el Script genera 3 archivos màs la base de datos .pdb, la imagen .svg donde se puede vizualizar la grafica
de la proteina solicitada, archivo.dot que es el que se usa para generar la grafica, y un archivo.txt donde se encuentra la filtracion y la data de la proteina solicitada.

Mencionar que, si el programa no es interrupido, con factores del usuario o mala conexiòn de internet, no existe un mètodo para verificar si los archivos son correctos (dado que podrian estar dañados),
 pero de lo contrario, si no existe una interrupciòn el programa deberia tener una funcional minima.
## Construido con.
Se mencionarà las herramientas usadas, y la funciòn en ESTE proyecto.

* [BASH] - Script que corre los comandos.
* [AWK] - Manipulados de texto, especificamente la base de datos.
* [graphviz] - Graficador de las cadenas polipeptídicas.
## Autores.

* Benjamìn Adolfo Sanzana Silva [sanzana](https://github.com/baaass2/bsanzana_reposoluciones)

