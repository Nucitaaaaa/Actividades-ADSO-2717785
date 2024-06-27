
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calcular Salario</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Calcular Salario</h1>
        <form action="act2_calcular.php" method="post">
            <label for="nombre_vendedor">Nombre del Vendedor:</label>
            <input type="text" name="nombre_vendedor" id="nombre_vendedor" required><br>
            <label for="autos_vendidos">Cantidad de Automóviles Vendidos:</label>
            <input type="number" name="autos_vendidos" id="autos_vendidos" required><br>
            <label for="valor_ventas">Precio Total de Automóviles Vendidos:</label>
            <input type="number" step="0.01" name="valor_ventas" id="valor_ventas" required><br>
            <input type="submit" value="Calcular Salario">
        </form>
    </div>
</body>
</html>


