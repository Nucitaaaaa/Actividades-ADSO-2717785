
<?php
if ($_POST) {
    $parcial1 = $_POST['parcial1'];
    $parcial2 = $_POST['parcial2'];
    $parcial3 = $_POST['parcial3'];
    $examen_final = $_POST['examen_final'];
    $trabajo_final = $_POST['trabajo_final'];

    $promedio_parciales = ($parcial1 + $parcial2 + $parcial3) / 3;
    $nota_final = ($promedio_parciales * 0.35) + ($examen_final * 0.35) + ($trabajo_final * 0.30);

    echo '<p>Nota final: ' . $nota_final . '</p>';
    echo '<p>' . ($nota_final > 2.99 ? 'Aprobó' : 'No aprobó') . '</p>';
}
?>