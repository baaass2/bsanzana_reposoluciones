def romano_a_arabigo(romano):
	num_array=[]


	for i in range(0,len(romano)):
		if(romano[i]=='M'):
			num_array.append (1000)
		elif(romano[i]=='D'):
			num_array.append (500)
		elif(romano[i]=='C'):
			num_array.append (100)
		elif(romano[i]=='L'):
			num_array.append (50)
		elif(romano[i]=='X'):
			num_array.append (10)
		elif(romano[i]=='V'):
			num_array.append (5)
		elif(romano[i]=='I'):
			num_array.append (1)	
			
	total=0
	for i in range(0, len(num_array)):
		if(num_array[i]>num_array[i+1]):
			total=num_array[i]+num_array[i+1]
		elif(num_array[i]<num_array[i+1]):
			total=num_array[i+1]-num_array[i]
		elif(num_array[len(num_array)]==num_array[len(num_array)]):
			total= total+num_array[len(num_array)]
		
	print("NUM ROMANO: ",total)
	
"""def arabigo_a_romano(arabigo):
	rom_array=[]
	mod=10**(len(arabigo)-1)
	arabigo2=int(arabigo)
	for i in range(0, len(arabigo)):
		arabigo2=arabigo2%mod
		if(arabigo2==1000):
			rom_array.append ('M')
		elif(romano[i]=='D'):
			rom_array.append (500)
		elif(romano[i]=='C'):
			rom_array.append (100)
		elif(romano[i]=='L'):
			rom_array.append (50)
		elif(romano[i]=='X'):
			rom_array.append (10)
		elif(romano[i]=='V'):
			rom_array.append (5)
		elif(romano[i]=='I'):
			rom_array.append (1)	"""
		
		
		

print("INTRODUZCA SU NUMERO ROMANO: ")
romano=input()
romano_a_arabigo(romano)
"""print("INTRODUZCA SU NUMERO ARABIGO: ")
arabigo=input()
arabigo_a_romano(arabigo)"""		

		

	
