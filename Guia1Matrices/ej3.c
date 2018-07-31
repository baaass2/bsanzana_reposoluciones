
#include <stdio.h>
#include <stdlib.h>
void relleno(int i, int k){
	
	int x=0, y=0, valor=0, contador=0, suma=0, sumatotal=0;
	int matriz[i][k];
	
	for(x=0; x<i; x++){				//se llena la matriz//
		for(y=0; y<k; y++){
			printf("\nINGRESE VALOR A %d, %d: ", x, y);
			scanf("%d", &valor);
			matriz[x][y]= valor;
		}
		system("clear");
	}
	
	for(x=0; x<i; x++){       //imprime la matriz//
		for(y=0; y<k; y++){
			printf("%d, ", matriz[x][y]);
		}
		printf("\n");
	}
	
	for(x=0; x<i; x++){					//suma las fila, haciendo que los elementos se guarden en contador, y se vayan sumando a "suma"//
		for(y=0; y<k; y++){			
			contador = matriz[x][y];
			suma = contador+ suma;
		}
		printf("\n SUMA DE LA  FILA %d es: %d",x, suma);
		suma=0;
		contador=0;
	}
	for(y=0; y<i; y++){					////suma las columna, haciendo que los elementos se guarden en contador, y se vayan sumando a suma//
		for(x=0; x<k; x++){
			contador = matriz[x][y];
			suma = contador+ suma;
		}
		printf("\n SUMA DE LA COLUMNA %d es: %d",x, suma);
		suma=0;
		contador=0;
	}
	
	for(x=0; x<i; x++){						//"sumatotal" guarda la suma de toda la matriz//
		for(y=0; y<k; y++){
			sumatotal = sumatotal + matriz[x][y];
		}
	}
	printf("\n SUMA TOTAL: %d", sumatotal);
			
}


int main()
{
	int i, k;
	printf("NUMERO DE FILAS: ");
	scanf("%d", &i);
	printf("NUMERO DE COLUMNAS: ");
	scanf("%d", &k);
	
	relleno(i, k);
	
	return 0;
}

