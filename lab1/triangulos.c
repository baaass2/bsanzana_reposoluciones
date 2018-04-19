

#include <stdio.h>

int main()
{
	int l1,l2,l3;
	
	printf("ingresar l1: ");
	scanf("%d",&l1);
	printf("ingresar l2: ");
	scanf("%d",&l2);
	printf("ingresar l3: ");
	scanf("%d",&l3);
	
	if (l1==l2 && l2==l3){
		printf("equilatero");
	}
	else if ((l1==l2 && l2!=l3) || (l2==l3 && l3!=l1) || (l3==l1 && l1!=l2)){
		printf("isoceles");
	}
	else if(l1!=l2 && l2!=l3 && l3!=l1){
		printf("escaleno");
	}
	return 0;
}

