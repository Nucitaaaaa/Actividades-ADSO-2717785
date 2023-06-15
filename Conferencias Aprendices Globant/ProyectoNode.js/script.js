
function tabla() {
    const tbody = document.getElementById("tBody");
    fetch("/api/estudiantes")
        .then(response => response.json())
        .then(data => {
            data.forEach(function(item) {

                const fila = tbody.insertRow();

                const celda1 = fila.insertCell();
                const celda2 = fila.insertCell();
                const celda3 = fila.insertCell();
                const celda4 = fila.insertCell();
                const celda5 = fila.insertCell();
                const celda6 = fila.insertCell();

                celda1.textContent = item.id;
                celda2.textContent = item.nombre;
                celda3.textContent = item.apellido;
                celda4.textContent = item.edad;
                celda5.textContent = item.semestre;
                celda6.textContent = item.estudia ? "Si" : "No";
                });
            });
    }

    tabla()