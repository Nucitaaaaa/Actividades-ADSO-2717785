
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calcular Amortización</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <form action="act4_calcular.php" method="post">
            <label for="cedula">Cédula:</label>
            <input type="text" name="cedula" id="cedula" required><br>
            <label for="nombre">Nombre:</label>
            <input type="text" name="nombre" id="nombre" required><br>
            <label for="monto">Monto del Crédito:</label>
            <input type="number" step="0.01" name="monto" id="monto" required><br>
            <label for="interes">Tasa de Interés Mensual (%):</label>
            <input type="number" step="0.01" name="interes" id="interes" required><br>
            <label for="plazo">Plazo (meses):</label>
            <input type="number" name="plazo" id="plazo" required><br>
            <input type="submit" value="Calcular Amortización">
        </form>
    </div>
</body>
</html>

