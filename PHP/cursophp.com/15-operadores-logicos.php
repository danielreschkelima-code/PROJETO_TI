<?php
// Operadores lógicos
// Nos permitem fazer comparações entre expressões
// e (&& - and)
// ou (|| - or)
// ou exclusivo (xor)
// negação (!)

$idade = 18;
$nome = "Daniel";

if(($idade == 17) and ($nome == "Daniel")):
    echo "É verdadeiro";
else:
    echo "É falso";
endif;