/*
 * INICIO
 * Solicitar base del rectangulo.
 * Solicitar altura del rectangulo.
 * Calcular perimetro y area con sus respectivas operaciones.
 * Imprimir el Area, y el Perimetro. 
 * FIN
 */


#include <stdio.h>

int main()
{
	int b,h,P,A;
	
	printf("Ingresar base del rectangulo: ");
	scanf("%d",&b);
	printf("Ingresar altura del rectangulo: ");
	scanf("%d",&h);
	P= 2*(b+h);
	A= (b*h);
	printf("La superficie de su rectangulo es: %d\n",A);
	printf("El perimetro de su rectangulo es : %d",P);
	
	
	return 0;
}

