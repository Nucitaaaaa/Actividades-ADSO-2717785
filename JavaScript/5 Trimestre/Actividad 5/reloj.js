
function mostrarHora() {
    const dia = new Date();
    let hora = dia.getHours();
    let minutos = dia.getMinutes();
    // let horario = hora >= 12 ? 'P.M' : 'A.M';

    hora = hora % 12 || 12; //convertir de 24 a 12 h

    minutos < 10 ? minutos = '0' + minutos : minutos = minutos

    const horaActual = `${hora}:${minutos}`;

    document.getElementById('reloj').textContent = horaActual;
}

setInterval(mostrarHora, 1000);
mostrarHora();

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
        document.getElementById("cronometro").textContent = "00:00:00";
    }

    function agregarCeros(valor) {
        return valor < 10 ? "0" + valor : valor;
    }

    document.getElementById("inicio").addEventListener("click", iniciarCronometro);
    document.getElementById("parar").addEventListener("click", pararCronometro);
    document.getElementById("reiniciar").addEventListener("click", reiniciarCronometro);

}

cronometro()

function temporizador() {

}

