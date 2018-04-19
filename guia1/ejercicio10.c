/*
 *INICIO
 * Imprimir nombre de la compañia.
 * Solicitar kilometros el viaje.
 * Guardar datoe en variable.
 * Solicitar costo por kilometro.
 * Guardar dato en variable.
 * Realizar operacion (multiplicación).
 * Imprimir el valor del viaje.
 * FIN
 * 
 * 
 */


#include <stdio.h>

int main()
{
	float kilometros,costo,x;
	
	printf("Buses Camino al cielo\n");
	printf("Ingresar kilometros del viaje: ");
	scanf("%f",&kilometros);
	printf("Costo por Kilometro: ");
	scanf("%f",&costo);
	x=(kilometros*costo);
	printf("Valor del viaje es de: %f pesos.",x);
	
	
	return 0;
}

