//INTEGRANTES: PEDRO SALINAS && BENJAMÍN SANZANA//
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_CYAN    "\x1b[36m"


int revisarfilalibre(int matriz[8][8], int y){
	
	int i=0, x=0;		
		
	for(i=7; i>=0; i--){            //VUELVE A REVISAR ESPACIO LIBRE, YA QUE LA X QUEDO EN UNA POSICION ARRIBA//
		for(y=0; y<8; y++){
			if(matriz[i][y]==0){
				x=i;
				i=0;
				break;
			}
		}
	}
	
	return x;
}
int revisarespacio(int matriz[8][8], int y){
	
	int i=0, x=0;
	
	for(i=7; i>=0; i--){     			//REVISA ESPACIO LIBRE//
		if(matriz[i][y]==0){
			x=i;
			break;
		}
	}	
	
	return x;	
}
int revision(int matriz[8][8], int jugador){
	int i=8, k=8;
	int x=0, y=0, ganador=0;
	
	// REVISION DE FILAS//
	for(x=0; x<i; x++){ 
		for(y=0; y<k-3; y++){
			if(matriz[x][y] == jugador && matriz[x][y+1] == jugador && matriz[x][y+2] == jugador && matriz[x][y+3] == jugador){
				ganador=jugador;
				break;
			}
		} 
	}
	//REVISION COLUMNAS//
	for(x=0; x<i-3; x++){
		for(y=0; y<k; y++){
			if(matriz[x][y] == jugador && matriz[x+1][y] == jugador && matriz[x+2][y] == jugador && matriz[x+3][y] == jugador){
				ganador=jugador;
				break;
			}
		}
	}
	//REVISION DIAGIONAL (PENDIENTE NEGATIVA) HACIA ABAJO//
	for(x=0; x<i-3; x++){
		for(y=0; y<k-3; y++){
			if(matriz[x][y] == jugador && matriz[x+1][y+1] == jugador && matriz[x+2][y+2] == jugador && matriz[x+3][y+3] == jugador){
				ganador=jugador;
				break;
			}
		}
	}

	//REVISION DIAGONAL (PENDIENTE NEGATIVA) MITAD ARRIBA //
			for(y=0; y<k-4; y++){
				if(matriz[x][y+1] == jugador && matriz[x+1][y+2] == jugador && matriz[x+2][y+3] == jugador && matriz[x+3][y+4] == jugador){
				ganador=jugador;
				break;
				}
			}
	//REVISION DIAGONAL (PENDIENTE POSITIVA) HACIA ARRIBA//
	for(x=7; x>=3; x--){
		for(y=0; y<k-3; y++){
			if(matriz[x][y] == jugador && matriz[x-1][y+1] == jugador && matriz[x-2][y+2] == jugador && matriz[x-3][y+3] == jugador){
				ganador=jugador;
				break;
			}
		}
	}
	//REVISION DIAGONAL (PENDIENTE POSITIVA) HACIA ABAJO//
	for(x=7; x>=4; x--){
		for(y=0; y<k-3; y++){
			if(matriz[x][y+1] == jugador && matriz[x-1][y+2] == jugador && matriz[x-2][y+3] == jugador && matriz[x-3][y+4] == jugador){
				ganador=jugador;
				break;
			}
		}
	}
	return ganador;
}

int dados(){

	int dado1, dado2;
	int jugador=0;
	
	srand(time(NULL));
	
	while(jugador==0){
			
		printf("Se estan lanzando los dados.......\n");
			
		sleep(2);
			
		dado1=rand()%6+1;
		dado2=rand()%6+1;
			
		printf("El jugador 1 obtuvo: [%d] y el jugador 2: [%d]\n",dado1,dado2);
			
		if(dado1>dado2){
			printf("El jugador 1 empieza \n");
			jugador=1;
		}
		else if(dado1<dado2){
			printf("El jugador 2 empieza \n");
			jugador=2;
		}
		else{ 
			printf("Igual valor de dados, repite el lanzamiento..\n");
			jugador=0;
		}
			
		sleep(3);
	}
		
	
	return jugador;
	
}
int mododejuego(){
	
	int mod;
	
	printf("\n------------------------------------------------");
	printf("\n MOD Jugador Solo ==  [1]");
	printf("\n MOD Jugador1 vs Jugador2 == [2]");
	printf("\n------------------------------------------------");
	printf("\n¿Modo de juego?: ");
	scanf("%d", &mod);
	
	
	while(mod!= 1 && mod!=2){
		printf("Ha ingresado un mod erroneo, vuelva a ingresarlo porfavor.\n");
		printf("¿Modo de juego?: ");
		scanf("%d", &mod);
	}
	system("clear");
	
	return mod;
}
void pintartablero(int matriz[8][8], int largo){
	
		
		int i=0, y=0;
		
		for(i=0; i<largo; i++){
			for(y=0; y<largo; y++){
				if(matriz[i][y]==1){
					printf(ANSI_COLOR_CYAN "%d,", matriz[i][y]);
				}
				else if(matriz[i][y]==2){
					printf(ANSI_COLOR_RED "%d,", matriz[i][y]);
				}
				else if(matriz[i][y]==0){
					printf(ANSI_COLOR_GREEN "%d,", matriz[i][y]);
				}
			}
			printf("\n");
		}
		printf("------------------------------------------------\n");
	}
	
void juego1vs1(int matriz[8][8], int jugador){

	int x=7, y=0;
	int largo=8, ganador=0;
	int jugadas=0;
		
	while(jugadas<65){
		
		pintartablero(matriz, largo);
		
		printf("\nINGRESE COLUMNA JUGADOR %d: ",jugador);
		scanf(" %d",&y);
		
		while(y>8 || y<1){
			printf("\n HA INGRESADO UN NUMERO DE COLUMNA INCORRECTA!!");
			printf("\n VUELVA HA INGRESAR UNA COLUMNA JUGADOR %d: ",jugador);
			scanf(" %d",&y);			
		}
		while(matriz[0][y-1]==1 || matriz[0][y-1]==2){	
			printf("Ese espacio ya esta ocupado, juega en otra columna porfavor.\n");
			printf("\nINGRESE COLUMNA JUGADOR %d: ",jugador);
			scanf(" %d",&y);
		}
		y--;
	
		if(matriz[x][y]==0){
			if(jugador==1){
				matriz[x][y]=1;
				jugadas++;
				ganador=revision(matriz, jugador);
				jugador++;
			}
			else if(jugador==2){
				matriz[x][y]=2;
				jugadas++;
				ganador=revision(matriz, jugador);
				jugador--;
			}
		}
		
		else if(matriz[x][y]!=0){
			
			x = revisarespacio(matriz, y);
				
			if(jugador==1){
				matriz[x][y]=1;
				jugadas++;
				ganador=revision(matriz, jugador);
				jugador++;
			}
			else if(jugador==2){
				matriz[x][y]=2;
				jugadas++;
				ganador=revision(matriz, jugador);
				jugador--;
			}
		}
		
		x = revisarfilalibre(matriz, y);		

		system("clear");
		
		if(ganador==1 || ganador==2){
			printf("GANADOR %d!!!!\n",ganador);
			printf("GANADOR %d!!!!\n",ganador);
			pintartablero(matriz, largo);
			jugadas=65;
		}
		if (jugadas==64){
			printf("El tablero esta lleno!!!\n");
			printf("ha ocurrido UN EMPATE!!!\n");
			pintartablero(matriz, largo);
			break;					
		}
	}
}

void juego1vsbot(int matriz[8][8],int jugador){
	
	int x=7, y=0;
	int largo=8, ganador=0;
	int jugadas=0;
	
	srand(time(NULL));
	
	while(jugadas<65){
	
		pintartablero(matriz, largo);
		
		if(jugador==1){
			printf("\nINGRESE COLUMNA JUGADOR %d: ",jugador);
			scanf(" %d",&y);
			
			while(y>8 || y<1){
				printf("\n HA INGRESADO UN NUMERO DE COLUMNA INCORRECTA!!");
				printf("\n VUELVA HA INGRESAR UNA COLUMNA JUGADOR %d: ",jugador);
				scanf(" %d",&y);
			}
			while(matriz[0][y-1]==1 || matriz[0][y-1]==2){	
				printf("Ese espacio ya esta ocupado, juega en otra columna porfavor.\n");
				printf("\nINGRESE COLUMNA JUGADOR %d: ",jugador);
				scanf(" %d",&y);
			}
			y--; // SIRVE PARA QUE EL JUGADOR ESCRIBA SOLO COLUMNAS DE 1-8, PERO PARA LA MATRIZ SERA 0-7//
			}
			
			else if(jugador==2){ //GENERA NUMERO ALEATORIO PARA EL BOT//
				y=rand()%8+1;
				y--;
			}
			
			if(matriz[x][y]==0){
				if(jugador==1){
					matriz[x][y]=1;
					jugadas++; //SUMA 1 SI HAY UN MOVIMIENTO DENTRO DE LAS REGLAS//
					ganador=revision(matriz, jugador);
					jugador++; //CAMBIO DE JUGADOR//
				}
			
			else if(jugador==2){
				matriz[x][y]=2;
				jugadas++;
				ganador=revision(matriz, jugador);
				jugador--; //CAMBIO DE JUGADOR//
				}
			}
			
			else if(matriz[x][y]!=0){
				
				x = revisarespacio(matriz, y);
	
				if(jugador==1){
					matriz[x][y]=1;
					jugadas++;
					ganador=revision(matriz, jugador);
					jugador++;
				}
				else if(jugador==2){
					matriz[x][y]=2;
					jugadas++;
					ganador=revision(matriz, jugador);
					jugador--;
				}
			}	
		system("clear");
		
		x = revisarfilalibre(matriz, y);
			
			if(ganador==2){
				printf("GANADOR ROBOT!!\n");
				printf("GANADOR ROBOT!!\n");
				pintartablero(matriz, largo);
				jugadas=65;
			}
		
			else if(ganador==1){
				printf("GANADOR JUGADOR 1\n");
				printf("GANADOR JUGADOR 1\n");
				pintartablero(matriz, largo);
				jugadas=65;
			}
			
			if (jugadas==64){
			printf("El tablero esta lleno!!!\n");
			printf("ha ocurrido UN EMPATE!!!\n");
			pintartablero(matriz, largo);
			break;					
		}
	}
}
	
void generadordetablero(){
	
	int matriz[8][8];
	int x=0, y=0, jugador;
	int mod;
	
	for(x=0; x<8; x++){
		for(y = 0 ; y<8; y++){
			matriz[x][y]=0;
		}
	}
	
	mod=mododejuego();
	jugador=dados();
			
	if(mod==1){
		juego1vsbot(matriz, jugador);
	}
	else if(mod==2){
	juego1vs1(matriz, jugador);
	}

}

int main(){
	generadordetablero();
	return 0;
}

