/*
 *INICIO
 * Declarar que juan equivale a 5 (huevos), manuel equivale a 3(huevos) y antonio se asume que los $80 son 8 huevos.
 * Declarar que en si hay 8 huevos fisicamente.
 * En una funcion dividir los huevos totales en 3, de esta manera obtengo cuanto debe comer cada uno.
 * El resultado de la division se lo resto a la huevos por persona que se dan, y de esa manera obtengo el valor que tienen a favor de lo que aportaron.
 * Luego multiplico por 10 para de esa manera tranformarlo a pesos!
 * Imprimir el pago que tiene que dar antonio a sus amigos, y los pesos que se tiene que quedar.
 * FIN!
 * 
 */


#include <stdio.h>
#include <stdio.h>

float calcular_huevos (float amigosantonio, float huevostotales){

	float huevosporpersona, pesos;
	
	huevosporpersona= (huevostotales/3);
	amigosantonio= (amigosantonio-huevosporpersona);
	pesos= (amigosantonio*10);
	
	return pesos;
	
}

int main()
{
	int juan=5, manuel=3, antonio=8, huevostotales=8;
	float dinerojuan, dineromanuel, dineroantonio;
	
	dinerojuan = calcular_huevos(juan, huevostotales);
	dineromanuel = calcular_huevos(manuel, huevostotales);
	dineroantonio= calcular_huevos(antonio, huevostotales);
	
	printf("Juan debe recibir %.2f pesos", dinerojuan);
	printf("\nManuel debe recibir %.2f pesos", dineromanuel);
	printf("\nAntonio debe quedarse con  %.2f pesos", dineroantonio);
	

	return 0;
}

