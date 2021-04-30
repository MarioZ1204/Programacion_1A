Algoritmo GANADOR_PAR
	//Si el numero esta entre uno Y diez Y es impar, o esta entre 20 y 30 y es par 
	Definir num Como Entero
	Escribir "Ingresar número"
	Leer num
	Si (num >= 1) y (num <= 10) y (num mod <> 20) o (num >=20) y (num <= 30) y (num mod 2 = 0) Entonces 
		Escribir "Ganador"
	SiNo
		Escribir "Perdedor"
	Fin Si
FinAlgoritmo
