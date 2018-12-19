Jail_max_v1

El proyecto es un programa el cual tiene como finalidad uilizarse en la distribucion administrativa de reos en determinadas carceles, el software contara con la funcion de poder iniciar sesion con una determinada cuenta, para ello incluimos un boton el cual se llama "crear cuenta" y sirve expresamente para esto, donde aparte tambien se puede elegir el rango que tendra esta cuenta, los cuales pueden ser:

-Guardia: solo revisa hoja de vida, y lista de prisioneros
-Secretaria: puede agregar y cambiar describipcion y sentencia
-Alcaide: cambia estado de los prisioneros

Cada cuenta que se cree tendra que ser de minimo 5 digitos, al igual que la contraseña.
Una vez iniciado la sesion, se desplegara la ventana para seleccionar la carcel que se quiera administras, donde tambien habra un boton para crear carcel, donde se vera la cantidad de celdas que tendra esta, al igual que la cantidad de prisioneros que podra contener cada una.

Una vez ingresado al menu principal, se tendran opciones para añadir prisioneros, ver todos los prisioneros y sus estados, al igual que la funcionalidad de poder ver un grafico el cual nos representara la cantidad de presos que hay en cada celda de la prision y finalmente una entrada de texto que servira para poder buscar presos por rut completo y de esta forma poder editar sus datos al igual que su estado.

Para poder concretar nuestro proyecto de manera efectiva, ambos integrantes hicimos uso de github para poder traspasarnos nuestros avances de manera optina (los avances se encuentran en el historial de el repositorio donde fue subido el proyecto https://github.com/baaass2/bsanzana_reposoluciones/commits/master/proyecto2)

Pre-requisitos:

-Se recomienda tener instalada cualquier distribucion de Linux (ya que, por ejempplo en windowns, es recurrente que ocurran percanses)
-Para poder correr el programa se requiere tener instalado Python v3.7(los diccionarios no se desordenan en esta version y el codigo esta ajustado a esta caracteristica), ya sea en su sistema operativo o en un entorno virtual previamente creado (se recomienda encarecidamente el entorno virtual y de hecho el readme está orientado a hacer uso de el).
-Se necesita tambien tener instalado glade en la maquina y pygobject en el entorno virtual.
-Es requerido tener instalado la libreria externa matplotlib, la cual fue utilizada para aplicar el grafico.

Instalacion:

-Ir al siguiente link https://www.linux.org/ y dirigirse a la pestaña de download donde se podran encontrar todas las distribuciones de este sistema operativo, con guias incluidas y de manera completamente gratuita.
-Para la instalacion de Python v3.x, se recomienda visitar el siguiente link donde se muestra un pequeño tutorial de como instalarlo de manera correcta, https://srvbioinf1.utalca.cl/wiki/programacion/python/instalacion
-Y finalmente si se opta por utilizar un entorno virtual (recomendado), favor de dirigirse a este link donde hay un tutorial perfectamente detallado de como crear uno y hacer uso de este https://srvbioinf1.utalca.cl/wiki/programacion/python/entorno-virtual
-°De otra forma recomiendo que se descargue el siguiente script y se haga uso de el para poder descargar python de una forma mas sencilla (ademas de dejar todo listo para hacer el entorno virtual y dejar los comandos listos para ello) http://gitlab.com/confor/python/raw/master/instalar-python-nuevo.sh
-Para instalar glade, abrir la terminal y escribir: "apt-get install", sin las comillas.
-Para instalar pygobject escribir en la terminal y con el entorno virtual abierto: "pip install pygobject", sin las comillas.
-Para instalar matplotlib, es necesario activar el entorno virtual y dentro de este escribir: "python -m pip install -U pip" y "python -m pip install -U matplotlib" (sin las comillas, para mas informacion visitar https://matplotlib.org/users/installing.html)
											    


Detalles:

El programa en general funciona y de una manera bastante correcta, ya que nos enfocamos bastante en la eliminacion de errores, por lo que no deberia de dar ninguno, almenos que nosotros hayamos vistos, probablemente falto la funcion de poder eliminar cuentas y carceles, sin embargo no lo consideramos de vital importancia y siempre se podran eliminar los json para esto. Tal vez si se hubiese tenido un poco mas de tiempo hubiesemos terminado cuestiones como estas, pero en general creemos que cumple con lo que se queria lograr y eso es lo mas importante en definitiva.}

Construido con:

Para la elaboracion de el programa se utilizo:
-Editor de texto gnome-builder y Geany
-Glade

Desarrolladores:
----------Benjamin Sanzana y Pedro Salinas--------------------------