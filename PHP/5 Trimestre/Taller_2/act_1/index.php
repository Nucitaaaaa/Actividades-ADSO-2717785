
<?php
//Primera linea
$equipo1_1 = [280,150,195,270,190];
$equipo2_1 = [190,90,101,112,98];
$equipo3_1 = [145,167,189,198,80];

//Segunda linea
$equipo1_2 = [101,198,165,145,178];
$equipo2_2 = [123,189,210,250,202];
$equipo3_2 = [110,90,115,190,120];

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Actividad 1 Taller 2</title>
</head>
<body>
    <h2>Tabla de puntuaciones</h2>
    <h3>Primera linea</h3>
    <br>
    <table>
        <thead>
            <th>------</th>
            <th>Jugador 1</th>
            <th>Jugador 2</th>
            <th>Jugador 3</th>
            <th>Jugador 4</th>
            <th>Jugador 5</th>
        </thead>
        <tbody>
            <tr>
                <th>Equipo 1</th>
                <?php
                foreach($equipo1_1 as $jugador){
                    echo '<td>'. $jugador . '</td>';
                }
                ?>
            </tr>
            <tr>
                <th>Equipo 2</th>
                <?php
                foreach($equipo2_1 as $jugador){
                    echo '<td>'. $jugador . '</td>';
                }
                ?>
            </tr>
            <tr>
                <th>Equipo 3</th>
                <?php
                foreach($equipo3_1 as $jugador){
                    echo '<td>'. $jugador . '</td>';
                }
                ?>
            </tr>
        </tbody>
    </table>
    <br>
    <h3>Segunda linea</h3>
    <br>
    <table>
        <thead>
            <th>------</th>
            <th>Jugador 1</th>
            <th>Jugador 2</th>
            <th>Jugador 3</th>
            <th>Jugador 4</th>
            <th>Jugador 5</th>
        </thead>
        <tbody>
            <tr>
                <th>Equipo 1</th>
                <?php
                foreach($equipo1_2 as $jugador){
                    echo '<td>'. $jugador . '</td>';
                }
                ?>
            </tr>
            <tr>
                <th>Equipo 2</th>
                <?php
                foreach($equipo2_2 as $jugador){
                    echo '<td>'. $jugador . '</td>';
                }
                ?>
            </tr>
            <tr>
                <th>Equipo 3</th>
                <?php
                foreach($equipo3_2 as $jugador){
                    echo '<td>'. $jugador . '</td>';
                }
                ?>
            </tr>
        </tbody>
    </table>
    <br>
    <h3>Actividad</h3>
    <?php
    //1

    $prom = 0;
    $count = 0;
    $puntuaciones = array_merge($equipo1_1, $equipo1_2);
    foreach($puntuaciones as $puntuacion){
        $prom += $puntuacion;
        $count++;
    }
    echo '<p>' . '1. Promedio del equipo 1: ' . $prom / $count . '</p>'
    ?>
    <br>
    <?php
    //2

    $sum = 0;
    $puntuaciones = array_merge($equipo3_1, $equipo3_2);
    foreach($puntuaciones as $puntuacion){
        $sum += $puntuacion;
    }
    echo '<p>' . '2. Suma de puntos del equipo 3: ' . $sum . '</p>'
    ?>
    <br>
    <?php
    //3

    unset($equipo2_1[3]);
    unset($equipo2_2[3]);
    
    $promedio1 = array_sum($equipo2_1) / count($equipo2_1);
    $promedio2 = array_sum($equipo2_2) / count($equipo2_2);

    $promedio = ($promedio1 + $promedio2) / 2;

    echo '<p>3. Promedio del Equipo 2 sin contar el jugador 4: ' . $promedio . '</p>';
    ?>
    <br>
    <?php
    //4

    $sum = 0;
    $puntuaciones = [$equipo1_1[1], $equipo1_2[1], $equipo2_1[1], $equipo2_2[1], $equipo3_1[1], $equipo3_2[1]];
    foreach($puntuaciones as $puntuacion){
        $sum += $puntuacion;
    }
    echo '<p>' . '4. Suma de puntos jugadores 2: ' . $sum . '</p>'
    ?>
    <br>
    <?php
    //5
    $jugador = 0;
    $equipo = 0;
    $puntuacionMayor = 0;
    foreach($equipo1_1 as $key => $puntuacionJugador){
        if($puntuacionJugador > $puntuacionMayor){
            $jugador = $key + 1;
            $equipo = 1;
            $puntuacionMayor = $puntuacionJugador;
        }
    }
    foreach($equipo2_1 as $key => $puntuacionJugador){
        if($puntuacionJugador > $puntuacionMayor){
            $jugador = $key + 1;
            $equipo = 2;
            $puntuacionMayor = $puntuacionJugador;
        }
    }
    foreach($equipo3_1 as $key => $puntuacionJugador){
        if($puntuacionJugador > $puntuacionMayor){
            $jugador = $key + 1;
            $equipo = 3;
            $puntuacionMayor = $puntuacionJugador;
        }
    }
    echo '<p>' . '5. Puntuación del mejor jugador de la primera linea : ' . 'Jugador ' . $jugador . ' con ' . $puntuacionMayor . ' puntos' . ' del equipo '. $equipo . '</p>'
    ?>
    <br>
    <?php
    //6
    $jugador = 0;
    $equipo = 0;
    $puntuacionMayor = 0;
    foreach($equipo1_2 as $key => $puntuacionJugador){
        if($puntuacionJugador > $puntuacionMayor){
            $jugador = $key + 1;
            $equipo = 1;
            $puntuacionMayor = $puntuacionJugador;
        }
    }
    foreach($equipo2_2 as $key => $puntuacionJugador){
        if($puntuacionJugador > $puntuacionMayor){
            $jugador = $key + 1;
            $equipo = 2;
            $puntuacionMayor = $puntuacionJugador;
        }
    }
    foreach($equipo3_2 as $key => $puntuacionJugador){
        if($puntuacionJugador > $puntuacionMayor){
            $jugador = $key + 1;
            $equipo = 3;
            $puntuacionMayor = $puntuacionJugador;
        }
    }
    echo '<p>' . '6. Puntuación del mejor jugador de la segunda linea : ' . 'Jugador ' . $jugador . ' con ' . $puntuacionMayor . ' puntos' . ' del equipo '. $equipo . '</p>'
    ?>
    <br>
    <?php
    //7
    function jugadorGanador($equipos1, $equipos2) {
        $jugadorGanador = ['equipo' => 0, 'jugador' => 0, 'puntuacion' => 0];
    
        foreach ($equipos1 as $equipo => $jugadores) {
            foreach ($jugadores as $index => $puntuacion) {
                if ($puntuacion > $jugadorGanador['puntuacion']) {
                    $jugadorGanador = ['equipo' => $equipo + 1, 'jugador' => $index + 1, 'puntuacion' => $puntuacion];
                }
            }
        }
    
        foreach ($equipos2 as $equipo => $jugadores) {
            foreach ($jugadores as $index => $puntuacion) {
                if ($puntuacion > $jugadorGanador['puntuacion']) {
                    $jugadorGanador = ['equipo' => $equipo + 1, 'jugador' => $index + 1, 'puntuacion' => $puntuacion];
                }
            }
        }
    
        return $jugadorGanador;
    }
    
    $jugadorGanador = jugadorGanador([$equipo1_1, $equipo2_1, $equipo3_1], [$equipo1_2, $equipo2_2, $equipo3_2]);
    echo '<p>7. Jugador ganador del torneo: Jugador ' . $jugadorGanador['jugador'] . ' del equipo ' . $jugadorGanador['equipo'] . ' con puntuación de ' . $jugadorGanador['puntuacion'] . '</p>';
    ?>
    <br>
    <?php
    //8
    $equipo = 0;
    $equipo1 = array_merge($equipo1_1, $equipo1_2);
    $equipo2 = array_merge($equipo2_1, $equipo2_2);
    $equipo3 = array_merge($equipo3_1, $equipo3_2);
    $puntuacionEquipo1 = 0;
    $puntuacionEquipo2 = 0;
    $puntuacionEquipo3 = 0;

    foreach($equipo1 as $puntuacion){
        $puntuacionEquipo1 += $puntuacion;
    }

    foreach($equipo2 as $puntuacion){
        $puntuacionEquipo2 += $puntuacion;
    }

    foreach($equipo3 as $puntuacion){
        $puntuacionEquipo3 += $puntuacion;
    }

    if($puntuacionEquipo1 > $puntuacionEquipo2 && $puntuacionEquipo1 > $puntuacionEquipo3){
        $equipo = 1;
        echo '<p>' . '8. Equipo ganador del torneo: Equipo ' . $equipo . ' con '. $puntuacionEquipo1 . ' puntos' .'</p>';
    }
    else if($puntuacionEquipo2 > $puntuacionEquipo1 && $puntuacionEquipo2 > $puntuacionEquipo3){
        $equipo = 2;
        echo '<p>' . '8. Equipo ganador del torneo: Equipo ' . $equipo . ' con '. $puntuacionEquipo2 . ' puntos' .'</p>';
    }
    else {
        $equipo = 3;
        echo '<p>' . '8. Equipo ganador del torneo: Equipo ' . $equipo . ' con '. $puntuacionEquipo3 . ' puntos' .'</p>';
    }

    ?>
    <br>
    <?php
    //9
    $equipo = 0;
    $puntuacionEquipo1 = 0;
    $puntuacionEquipo2 = 0;
    $puntuacionEquipo3 = 0;

    foreach($equipo1_2 as $puntuacion){
        $puntuacionEquipo1 += $puntuacion;
    }

    foreach($equipo2_2 as $puntuacion){
        $puntuacionEquipo2 += $puntuacion;
    }

    foreach($equipo3_2  as $puntuacion){
        $puntuacionEquipo3 += $puntuacion;
    }

    if($puntuacionEquipo1 < $puntuacionEquipo2 && $puntuacionEquipo1 < $puntuacionEquipo3){
        $equipo = 1;
        echo '<p>' . '9. Equipo con menos puntos de la segunda linea: Equipo ' . $equipo . ' con '. $puntuacionEquipo1 . ' puntos' .'</p>';
    }
    else if($puntuacionEquipo2 < $puntuacionEquipo1 && $puntuacionEquipo2 < $puntuacionEquipo3){
        $equipo = 2;
        echo '<p>' . '9. Equipo con menos puntos de la segunda linea: Equipo ' . $equipo . ' con '. $puntuacionEquipo2 . ' puntos' .'</p>';
    }
    else {
        $equipo = 3;
        echo '<p>' . '9. Equipo con menos puntos de la segunda linea: Equipo ' . $equipo . ' con '. $puntuacionEquipo3 . ' puntos' .'</p>';
    }

    ?>
    <br>
    <?php
    //10
    $equipo = 0;
    $puntuacionEquipo1 = 0;
    $puntuacionEquipo2 = 0;
    $puntuacionEquipo3 = 0;

    foreach($equipo1_1 as $puntuacion){
        $puntuacionEquipo1 += $puntuacion;
    }

    foreach($equipo2_1 as $puntuacion){
        $puntuacionEquipo2 += $puntuacion;
    }

    foreach($equipo3_1  as $puntuacion){
        $puntuacionEquipo3 += $puntuacion;
    }

    if($puntuacionEquipo1 < $puntuacionEquipo2 && $puntuacionEquipo1 < $puntuacionEquipo3){
        $equipo = 1;
        echo '<p>' . '10. Equipo con menos puntos de la primera linea: Equipo ' . $equipo . ' con '. $puntuacionEquipo1 . ' puntos' .'</p>';
    }
    else if($puntuacionEquipo2 < $puntuacionEquipo1 && $puntuacionEquipo2 < $puntuacionEquipo3){
        $equipo = 2;
        echo '<p>' . '10. Equipo con menos puntos de la primera linea: Equipo ' . $equipo . ' con '. $puntuacionEquipo2 . ' puntos' .'</p>';
    }
    else {
        $equipo = 3;
        echo '<p>' . '10. Equipo con menos puntos de la primera linea: Equipo ' . $equipo . ' con '. $puntuacionEquipo3 . ' puntos' .'</p>';
    }

    ?>
    <br>
    <?php
    //11
    $jugadores = [];
    $equipoJugadores = [];

    foreach($equipo1_1 as $key => $puntuacionJugador){
        if($puntuacionJugador > 200){
            $jugador = $key + 1;
            array_push($jugadores, $jugador);
            $equipo = 1;
            array_push($equipoJugadores, $equipo);
        }
    }
    foreach($equipo2_1 as $key => $puntuacionJugador){
        if($puntuacionJugador > 200){
            $jugador = $key + 1;
            array_push($jugadores, $jugador);
            $equipo = 2;
            array_push($equipoJugadores, $equipo);
        }
    }
    foreach($equipo3_1 as $key => $puntuacionJugador){
        if($puntuacionJugador > 200){
            $jugador = $key + 1;
            array_push($jugadores, $jugador);
            $equipo = 3;
            array_push($equipoJugadores, $equipo);
        }
    }
    echo '<p>' . '11. Jugadores de la primera linea con mas de 200 puntos : ';
    
    foreach($jugadores as $index => $jugador) {
        $equipo = $equipoJugadores[$index];
        echo '<p>- Jugador ' . $jugador . ' del equipo ' . $equipo . '</p>';
    }

    ?>
    <br>
    <?php
    //12
    $jugadores = [];
    $equipoJugadores = [];

    foreach($equipo1_2 as $key => $puntuacionJugador){
        if($puntuacionJugador > 100 && $puntuacionJugador < 150){
            $jugador = $key + 1;
            array_push($jugadores, $jugador);
            $equipo = 1;
            array_push($equipoJugadores, $equipo);
        }
    }
    foreach($equipo2_2 as $key => $puntuacionJugador){
        if($puntuacionJugador > 100 && $puntuacionJugador < 150){
            $jugador = $key + 1;
            array_push($jugadores, $jugador);
            $equipo = 2;
            array_push($equipoJugadores, $equipo);
        }
    }
    foreach($equipo3_2 as $key => $puntuacionJugador){
        if($puntuacionJugador > 100 && $puntuacionJugador < 150){
            $jugador = $key + 1;
            array_push($jugadores, $jugador);
            $equipo = 3;
            array_push($equipoJugadores, $equipo);
        }
    }
    echo '<p>' . '12. Jugadores de la segunda linea con puntuacion entre 100 y 150 : ';
    
    foreach($jugadores as $index => $jugador) {
        $equipo = $equipoJugadores[$index];
        echo '<p>- Jugador ' . $jugador . ' del equipo ' . $equipo . '</p>';
    }

    ?>
    <br>
    <?php 
    function ordenarPrimeraLinea($equipo1, $equipo2, $equipo3) {
        $jugadores = [];
        $equipos = ['equipo1' => $equipo1, 'equipo2' => $equipo2, 'equipo3' => $equipo3];
    
        foreach ($equipos as $equipo => $puntuaciones) {
            foreach ($puntuaciones as $index => $puntuacion) {
                $jugadores[] = ['equipo' => $equipo, 'jugador' => $index + 1, 'puntuacion' => $puntuacion];
            }
        }
    
        usort($jugadores, function($a, $b) {
            return $b['puntuacion'] <=> $a['puntuacion'];
        });
    
        return $jugadores;
    }
    
    $jugadoresOrdenados = ordenarPrimeraLinea($equipo1_1, $equipo2_1, $equipo3_1);
    echo '<p>13. Orden de la primera línea de mayor a menor:</p>';
    foreach ($jugadoresOrdenados as $jugador) {
        echo '<p>' . $jugador['equipo'] . ' - Jugador ' . $jugador['jugador'] . ' con puntuación ' . $jugador['puntuacion'] . '</p>';
    }
    ?>
</body>
</html>