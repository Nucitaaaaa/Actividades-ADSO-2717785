
<?php 

$errores = '';

if (isset($_POST['submit'])) {
    $nombre = $_POST['nombre'];
    $nombre = $_POST['correo'];

    if (!empty($nombre)) {
        $nombre = filter_var($nombre, FILTER_SANITIZE_STRING);
        echo(`Tu nombre es $nombre` . '<br>');
    } 
    else {
        $errores .= 'Por favor ingresa un nombre <br />';
    }

    if (!empty($correo)) {
        $nombre = filter_var($correo, FILTER_SANITIZE_EMAIL);
    
        if(!filter_var($correo, FILTER_VALIDATE_EMAIL)) {
            $errores .= 'Por favor ingresa un correo valido <br />';
        } 
        else {
            echo(`Tu correo es $correo` . '<br>');
        }
    } 
    else {
        $errores .= 'Por favor ingresa un correo <br />';
    }

}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario</title>
    <style>
        .error {color:red;}
    </style>
</head>
<body>
    <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
        <input type="text" placeholder="Nombre:" name="nombre" id="nombre">
        <input type="text" placeholder="Correo:" name="correo" id="correo">
        
        <?php if(!empty($errores)): ?>
            <div class="error"><?php echo $errores; ?></div>
        <?php endif; ?>

        <input type="submit" value="Submit">
    </form>
</body>
</html>









