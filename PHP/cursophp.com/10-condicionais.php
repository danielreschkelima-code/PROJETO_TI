<?php
/*
 * Condicionais
 * If
 * Else
 * elseif
*/
$numero = 10;

if ($numero == 10):
    echo "É igual a 10.";
elseif($numero <= 9):
    echo "É menor que 10.";
else:
    echo "É maior que 10.";
endif;
echo "<hr>";

// Operador ternário:
$media = 7;
echo ($media >= 7) ? "Aprovado!" : "Reprovado";

/*
 * Condicionais
 * switch
 * case
*/
$cor = "vermelho";

switch ($cor):
    case "vermelho":
    echo "Sua cor favorita é o vermelho.";
    break;
    
    case "roxo":
    echo "Sua cor favorita é o roxo.";
    break;
    
    case "verde":
    echo "Sua cor favorita é o verde.";
    break;

    default:
    echo "Tu não tem cor favorita.";

endswitch;