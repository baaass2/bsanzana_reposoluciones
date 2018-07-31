#include <stdio.h>

int main()
{	
	int x, y;
	int matriz[4][4] = {{8, 1, 3, 5}, {1, 7, 4, 5}, {3, 4, 9, 5},{5, 5, 5, 5}};
	int n=4, contador=0;
	for(x=0; x<n; x++){
		for(y=0; y<n; y++){
			printf("%d,", matriz[x][y]);
		}
		printf("\n");
	}
	for(x=0; x<n; x++){
		for(y=0; y<n; y++){
				if(matriz[x][y]== matriz[y][x]){
					contador++;
				}
		}
	}
	if(contador==(n)){
		printf("\n SIMETRICA");
	}
	else if(contador!=(n)){
		printf("\n NO ES SIMETRICA");
	}
		
			
			
	
	return 0;
}

