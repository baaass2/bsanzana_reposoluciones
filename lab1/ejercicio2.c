/*
 * Pedir cantidad de personas que van a comer (Contando a Pedro)
 * Guardar Variable
 * Pedir total de la cuenta
 * Guardar variable
 * Realizar las operaciones correspondientes (detallado en el codigo)
 * Imprimir total
 * 

 */


#include <stdio.h>

int main()
{ 
	int amigos,total;
	float iva,x,y,z;
	
	printf("¿cuantos comieron? (contar a Pedro): ");
	scanf("%d",&amigos);
	printf("¿cuanto es el total de la cuenta?: ");
	scanf("%d",&total);
	
	iva=(total*0.19); // opero el iva al total//
	x=(iva+total);    //sumo el iva al total//
	y=(x*0.1);        //al total+iva le saco el 10% (propina)//
	y=(x+y);          // sumo el 10% al total//
	z=(y/amigos);      // total+19%+10& lo divido entre los amigos//
	
	printf("El total que debe pagar cada comensal: %f",z); 
	
	
	
	
	
	return 0;
}

