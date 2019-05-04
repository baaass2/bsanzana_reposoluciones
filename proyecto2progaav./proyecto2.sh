#!/bin/bash

function DescargarBD {
    if [[ -f "bd-pdb.txt" ]]; then
        echo "Base de datos actualmente descargada."
    else
        echo "Se descargara la base de datos."
    wget https://icb.utalca.cl/~fduran/bd-pdb.txt   
    
    fi
}

function DescargarPBD {
    if [[ -f "$1.pdb" ]]; then
        echo "PDB ya descargado."
    else
        echo "Se descargara PDB solicitado con la ID $1."
        wget https://files.rcsb.org/download/$1.pdb
    fi
}

function FiltrarPDB {
    echo "Comenzara la filtracion de archivo PDB."
    awk '$1 == "HETATM" && $4 != "HOH" { print $4" "$5" "$6" "$7" "$8" "$9 }' $1.pdb >> hetatm_$1.txt
    awk '$1 == "ATOM" { print $2" "$3" "$4" "$5" "$6" "$7" "$8" "$9 }' $1.pdb | \
    awk 'length($2) >= 4 {$2 = substr($2,1,3)" "substr($2,5,7)} { print $0 }' | \
    awk 'length($3) > 3 { $3 = substr($3,2,4)} { print $0 }' >> atom_$1.txt
}

function LigandoPDB {
    echo "Comenzara la busqueda de ligandos."
    awk -v ID="$1" -v CONVFMT='%.0f ' -f encontrarligando.awk hetatm_$1.txt
    echo "Se encontraran el centro geometrico de los ligandos"
    totalligandos=`ls | grep -ic "$1lig"`
    for (( i=1; i <= totalligandos; i++ )); do
        ligando=`ls | grep -i "$1lig" | sed -n "$i p"`
        echo $ligando
        LIGA=${ligando:7}
        awk -v CONVFMT='%.0f ' -f centrogeometrico.awk $ligando >> vector$ligando.txt
        X=`sed -n '1 p' vector$ligando.txt`
        Y=`sed -n '2 p' vector$ligando.txt`
        Z=`sed -n '3 p' vector$ligando.txt`
        awk -v Xcg=$X -v Ycg=$Y -v Zcg=$Z -v DIS=$2 -v CONVFMT='%.0f ' -f creargrafico.awk atom_$1.txt >> final$ligando.dot
        dot -Tpng -o SVG$LIGA.png final$ligando.dot

    done

}

DescargarBD
OPC="Y"
while [[ "$OPC" != "N"   ]]; do
    echo "Ingrese ID de Proteina: "
    read ID
    ID=${ID^^}
    echo "Ingrese distancia: "
    read DIS

    SALIR="0"
    while [[ $SALIR != "1" ]]; do
        if [[ -f "$ID.dot" ]]; then
            echo "La proteina seleccionada ya tiene construido su grafico."
            echo "Ingrese otra ID de proteina: "
            read ID
            ID=${ID^^}
        else
            SALIR="1"
        fi

    done

    PROTEINA=`grep -w "$ID" bd-pdb.txt | rev | awk -F, '{ print $1 }' | rev`

    SALIR="0"
    while [[ $SALIR != "1" ]]; do
        if [[ $PROTEINA == '"Protein"' ]]; then
            echo "Existe proteina en la BD."
            DescargarPBD $ID
            FiltrarPDB $ID
            LigandoPDB $ID $DIS
            SALIR="1"
        else
            echo "ID no es una proteina."
            echo "Ingrese otra ID de proteina: "
            read ID
            ID=${ID^^}
            PROTEINA=`grep -w "$ID" bd-pdb.txt | rev | awk -F, '{ print $1 }' | rev`
        fi
    done

    echo "Se ha finalizado la filtracion y construccion del grafico."
    echo "¿Quiere graficar otra proteina (Y/N)"
    read OPC
    OPC=${OPC^^}
done

echo "Hasta luego!"
