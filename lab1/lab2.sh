#!/bin/bash
cd /$HOME
echo "Ingrese nombre de carpeta: "
read NOMBRE

if [[ -d $NOMBRE ]]; then
  echo "Esta carpeta ya existe"
  echo "Ingrese nombre a cambiar"
  read NOMBRE2
  mv $NOMBRE $NOMBRE2
  cd $NOMBRE2
else
  mkdir $NOMBRE
  cd $NOMBRE
fi

touch 1t4vdocking.mol2
touch 1t4vreferencia.mol2
touch 2r2mdocking.mol2
touch 2r2mreferencia.mol2
touch 3ldxdocking.mol2
touch 3ldxdockingnew.mol2
touch 3ldxreferencia.mol2
touch 3ldxreferencianew.mol2


for i in $( ls ) ; do
  x=`echo $i | cut -c 1`
done
for (( j = x; j>= 1 ; j-- )); do
  mkdir c$j
done

for i in $( ls ) ; do
  x=`echo $i | cut -c 1`
  if [[ $x == 1 ]]; then
    mv $i c1
  elif [[ $x == 2 ]]; then
    mv $i c2
  elif [[ $x == 3 ]]; then
    mv $i c3
  fi
done
