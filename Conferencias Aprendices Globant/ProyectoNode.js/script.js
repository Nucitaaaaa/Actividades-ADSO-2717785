
//Se crea una funcion para convertir los objetos a texto sin formato y ubicarlos en una tabla. 
function tabla() {
    const tbody = document.getElementById("tBody"); //se llama a el id de t-body, donde iran los td (datos)
    fetch("http://localhost:3030/api/estudiantes")  //se especifica la ruta de donde se van a sacar los datos a través de fetch(Es una función la cual permite las solicitudes http desde el lado del cliente)
        .then(response => response.json()) //se convierten los datos obtenidos a objetos json (JavaScript Object Notation)
        .then(data => { //ya con los datos en formato JSON 
            data.forEach(function(estudiantes) { //Por cada objeto que se encuentre en el array estudiantes

                const fila = tbody.insertRow(); //se inserta una fila 

                const celda1 = fila.insertCell(); //y 6 celdas, una por cada atributo del objeto
                const celda2 = fila.insertCell();
                const celda3 = fila.insertCell();
                const celda4 = fila.insertCell();
                const celda5 = fila.insertCell();
                const celda6 = fila.insertCell();

                celda1.textContent = estudiantes.id; //Aqui, se especifica en orden, que debe ir en cada celda, llamando a cada atributo en el array de estudiantes
                celda2.textContent = estudiantes.nombre;
                celda3.textContent = estudiantes.apellido;
                celda4.textContent = estudiantes.edad;
                celda5.textContent = estudiantes.semestre;
                celda6.textContent = estudiantes.estudia ? "Si" : "No"; //aqui se utiliza un operador ternario que actua como un condicional, para escribir en esa celda "Si" si estudia es igual a true, y "No" si no lo es
                });
            });
    }

    tabla(); //se llama a la función