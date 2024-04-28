
function generatePassword() {
    let letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
    let specialChars = ['!', '@', '#', '$', '%', '^', '&', '?'];
    let password = "";
    let characters = [];

    let passwordDiv = document.getElementById("password");
    let length = parseInt(document.getElementById("passwordLength").value);
    let lettersCheckbox = document.getElementById("letters");
    let numbersCheckbox = document.getElementById("numbers");
    let specialCharsCheckbox = document.getElementById("specialChars");

    if (lettersCheckbox.checked) {
        characters.push(...letters);
    }

    if (numbersCheckbox.checked) {
        characters.push(...numbers);
    }

    if (specialCharsCheckbox.checked) {
        characters.push(...specialChars);
    }

    if (characters.length === 0) {
        passwordDiv.innerText = "Debe seleccionar al menos un tipo de caracteres permitidos.";
        return;
    }

    if (!length) {
        passwordDiv.innerText = "Debe indicar la longitud deseada para la contraseña.";
        return;
    }

    else if (length < 8 || length > 16){
        passwordDiv.innerText = "La longitud de la contraseña debe ser entre 8 y 16 caracteres.";
        return;
    }

    while (password.length < length) {
        let randomCharIndex = Math.floor(Math.random() * characters.length);
        password += characters[randomCharIndex];
    }
    
    passwordDiv.innerText = password.length > 0 ? password : "Error inesperado"; 
    characters = [];
}
