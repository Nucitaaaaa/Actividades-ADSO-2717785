
<?php

$conexion = new mysqli('localhost', 'root', '', 'pruebadatos');

if($conexion->connect_errno){
    die('Hubo un error en la conexión');
}else{
    $sql = "INSERT INTO usuarios (id, nombre, edad) VALUES(null, 'sonia', 30)";
    $resultado = $conexion->query($sql);

    if($conexion->affected_rows>=1){
        echo 'filas agregadas:' . $conexion->affected_rows;
    }
}

?>