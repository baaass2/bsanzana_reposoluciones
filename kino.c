#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void ordburbuja(int a[], int n){
	int interruptor=1;
	int pasada, j;
	
	for(pasada = 0; pasada < n -1 && interruptor; pasada++){
		
		interruptor = 0;
		
		for(j=0; j<n-pasada-1; j++)
			if(a[j] > a[j+1]){
				
				int aux;
				interruptor = 1;
				aux = a[j];
				a[j]= a[j+1];
				a[j+1]=aux;
			}
		}
	}	

void arreglonumerosganadores(){

	int arreglokino[25];
	int arreglousr[15];
	int numero, numero2, k, i, ticket, aciertos=0;
	
	
	srand(time( 0 ));
	
	for(i=0; i<25; i++){
	
	numero = ( rand( )%26);
	
	arreglokino[i] = numero;
	}
	i=0;
	while(i<25){
		k=1;
		while(k<24){
			
			if(arreglokino[i]==arreglokino[k]){
				numero2 = ( rand( )%26);
				arreglokino[i]=numero2;
			}
			else if(arreglokino[i]!=arreglokino[k]){
			k++;
			}
		}
	i++;	
	}
		ordburbuja(arreglokino, 25);
	
	for(i=0; i<25; i++){
	printf("%d,", arreglokino[i]);
	}
	
	
	
	
	for(i=0; i<15; i++){

	printf("\nINGRESAR NUMERO DEL 0-15 (SIN REPETIR) %d: ", i+1);
	scanf("%d", &ticket);
	arreglousr[i]=ticket;
	}
	
	ordburbuja(arreglousr,15);
	
	for(i=0; i<25; i++){
		k=1;
		while(k<25){
			if(arreglokino[i]==arreglousr[k]){
				aciertos++;
			}
			else if(arreglousr[i]!=arreglokino[k] && arreglousr[i] < arreglokino[k]){
			break;
			}
			k++;
		}
	}
	printf("\n NUMERO DE ACIERTOS: %d", aciertos);
} 
	
	
int main(){
	
	arreglonumerosganadores();
	
	return 0;
}

//**1. kino de 25 
   //2. usr pone 15 y el computador al azar 25
 // 3. 10 para el premio
 //porque en quicksort se elije el de almedio  yno otro
