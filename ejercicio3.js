/*Ejercicio 3
En el siguiente ejercicio vamos a practicar la concatenación de strings y el bucle do while

Realiza un script que pida cadenas de texto  hasta que se pulse “cancelar”. Al salir con “cancelar” deben mostrarse todas las cadenas concatenadas con un guión - */

let listaString = ""

while (true){
    let string = prompt("Digite algo o 'cancelar' para terminar")
    
    if (string == "cancelar"){
        break
    }
    listaString += string + " - "
}

console.log(listaString)
