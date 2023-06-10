
//API lista de tareas

//creación API

const express = require("express");
const app = express();
const port = process.env.PORT || 30;
app.use(express.json());

//DB

const tareas = [
    {id:1, titulo:"Dibujo Artistica", descripcion:"Hacer un dibujo sobre el amor", vence:"30/08/23", estado:"Terminada"},
    {id:2, titulo:"Plano Matematicas", descripcion:"Hacer un plano", vence:"20/06/23", estado: "Pendiente"}
]

//Rutas

app.get("/", (req, res) => {
    res.send("LISTA DE TAREAS")
})

app.get("/api/tareas", (req, res) => {
    res.send(tareas)
})

app.get("/api/tareas/:id", (req, res) => {
    const tarea = tareas.find((e) => e.id === parseInt(req.params.id))
    if (!tarea) return res.status(404).send("Tarea No Encontrada")
    else res.send(tarea)
})

app.get("/api/tareas/estado/:estado", (req, res) => {
    const tarea = tareas.filter((p) => p.estado === req.params.estado)
    if (!tarea) return res.status(404).send("Tarea No Encontrada")
    else res.send(tarea)
})

app.get("/api/tareas/titulo/:titulo", (req, res) => {
    const tarea = tareas.find((t) => t.titulo === req.params.titulo)
    if (!tarea) return res.status(404).send("Tarea No Encontrada")
    else res.send(tarea)
})

app.post("/api/tareas", (req, res) => {
    const nuevaTarea = {
        id: tareas.length + 1,
        titulo: req.body.titulo, 
        descripcion: req.body.descripcion, 
        vence: req.body.vence,
        estado: req.body.estado
    }
    tareas.push(nuevaTarea);
    res.send(nuevaTarea)
})

app.put("/api/tareas/:id", (req, res) => {
    const tarea = tareas.find((c) => c.id === parseInt(req.params.id))
    if (!tarea) return res.status(404).send("Tarea No Encontrada")
    else {
        tarea.id = parseInt(req.body.id),
        tarea.titulo = req.body.titulo,
        tarea.descripcion = req.body.descripcion,
        tarea.vence = req.body.vence
        tarea.estado = req.body.estado

        res.send(tarea)
    }
})

app.patch("/api/tareas/:id/estado", (req, res) => {
    const tarea = tareas.find((es) => es.id === parseInt(req.params.id))
    if (!tarea) return res.status(404).send("Tarea No Encontrada")
    else {
        tarea.estado = req.body.estado

        res.send(tarea)
    }
})

app.delete("/api/tareas/:id", (req, res) => {
    const tarea = tareas.find((d) => d.id === parseInt(req.params.id))
    if (!tarea) return res.status(404).send("Tarea No Encontrada")
    else res.send(tarea)

    const index = tareas.indexOf(tarea)
    tareas.splice(index, 1)
    res.send(tarea)
})

app.listen(port, () => console.log(`Escuchando al puerto ${port}...`))
