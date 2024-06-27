
<?php
if ($_POST) {
    $nombre_paciente = $_POST['nombre_paciente'];
    $peso = $_POST['peso'];
    $altura = $_POST['altura'];

    $imc = $peso / ($altura * $altura);
    $categoria = '';

    if ($imc < 18.5) {
        $categoria = 'Bajo peso';
    } elseif ($imc < 24.9) {
        $categoria = 'Peso normal';
    } elseif ($imc < 29.9) {
        $categoria = 'Sobrepeso';
    } else {
        $categoria = 'Obesidad';
    }

    echo '<p>Nombre del Paciente: ' . htmlspecialchars($nombre_paciente) . '</p>';
    echo '<p>IMC: ' . number_format($imc, 2) . '</p>';
    echo '<p>Categoría: ' . $categoria . '</p>';
}
?>
