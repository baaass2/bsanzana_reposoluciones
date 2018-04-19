/*
 * Solicitar lado a
 * Guardar lado a
 * Solicitar lado b
 * Guardar lado b
 * Hacer operacion para calcular Hipotenusa
 * Imprimir en pantalla hipotenusa
 * 
 */


#include <stdio.h>

int main()
{
	int a, b, c, b2, a2;
	
	printf("Escribir lado a: ");
	scanf("%d",&a);
	printf("Escribir lado b: ");
	scanf("%d",&b);
	a2=(a*a);
	b2=(b*b);
	c= b2+a2;
	printf("La hipotenusa al cuadrado es: %d",c);
	
	return 0;
}

