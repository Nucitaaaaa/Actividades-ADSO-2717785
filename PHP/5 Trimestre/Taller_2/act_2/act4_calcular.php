
<?php
if ($_POST) {
    $cedula = $_POST['cedula'];
    $nombre = $_POST['nombre'];
    $monto = $_POST['monto'];
    $interes_mensual = $_POST['interes'] / 100;
    $plazo = $_POST['plazo'];

    $cuota_fija = $monto * $interes_mensual / (1 - pow(1 + $interes_mensual, -$plazo));

    echo "<h2>Tabla de Amortización</h2>";
    echo "<p>Cédula: $cedula</p>";
    echo "<p>Nombre: $nombre</p>";
    echo "<table border='1'>";
    echo "<tr><th>No. Cuota</th><th>Saldo Anterior</th><th>Valor Cuota Fija</th><th>Abono Interés</th><th>Abono Capital</th><th>Nuevo Saldo</th></tr>";

    $saldo_anterior = $monto;

    for ($i = 1; $i <= $plazo; $i++) {
        $abono_interes = $saldo_anterior * $interes_mensual;
        $abono_capital = $cuota_fija - $abono_interes;
        $nuevo_saldo = $saldo_anterior - $abono_capital;

        echo "<tr>
                <td>$i</td>
                <td>" . number_format($saldo_anterior, 2) . "</td>
                <td>" . number_format($cuota_fija, 2) . "</td>
                <td>" . number_format($abono_interes, 2) . "</td>
                <td>" . number_format($abono_capital, 2) . "</td>
                <td>" . number_format($nuevo_saldo, 2) . "</td>
              </tr>";

        $saldo_anterior = $nuevo_saldo;
    }

    echo "</table>";
}
?>