
document.addEventListener('DOMContentLoaded', function() {
    agregarTarea();
});

function agregarTarea() {
    document.getElementById('formulario-tarea').addEventListener('submit', function(event) {
        event.preventDefault();

        const nombre = document.getElementById('nombre').value;
        const contenido = document.getElementById('contenido').value;
    
        const tarea = { nombre, contenido };
    
        fetch('http://localhost:3030/tareas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(tarea)
        })
        .then(response => response.json())
        .then(data => {
            agregarTareaALista(data);
        })
        .catch(error => console.error('Error:', error));
    });
}

function agregarTareaALista(tarea) {
    const tareasElement = document.getElementById("tareas"); 
    
    let div = document.createElement("div");
                
    let nombre = document.createElement("h4");
    let nombreContent = document.createTextNode(`- ${tarea.nombre}`);
    nombre.appendChild(nombreContent);  
    
    let contenido = document.createElement("p");
    let contenidoContent = document.createTextNode(`Descripcion: ${tarea.contenido}`);
    contenido.appendChild(contenidoContent);

    const eliminar = document.createElement("button");
    eliminar.textContent = "Eliminar";
    eliminar.addEventListener("click", () => {
        eliminarTarea(tarea.id);
        div.remove();
    });

    div.appendChild(nombre);
    div.appendChild(contenido);
    div.appendChild(eliminar)

    tareasElement.appendChild(div);
}

function eliminarTarea(id) {
    fetch(`http://localhost:3030/tareas/tarea/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('No se pudo eliminar la tarea');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); 
    })
}

function lista() {
    const tareasElement = document.getElementById("tareas"); 
    fetch("http://localhost:3030/tareas")
        .then(response => response.json())
        .then(data => { 
            tareasElement.innerHTML = "";

            data.forEach(function(tarea) {
                let div = document.createElement("div");
                
                let nombre = document.createElement("h4");
                let nombreContent = document.createTextNode(`- ${tarea.nombre}`);
                nombre.appendChild(nombreContent);  
                
                let contenido = document.createElement("p");
                let contenidoContent = document.createTextNode(`Descripcion: ${tarea.contenido}`);
                contenido.appendChild(contenidoContent);

                const eliminar = document.createElement("button");
                eliminar.textContent = "Eliminar";
                eliminar.addEventListener("click", () => {
                    eliminarTarea(tarea.id);
                    div.remove();
                });
            
                div.appendChild(nombre);
                div.appendChild(contenido);
                div.appendChild(eliminar)

                tareasElement.appendChild(div);
            });
        });
}

lista();

