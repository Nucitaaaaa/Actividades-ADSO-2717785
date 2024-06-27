
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calcular IMC</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Calcular IMC</h1>
        <form action="act3_calcular.php" method="post">
            <label for="nombre_paciente">Nombre del Paciente:</label>
            <input type="text" name="nombre_paciente" id="nombre_paciente" required><br>
            <label for="peso">Peso (kg):</label>
            <input type="number" step="0.1" name="peso" id="peso" required><br>
            <label for="altura">Estatura (m):</label>
            <input type="number" step="0.01" name="altura" id="altura" required><br>
            <input type="submit" value="Calcular IMC">
        </form>
    </div>
</body>
</html>
