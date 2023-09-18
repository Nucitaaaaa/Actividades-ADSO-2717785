
<?php

$conexion = new mysqli('localhost', 'root', '', 'pruebadatos');

if($conexion->connect_errno){
    die('Hubo un error en la conexión');
}else{
    $sql = "SELECT * FROM usuarios";
    $resultado = $conexion->query($sql);

    if($resultado->num_rows){
        while($fila=$resultado->fetch_assoc()){
            echo $fila ['id'].'   '.$fila['nombre']. '<br/>';
        }
    }else{
        echo 'no hay datos';
    }
    }

?>