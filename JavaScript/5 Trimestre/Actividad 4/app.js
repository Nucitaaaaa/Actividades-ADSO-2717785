
var tasks = []

function addTask(){
    let newTask = document.getElementById("nuevaTarea").value

    tasks.push(newTask)

    renderTasks()
}

function renderTasks() {
    let tasksList = document.getElementById("tarea")
    tasksList.innerHTML = ""

    tasks.forEach((task) => {
        let element = document.createElement("li");
        let content = document.createTextNode(`${task}`);
        element.appendChild(content);

        tasksList.appendChild(element);
    });
    
}