
<?php 
#Validación con Post
print_r($_POST);

if (!$_POST) {
    header('Location: http://localhost/Taller_2/act_2/index.php'); #arreglar url para github
}

$nombre = $_POST['nombre'];
$sexo = $_POST['sexo'];
$year = $_POST['year'];
$terminos = $_POST['terminos'];

echo '<br>' .'Hola, ' . $nombre . ' eres ' , $sexo;


#Validación con Get
// print_r($_GET);

// if (!$_GET) {
//     header('Location: http://localhost/Taller_2/act_2/index.php'); #arreglar url para github
// }

// $nombre = $_POST['nombre'];
// $sexo = $_POST['sexo'];
// $year = $_POST['year'];
// $nombre = $_POST['terminos'];

// $valNombre = $nombre ? $nombre . '<br>' : 'Usuario Desconocido';

// echo $valNombre . '<br>';
// echo $sexo . '<br>';
// echo $year . '<br>';
// echo $terminos . '<br>';

?>