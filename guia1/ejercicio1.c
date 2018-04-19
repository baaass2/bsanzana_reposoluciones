/*
 * INICIO
 * Solicitar número de matricula
 * Guardar numero de matricula
 * Pedir Notas
 * Guardar Notas
 * Ejecutar operacion para obtener media de las notas
 * Imprimir en pantalla número de matricula
 * Imprimir en patanlla media de las notas
 * FIN
 * 
 * 
 */


#include <stdio.h>

int main()
{
	int matricula;
	float n1,n2,n3,media;

	printf("Ingrese Matricula: ");
	scanf("%d",&matricula);
	printf("Ingresar Nota 1: ");
	scanf("%f",&n1);
	printf("Ingresar Nota 2: ");
	scanf("%f",&n2);
	printf("Ingresar Nota 3: ");
	scanf("%f",&n3);
	media=(n1+n2+n3)/3;
	printf("Tú número de matricula es: %d\n",matricula);
	printf("El promedio de tus 3 notas es: %f",media);
	
	
	return 0;
}




