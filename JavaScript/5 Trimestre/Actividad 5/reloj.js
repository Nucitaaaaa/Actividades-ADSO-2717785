
function mostrarHora() {
    const dia = new Date();
    let hora = dia.getHours();
    let minutos = dia.getMinutes();
    let segundos = dia.getSeconds();
    let horario = hora >= 12 ? 'PM' : 'AM';

    hora = hora % 12 || 12; //convertir de 24 a 12 h

    minutos < 10 ? minutos = '0' + minutos : minutos = minutos
    segundos < 10 ? segundos = '0' + segundos : segundos = segundos

    const horaActual = `${hora}:${minutos}:${segundos} ${horario}`;

    document.getElementById('reloj').textContent = horaActual;
}

setInterval(mostrarHora, 1000);
mostrarHora();

function cronometro() {
    
}

function temporizador() {

}

// performance.