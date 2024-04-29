
function mostrarHora() {
    const dia = new Date();
    let hora = dia.getHours();
    let minutos = dia.getMinutes();
    let horario = hora >= 12 ? 'p.m' : 'a.m';

    hora = hora % 12 || 12; //convertir de 24 a 12 h

    minutos < 10 ? minutos = '0' + minutos : minutos = minutos

    const horaActual = `${hora}:${minutos} ${horario}`;

    document.getElementById('reloj').textContent = horaActual;
}

setInterval(mostrarHora, 1000);
mostrarHora();

function cronometro() {
    
}

function temporizador() {

}

// performance.