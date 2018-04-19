
/*  Inicio
 * Pedir votos
 * Guardar votos en variable "X"
 * Dependiendo del valor de "X", sumar voto a candidato correspondiente
 * Imprimir texto que pedi la letra "F" para no seguir
 * Guardar letra en variable "tecla"
 * Si la tecla es diferente a F seguir pidiendo votos
 * Imprimir los votos con los candidatos correspondientes
 * Realizar operacion para sacar el porcentaje
 * Imprimir oorcentaje de los candidatos
 * Imprimir Ganador
 * 
 * 
 * 
 */

#include <stdio.h>

int main()
{
	int candidato1=0, candidato2=0, candidato3=0, nulo=0, x, i=0;
	char tecla;
	float porcentaje,porcentaje2,porcentaje3;
	
	
	while(tecla!='f'){
		
		printf("ingrese voto: ");
		scanf ("%d", &x);
		
		if (x==1){
			candidato1++;
		}
		else if (x==2){
			candidato2++;
		}
		else if (x==3){
			candidato3++;
		} 
		else {
			nulo++;
		}
	
		while (getchar()!='\n');
	    printf("otro voto? apreta f para terminar y otro letra cualquiera sigue: \n ");   
		scanf("%c", &tecla);
		
		i++;
		
	}
		
	printf("candidato 1: %d \n",candidato1);
	printf("candidato 2: %d \n",candidato2);
	printf("candidato 3: %d \n",candidato3);
	printf("votos nulos: %d \n",nulo);
	
	porcentaje=(100*candidato1)/i;
	porcentaje2=(100*candidato2)/i;
	porcentaje3=(100*candidato3)/i;
	printf("porcentaje del candidato1 %f \n",porcentaje);
	printf("porcentaje del candidato2 %f \n",porcentaje2);
	printf("porcentaje del candidato2 %f \n",porcentaje3);
	
	if (candidato1>candidato2 && candidato1>candidato3){
		printf("GANADOR CANDIDATO 1 \n");
	}
	else if (candidato2>candidato1 && candidato2>candidato3){
		printf("GANADOR CANDIDATO 2 \n");
	}
	else if (candidato3>candidato1 && candidato3>candidato2){
		printf("GANADOR CANDIDATO 3\n");
	}
	else if (candidato1==candidato2 || candidato1==candidato3 || candidato3==candidato2){
		printf("EMPATE\n");
	}
	
	
	
	
}
	
		
	
	
	
	


