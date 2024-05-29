
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
