<?php
// Arrays
$carros = array("Celta", "Chevrlet", 10=>"Fiat"); // dá pra definir os índices, por padrão começam do 0.
print_r($carros); // print_r serve para imprimir arrays. Outros comandos dão erro para IMPRIMIR o array.
echo $carros[1];
echo $carros[10];

// inserindo novos valores:

$carros[] = 'Amarok';
print_r($carros);

$carros[20] = 'Camaro';
print_r($carros);

echo "<br><hr><br>";

// Outro jeito de criar array:

$clientes = ["Rodrigo", "Candida", "Josefina"];
echo $clientes[2];