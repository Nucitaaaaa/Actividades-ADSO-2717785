
function lista() {
    const tareasElement = document.getElementById("tareas"); 
    fetch("http://localhost:3030/tareas")
        .then(response => response.json())
        .then(data => { 
            tareasElement.innerHTML = "";

            data.forEach(function(tarea) { 
                let element = document.createElement("li");
                let content = document.createTextNode(`ID: ${tarea.id} , Nombre: ${tarea.nombre} , Contenido: ${tarea.contenido}`);
                
                element.appendChild(content);
                tareasElement.appendChild(element);
            });
        });
}
lista();


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

function agregarTareaALista(tarea) {
    const tareasElement = document.getElementById('tareas');
    const element = document.createElement('li');
    const content = document.createTextNode(`ID: ${tarea.id}, Nombre: ${tarea.nombre}, Contenido: ${tarea.contenido}`);
    
    element.appendChild(content);
    tareasElement.appendChild(element);
}    
