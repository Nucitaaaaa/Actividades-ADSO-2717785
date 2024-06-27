

<?php
if ($_POST) {
    $nombre_vendedor = $_POST['nombre_vendedor'];
    $autos_vendidos = $_POST['autos_vendidos'];
    $valor_ventas = $_POST['valor_ventas'];

    $salario_basico = 737000;
    $comision_por_auto = 50000;
    $porcentaje_venta = 0.05;

    $salario_total = $salario_basico + ($comision_por_auto * $autos_vendidos) + ($porcentaje_venta * $valor_ventas);

    echo '<p>Nombre del Vendedor: ' . htmlspecialchars($nombre_vendedor) . '</p>';
    echo '<p>Salario Total: ' . number_format($salario_total, 2) . '</p>';
}
?>
