#include <stdio.h>
#include <string.h>
void burbuja(int a[], int n){
	
	int i, j;
	
	for(i=0; i<n; i++){
		for(j=0; j<n-1; j++)
			if(a[j] > a[j+1]){
				
				int aux;
				aux = a[j];
				a[j]= a[j+1];
				a[j+1]=aux;
			}
		}
} 
int main()
{	
	
	int n=0;
	int i=0;
	int largo=0;
	
	printf("\nINGRESE LARGO: ");
	scanf(" %d", &largo);
	
	char secuencia[largo];		
	
	for(i=0; i<largo; i++){
		printf("INGRESE SECUENCIA: ");
		scanf(" %c", &secuencia[i]);
	}
	
	int secuencianum[n];
	
	
	for(i=0; i<largo; i++){
		if(secuencia[i]=='a' || secuencia[i]=='A'){
			secuencianum[i]=1;
		}
		else if(secuencia[i]=='c' || secuencia[i]=='C'){
			secuencianum[i]=2;
		}
		else if(secuencia[i]=='g' || secuencia[i]=='G'){
			secuencianum[i]=3;
		}
		else if(secuencia[i]=='t' || secuencia[i]=='T'){
			secuencianum[i]=4;
		}
	}
	
	burbuja(secuencianum, largo);
	
	printf("SECUENCIA ORDENADA ALFABETICAMENTE\n");
	
	for(i=0; i<largo; i++){
		if(secuencianum[i]==1){
			printf("a ");
		}
		else if(secuencianum[i]==2){
			printf("c ");
		}
		else if(secuencianum[i]==3){
			printf("g ");
		}
		else if(secuencianum[i]==4){
			printf("t ");
		}
	}
	
	
	
	//ORDEN ALFABETICO//
	
	return 0;
}

