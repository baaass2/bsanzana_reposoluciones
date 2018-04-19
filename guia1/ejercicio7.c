/*
 * INICIO
 * Solicitar los dias que se quiere transformar a segundos
 * Guardar dato en variable
 * Hacer operaciones para obtener los dias en segundos
 * Imprimir resultado
 * FIN
 * 
 */


#include <stdio.h>

int main()
{
	int dias,horas,minutos,segundos;
	
	printf("¿Cuántas dias quiere transformar a segundos?: ");
	scanf("%d",&dias);
	horas=(24*dias);
	minutos=(60*horas);
	segundos=(60*minutos);
	printf("El resultado de la transformación es: %d ",segundos);

	
	return 0;
}

