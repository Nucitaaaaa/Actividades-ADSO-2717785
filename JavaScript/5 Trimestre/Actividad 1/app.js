
//*Ejercicio 1  
//!falta
function pi() {
    let PI = Math.PI;


} 


//*Ejercicio 2 
function calculateIva(price, iva){
    let divTotal = document.getElementById("totalIva");
    
    price = parseInt(document.getElementById("price").value);
    iva = parseInt(document.getElementById("iva").value);

    let defIva = 0.19;
    let valIva = iva / 100;
    let priceIva = price * valIva;

    let total = price + priceIva;

    if(!iva){
        total = price + (price * defIva);
    }

    divTotal.innerText = `${total}`;
}


//*Ejercicio 3
function reverseWord(word) {
    let divWord = document.getElementById("reversedWord");

    word =  document.getElementById("word").value;
    
    let wordLetters = word.split("");
    let reversedWord = wordLetters.reverse();

    let newWord = "";

    for (let letter of reversedWord) {
        newWord += letter;
    }
    
    divWord.innerText = `${newWord}`;

}


//*Ejercicio 4
