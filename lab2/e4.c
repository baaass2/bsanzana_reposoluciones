/* INICIO
 * Pedir goles que hizo el equipo los gloriosos
 * guardar variable
 * Pedir goles de adversario
 * Guardar variable
 * realizar un ciclo con maximo de 5
 * crear variable puntaje
 * si los goles de LG es  mayor a adversario sumo 3 a puntaje
 * si los goles de LG es  igual a adversario sumo 1 a puntaje
 * si los goles de LG es  menor a adversario sumo 0 a puntaje
 * imprimir puntaje.
 * FIN

 */


#include <stdio.h>

int main()
{
	int i=0, puntaje=0, goldegloriosos, goldeadversario;
	
	while(i<5){
	
	printf("Escribir los goles que hizo el equipo los gloriosos: ");
	scanf("%d", &goldegloriosos);
	printf("Escribir los goles del adversario: ");
	scanf("%d", &goldeadversario);
	printf("---------------------------------------------------\n");
	
	if (goldegloriosos>goldeadversario){
		puntaje=puntaje+3;
	}
	else if(goldegloriosos<goldeadversario){
		puntaje=puntaje+1;
	}
	else if (goldegloriosos==goldeadversario){
		puntaje=puntaje+0;
	}
	
	i++;
}

	printf("Los puntos totales de Los Gloriosos %d: ", puntaje);
	
	
	return 0;
}

