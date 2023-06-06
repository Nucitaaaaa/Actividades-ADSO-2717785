
//nmp init: inicia el proyecto
//npm install express: instala el framework express en el proyecto
//npm install -g nodemon: instala nodemon en el proyecto

const express = require("express"); //importa express
const app = express();  //inicia express
const port = process.env.port || 30 //establece el puerto
app.use(express.json()) //inicia el middleware


const estudiantes = [ //crea el array con los objetos a almacenar en la base de datos 
{id:1, nombre:"jose"},
{id:2, nombre:"juan"}
]

//rutas

app.get("/", (req, res) =>{  //Ruta principal de la API 
    res.send("Esta es mi api");
})

app.get("/api/estudiantes", (req, res) => {
    res.send(estudiantes);
})

app.get("/api/estudiantes/:id", (req, res) => {
    const alumno = estudiantes.find((e) => e.id === parseInt(req.params.id))
    if (!alumno) return res.status(404).send("Estudiante no encontrado")
    else return res.send(alumno);
})

app.post("/api/estudiantes", (req, res) => {
    const alum = {
        id: estudiantes.length + 1,
        nombre: req.body.nombre
    }

    estudiantes.push(alum)
    res.send(alum)
})

app.delete("/api/estudiantes/:id", (req, res) => {
    const alumno = estudiantes.find((d) => d.id === parseInt(req.params.id))
    if (!alumno) return res.status(404).send("Estudiante no encontrado")
    else res.send(alumno); //no poner return

    const index = estudiantes.indexOf(alumno);
    estudiantes.splice(index, 1);
    res.send(alumno);  
});

app.listen(port, () => console.log(`Escuchando al puerto ${port}...`)) //Ruta de escucha al puerto 