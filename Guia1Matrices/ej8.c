#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void matriz1(int i, int k){
	
	int matriz[i][k];
	int x=0, y=0, num=0;
	int fila=i, columna=k;
	
	srand(time( 0 ));
	
	for(x=0; x<fila; x++){
		for(y=0; y<columna; y++){
			num = rand( )%9;
			matriz[x][y]=num;
		}
	}
	for(x=0; x<fila; x++){
		for(y=0; y<k; y++){
			printf("%d, ", matriz[x][y]);
		}
		printf("\n");
	}
	printf("\n");
	
	for(x=i-1; x>=0; x--){
		for(y=0; y<k; y++){
			printf("%d, ", matriz[x][y]);
		}
		printf("\n");
	}
	
}

int main()
{	
	int i, k;
	printf("NUMERO DE FILAS: ");
	scanf("%d", &i);
	printf("NUMERO DE COLUMNAS: ");
	scanf("%d", &k);
	
	matriz1(i, k);
	return 0;
}

