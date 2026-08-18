<?php

for ($contador = 0; $contador <= 10; $contador += 1):
    echo "O contador é $contador<br>";
endfor;

echo "<hr>";

$cores = array("verde", "vermelho", "azul");

foreach($cores as $indice => $valor):
    echo  $indice." - ".$valor."<br>";
endforeach;