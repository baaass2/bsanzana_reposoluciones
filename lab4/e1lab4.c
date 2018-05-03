/*INICIO
 * 
 * Pedir numero para invertir!
 * Crear funcion en la cual hay un ciclo con la condicional que se ejecute siempre cuando sea diferente a cero.
 * En el ciclo usar el mod %10 al numero ingresado de esta manera obtengo el resto y lo imprimo!
 * En el mismo ciclo el numero lo divido por 10 para seguir obteniendo un numero que al sacarle el resto va siendo el numero ingresado invertidamente!
 * FIN!
*
 */


#include <stdio.h>
#include <stdlib.h>

int ciclo_numeroainvertir (int numero){
	
	int resto;
	
	while (numero!=0){
	resto= numero%10;
	numero = numero/10;
	printf("%d", resto);
	
	}
	return resto;
	
}

int main()
{
	
	int numero;
	
	printf("Ingrese número: ");
	scanf("%d", &numero);
	
	ciclo_numeroainvertir(numero);
	
	
	
	
	return 0;
}

