
## 1. Letra de cada palabra en mayuscula
name = "leonardo pinto"
print(name.title())

## 2. Convertir a mayuscula
book = "cien años de soledad"
print(book.upper())

## 3. Crear un identificador
hi = "Hola Mundo Python"
print(hi.lower().replace(" ", "-"))

## 4. Elimina espacios
hi = "    Hola Mundo  "
print(hi.strip())

## 5. Extraer el dominio
email = "usuario@example.com"
print(email.split("@"))

## 6. Reemplazar puntos por espacios
replace = "Hola.Mundo"
print(replace.replace(".", " "))

## 7. Posicion de subcadena
substring = "Hola Python"
print(substring.find("Python"))

## 8. Verificar si la cadena es un numero
number = "1234"
print(number.isnumeric())

## 9. Capitaliza la primera letra de la frase
phrase = "hola mundo"
print(phrase.capitalize())

## 10. Convierte todo a minuscula
warning = "!NO PASE PELIGRO¡"
print(warning.lower())


## 11. Eliminar comillas
hi = '"hola mundo"' 
print(hi.replace('"', ""))

## 12. Dividir la plabras con espacios como separadores
hi = "Hola Mundo Python"
print(hi.split())

## 13. Cambiar espacios por guion bajo
hi = "Hola Mundo Python"
print(hi.replace(" ", "_"))

## 14. Posicion de la palabra clave
clue = "La palabra clave esta en la posicion"
print(clue.find("clave"))

## 15. Verificar si postal code es numerico
postalCode = "050001"
print(postalCode.isalnum())
