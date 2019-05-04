
{
    LIGANDO[NR] = $1
    CADENA[NR] = $2
    RES[NR] = $3
    X[NR] = $4
    Y[NR] = $5
    Z[NR] = $6
    
}


END {
    
    for(i = 1; i <= NR; i++){
        printf "%s " "%s " "%s " "%s " "%s " "%s \n",LIGANDO[i],CADENA[i],RES[i],X[i],Y[i],Z[i] >> ID"LIG"LIGANDO[i]CADENA[i]RES[i]
    }

}
