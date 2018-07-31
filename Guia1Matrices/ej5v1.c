

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
void matrizaleatoria(){
	
	int fila=0, columna=0;
	
	printf("INGRESE NUMERO DE FILAS: ");
	scanf("%d",&fila);
	
	printf("INGRESE NUMERO DE COLUMNA: ");
	scanf("%d",&columna);
	
	int matriz[fila][columna];
	int x=0, y=0, num=0;
	
	
	srand(time( 0 ));
	

	
	for(x=0; x<fila; x++){
		for(y=0; y<columna; y++){
			num= rand( )%9;
			matriz[x][y]=num;
		}
	}
			
	for(x=0; x<fila; x++){
		for(y=0; y<columna; y++){
			printf("%d ", matriz[x][y]);
		}
		printf("\n");
	}
	printf("\n");
	printf("\n");
	printf("\n");
	printf("\n");
	printf("\n");
	printf("\n");
	
	for(x=0; x<columna; x++){
		for(y=0; y<fila; y++){
			printf("%d ", matriz[y][x]);
		}
		printf("\n");
	}
	
	
	
	
}

int main()
{
	matrizaleatoria();
	
	return 0;
}

