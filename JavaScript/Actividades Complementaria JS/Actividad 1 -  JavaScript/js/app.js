
var nombre = prompt('Ingresa tu nombre aquí: ');
var añoNacimiento = parseInt(prompt('Ingrese su fecha de nacimiento aquí: '));

const fecha = new Date();
const fechaActual= fecha.getFullYear();

var edad = fechaActual - añoNacimiento;

if (edad < 9) {
    document.write(`Hola ${nombre}, tienes ${edad} años, eres un niño`)
} else if (edad < 18) {
    document.write(`Hola ${nombre}, tienes ${edad} años, eres un adolencente`) 
} else {
    document.write(`Hola ${nombre}, tienes ${edad} años, eres un adulto`)
    }

