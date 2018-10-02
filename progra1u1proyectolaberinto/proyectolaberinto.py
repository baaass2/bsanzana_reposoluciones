from time import sleep
import random
import copy
import os


def laberinto(matriz,x,y):
	a = 1
	b = 1
	c = int (x / 2 )
	d = y-6
	matriz[a][b] = ' '
	while matriz[c][d] == '█':
		movimiento=random.randint(1,4)
		#Right
		if b == d:
		    for i in range(1,x-1):
		        matriz[i][d] = ' '
		else:
		    if movimiento == 1:
		        b = b+1
		        if b != y-2:
		            matriz[a][b] = ' '
		        else:
		            b = b-1
		#Up
		    elif movimiento == 2:
		        a = a-1
		        if a != 0:
		            matriz[a][b] = ' '
		        else:
		            a = a+1
		#Down
		    elif movimiento == 3:
		        a = a+1
		        if a != x-1:
		           matriz[a][b] = ' '
		        else:
		            a = a-1
	rellenar(matriz,x,y)


def rellenar(matriz,x,y):
	a = x-2
	b = 1
	c = int(x/2)
	matriz[a][b] = ' '
	matriz[c][y-6] = '█'
	while matriz[c][y-6] == '█':
		movimiento = random.randint(1,4)
		#Right
		if b == y-3:
		    for i in range(1,x-1):
		        matriz[i][y-6] = ' '
		else:
		    if movimiento == 1:
		        b = b+1
		        if b != y-2:
		            matriz[a][b] = ' '
		        else:
		            b = b-1
		#Up
		    elif movimiento == 2:
		        a = a-1
		        if a != 0:
		            matriz[a][b] = ' '
		        else:
		            a = a+1
		#Down
		    elif movimiento == 3:
		        a = a+1
		        if a != x-1:
		           matriz[a][b] = ' '
		        else:
		            a = a-1
	rellenar_2(matriz,x,y)


def rellenar_2(matriz,x,y):
	a = int(x/2)
	b = random.randint(y-6,y-3)
	matriz[a][b] = ' '
	c = int(x/2)
	d = 1
	matriz[c][d] = '█'

	while matriz[c][d] == '█':
		movimiento=random.randint(1,4)
	#Left
		if b == 1:
		    for i in range(1,x-1):
		        matriz[i][1] = ' '

		else:
		    if movimiento == 1:
		        b = b-1
		        if b != 0:
		            matriz[a][b] = ' '
		        else:
		            b = b+1
	#Up
		    elif movimiento == 2:
		        a = a-1
		        if a != 0:
		            matriz[a][b] = ' '
		        else:
		            a = a+1
	#Down
		    elif movimiento == 3:
		        a = a+1
		        if a != x-1:
		           matriz[a][b] = ' '
		        else:
		            a = a-1
	despejar_caminos(matriz,x,y)


def despejar_caminos(matriz,x,y):
	randoms = 0
	while randoms != 50:
		a = random.randint(1,18)
		b = random.randint(1,96)
		if matriz[a][b+1] == ' ' or matriz[a+1][b] == ' ' or matriz[a-1][b] == ' ' or matriz[a][b-1] == ' ':
		    matriz[a][b] = ' '
		    randoms = randoms+1
		else:
		    randoms = randoms

	randoms = 0
	while randoms != 50:
		a = random.randint(1,19)
		b = random.randint(1,97)
		matriz[a][b] = '█'
		randoms = randoms+1

	for i in range(1,x):
		matriz[i][y-10] = '█'

	for i in range(1,x):
		matriz[i][y-70] = '█'

	for i in range(1,x):
		matriz[i][y-50] = '█'

	for i in range(56,y-2):
		matriz[x-4][i] = '█'
	camino_victoria(matriz,x,y)


def camino_victoria(matriz,x,y):
	salir = 0
	while salir != 1:
		a = random.randint(1,12)
		b = random.randint(1,31)
		if matriz[a][b+1] == '█' and matriz[a+1][b] == '█' and matriz[a-1][b] == '█' and matriz[a][b-1] == '█':
		    matriz[a][b] == ' '
		    for i in range(1,b+1):
		        matriz[1][i] = ' '
		    for i in range(1,13):
		        matriz[i][b] = ' '
		    for i in range(b,67):
		        matriz[12][i] = ' '
		    for i in range(13,19):
		        matriz[i][66] = ' '
		    for i in range(66,98):
		        matriz[18][i] = ' '
		    salir = 1
		else:
		    salir = 0
	start(matriz,x,y)


def start(matriz,x,y):
	a = 1
	b = 0
	opc = 0
	salir = 0
	matriz[a][b] = 'X'
	matriz2 = copy.deepcopy(matriz)

	while(salir != 1):
		
		for i in range (0,x):
			for k in range(0,y):
				if(matriz[i][k]=='X'):
					print("\033[4;35;47m"+matriz[i][k],end = "" +"\033[0;m")
				elif(matriz[i][k]!='X'):	
					print(matriz[i][k],end = "")
			print()

		print("\033[4;35;47m"+"MOVIMIENTO: "+"\033[0;m")
		movi = input()

		if(movi == 'A'):
			if(matriz[1][0]=='X'):
				print("\033[4;35;47m"+"ERROR: MOVIMIENTO IMPOSIBLE"+"\033[0;m")
				sleep(1)
			elif(matriz[1][0]!='X'):	
				b = b-1
				if(matriz[a][b] == '█'):
					b = b+1
					print("\033[4;35;47m"+"ERROR: CHOCASTE CON MURALLA"+"\033[0;m")
					sleep(1)
				elif(matriz[a][b] == ' '):
					matriz[a][b+1] = ' '
					matriz[a][b] = 'X'
					matriz2[a][b] = 'X'

		elif(movi == 'S'):
			a = a+1
			if(matriz[a][b] == '█'):
				a = a-1
				print("\033[4;35;47m"+"ERROR: CHOCASTE CON MURALLA"+"\033[0;m")
				sleep(1)
			elif(matriz[a][b] == ' '):
				matriz[a-1][b] = ' '
				matriz[a][b] = 'X'
				matriz2[a][b] = 'X'

		elif(movi == 'D'):
			b = b+1
			if(matriz[a][b] == '█'):
				b=b-1
				print("\033[4;35;47m"+"ERROR: CHOCASTE CON MURALLA"+"\033[0;m")
				sleep(1)
			elif(matriz[a][b] == ' '):
				matriz[a][b-1] = ' '
				matriz[a][b] = 'X'
				matriz2[a][b] = 'X'
			if(matriz[18][99] == 'X'):
				salir = 1

		elif(movi == 'W'):
			a=a-1
			if(matriz[a][b] == '█'):
				a = a+1
				print("\033[4;35;47m"+"ERROR: CHOCASTE CON MURALLA"+"\033[0;m")
				sleep(1)
			elif(matriz[a][b] == ' '):
				matriz[a+1][b] = ' '
				matriz[a][b] = 'X'
				matriz2[a][b] = 'X'

		elif(movi != 'A' or movi != 'D' or movi != 'S' or movi != 'W'):
			print("\033[4;35;47m"+"ERROR: SOLO INGRESAR LETRA A,S,W,D EN MAYÚS "+"\033[0;m")
			sleep(1)
		os.system('clear')
	print("\033[4;35;47m"+"!!!! HAS LOGRADO ENCONTRAR LA SALIDA!!!!!! "+"\033[0;m")
	
	salir=0
	while(salir != 1):
		
		print("\033[4;35;47m"+"----------- MENÚ ----------- "+"\033[0;m")
		print("\033[4;35;47m"+"1.- REINICIAR JUEGO (NUEVO MAPA): "+"\033[0;m")
		print("\033[4;35;47m"+"2.- MOSTRAR MOVIMIENTOS: "+"\033[0;m")
		print("\033[4;35;47m"+"3.- SALIR: "+"\033[0;m")
		print("\033[4;35;47m"+"---------------------------- "+"\033[0;m")
		opc = input()
		
		if(opc == '1'):
			for i in range(x):
				for k in range(y):
					matriz[i][k]='█'
			armazon(matriz, x, y)
		elif(opc == '2'):
			for i in range (0,x):
				for k in range(0,y):
					if(matriz2[i][k] == 'X'):
						print("\033[4;35;47m"+matriz2[i][k],end = "" +"\033[0;m")
					elif(matriz2[i][k] != 'X'):	
						print(matriz2[i][k],end = "")
				print()
		elif(opc == '3'):
			salir = 1
		elif(opc != '1' or opc != '2' or opc != '3'):
			print("\033[4;35;47m"+"ERROR: NUMERO INCORRECTO"+"\033[0;m")
			sleep(1)


def armazon(matriz, x, y):
	#FUNCIÓN DE ELEMENTOS ESTATICOS
	
	#FIJAR LA ENTRADA Y LA SALIDA.
	matriz[1][0] = 'X'
	matriz[x-2][y-2] = ' '
	#COLUMNA INVISIBLE
	for i in range(0,x):
		matriz[i][y-1] = ' '	
	laberinto(matriz,x,y)


def creacionmatriz():
	x = 20
	y = 100
	
	matriz = [x] * x
	for i in range(x):
		matriz[i] = ['█'] * y
	
	print("\033[4;35;47m"+"------------------------------------------------------------- "+"\033[0;m")
	print("\033[4;35;47m"+"------------------------------------------------------------- "+"\033[0;m")
	print("\033[4;35;47m"+"--------------------[BIENVENIDO AL LABERINTO]---------------- "+"\033[0;m")
	print("\033[4;35;47m"+"------------------------------------------------------------- "+"\033[0;m")
	print("\033[4;35;47m"+"------------------------------------------------------------- "+"\033[0;m")
	sleep(3)
	os.system('clear')
	
	armazon(matriz, x, y)

creacionmatriz()
