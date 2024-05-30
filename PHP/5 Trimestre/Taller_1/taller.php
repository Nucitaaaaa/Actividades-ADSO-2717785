
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Taller 1 php</title>
</head>
<body>
    <h1>Taller 1 PHP</h1>
    <h3>Ejercicio 1</h3>
    <?php 
    //1. Cálculo de la serie de Fibonacci hasta un número dado 
    function fibonacci($num){
        $sum = 0;
        $num1 = 0;
        $num2 = 1;

        echo $num1 . "," . $num2 . ",";

        while ($sum < $num){
            $sum = $num1 + $num2;

            if ($sum > $num) {
                break;
            }

            else {
                echo $sum . ",";

                $num1 = $num2;
                $num2 = $sum;
            }
        }

    } fibonacci(10);
    ?>
    <br><br>
    <h3>Ejercicio 2</h3>
    <?php 
    //2. Verificar si un número o una frase es palíndromo 
    function palindromo($word){
        $reversed = strrev($word);

        if($word === $reversed){
            echo $word . " Es un palíndromo" . "<br>";
        }
        else {
            echo $word . " No es un palíndromo" . "<br>";
        }

    } palindromo("121"); palindromo("amor");
    ?>
    <br>

    <h3>Ejercicio 3</h3>
    <?php 
    //3. Calcular la suma de los dígitos de un número 
    function sumarDigitos($num){
        $sum = 0;

        for($i = 0; $i <= strlen($num); $i++){
            $sum += $i;
        }

        echo "La suma de los digitos {$num} es: {$sum}";

    } sumarDigitos(123456789);
    ?>
    <br><br>

    <h3>Ejercicio 4</h3>
    <?php 
    //4. Eliminar elementos duplicados de un arreglo  
    function eliminarDuplicados($arr){
        $newArr = array_unique($arr);

        echo "Array con elementos duplicados: ";
        echo "<pre>";
        print_r($arr);
        echo "</pre>";
        
        echo "Array sin elementos duplicados:";
        echo "<pre>";
        print_r($newArr);
        echo "</pre>";

    } eliminarDuplicados([1,1,2,3,4,5,5,6]);
    ?>
    <br><br>

    <h3>Ejercicio 5</h3>
    <?php 
    //5. Imprimir un patrón de asteriscos  
    function patron($num){

        for($i = 0; $i <= $num; $i++){
            for ($j = 1; $j <= $i; $j++) {
                echo "*";
            }
            echo "<br>";
        }
    } patron(7);
    ?>
    <br><br>

<h3>Ejercicio 6</h3>
<?php 
//6. Crear un arreglo asociativo e imprimir sus claves y valores  
function objeto($obj){

    foreach($obj as $key => $value) {
        echo $key . ": " . $value . "<br>";
    }

} objeto(['apple'=>'manzana', 'grape'=>'uva', 'pineaple'=>'piña']);
?>
<br><br>

<h3>Ejercicio 7</h3>
<?php
//7. Encontrar el producto de los elementos únicos en un arreglo  
function productoElementosUnicos($arr,  $element) {
    $unico = array_unique($arr);
    
    foreach ($unico as $num) {
        $element *= $num;
    }
    
    echo "El resultado es: $element";
}

echo productoElementosUnicos([1, 2, 3, 2, 4, 1], 1); 
?>
<br><br>

<h3>Ejercicio 8</h3>
<?php
//8. Rotar un arreglo a la izquierda y a la derecha 
function rotarIzquierda($arr, $pos) {
    $pos = $pos % count($arr);
    return array_merge(array_slice($arr, $pos), array_slice($arr, 0, $pos));
}

function rotarDerecha($arr, $pos) {
    $pos = $pos % count($arr);
    return array_merge(array_slice($arr, -$pos), array_slice($arr, 0, -$pos));
}

echo "<pre>";
print_r(rotarIzquierda([1, 2, 3, 4, 5], 2)); 
print_r(rotarDerecha([1, 2, 3, 4, 5], 2)); 
echo "</pre>";
?>

</body>
</html>


