
//*Dependencias
const express = require("express");
const cors = require("cors"); 

//*App
const app = express(); 
app.use(express.json());
app.use(cors()) 

//*Puerto
const port = process.env.port || 3030;

//TODO - Almacenar Tareas (Temporal)
const tareas = [
    { id: 1, nombre: "Hacer aseo", contenido:"En la casa :D"},
    { id: 2, nombre: "Tarea PHP", contenido:"No quiero hacerla xd"},
];


//?Rutas

app.get("/", (req, res) => {
    res.send("Ruta Index");
});

app.get("/tareas", (req, res) => {
    res.send(tareas)
});

app.get("/tareas/tarea/:id", (req, res) => {
    const tarea = tareas.find((task) => task.id === parseInt(req.params.id))

    if (!tarea) return res.status(404).send("No se encontró la tarea")
    else res.send(tarea)
});

app.post("/tareas", (req, res) => {
    const tarea = {
        id: tareas.length + 1,
        nombre: req.body.nombre,
        contenido: req.body.contenido,
    };
    tareas.push(tarea);

    res.send(tarea);
});

app.put("/tareas/tarea/:id", (req, res) => {
    const tarea = tareas.find((task) => task.id === parseInt(req.params.id));

    if (!tarea) return res.status(404).send("No se encontró la tarea");

    else {
        tarea.id = req.body.id,
        tarea.nombre = req.body.nombre,
        tarea.contenido = req.body.contenido,
        
        res.send(tarea)
    }
})

app.delete("/tareas/tarea/:id", (req, res) => {
    const tarea = tareas.find((task) => task.id === parseInt(req.params.id))

    if (!tarea) return res.status(404).send("No se encontró la tarea")
    else res.send(tarea)

    const index = tareas.indexOf(tarea);
    tareas.splice(index, 1);
    res.send(`Tarea eliminada: ${tarea}`);
});


//*Conexión al puerto
app.listen(port, () => console.log(`Escuchando al puerto ${port}....`));
