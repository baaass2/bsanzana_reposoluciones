{
    X[NR] = $4
    Y[NR] = $5
    Z[NR] = $6
}

END {
    aux = 0
    for(i = 1; i <= NR; i++){
        aux = X[i] + aux    
    }
    print (aux/NR)
    aux = 0

    for(i = 1; i <= NR; i++){
        aux = Y[i] + aux    
    }
    print (aux/NR)
    aux = 0

    for(i = 1; i <= NR; i++){
        aux = Z[i] + aux    
    }
    print (aux/NR)


}
