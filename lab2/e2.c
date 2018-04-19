/* INICIO
 * pedir valor 
 * guardar variable
 * si variable es menos o igual a 9 
 * hacer ciclo con for para que me enliste los numeros
 * con otro ciclo me enlistara los numeros pero restandolos 1 en 1 hasta llegar a un tope de 1
 * FIN
*
 * 
 */


#include <stdio.h>

int main()
{
	int valor, i=1;
	
	printf("Ingrese valor: ");
	scanf("%d", &valor);
	
	if (valor<=9 && valor!=0){
		
		for(i=1; i<=valor; i++){
		printf("%d",i);
	}
	
		for(i=valor; i==1; i--)
		printf("%d",i);
	}
	
	
	
	
	


	
	return 0;
}

