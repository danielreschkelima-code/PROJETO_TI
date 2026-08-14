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

// Count
echo count($carros); // = len do python
echo  "<hr>";

// Foreach para percorrer arrays:
foreach($carros as $valor) {
    echo $valor."<br>";
}
echo "<hr>";

// Arrays associativos (dicionários do python)
$pessoa = array("nome"=> "Daniel", "idade"=> 18, "altura"=> 1.74);
$pessoa["cidade"] = "Porto Alegre";

foreach($pessoa as $indice => $valor) {
    echo $indice.":".$valor."<br>";
}
echo "<hr>";

// Array multidimensonal
$biologia = array(
        "plantas"=> array("Camomila", "Babosa", "Pinheiro"),
        "animais"=> array("Cachorro", "Gato", "Coruja"),
        "cogumelos"=> array("Vermelho", "Marrom", "Mágico")
        );
echo $biologia["cogumelos"][2];
echo "<br>";

foreach($biologia["cogumelos"] as $indice => $valor) {
    echo $indice.":".$valor."<br>";
}
echo "<hr>";