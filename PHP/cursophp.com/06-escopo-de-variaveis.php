<?php
// ESCOPO GLOBAL
$nome = "Daniel";
$a = 1;
$b = 3;
$c = 7;

function exibeNome() {
    global $nome; // puxa a variável $nome do escopo global.
    echo $nome;
}
exibeNome();

echo "<hr>";
////////////////////////////////////////////

function exibeCidade() {
    // ESCOPO LOCAL
    // Para usarmos uma variável que é criada de dentro de uma função fora dela, nós precisamos definir ela como global antes.
    global $cidade;
    $cidade = "Porto Alegre";
}

exibeCidade();
echo $cidade;

echo "<hr>";
////////////////////////////////////////////

function soma() {
    // para somarmos a, b e c dentro dessa função, nós precisamos puxá-los do escopo global para dentro da função com o GLOBALS.
    echo $GLOBALS['a'] + $GLOBALS['b'] + $GLOBALS['c'];
}

soma();