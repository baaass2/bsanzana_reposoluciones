function DescargarBD {
  if [[ -f "bd-pdb.txt" ]]; then
      echo "Base de datos actualmente descargada."
  else
    echo "Se descargara la base de datos."
    wget https://icb.utalca.cl/~fduran/bd-pdb.txt
  fi
}

function DescargarPBD {
  if [[ -f "$1.txt" ]]; then
    echo "PDB ya descargado."

  else
    echo "Se descargara PDB solicitado con la ID $1."
    wget https://files.rcsb.org/download/$1.pdb
    mv $1.pdb $1.txt
    FiltrarPDB $1
  fi
}

function FiltrarPDB {
  echo "Comenzara la filtracion de archivo PDB."
  awk '$1 == "ATOM" { print $3" "$4" "$5" "$6 }' $1.txt >> $11.txt
  awk 'length($1) >= 4 {$1 = substr($1,1,3)" "substr($1,5,6)} { print $0 }' $11.txt >> ATOM$111.txt
  awk 'length($2) > 3 { $2 = substr($2,2,3)} { print $0 }' ATOM$111.txt >> $1final.txt
}

DescargarBD

echo "Ingrese ID de Proteina: "
read ID
ID=${ID^^}

SALIR="0"
while [[ $SALIR != "1" ]]; do
  if [[ -f "$ID.dot" ]]; then
    echo "La proteina seleccionada ya tiene construido su grafico."
    echo "Ingrese nuevamente proteina: "
    read ID
    ID=${ID^^}
  else
    SALIR="1"
  fi

done

PROTEINA=`grep -i "$ID" bd-pdb.txt | rev | awk -F, '{ print $1 }' | rev`

SALIR="0"
while [[ $SALIR != "1" ]]; do
  if [[ $PROTEINA == '"Protein"' ]]; then
    echo "Existe proteina en la BD."
    DescargarPBD $ID
    SALIR="1"
  elif [[ $PROTEINA != '"Protein"' ]]; then
    echo "ID Incorrecto."
    echo "Ingrese nuevamente proteina: "
    read ID
    ID=${ID^^}
    PROTEINA=`grep -i "$ID" bd-pdb.txt | rev | awk -F, '{ print $1 }' | rev`
  fi
done

awk -v CONVFMT='%.0f ' -f creargrafico.awk "$ID"final.txt >> "$ID"final.dot
uniq "$ID"final.dot >> "$ID".dot
dot -Tsvg -o "$ID".svg "$ID".dot
