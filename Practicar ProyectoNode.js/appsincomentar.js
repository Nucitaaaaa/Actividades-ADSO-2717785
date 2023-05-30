
const express = require("express");
const app = express();
const port = process.env.port || 3030;
app.use(express.json());

const estudiantes = [
    {id: 1, nombre: "Miguel", apellido: "Perdomo", edad: 19, semestre: 2, estudia: true},
    {id: 2, nombre: "Juan", apellido: "Figueroa", edad: 29, semestre: 10, estudia: false}
];

app.get("/", (req, res) => {
    res.send("Esta es mi API");
});

app.get("/api/estudiantes", (req, res) => {
    res.send(estudiantes);
});

app.get("/api/estudiantes/:id", (req, res) => {
    const alumno = estudiantes.find((e) => e.id === parseInt(req.params.id));
    if (!alumno) return res.status(404).send("Estudiantes no encontrado");
    else res.send(alumno);
});

app.post("/api/estudiantes" , (req, res) => {
    const alum = {
    id: estudiantes.length + 1,
    nombre: req.body.nombre,
    apellido: req.body.apellido,
    edad: parseInt(req.body.edad),
    semestre: parseInt(req.body.semestre),
    estudia: req.body.estudia === true,
    };
    estudiantes.push(alum);
    res.send(alum);
});

app.delete("/api/estudiantes/:id", (req, res) => {
    const alumno = estudiantes.find((d) => d.id === parseInt(req.params.id));
    if (!alumno) return res.status(404).send("Estudiante no encontrado");
    else res.send(alumno);

    const index = estudiantes.indexOf(alumno);        
    estudiantes.splice(index, 1);
    res.send(alumno);
});

app.listen(port, () => console.log(`Escuchando al puerto ${port}....`));
