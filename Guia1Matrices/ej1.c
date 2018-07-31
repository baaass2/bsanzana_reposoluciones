

#include <stdio.h>

void matriz(int i, int k){
	
	int matrizz[i][k];
	int j=0, l=0;
	
	for(j=0; j<i; j++){
		for(l=0; l<k; l++){
			matrizz[j][l]=0;
		}
	}
	for(j=0; j<i; j++){
		for(l=0; l<k; l++){
			printf("%d, ", matrizz[j][l]);
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
	
	matriz(i, k);
	return 0;
}

