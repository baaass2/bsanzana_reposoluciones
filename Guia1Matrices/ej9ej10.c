#include <stdio.h>
#include <string.h>
void imprimir(char adn[], int contador){
	
	for(int i=0; i<976; i++){
		printf("%c", adn[i]);
	}
	printf("\nSE ENCONTRARON %d MATCH", contador);
	
}
void mayuscula(char adn[], int i, int largo){

	for(int j=0; j<largo; j++){
		
		if(adn[i]=='a'){
			adn[i]='A';
		}
		else if(adn[i]=='t'){
			adn[i]='T';
		}
		else if(adn[i]=='c'){
			adn[i]='C';
		}
		else if(adn[i]=='g'){
			adn[i]='G';
		}
		i--;
	}
}
void sequence(){

	
	char adn[976]="gtgggggggtttatgcctttagaacagcagactactgataactccaatcctgggttgaaaatgccaagggcgccagagagccaaacgatgagcgttggaccacaaacgataaaaactcactttctccgtggggtgaaagcgattctttctggcccgtatccgccagcacttaaagttgcattcggcgcggccctaccgctgctaattggggtaattgtcctaggattgtacgtaacgcttggcgggcacagccgcaagaaagcccacgcagccgcgatagatgctttggtcgagaagcacgaagcatgctacaaggtccaagcaaagattgcacacggcaggcttgccttacagtccgctgtggtgtctgttgcggatgccagcatgcaacaactccagttcgtgcagcaaggaattctcatgtgtgtcggagagctcgacgatatgcagaagttccggacccgactggataatgaaatcagtgccatcaaccagcgaattcccagcattgtcgaggaggtaagaaaacacaccgacgatgcgcttgagtggaatcttgctagaaccaagaacattttagagggcactgaagagcgcctgaaggatatgggcaatgagttggtgcgctacctagacgatgctcgcgccctcattgaaaatgcacgtatagctgcaggatcaatgcaacacctcgttggtgatgaggtgagaaagcagcttgctgaggttctagtaaaagttgcagaagtaagtaatggctttattgcgcttaagaagagtgtatctggctatttggaaaaaagcagtggacttgttgctagggaagttagggcaatcctggatgaccgcatgcgaagcctgcggaccatgtacaaaatgtgggatgcagaacaaaactccgtagtcagcgtgtgtaccacgctccaaaaggcaagcatggaggctgccgcggtagcaagt";

	int largo=0;
	
	printf("INGRESE LARGO DE SECUENCIA: ");
	scanf("%d", &largo);
	
	char adn2[largo];
	
	printf("INGRESE SECUENCIA A BUSCAR(letras minusculas): ");
	scanf(" %s", adn2);
	
		
	int i=0, k=0, contador=0;
	
	for(i=0; i<976; i++){
		if(adn[i]==adn2[k]){
			k++;
			
		}else{
			if(k>0){
				if(adn[i]==adn2[0]){
					k=1;
				}
				else{
					k=0;
				}
			}
		}
		if(k==largo){
			contador++;
			mayuscula(adn, i, largo);
			k=0;
			}
	}
	
	
	
		imprimir(adn, contador);
}
	











int main()
{
	sequence();
	return 0;
}

