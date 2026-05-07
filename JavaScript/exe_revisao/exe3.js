/*
Peça um número inteiro.
Informe se é par ou ímpar.
*/
const readline = require("readline-sync");

//Entrada
let numero = readline.questionInt("Digite um número inteiro: ");

//Saída
if (numero % 2 === 0){
    console.log(`O número ${numero} é primo.`);
}
else{
    console.log(`O número ${numero} é ímpar.`);
}
