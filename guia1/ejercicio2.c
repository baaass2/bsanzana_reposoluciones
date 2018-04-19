/*
 * INICIO
 * Solicitar número para el ejercicio de calcular cubo y cuadrado
 * Guardar número
 * Realizar operaciones
 * Imprimir número que esta en cuestion
 * Imprimir las correspondientes operaciones
 * FIN
 */


#include <stdio.h>

int main()
{
	int cuadrado,cubo,a;
	
	printf("Ingresar número entero positvo para calcular su cuadrado y cubo: ");
	scanf("%d",&a);
	cuadrado= (a*a);
	cubo= (a*a*a);
	printf("El número en ejercicio %d\n",a);
	printf("Cuadrado: %d\n",cuadrado);
	printf("Cubo: %d\n",cubo);
	
	return 0;
}


