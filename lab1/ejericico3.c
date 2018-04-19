/*
 * Pedir costo de la compra
 * Guardar Variable
 * Realizar comparacion si es mayor o menos a 2500
 * si es mayor a 2500 restarle el 15%
 * si es menor o igual 2500 restarle 8%
 * Imprimir total de la compra
 
 */


#include <stdio.h>

int main()
{
	float compra,total,descuento,descuento2;
	
	printf("Costo de la compra: ");
	scanf("%f",&compra);
	
	if (compra > 2500){
		
		descuento=(compra*0.15);
		total=(compra-descuento);
	}
	else if (compra<=2500){
		
		descuento2=(compra*0.08);
		total=(compra-descuento2);
	}
	
	printf("total de la compra + descucento %f",total);
		
	
	return 0;
}

