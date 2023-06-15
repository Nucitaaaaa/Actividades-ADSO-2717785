
//Se crea una funcion para convertir los objetos a texto sin formato y ubicarlos en una tabla. 
function tabla() {
    const tbody = document.getElementById("tBody"); //se llama a el id de t-body, donde iran los td (datos)
    fetch("/api/estudiantes")  //se especifica la ruta de donde se van a sacar los datos a través de fetch(Es una función la cual permite las solicitudes http desde el lado del cliente)
        .then(response => response.json()) //se convierten los datos obtenidos a objetos json (JavaScript Object Notation)
        .then(data => { //ya con los datos en formato JSON 
            data.forEach(function(item) { //Por cada objeto o item que se encuentre

                const fila = tbody.insertRow(); //se inserta una fila 

                const celda1 = fila.insertCell(); //y 6 celdas, una por cada atributo del objeto
                const celda2 = fila.insertCell();
                const celda3 = fila.insertCell();
                const celda4 = fila.insertCell();
                const celda5 = fila.insertCell();
                const celda6 = fila.insertCell();

                celda1.textContent = item.id; //Aqui, se especifica en orden, que debe ir en cada celda 
                celda2.textContent = item.nombre;
                celda3.textContent = item.apellido;
                celda4.textContent = item.edad;
                celda5.textContent = item.semestre;
                celda6.textContent = item.estudia ? "Si" : "No"; //aqui se utiliza un operador ternario que actua como un condicional, para escribir en esa celda "Si" si estudia es igual a true, y "No" si no lo es
                });
            });
    }

    tabla() //se llama a la función