
<?php 

include 'includes/header.php'; //incluir el contenido de otros archivos

//Formas de hacer print en php
echo 'Hola mundo con codigo PHP';
echo("hola mundo 2");
print("hola mundo 3");
print_r("hola mundo 4");
var_dump("Hola mundo con var_dump");

$nombre = "juan"; //Crear una variable 
echo($nombre);
echo gettype($nombre);

//Formas de crear una constante
define('rol','instructor'); 
echo(rol);
const gravedad = '9.8';
echo gravedad;

$dia = date('d');
echo "el dia de hoy es $dia";

$array = []; //crear un array
var_dump(($array));

//operadores

$a = 3;
$b = 5;

echo($a + $b . "<br/>"); //? . forma de concatenar?
echo($a - $b . "<br/>");
echo($a * $b . "<br/>");
echo($a / $b . "<br/>");
echo($a % $b . "<br/>");
echo($a ** $b . "<br/>");

//operadores: = , ==, ===, !=, <> (diferente), >, >=, <, <=

//Condicionales

if ($dia > 20){ //Forma tradicional
    echo "falta poco para que termine el mes";
} else {
    echo "No falta poco para que termine el mes";
}

$faltaPoco = $dia > 20 ? "falta poco para que termine el mes" : "No falta poco para que termine el mes"; //condicional ternario
echo $faltaPoco;

//funcion random
$azar = rand(1, 10);
echo $azar;

$a++; //aumentar 1
echo $a;

$b--; //decrementar 1
echo $b;

$a += 4; //aumentar / decrementar 
echo $a;

//*Funciones para strings

$nombre = "    Maria Paula Buenaventura Garcia    ";
echo("<br/>");
echo(strlen($nombre)); //Saber cantidad de caracteres (incluido espacios)

echo("<br/>");
$nuevoNombre = trim($nombre); //quitar espacios de los lados 
echo($nuevoNombre);

echo("<br/>");
echo(strtoupper($nombre)); //convierte texto a mayuscula
echo("<br/>");
echo(strtolower($nombre)); //convierte texto a minuscula

echo("<br/>");
var_dump(strtoupper($nombre)==strtolower($nombre));

echo("<br/>");
$nombre = str_replace('Maria Paula', 'Paula Maria', $nombre); //reemplaza el contenido que coincide con el primer parametro con el segundo parametro
echo $nombre;

echo("<br/>");
var_dump(strpos($nombre, 'aul')); //encuentra la posicion numerica de el parametro 2, si no existe, devuelve false

echo("<br/>");
echo "mi nombre es " . $nombre . "tengo " . $azar . " años";  //forma de concatenar en php


//*Arrays

//formas de hacerlos
$carrito = [];
$semana = array("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo");

echo("<br/>");
echo($semana[0]."</br>");
echo($semana[1]."</br>");
echo($semana[2]."</br>");
echo($semana[3]."</br>");
echo($semana[4]."</br>");
echo($semana[5]."</br>");
echo($semana[6]."</br>");

echo("<br/>");
$carrito[1] = "circulo"; //añadir un elemento a una posición especifica
echo $carrito[1];

echo "<pre>";
array_push($carrito, "triangulo"); //añadir un elemento al final del array
echo $carrito[2];
echo "</pre>";


echo "<pre>";
array_unshift($carrito, "cuadrado"); //añadir un elemento al principio del array
echo $carrito[0];
echo "</pre>";

echo("<br/>");
var_dump($carrito);


//?Recorrer un array con forEach

echo("<br/>");
foreach($semana as $nombreDia) {
    echo $nombreDia . "</br>";
}


//*Diccionarios / objetos 

$numeros = ['one'=>'uno','two'=>'dos','three'=>'tres' ]; //creacion de objetos 
$numeros2 = array('one'=>'uno','two'=>'dos','one'=>'uno');

echo("<br/>");
echo($numeros['one'] . "</br>"); //acceder a objetos por clave


//?Arreglos multidimencionales

$multi = array(
    array('Juan', 34, 'Ingeniero', '12/11/1989', 1200000),
    array('Pedro', 22, '01/05/2001'),
    array('Ana', 21, array(2, 'O+'))
);

echo("<br/>");
echo "la edad de nacimiento de " . $multi[1][0] . " es " . $multi[1][2];
echo("<br/>");
echo $multi[0][0] . " es " . $multi[0][2];
echo("<br/>");
echo "El rh de Ana es " . $multi[2][2][1];

$juan = array('Juan', 34, 'Ingeniero', '12/11/1989', 1200000);
$vacio = array();

//revisa si un array esta vacio
echo("<br/>");
var_dump(empty($juan));
echo("<br/>");
var_dump(empty($vacio));

//revisa si un array existe o ha sido creado
echo("<br/>");
var_dump(isset($juan));
echo("<br/>");
var_dump(isset($lleno));
echo("<br/>");
var_dump(isset($numeros['one'])); //revisa si una propiedad de un array asociativo esta definida

echo("<br/>");
echo("<br/>");
var_dump(in_array(34,$juan)); //comprueba si un elemento esta en un array

rsort($juan); //ordenar de manera descendente
sort($juan); //ordenar de manera ascendente

?>