<?php
//Variáveis variáveis
$bebida = "refrigerante";

// Deve ser lido como $($bebida = refrigerante) = $refrigerante
$$bebida = "Guárana";

echo $refrigerante; // SAÍDA: Guárana

////////////////////////////////////////////////]

$destino = "cidade";
$$destino = "Porto Alegre"; 

echo $cidade; //SAÍDA: Porto Alegre