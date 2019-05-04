BEGIN {
  FORMA1 = "node [shape=box]"
  FORMA2 = "node [shape=circle]"
  FLECHA = "%s%s%s%s%s"" -> ""%s%s%s"
  UNIONLIG = "%s%s%s"" -> ""LIGANDO"
  LIGLABEL = "%s [ label = \"" "%s" "\" ]"   
  LABEL = "%s%s%s%s%s[ label = \"" "%s" "\" ]"
  AALABEL = "%s%s%s [ label = \"" "%s" "\" ]"
  LCADENA = "%s%s%s -> %s%s%s [ label = \"" "Cadena %s" "\" ];"
  #FORMULA = ((%f-Xcg)^2+(%f-Ycg)^2+(%f-Zcg)^2))^(0,5)
  printf "digraph G {\n"
  printf "rankdir=LR;\n"
}

{   
    LINEA[NR] = $1
    ATOMO[NR] = $2
    AA[NR] = $3
    CADENA[NR] = $4
    RES[NR] = $5
    X[NR] = $6
    Y[NR] = $7
    Z[NR] = $8
}
    
END {
    #printf ""LIGLABEL"\n",LIG,LIG
    for(i = 1; i <= NR; i++){
        RESULTADO = ( (X[i]-Xcg)^2 + (Y[i]-Ycg)^2 + (Z[i]-Zcg)^2 )^(0.5)
        for(k = i; k <= NR; k++){
            if(AA[k] != AA[k+1] && RES[k] != RES[k+1]){
                i = k+1
                break
            }
        }
        if(RESULTADO <= DIS){
            printf ""AALABEL"\n",AA[i],CADENA[i],RES[i],AA[i]
            printf "%s\n",FORMA1
            printf ""UNIONLIG"\n",AA[i],CADENA[i],RES[i]
            printf "%s\n",FORMA2
            for(j = 0; j <= NR; j++){
                if(AA[i] == AA[j] && RES[i] == RES[j] && CADENA[i] == CADENA[j]){
                    printf ""LABEL"\n",ATOMO[j],AA[j],CADENA[j],RES[j],LINEA[i],ATOMO[j]
                    printf ""FLECHA"\n",ATOMO[j],AA[j],CADENA[j],RES[j],LINEA[i],AA[j],CADENA[j],RES[j]    
                }

            }

        }

    }

  print "}"
}
