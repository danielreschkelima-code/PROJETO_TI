<?php
// Constantes
define("NOME", "Daniel"); // função que define constantes. Geralmente const em letra maíuscula. Elas são naturalmente globais.
define("IDADE", 18);
define("ALTURA", 1.74);
define("CASADO", true);

define("FRUTAS", ['Banana', 'Bergamota', 'Morango', 'Maçã']);

echo 'Meu nome é '.NOME.' e minha idade é '.IDADE.' e minha altura é '.ALTURA.' m.';
echo '<hr>';
echo 'Minha fruta favorita é: '.FRUTAS[1].'.';

// Constantes são globais no php
function exibeNome() {
    echo NOME;
}

exibeNome();