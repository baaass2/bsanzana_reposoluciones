/*INICIO
 * Solicitar número de galones vendidos
 * Guardar dato en variable
 * Hacer calculo para saber cuantos litro se vendieron
 * Multiplicar litros por $820
 * Imprimir cuantos litros se vendió
 * Imprimir cuanto debe cancelar en pesos
 * FIN
 * 
 * 
 */


#include <stdio.h>

int main()
{
	float galones,calculo,calculo2;
	int litros=3785;
	
	printf("Ingresar ¿Cuántos galones se vendieron?: ");
	scanf("%f",&galones); 	 	
	calculo= (galones*litros);	
	calculo2=(820*calculo); 	 	
	printf("El cliente compro %f litros de gasolina \n",calculo); 	
	printf("Debe cancelar %f pesos\n",calculo2);
	
	return 0;
}

