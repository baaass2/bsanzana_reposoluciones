/* INICIO
 * Pedir peso del niño
 * guardar variable
 * pedir edad en meses del niño 
 * guardar variable
 * si el niño tiene menor a 12 meses  multiplicar kilo por los miligramos
 * ya que el niño es menor a 12 meses hay que dividirlo en 3
 * y para transformarlo a gotas se multiplica por 25
 * 
 * en cambio si el niño tiene mayor a 12 meses multiplicar kilo por los miligramos
 * y luego transformalo a gotas, multiplicando por 25
 * 
 * imprimir dosis en gotas!
 * FIN
 * 
 * 
 * 
 * 

 */


#include <stdio.h>

int main()
{
	float kilo, dosis, gotas, edad;
	
	
	printf ("¿Cuanto pesa el niño?: ");
	scanf("%f", &kilo);
	printf ("¿Edad del niño en meses?: ");
	scanf("%f", &edad);
	
	if (edad<12){
	dosis= 0.2*kilo;
	dosis= dosis/3;
	gotas= dosis*25;
}
	else if (edad>=12){
		dosis= 0.2*kilo;
		gotas= dosis*25;
	}
	
	printf("Debe consumir %f: ", gotas);
	
	return 0;
}

