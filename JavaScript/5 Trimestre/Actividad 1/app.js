
//*Ejercicio 1  
function pi() {
    let divPi= document.getElementById("pi");
    let buttonPi= document.getElementById("buttonPi");
    let PI = Math.PI;
    let roundedPi = PI.toFixed(2)

    if(divPi.innerText == PI){
        divPi.innerText = `${roundedPi}`;
        buttonPi.innerText = `No Redondear`
    }
    else{
        divPi.innerText = `${PI}`;
        buttonPi.innerText = `Redondear`
    }
    
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
function randomNum1(min, max) {
    let divNum1 = document.getElementById("randomNum1");
    min =  parseInt(document.getElementById("min").value);
    max =  parseInt(document.getElementById("max").value);

    if(min < max){
        let randomNumber = Math.floor(Math.random() * (max  - min) + min);
        divNum1.innerText = `${randomNumber}`;
    }
    else{
        divNum1.innerText = `El numero minimo debe ser menor al numero maximo`;
    }
}


//*Ejercicio 5
function randomNum2() {
    let divNum2 = document.getElementById("randomNum2");

    let min = 1;
    let max = 1000;
    let randomNums = [];
    let finalNums = ""

    while(randomNums.length < 100) {
        let randomNumber = Math.floor(Math.random() * (max  - min) + min);
        let findNum = randomNums.find(num => num === randomNumber);

        if(findNum == undefined) {
            randomNums.push(randomNumber);
        }
    }

    for(num of randomNums){
        finalNums += `${num},`
    }
    
    console.log(randomNums)
    divNum2.innerText = `${finalNums}.`;
}