#!/bin/bash
DIA=`date +%d`
MES=`date +%m`
ANO=`date +%Y`
if [[ $2 ]]; then
  echo "Error, no se puede ingresar más de un parametro"
  exit 1
fi

if [[ $1 == "-s" || $1 == "--short" ]]; then
  echo "$DIA/$MES/$ANO"
  exit 1
elif [[ $1 == "-l" || $1 == "--long" ]]; then
  echo "El dia es $DIA del mes $MES del año $ANO"
  exit 1
elif [[ $# == 0 ]]; then
  cal
  exit 1

elif [[ $1 -ne "-s" || $1 -ne "--short" || $1 -ne "-l" || $1 -ne "--long" ]]; then
  echo "Paramatro totalmente incorrecto"
fi
