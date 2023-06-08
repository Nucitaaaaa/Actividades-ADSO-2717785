//creacion de la API
const express = require("express"); //Se importa el framework Express
const app = express(); //Se llama al framework Express
const port = process.env.port || 3030; //Se define el puerto donde se ejecutará la API
app.use(express.json()); //se agrega el middleware con use (intermediario entre el server y el cliente que procesa solicitudes.)

//Lista estudiantes 

const estudiantes = [ //Se crea la constante de estudiantes, la cual es un array que contiene dos objetos, con los datos de cada estudiante
{id: 1, nombre: "Miguel", apellido: "Perdomo", edad: 19, semestre: 2, estudia: true}, 
{id: 2, nombre: "Juan", apellido: "Figueroa", edad: 29, semestre: 10, estudia: false}
];

//rutas

//ruta1

app.get("/", (req, res) => { //Se crea la ruta principal de la API
    res.send("Esta es mi API") //cuando se haga la solicitud GET a la ruta principal, lo cual es el req, res (Respuesta) mostrará en pantalla el mensaje escrito 
});

//ruta2

app.get("/api/estudiantes", (req, res) => { //Se crea la ruta a la constante estudiantes de la API
    res.send(estudiantes) //cuando se haga la solicitud GET a la ruta, lo cual es el req, res (Respuesta) mostrará en pantalla todos los datos que contenga la constante
});

//ruta3

app.get("/api/estudiantes/:id", (req, res) => { //Se crea la ruta a la constante id(alumno) de la API
    const alumno = estudiantes.find((e) => e.id === parseInt(req.params.id)); //se crea la constante alumno, la cual al ejecutarse busca y compara en el array estudiantes(e) el id que se le ha especificado 
    if (!alumno) //si el alumno no se encuentra (si alumno es diferente de alumno)
    return res //se retorna una respuesta
        .status(404) //se actualiza el status a error 404 (not found)
        .send("Estudiantes no encontrado"); //se muestra este mensaje
    else res.send(alumno); //si el alumno se encuentra, se mostrarán los datos de ese alumno en especifico. 
});

//ruta4

app.post("/api/estudiantes" , (req, res) => { //Se crea la ruta a la constante para crear un alumno de la API (Se inicia un proceso de CRUD)
    const alum = { //Se crea la constante alumno, la cual al llamarla, crea un objeto llamado alumno al cual se le tiene que especificar la información de cada una de las variables en la lista, a traves de las solicitudes HTTP, para su posterior adicion a la base de datos 
        id: estudiantes.length + 1, // se utiliza para asignar un valor único a la propiedad "id" al momento de crear un nuevo objeto estudiante.
        nombre: req.body.nombre, //se utiliza para acceder al valor de la propiedad "nombre" del objeto body contenido en la solicitud req.
        apellido: req.body.apellido, //se utiliza para acceder al valor de la propiedad "apellido" del objeto body contenido en la solicitud req.
        edad: parseInt(req.body.edad), //se utiliza para acceder al valor de la propiedad "edad" del objeto body contenido en la solicitud req.
        semestre: parseInt(req.body.semestre), //se utiliza para acceder al valor de la propiedad "semestre" del objeto body contenido en la solicitud req.
        estudia: req.body.estudia === true, //se utiliza para verificar si el valor de la propiedad "estudia" en el objeto body de la solicitud req es igual a true.
    };
    estudiantes.push(alum); //Este agrega el objeto alum, al final del array de estudiantes
    res.send(alum); //Este muestra en la pantalla los datos del estudiante que se ha creado
});

//ruta5

app.delete("/api/estudiantes/:id", (req, res) => { //Se crea la ruta para eliminar estudiantes del array de la constante estudiantes
    const alumno = estudiantes.find((d) => d.id === parseInt(req.params.id)); //se crea la constante alumno, la cual al ejecutarse busca y compara en el array estudiantes(e) el id que se le ha especificado 
    if (!alumno) return res.status(404).send("Estudiante no encontrado"); //si no es alumno, retorna un error de status 404 y muestra un mensaje a la pantalla.
    else res.send(alumno); //si si se encuentra, se envia la respuesta 

    const index = estudiantes.indexOf(alumno); //Se busca el id del alumno en el array estudiantes
    estudiantes.splice(index, 1); //se elimina el objeto del array
    res.send(alumno); //se muestra el alumno eliminado
});

//ruta6

app.listen(port, () => console.log(`Escuchando al puerto ${port}....`)); //se crea la ruta  para escuchar al puerto, inicia el servidor y lo configura para escuchar las solicitudes entrantes en el puerto especificado, mostrando el mensaje del console.log













