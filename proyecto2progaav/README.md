# Graficador de aminoacidos que se encuentran en un distancia determinada de un ligando. (GADL)
A travès de la utilizaciòn Bash Script, se hace una descarga de una base de datos, que contienen archivos .pdb de una determinada proteina, de esta utilizando awk(manipulador de texto)
se puede filtrar la data, para obtener informacion indicada para procesarla y obtener un formato .png, en cual se obtiene un grafica sencilla de como exite a una distancia deterimada atomos de un determinado aminoacido, las distancia es ingresada por el usuario.

El proyecto esta alojado en el siguente repositorio:
https://github.com/baaass2/bsanzana_reposoluciones/tree/master/proyecto2progaav
Ahì se encuentra la ùltima actualizaciòn del proyecto.
### Pre-requisitos.
Tener una conexion a internet.
Un vizualizador de imagenes, se recomienda sencillamante el mismo navegador.
Instalar el paquete graphviz:
	sudo apt-get install graphiz
Se recomienda tener el programa en una carpeta, ya que genera varios archivos.
### Instalación.
Ya que es un Script solo se necesita abrir una terminal y llamarlo, de la siguente manera:
	bash proyecto2.sh
### Anàlisis.
El programa consiste en que luego de ser ejecutado el Script, se solicita una ID de proteina, estas se pueden obtener en la primera ejecuciòn del programa, en la cual se descarga. Luego se solicita la distancia de la cual se quiere obtener un grafica de los aminoacidos que se encuentran en dicha distancia, para generar el grafico, primero hay que explicar que se maneja el concepto de centro geometrico del ligando, esto quiere decir un promedio de los componentes de los vectores de los atomos del ligando, al obtener un vector final, este se calcula el modulo con cada vector de los atomos del determinado pdb de la proteina manipulada, a través de un algoritmo (el cual esta comentado), al encontrar un atomo que se encuentra en una distancia menor o igual a la ingresada por el usuario, este atomo y el aminoacido por completo es
graficado. Dando como producto 2 carpetas que contienen los archivos "temp", donde se encuentra toda la información filtrada y manipulada del pdb, y otra carpeta render, donde se encuentra las imagenes de los ligando.
Mencionar que, si el programa no es interrupido, con factores del usuario o mala conexiòn de internet, no existe un mètodo para verificar si los archivos son correctos (dado que podrian estar dañados),
 pero de lo contrario, si no existe una interrupciòn, el programa deberia tener una funcionalidad minima. Y por último, al ingresar la distancia se aclara en este README, que tiene que ser ingresado un numero real positivo.
## Construido con.
Se mencionarà las herramientas usadas, y la funciòn en ESTE proyecto.

* [BASH] - Script que corre los comandos.
* [AWK] - Manipulados de texto, especificamente la base de datos.
* [graphviz] - Graficador de los aminoacidos que estan a la distancia indicada del CG del ligando.
## Autores.

* Benjamìn Adolfo Sanzana Silva [baaass2](https://github.com/baaass2/bsanzana_reposoluciones)

