
//; 

const express = require("express");
const app = express();
const port = process.env.port || 300; //process.env.port(no me acordaba xd)
app.use(express.json());

const estudiantes = [
    {id:1, nombre:"pepito", apellido:"perez", edad:17, semestre:8, estudia:true},
    {id:2, nombre:"jose", apellido:"ramirez", edad:19, semestre:3, estudia:true},
]

//puertos 

//1

app.get("/", (req, res) => {
    res.send("Esta es mi API")
})

//2

app.get("/api/estudiantes", (req, res) => {
    res.send(estudiantes);
})

//3

app.get("/api/estudiantes/:id", (req,res) => {
const alumno = estudiantes.find((e) => e.id === parseInt(req.params.id)) //parseInt(me falto XD)
if (!alumno)
res.status(404).send("No se encontró al estudiante")
else res.send(alumno);
})

//4

app.post("/api/estudiantes", (req, res) => {
    const alum = {
        id: estudiantes.length + 1,
        nombre: req.body.nombre,
        apellido: req.body.apellido,
        edad: parseInt(req.body.edad),
        semestre: parseInt(req.body.edad),
        estudia: req.body.estudia === true,
    };  //; falto xd
    estudiantes.push(alum); //; falto
    res.send(alum);
})

//puse alum en donde iba alumno y alumno en donde iba alumn XDDD

//5

app.delete("/api/estudiantes/:id", (req, res) => {
    const alumno = estudiantes.find((d) => d.id === parseInt(req.params.id)) //parseInt(me falto XD)
if (!alumno)
res.status(404).send("No se encontró al estudiante")
else res.send(alumno);

const index = estudiantes.indexOf(alumno)
estudiantes.splice(index, 1)
res.send(alumno);
})


//6

app.listen(port, () => console.log(`Escuchando al puerto ${port}...`))