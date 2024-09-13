# conversion de cadena a enteros
cadena_a_entero = int("12345")
print(cadena_a_entero)

# Conversión de cadena a flotante
cadena_a_flotante = float("7.22")
print(cadena_a_flotante)

# Conversión de número a cadena
numero_a_cadena = str(6789)
print(numero_a_cadena)

# Multilineas de cadena
texto_multilinea = """Este es un ejemplo de 
 multilineas de cadenas
 en Python."""
print(texto_multilinea)

# Funcion len()
cadena = "Hola Mundo"
longitud = len(cadena)
print(longitud)

# Subcadenas
cadena = "Hola Mundo"
primeros_n = cadena[:2]
print(primeros_n)

cadena = "Hola Mundo"
caracteres_medio = cadena[5:7]
print(caracteres_medio)

cadena = "Hola Mundo"
ultimos_n = cadena[-4:]
print(ultimos_n)

# funcion upper()
cadena = "Hola Mundo"
mayusculas = cadena.upper()
print(mayusculas)

# Funcion lower()
minusculas = cadena.lower()
print(minusculas)

# Multilineas de cadena de caracteres
multilinea = """Esta es un
ejemplo de 
multilineas de 
cadena de
caracteres."""
print(multilinea)

# Funcion strip()
cadena = "    Hernan Cortes    "
sin_espacios = cadena.strip()
print(sin_espacios)

# Funcion replace()
cadena = "Hernan Cortes"
cadena_reemplazada = cadena.replace("Cortes", "Ingeniero")
print(cadena_reemplazada)

# Funcion split
cadena = "Hernan Dario Cortes"
funcion = cadena.split()
print(funcion)

# Formato f-string
nombre = "Hernan Cortes"
edad = 31
mensaje = f"Mi nombre es {nombre} y tengo {edad} años."
print(mensaje)



