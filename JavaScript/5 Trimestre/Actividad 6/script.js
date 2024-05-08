
var listaEmpleados = []
var editando = -1

//Creacion de la clase
class Empleado {
    constructor(nombre, cargo) {
        this.nombre = nombre;
        this.cargo = cargo;
    }

    agregarEmpleado(empleado) {
        listaEmpleados.push(empleado)
    }
}


//Traer datos del DOM
var nombreEmpleado = document.getElementById("nombre")
var cargoEmpleado = document.getElementById("cargo")
var listaDeEmpleados = document.getElementById("listaEmpleados")


//CRUD
function mostrarEmpleados() {
    listaDeEmpleados.innerHTML = ""

    listaEmpleados.forEach((empleado,index) => {
        const li = document.createElement("li");
        li.textContent = `${empleado.nombre} - ${empleado.cargo}`;

        const eliminar = document.createElement("button");
        eliminar.textContent = "Eliminar";
        eliminar.addEventListener("click", () => {
            listaEmpleados.splice(empleado, 1);
            mostrarEmpleados();
        });

        const editar = document.createElement("button");
        editar.textContent = "Editar";
        editar.addEventListener("click", () => {
            editarEmpleado(index);
            mostrarEmpleados();
        });

        li.appendChild(eliminar);
        li.appendChild(editar)
        listaDeEmpleados.appendChild(li);
    });
}

function agregarEmpleado() {
    let nombre = nombreEmpleado.value
    let cargo = cargoEmpleado.value

    if (!nombre || !cargo) {
        alert('Debe completar todos los campos');
        return;
    }

    if(editando !== -1) {
        listaEmpleados[editando].nombre = nombre;
        listaEmpleados[editando].cargo = cargo;
        editando = -1
    }

    else {
        let empleado = new Empleado(nombre, cargo)
        empleado.agregarEmpleado(empleado)
    }

    nombreEmpleado.value = ""
    cargoEmpleado.value = ""

    mostrarEmpleados()
}

function editarEmpleado(indice) {
    const empleado = listaEmpleados[indice]
    nombreEmpleado.value = empleado.nombre;
    cargoEmpleado.value = empleado.cargo;
    editando = indice;
}

window.addEventListener("load", mostrarEmpleados());