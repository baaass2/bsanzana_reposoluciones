BEGIN {
  FORMA1 = "node [shape=box]"
  FORMA2 = "node [shape=circle]"
  FLECHA = "%s%s%s%s"" -> ""%s%s%s"
  LABEL = "%s%s%s%s[ label = \"" "%s" "\" ]"
  AALABEL = "%s%s%s [ label = \"" "%s" "\" ]"
  LCADENA = "%s%s%s -> %s%s%s [ label = \"" "Cadena %s" "\" ];"
  printf "digraph G {\n"
  printf "rankdir=LR;\n"
  #printf "size=\"""60""\" \n"
  printf "%s\n",FORMA1
}

{

  for(i = 1; i <= NR; i++){
    ATOMO[NR] = $1
    AA[NR] = $2
    CADENA[NR] = $3
    RES[NR] = $4
  }

  #printf $1_$2_$3_$4" "LABEL"\n",$1
  #printf $1_$2_$3_$4 FLECHA $2_$3_$4"\n"

}

END {

  for(i = 1; i <= NR; i++){
    printf ""LABEL"\n",ATOMO[i],AA[i],CADENA[i],RES[i],ATOMO[i]
    printf ""FLECHA"\n",ATOMO[i],AA[i],CADENA[i],RES[i],AA[i],CADENA[i],RES[i]
  }

  for(i = 1; i <= NR; i++){
    printf ""AALABEL"\n",AA[i],CADENA[i],RES[i],AA[i]
  }
  printf "%s\n",FORMA2
  for(i = 1; i <= NR; i++){
    if(AA[i] != AA[i+1] || RES[i] != RES[i+1]){
      if(CADENA[i] == CADENA[i+1]){
        printf ""LCADENA"\n",AA[i],CADENA[i],RES[i],AA[i+1],CADENA[i+1],RES[i+1],CADENA[i]
      }
    }
  }
  print "}"
}
