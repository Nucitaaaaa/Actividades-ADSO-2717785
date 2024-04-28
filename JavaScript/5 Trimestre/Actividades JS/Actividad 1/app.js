
//*Ejercicio 1  
function pi() {
    let divPi = document.getElementById("roundedPi");
    let buttonPi = document.getElementById("roundButton");
    let PI = Math.PI;
    let roundedPi = PI.toFixed(2);

    divPi.innerText = `${roundedPi}`;  
} 


//*Ejercicio 2 
function calculateIva() {
    let divTotal = document.getElementById("totalWithIva");
    let price = parseInt(document.getElementById("productPrice").value);
    let iva = parseInt(document.getElementById("vat").value);
    let defaultIva = 0.19;

    if (!price) {
        divTotal.innerText = `El campo "precio" no puede estar vacío`;
    } 
    
    else {
        let valIva = iva / 100;
        let priceIva = price * valIva;
        let total = price + priceIva;

        if (!iva) {
            total = price + (price * defaultIva);
        }

        divTotal.innerText = `El precio total es de $${total}`;
    }
}


//*Ejercicio 3
function reverseWord() {
    let divWord = document.getElementById("reversedWord");
    let word = document.getElementById("inputWord").value;
    
    if (!word) {
        divWord.innerText = `El campo "palabra" no puede estar vacío`;
    } else {
        let reversedWord = word.split("").reverse().join("");
        divWord.innerText = `${reversedWord}`;
    }
}


//*Ejercicio 4
function randomNum1() {
    let divNum1 = document.getElementById("randomNumResult");
    let min = parseInt(document.getElementById("minNum").value);
    let max = parseInt(document.getElementById("maxNum").value);

    if (min < max) {
        let randomNumber = Math.floor(Math.random() * (max - min) + min);
        divNum1.innerText = `${randomNumber}`;
    } else {
        divNum1.innerText = `El número menor debe ser menor que el número mayor`;
    }
}


//*Ejercicio 5
function randomNum2() {
    let randomNum2Val = document.getElementById("randomNums");
    let min = 1;
    let max = 1000;
    let randomNums = [];

    while (randomNums.length < 100) {
        let randomNumber = Math.floor(Math.random() * (max - min) + min);
        if (!randomNums.includes(randomNumber)) {
            randomNums.push(randomNumber);
        }
    }

    randomNum2Val.innerText = randomNums.join(", ");
}
