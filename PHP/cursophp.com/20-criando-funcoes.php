<?php

function exibirNome($nome) {
    echo "Meu nome é $nome";
}

exibirNome("Daniel");

echo "<hr>";

function calcularMedia($notas) {
    echo array_sum($notas)/count($notas); 
}

calcularMedia([10, 2, 5]);