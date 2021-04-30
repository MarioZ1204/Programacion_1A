Algoritmo ServicioMilitar
	Definir nom_ape, gen, enf, resp Como Caracter
	Definir  año_nac, año_actual, Edad Como Entero
	
	año_actual<-2021
	resp<-"y"
	Mientras  resp = "y" Hacer
		Borrar Pantalla
		
		Escribir "Digitar Nombres y Apellidos "
		Leer nom_ape 
		Escribir "Digitar Año de Nacimiento" 
		Leer año_nac
		Edad<-año_actual-año_nac
		Escribir " Su edad es " Edad " años "
		Si ( Edad >= 18 ) Entonces
			Escribir "Mayor de Edad" 
		SiNo
			Escribir "Menor de Edad" 
		FinSi
		Escribir "Digitar Genero (m/f) " 
		Leer gen 
		Escribir "Enfermedad Cronica (y/n)" 
		Leer enf
		
		Si ( año_nac<= 2003 ) y ( gen = "m" ) y ( enf = "n" ) o (año_nac <= 2003) y ( gen = "f") y ( enf = "n") Entonces
			Escribir "DEBE PRESTAR SERVICIO MILITAR" 
		SiNo
			Escribir "No cumple las condiciones" 
			Si ( año_nac<= 2003 ) y ( gen = "m" ) y ( enf = "y" ) Entonces 
				Escribir "DEBE PRESTAR SERVICIO SOCIAL" 
			SiNo
				Escribir "No cumple las codiciones" 
				Si ( año_nac<= 2003) y ( gen = "f" ) y ( enf = "y" ) Entonces 
					Escribir "NO DEBE PRESTAR SERVICIOS"
				SiNo 
					Escribir "No cumple las condiciones"
					Si ( año_nac>= 2002) y ( gen = "f" ) y ( enf = "n" ) Entonces
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
