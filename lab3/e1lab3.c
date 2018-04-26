/* INICIO
 * En el main pedir ingresar el valor por hora de trabajo
 * Guardar variable
 * Siguiendo en el main, pedir con un ciclo de maximo 6 , cuantas horas tabrajo en cada dia.
 * Crear funcion calculo_sueldo.
 * Ahi llegaran total_de_horas y valor_de_hora, y se multiplicaran.
 * Crear procedimiento llamado imprimir_sueldo.
 * Imprimir el resultado de la funcion llamada calculo_sueldo, en la variable sueldo.
 * FIN 
 * 
*/

#include <stdio.h>
#include <stdlib.h>
int calculo_sueldo (int total_de_horas, int valor_de_hora){

	int sueldo;
	sueldo=(total_de_horas*valor_de_hora);
	return sueldo;
}

void imprimir_sueldo (int sueldo){
	printf("El sueldo de la semana es: %d", sueldo);
	
}
	
int main(){
	
	
	int i=1, valor_de_hora, dia, total_de_horas=0, sueldo;
	printf("Ingrese el valor de la hora de trabajo: ");
	scanf("%d", &valor_de_hora);
	
	for (i=1; i<=6; i++){
	printf ("¿Cuantas horas trabajo el dia %d: ", i);
	scanf("%d", &dia);
	total_de_horas=(total_de_horas+dia);
    }
	
	sueldo=calculo_sueldo(total_de_horas, valor_de_hora);
	imprimir_sueldo(sueldo);
	
	return 0;
}


