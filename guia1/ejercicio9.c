/*INICIO
 * Solicitar sueldo base del vendedor
 * Guardar dato en variable
 * Solicitar el dato de cuanto vendió
 * Guardar dato en variable
 * Realizar operacion para obtener el 7% de las ventas extras
 * Imprimir el valor de la comisión
 * Sumar la comisión al sueldo base
 * Imprimir sueldo total
 * FIN
 * 
 * 
 * 
 */


#include <stdio.h>

int main()
{
	int sueldo;
	float comision,sueldototal,ventasextras;
	
	printf("Escribir sueldo base del vendedor: ");
	scanf("%d",&sueldo);
	printf("¿Cuánto vendió?: ");
	scanf("%f",&ventasextras);
	comision=(ventasextras*7)/100;
	printf("La comisión extra consta de: %.1f\n",comision);
	sueldototal= (comision+sueldo);
	printf("Sueldo total: %.1f\n",sueldototal);
	return 0;
	
}

