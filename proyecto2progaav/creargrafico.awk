BEGIN {
  FORMA1 = "node [shape=box]"
  FORMA2 = "node [shape=circle]"
  FLECHA = "%s%s%s%s%s"" -> ""%s%s%s"
  UNIONLIG = "%s%s%s"" -> ""LIGANDO"
  LIGLABEL = "%s [ label = \"" "%s" "\" ]"   
  LABEL = "%s%s%s%s%s[ label = \"" "%s" "\" ]"
  AALABEL = "%s%s%s [ label = \"" "%s" "\" ]"
  LCADENA = "%s%s%s -> %s%s%s [ label = \"" "Cadena %s" "\" ];"
  printf "digraph G {\n"
  printf "rankdir=LR;\n"
  DIS = 0 + DIS
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
    for(i = 1; i <= NR; i++){
        RESULTADO = ( (X[i]-Xcg)^2 + (Y[i]-Ycg)^2 + (Z[i]-Zcg)^2 )^(0.5) 
        if(RESULTADO <= DIS){
            #SI ENCUENTRA UN ATOMO QUE TENGA UNA DISTANCIA IGUAL O MENOR, SE NECESITA QUE SE GRAFIQUE TODOS EL AA, Y QUE
            #YA NO CONSIRERE ESE AMINOACIDO, SI NO, QUE SIGA CON EL AA SIGUENTE SI TIENE UN ATOMO DENTRO DE LA DISTANCIA DETERMINADA.
            for(k = i; k <= NR; k++){  
                if(AA[k] != AA[k+1] && RES[k] != RES[k+1]){
                    # imatch GUARDA EL INDICE CON DEL ATOMO QUE SE TIENE QUE GRAFICAR, MÀS SU NODOS HACIA EL AA.
                    imatch = i
                    # ESTA IGUALDAD SIRVE PARA QUE PASE A BUSCAR OTRO ATOMO DE OTRO AA, Y NO SIGA MANDANDO EXITO DE RESULTADO CON ATOMOS DE UN AA QUE YA PASO.
                    i = k    
                    break
                }
            }

            printf ""AALABEL"\n",AA[imatch],CADENA[imatch],RES[imatch],AA[imatch]
            printf "%s\n",FORMA1
            printf ""UNIONLIG"\n",AA[imatch],CADENA[imatch],RES[imatch]
            printf "%s\n",FORMA2
            for(j = 0; j <= NR; j++){
                #GRAFICA TODOS LOS ATOMOS DEL AA QUE ESTA DENTRO DE LA DISTANCIA.
                if(AA[imatch] == AA[j] && RES[imatch] == RES[j] && CADENA[imatch] == CADENA[j]){
                    printf ""LABEL"\n",ATOMO[j],AA[j],CADENA[j],RES[j],LINEA[j],ATOMO[j]
                    printf ""FLECHA"\n",ATOMO[j],AA[j],CADENA[j],RES[j],LINEA[j],AA[j],CADENA[j],RES[j]    
                }

            }

        }

    }

  print "}"
}
