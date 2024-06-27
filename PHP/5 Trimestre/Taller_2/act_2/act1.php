
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calcular Nota Final</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Calcular Nota Final</h1>
        <form action="act1_calcular.php" method="post">
            <label for="parcial1">Parcial 1:</label>
            <input type="number" step="0.01" name="parcial1" id="parcial1" required><br>
            <label for="parcial2">Parcial 2:</label>
            <input type="number" step="0.01" name="parcial2" id="parcial2" required><br>
            <label for="parcial3">Parcial 3:</label>
            <input type="number" step="0.01" name="parcial3" id="parcial3" required><br>
            <label for="examen_final">Examen Final:</label>
            <input type="number" step="0.01" name="examen_final" id="examen_final" required><br>
            <label for="trabajo_final">Trabajo Final:</label>
            <input type="number" step="0.01" name="trabajo_final" id="trabajo_final" required><br>
            <input type="submit" value="Calcular Nota Final">
        </form>
    </div>
</body>
</html>

