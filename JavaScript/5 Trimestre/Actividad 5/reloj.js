

//? Reloj

function mostrarHora() {
    const dia = new Date();
    let hora = dia.getHours();
    let minutos = dia.getMinutes();

    hora = hora % 12 || 12; 

    minutos < 10 ? minutos = '0' + minutos : minutos = minutos

    const horaActual = `${hora}:${minutos}`;

    document.getElementById('reloj').textContent = horaActual;
}

setInterval(mostrarHora, 1000);
mostrarHora();


//? Cronometro


function cronometro() {
    let tiempoInicio = 0;
    let intervalo;
    let corriendo = false;

    function actualizarCronometro() {
        const tiempoActual = Date.now();
        const tiempoTranscurrido = tiempoActual - tiempoInicio;

        const horas = Math.floor(tiempoTranscurrido / 3600000);
        const minutos = Math.floor((tiempoTranscurrido % 3600000) / 60000);
        const segundos = Math.floor((tiempoTranscurrido % 60000) / 1000);

        const tiempoFormateado = `${agregarCeros(horas)}:${agregarCeros(minutos)}:${agregarCeros(segundos)}`;
        
        document.getElementById("cronometro").textContent = tiempoFormateado;
    }

    function iniciarCronometro() {
        document.getElementById("parar").style.display = 'block'
        document.getElementById("reiniciar").style.display = 'block'
        document.getElementById("inicio").style.display = 'none'
        if (!corriendo) {
            tiempoInicio = Date.now();
            intervalo = setInterval(actualizarCronometro, 1000);
            corriendo = true;
        }
    }

    function pararCronometro() {
        clearInterval(intervalo);
        corriendo = false;
    }

    function reiniciarCronometro() {
        pararCronometro();
        document.getElementById("inicio").style.display = 'block'
        document.getElementById("parar").style.display = 'none'
        document.getElementById("reiniciar").style.display = 'none'
        
        document.getElementById("cronometro").textContent = "00:00:00";
    }

    function agregarCeros(valor) {
        return valor < 10 ? "0" + valor : valor;
    }

    document.getElementById("inicio").addEventListener("click", iniciarCronometro);
    document.getElementById("parar").addEventListener("click", pararCronometro);
    document.getElementById("reiniciar").addEventListener("click", reiniciarCronometro);

} cronometro()


//?Temporizador 


let temporizador;
let tiempoRestante;
let temporizadorCorriendo = false;

const temporizadorDisplay = document.getElementById('temporizador');
const iniciarTemp = document.getElementById('iniciarTemp');
const seguirTemp = document.getElementById('seguirTemp');
const pausarTemp = document.getElementById('pausarTemp');
const reiniciarTemp = document.getElementById('reiniciarTemp');
const inputTiempo = document.getElementById('inputTiempo');

function iniciarTemporizador() {
    iniciarTemp.style.display = 'none'
    pausarTemp.style.display = 'block'
    reiniciarTemp.style.display = 'block'
    let tiempoInicial = inputTiempo.value;
    tiempoRestante = tiempoInicial;
    temporizadorCorriendo = true;

    temporizador = setInterval(actualizarTemporizador, 1000);
}

function actualizarTemporizador() {
    const horas = Math.floor(tiempoRestante / 3600);
    const minutos = Math.floor((tiempoRestante % 3600) / 60);
    const segundos = tiempoRestante % 60;

    temporizadorDisplay.textContent = `${formatoTiempo(horas)}:${formatoTiempo(minutos)}:${formatoTiempo(segundos)}`;

    if (tiempoRestante === 0) {
    detenerTemporizador();
    } else {
    tiempoRestante--;
    }
}

function formatoTiempo(tiempo) {
    return tiempo < 10 ? `0${tiempo}` : tiempo;
}

function detenerTemporizador() {
    clearInterval(temporizador);
    iniciarTemp.style.display = 'none'
    seguirTemp.style.display = 'block'
    temporizadorCorriendo = false;
}

function seguirTemporizador() {
    seguirTemp.style.display = 'none'
    tiempoRestante = tiempoRestante;
    temporizadorCorriendo = true;

    temporizador = setInterval(actualizarTemporizador, 1000);
}

function reiniciarTemporizador() {
    detenerTemporizador();

    iniciarTemp.style.display = 'block'
    seguirTemp.style.display = 'none'
    pausarTemp.style.display = 'none'
    reiniciarTemp.style.display = 'none'

    temporizadorDisplay.textContent = '00:00:00';
    inputTiempo.value = '';
}

iniciarTemp.addEventListener('click', () => {
    if (!temporizadorCorriendo && inputTiempo.value !== '') {
    iniciarTemporizador();
    }
});

seguirTemp.addEventListener('click', () => {
    if (!temporizadorCorriendo && inputTiempo.value !== '') {
    seguirTemporizador();
    }
});

pausarTemp.addEventListener('click', () => {
    if (temporizadorCorriendo) {
    detenerTemporizador();
    }
});

reiniciarTemp.addEventListener('click', () => {
    reiniciarTemporizador();
});

    

