Algoritmo ServicioMilitar
	Definir nom_ape, gen, enf, resp Como Caracter
	Definir  a�o_nac, a�o_actual, Edad Como Entero
	
	a�o_actual<-2021
	resp<-"y"
	Mientras  resp = "y" Hacer
		Borrar Pantalla
		
		Escribir "Digitar Nombres y Apellidos "
		Leer nom_ape 
		Escribir "Digitar A�o de Nacimiento" 
		Leer a�o_nac
		Edad<-a�o_actual-a�o_nac
		Escribir " Su edad es " Edad " a�os "
		Si ( Edad >= 18 ) Entonces
			Escribir "Mayor de Edad" 
		SiNo
			Escribir "Menor de Edad" 
		FinSi
		Escribir "Digitar Genero (m/f) " 
		Leer gen 
		Escribir "Enfermedad Cronica (y/n)" 
		Leer enf
		
		Si ( a�o_nac<= 2003 ) y ( gen = "m" ) y ( enf = "n" ) o (a�o_nac <= 2003) y ( gen = "f") y ( enf = "n") Entonces
			Escribir "DEBE PRESTAR SERVICIO MILITAR" 
		SiNo
			Escribir "No cumple las condiciones" 
			Si ( a�o_nac<= 2003 ) y ( gen = "m" ) y ( enf = "y" ) Entonces 
				Escribir "DEBE PRESTAR SERVICIO SOCIAL" 
			SiNo
				Escribir "No cumple las codiciones" 
				Si ( a�o_nac<= 2003) y ( gen = "f" ) y ( enf = "y" ) Entonces 
					Escribir "NO DEBE PRESTAR SERVICIOS"
				SiNo 
					Escribir "No cumple las condiciones"
					Si ( a�o_nac>= 2002) y ( gen = "f" ) y ( enf = "n" ) Entonces
						Escribir "DEBE PRESTAR SERVICIO SOCIAL"
					SiNo 
						Escribir "No cumple las codiciones"
					FinSi
				FinSi
			FinSi
		FinSi
	
		Escribir "Desea ingresar otro habitante? y/n "
		Leer resp
	FinMientras
	
	
FinAlgoritmo
