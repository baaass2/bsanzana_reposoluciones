#include <stdio.h>
#include <stdlib.h>

void rellenodematriz(){
	int matriz[4][5];
	int vector[4];
	int x, y, i;
	int fila=4, columna=5, valor=0, suma=0, contador=0;
	
	for(x=0; x<fila; x++){
		for(y=0; y<columna; y++){
			printf("INGRESE VALOR A %d,%d : ",x, y);
			scanf("%d", &valor);
			matriz[x][y]=valor;
		}
		system("clear");
	}
	i=0;
	for(x=0; x<fila; x++){
		for(y=0; y<columna; y++){
			contador = matriz[x][y];
			suma = suma + contador;
		}
			vector[i]=suma;
			i++;
		suma=0;
		contador=0;
	}
	for(x=0; x<fila; x++){
		for(y=0; y<columna; y++){
			printf("%d, ", matriz[x][y]);
		}
		printf("\n");
	}
	printf("----------------------------------------------------------\n");
	for(i=0; i<4; i++){
			printf("%d, ",vector[i]);
		}
}

int main()
{
	rellenodematriz();
	
	return 0;
}

