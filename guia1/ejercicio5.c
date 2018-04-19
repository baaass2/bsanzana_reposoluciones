/*
 * INICIO
 * Pedir a usuario nombre del dinosaurio
 * Guardar nombre en variable
 * Solicitar masa del dinosaurio
 * Guardar masa en variable
 * Solicitar longitud  del dinosaurio
 * Guardar longitud en variable
 * Realizar las correspondientes operaciones para transformar la unidad de medidas ingresadas a metros y kilogramos respectivamente
 * Imprimir en pantalla nombre del dinosaurio, masa en kilogramos y longitud en metros
 * 
 */


#include <stdio.h>

int main()
{
	float libra,pie,kg,m;
	char dino[64];
	
	printf("Ingresar nombre del dinosaurio: ");
	scanf("%s",&dino);
	printf("Ingrese masa en libras del dinosaurio %s:  ",dino);
	scanf("%f",&libra);
	printf("Ingrese longitud en pies del dinosaurio %s:  ",dino);
	scanf("%f",&pie);
	kg= (0.45*libra);
	m= (0.3048*pie);
	printf("--------------------------------------------\n");
	printf("Dinosaurio %s\n",dino);
	printf("Masa(kg)= %f\n",kg);
	printf("Longitud(m)= %f\n",m);
	printf("--------------------------------------------\n");
	
	
	return 0;
}

