/*
* INICIO
* En la funcion calculo_mes
* Imprimir el valor de la primera cuota, que es 10.000.
* Crear un ciclo con un maximo de 20.
* Hacer calculo que multiplique por 2 el valor de las cuotas, y se guarden en la misma variable.
* Imprimir las cuotas sucecivas con el correspondiente valor.
* FIN
*/

#include <stdio.h>
#include <stdlib.h>


int calculo_mes(){
	
	int i=2,valor_cuotas_sucecivas=10;
	
	int pri_cuota=10;
	printf(" Mes numero 1 debe pagar:  %d ", pri_cuota);
	
	for (i=2; i<=20; i++){
		valor_cuotas_sucecivas=(valor_cuotas_sucecivas*2);
		printf("\n Mes numero %.d debe pagar: %d ",i ,valor_cuotas_sucecivas);
	}
	return valor_cuotas_sucecivas;
}



int main(){
	
	calculo_mes();




return 0;
}
