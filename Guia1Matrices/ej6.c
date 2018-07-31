
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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


void matrizclima(){

	int matriz[7][24];
	int clima[168];
	
	int x=0, y=0, num=0;
	int fila=7, columna=24;
	
	srand(time( 0 ));
	
	for(x=0; x<fila; x++){
		for(y=0; y<columna; y++){
			num= (rand() % 40)-20;
			matriz[x][y]=num;
		}
	}
	
	//La máxima y mı́nima temperaturas de la semana.//
	
	int j=0;
	
	for(x=0; x<fila; x++){
		for(y=0; y<columna; y++){
			clima[j] = matriz[x][y];
			j++;
		}
	}
	burbuja(clima, 168);
	
	printf("\n La máxima fue de %d y la mı́nima fue de %d temperaturas de la semana.",clima[167], clima[0]);
	//La temperatura media de la semana.//
	int media=0;
	for(x=0; x<168; x++){
		media = media + clima[x];
	}
	
	printf("\n La temperatura media de la semana fue de : %d", (media/168));
	
	//El número de dı́as en los que la temperatura media fue superior a 30 grados.//
	int contador=0;
	
	for(x=0; x<168; x++){
		if (clima[x]==30){
			contador++;
		}
	}
	printf("\n El número de dı́as en los que la temperatura media fue superior a 30 grados: %d", contador);
	
	
	//La máxima y mı́nima temperaturas de cada dı́a.//
	int dia[24], l=0;

	for(x=0; x<fila; x++){
		j=0;
		for(y=0; y<columna; y++){
				dia[j] = matriz[x][y]; //dia[j] se lleva la primera fila, que en el contexto es dia1, asi suceviamente.
				j++;
		}
		burbuja(dia, 24); //ordena//
		
		printf("\n------------------------------DIA %d-------------------------------------------------------", x+1);
		printf("\n La máxima fue de %d y mı́nima fue de %d temperatura.", dia[23], dia[0]);
	//La temperatura media de cada dı́a.//
		media=0;
		for(l=0; l<24; l++){
			media = media + dia[l];
		}
		printf("\n La temperatura media fue de: %d",(media/24));
		printf("\n------------------------------------------------------------------------------------------");
	}
}
int main()
{
	matrizclima();
	
	return 0;
}

