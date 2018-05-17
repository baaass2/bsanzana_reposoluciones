/* INICIO
 * PEDIR NUMERO Y GUARDARLO
 * EN UN CICLO SACAR LOS RESTOS Y SUMARLOS
 * LOS RESTOS SUMADOS SI SIGUEN SIENDO MAYOR A 9, ENVIARLO A OTRO CICLO
 * POR LO CONTRARIO SE IMPRIME LA RAIZ VIRTUAL
 * EN ESE CICLO SE HACE EL MISMO PROCEDIMIENTO Y SE IMPRIME LA RAIZ VIRTUAL
 * FIN

 * 
 */


#include <stdio.h>
#include <stdlib.h>



int raizvirtual(int numero){
	
	int suma=0, resto, suma2=0;
	
	while(numero !=0 ){
		
	resto = numero%10;
	numero = numero-resto;
	numero = numero/10;
	
	suma = suma + resto;
	}
	
	if (suma >9){
		while(suma !=0 ){
		
		resto = suma%10;
		suma = suma-resto;
		suma = suma/10;
	
		suma2 = suma2 + resto;
		}
		printf("raizvirtual: %d", suma2);
	}
	
	
	
	else{
		printf("raizvirtual: %d" ,suma);
	}
	 
	
	return suma;
}	


	 
	 


int main(){
	int numero;
	
	printf("INGRESE NUMERO: ");
	scanf("%d", &numero);
	 
	raizvirtual(numero);
	return 0;
}
