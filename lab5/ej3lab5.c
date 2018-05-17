/*  INICIO
	PEDIR NUMERO Y GUARDARLO
 * 	CON 4 CICLOS SACAR LOS RESTOS QUE SERIAN LAS DESCOMPOSICION DEL NUMERO
 * LUEGO CON 24 CONDICIONALES VER CUAL ES EL NUMERO MAYOR Y NUMERO MENOR
 * (no se termino por falta de tiempo :,( 
 */


#include <stdio.h>
#include <stdlib.h>
int numeromayor(int numero){
	
	int resto, a=0, b=0, c=0, d=0;
	int i=0, x=0, t=0, p=0;
	
	while (i<=1){
	resto = numero%10;
	numero = numero-resto;
	numero = numero/10;
	a= resto;
	i++;
	printf("%d", a);
	}
	while (x<=1){
	resto = numero%10;
	numero = numero-resto;
	numero = numero/10;
	b= resto;
	x++;
	printf("%d", b);
	}
	while (t<=1){
	resto = numero%10;
	numero = numero-resto;
	numero = numero/10;
	c=resto;
	t++;
	printf("%d", c);
	}
	while (p<=1){
	resto = numero%10;
	numero = numero-resto;
	numero = numero/10;
	d= resto;
	p++;
	printf("%d", d);
	}

	
	
	if (a>b && a>c && a>d){
		printf("numero mayor: %d %d %d %d",a,b,c,d);
	}
	else if (a>b && a>c && a>d){
		printf("%d %d %d %d",a,b,c,d);
	}
	
	return p;
}
	





int ingresenumero(){
	int numero;
	printf("INGRESE NUMERO: ");
	scanf("%d", &numero);
	
	numeromayor(numero);
	
	
	return numero;
}

int main()
{
	ingresenumero();
	return 0;
}

