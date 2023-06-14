
const express = require("express");
const app = express();
const port = process.env.port || 3030;
app.use(express.json());
app.use(express.static('public'));

const estudiantes = [
    { id: 1, nombre: "Miguel", apellido: "Perdomo", edad: 19, semestre: 2, estudia: true },
    { id: 2, nombre: "Juan", apellido: "Figueroa", edad: 29, semestre: 10, estudia: false }
];

app.get("/", (req, res) => {
    res.send("Esta es mi API");
});

app.get("/api/estudiantes", (req, res) => {
    const estudiantesHTML = estudiantes.map(estudiante => `
        <tr>
            <td>${estudiante.id}</td>
            <td>${estudiante.nombre}</td>
            <td>${estudiante.apellido}</td>
            <td>${estudiante.edad}</td>
            <td>${estudiante.semestre}</td>
            <td>${estudiante.estudia ? 'Sí' : 'No'}</td>
        </tr>
    `).join('');

    const html = `
        <html>
        <head>
            <title>Tabla de Estudiantes</title>
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                }
        
                th, td {
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }
            </style>
        </head>
        <body>
            <h1>Tabla de Estudiantes</h1>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>Edad</th>
                    <th>Semestre</th>
                    <th>Estudia</th>
                </tr>
                ${estudiantesHTML}
            </table>
        </body>
        </html>
    `;

    res.send(html);
});

app.get("/api/estudiantes/:id", (req, res) => {
    const id = parseInt(req.params.id);
    const estudiante = estudiantes.find(est => est.id === id);

    if (estudiante) {
        const estudianteHTML = `
            <tr>
                <td>${estudiante.id}</td>
                <td>${estudiante.nombre}</td>
                <td>${estudiante.apellido}</td>
                <td>${estudiante.edad}</td>
                <td>${estudiante.semestre}</td>
                <td>${estudiante.estudia ? 'Sí' : 'No'}</td>
            </tr>
        `;

        const html = `
            <html>
            <head>
                <title>Tabla de Estudiantes</title>
                <style>
                    table {
                        border-collapse: collapse;
                        width: 100%;
                    }

                    th, td {
                        border: 1px solid black;
                        padding: 8px;
                        text-align: left;
                    }
                </style>
            </head>
            <body>
                <h1>Detalles del estudiante</h1>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Nombre</th>
                        <th>Apellido</th>
                        <th>Edad</th>
                        <th>Semestre</th>
                        <th>Estudia</th>
                    </tr>
                    ${estudianteHTML}
                </table>
            </body>
            </html>
        `;

        res.send(html);
    } else {
        res.status(404).send("Estudiante no encontrado");
    }
});


app.post("/api/estudiantes", (req, res) => {
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

//ruta no hecha en la conferencia (ruta put)

app.put("/api/estudiantes/:id", (req, res) => {
    const alumno = estudiantes.find((c) => c.id === parseInt(req.params.id));
    if (!alumno) return res.status(404).send("Estudiante no encontrado");

    else {
        alumno.id = req.body.id,
        alumno.nombre = req.body.nombre,
        alumno.apellido = req.body.apellido,
        alumno.edad = parseInt(req.body.edad),
        alumno.semestre = parseInt(req.body.semestre),
        alumno.estudia = req.body.estudia === true,

        res.send(alumno)
    }
})

app.delete("/api/estudiantes/:id", (req, res) => {
    const alumno = estudiantes.find((d) => d.id === parseInt(req.params.id));
    if (!alumno) return res.status(404).send("Estudiante no encontrado");
    else res.send(alumno);

    const index = estudiantes.indexOf(alumno);
    estudiantes.splice(index, 1);
    res.send(alumno);
});


app.listen(port, () => console.log(`Escuchando al puerto ${port}....`));













