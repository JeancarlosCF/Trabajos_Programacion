while (true){
    var nota =prompt("Ingrese la calificación o salir para terminar ");
    if(nota = 0 && nota<3){
        console.log("Muy insuficiente")
    }
    else if(nota = 3 && nota<5){
        console.log( "es insuficiente")
    }
    else if(nota = 5 && nota<6){
        console.log( "Suficiente")
    }
    else if(nota = 6 && nota<7){
        console.log("bien")
    }
    else if(nota = 7 && nota<9){
        console.log("Notable")
    }
    else if(nota = 9 && nota<10){
        console.log("Sobresaliente ")
    }
    else if(nota ==="salir"){
        break;
    }
    else{
        console.log("La nota ingresada no es valida :D")
    }
}
