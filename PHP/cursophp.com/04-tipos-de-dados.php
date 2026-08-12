<?php
/********* Escalares *********/
//string
$nome = "Olá mundo 123 !@#";
var_dump($nome);
if(is_string($nome)):
    echo "É uma string";
else:
    echo "Não é uma string";
endif; //precisa do endif
echo "<hr>";

// int
$idade = 18;
var_dump($idade); // mostra informações da variável
if(is_int($idade)):
    echo "É um inteiro";
else:
    echo "Não é um inteiro";
endif;
echo "<hr>";

$idade = 18;
var_dump($idade); // mostra informações da variável
if(is_int($idade)):
    echo "É um inteiro";
else:
    echo "Não é um inteiro";
endif;
echo "<hr>";

//float
$altura = 18;
var_dump($altura); // mostra informações da variável
if(is_int($altura)):
    echo "É um float";
else:
    echo "Não é um float";
endif;
echo "<hr>";

//boolean
$admin = true;
var_dump($admin); // mostra informações da variável
if(is_int($admin)):
    echo "É um booleano";
else:
    echo "Não é um booleano";
endif;
echo "<hr>";

/************ Compostos *************/
// array
$carros  = array("Gol", "Uno", "Camaro", 12, 20.6, true);
var_dump($carros);
if(is_array($carros)):
    echo "É um array";
else:
    echo "Não é um array";
endif;
echo "<hr>";

// object
class Cliente {
    public $nome;
    public function atribuirNome($nome) {
        $this->$nome = $nome;
    }
}

$cliente = new Cliente();
$cliente->atribuirNome("Rodrigo");
var_dump($cliente);
if(is_object($cliente)):
    echo "É um object";
else:
    echo "Não é um object";
endif;
echo "<hr>";

/************ Compostos *************/
// NULL
$cidade = NULL;
var_dump($cidade);

// Resource