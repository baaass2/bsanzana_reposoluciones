


#include <stdio.h>
void diagonal(int i, int k){
	
	int matriz[i][k];
	int x=0, y=0;
	
	for(x=0; x<i; x++){
		for(y=0; y<k; y++){
			
			if(x==y){
				matriz[x][y]=1; //las diagonales las hace 1, ya que la diagonal es x=y//
			}
			else{
				matriz[x][y]=0;
			}
		}
	}
	
	for(x=0; x<i; x++){
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
	
	diagonal(i, k);
	
	return 0;
}

