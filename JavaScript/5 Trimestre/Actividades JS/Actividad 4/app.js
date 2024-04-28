
let tasks = [];

function addTask() {
    let newTask = document.getElementById("nuevaTarea").value;

    if (newTask.trim() !== "") {
        tasks.push(newTask);
        renderTasks();
        document.getElementById("nuevaTarea").value = ""; // Limpiar el campo de entrada después de agregar la tarea
    } else {
        alert("Por favor, ingrese una tarea válida.");
    }
}

function renderTasks() {
    let tasksList = document.getElementById("tarea");
    tasksList.innerHTML = "";

    tasks.forEach((task) => {
        let element = document.createElement("li");
        let content = document.createTextNode(task);
        element.appendChild(content);

        tasksList.appendChild(element);
    });
}
