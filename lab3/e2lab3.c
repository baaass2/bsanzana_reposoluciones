/*INICIO
 * En el main 
 * Pedir numero del termometro a registrar
 * Guardar variabler 
 * hacer la escala del termometro a traves de printfs
 * En la funcion termometro 
 * restarle 1 al numero ingresado por usuario
 * hacer ciclo con maximo del numero ingresado por usuario
 * dentro del ciclo hacer printf con el guion
 * fuera del ciclo hacer un printf con *
 * En un procedimiento imprimir el estado del termometro
 * FIN

*/
#include <stdlib.h>
#include <stdio.h>

int termometro (int numero_de_termometro){
	
	int i=1;
	numero_de_termometro=numero_de_termometro-1;
	
	for (i=1; i<=numero_de_termometro; i++){
		printf("-");
	}
	
	printf("*");
	return numero_de_termometro;
}

void estado_de_termometro(int numero_de_termometro){
	
	printf("\n Estado del termometro: %d °C  " ,numero_de_termometro);
}




int main (){
	
	int numero_de_termometro;
	printf("Ingrese valor para el termometro: ");
	scanf("%d", &numero_de_termometro);
	printf("1         10        20        30        40        50  \n");
	printf("|        |         |         |         |         |\n");
			
	termometro(numero_de_termometro);
	estado_de_termometro(numero_de_termometro);

return 0;
}
