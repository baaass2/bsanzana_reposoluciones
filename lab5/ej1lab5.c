/*
	INICIO
*	PEDIR OPCION A O B
*  GENERAR 2 NUMEROS ALETORIOS Y GUARDARLOS EN 2 VARIABLS
* IMPRIMIR LOS 2 NUMEROS ALETORIOS
* HACER CONDICIONALES QUE SI A ES MAYOR A B Y EL USUARIO ELIGIO A ENTONCES SUMARLE UN CONTADOR
* POR EL CONTRARIO SUMARLE A UN CONTADOR DE PERDIDAS!
* HACER UN CONDICIONAL QUE B ES MAYOR A Y EL USUARIO ELIGIO B ENTONCES SUMARLE A UN CONTADOR
* POR EL CONTRARIO SUMARLE AL CONTADOR DE PERDIDAS
* IMPRIMIR  EL CONTADOR!
* ADEMÁS CREAR UNA OPCION EN LA CUAL SI PONEN N EL CICLO TERMINA
* FIN! 
 */


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int apuesta(){
	int numero, numero2, contador=0, contador1=0;
	char fin, opc;
	
	srand(time(0));
	
	while(fin!='N'){
		
	printf("\n ESCOJA ENTRE LA OPC A Y B: ");
	scanf(" %c", &opc);
	
	
	numero = (rand() %10)+1;
	numero2 = (rand() %10)+1;
	
	printf("A = %d y B = %d",numero, numero2);
	
		if (numero>numero2){
			if (opc=='A' || opc=='a'){
			printf("\nHAS GANADO!");
			contador++;
			}
			else{
			printf("\nHAS PERDIDO!");
			contador1++;
			}
		}
		else{
			if (opc=='B' || opc=='b'){
			printf("\nHAS GANADO!");
			contador++;
			}
			else{
			printf("\nHAS PERDIDO!");
			contador1++;
			}
		}
		
		printf("\nPARTIDAS GANADAS %d y PARTIDAS PERDIDAS %d",contador, contador1);
		
		printf("\n Quieres apostar otra vez ? (S/N): ");
		scanf(" %c" ,&fin);
	}
		printf("\nPARTIDAS GANADAS %d y PARTIDAS PERDIDAS %d",contador, contador1);
	
	
	
	return contador;
}

	
	
int main()
{
	apuesta();
	
	return 0;
}

