const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const routes = require('./routes/index'); // Asegúrate de que la ruta sea correcta

const app = express();
const port = 3000;

// Configuración de middlewares
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Servir archivos estáticos
app.use(express.static(path.join(__dirname, 'public')));

// Usar las rutas definidas en routes/index.js
app.use('/', routes);

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor corriendo en http://localhost:${port}`);
});
