/*
 * INICIO 
 * Solicitar valor para X
 * Guardar dato en variable
 * Hacer operacion para obtener el polinomio determinado
 * Imprimir resultado
 * FIN
 * 
 * 
 */


#include <stdio.h>

int main()
{
	float x,operacion;
	
	printf("Escribir valor de X para el polinomio p(x)=X³+2X²+3X+5: ");
	scanf("%f",&x);
	operacion=((x*x*x)+(2*(x*x)+(3*x)+5));
	printf("Resultado %f: ",operacion);
	
	
	
	return 0;
}

