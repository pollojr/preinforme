nota1=float(input("digite la primera nota"))
n1=(nota1*0.10)
nota2=float(input("digite la segunda nota"))
n2=(nota2*0.15)
nota3=float(input("digite la tercera nota"))
n3=(nota3*0.25)
nota4=float(input("digite la cuarta nota"))
n4=(nota4*0.15)
nota5=float(input("digite la quinta nota"))
n5=(nota5*0.35)

resultado=(n1+n2+n3+n4+n5)

if resultado >=3.0:
	if resultado>4.5:
		print("felicidades su nota es superior y es:  " , resultado)
	else: 
		print("aprobo mi materia pero puede mejorar y su nota es:  " , resultado)

else:
	if resultado <2.0:
		print("no puede habilitat mi materia y su nota es: ", resultado)
	else:
			print("no aprobo y debe habilitar esta materia y su nota es: " , resultado)
