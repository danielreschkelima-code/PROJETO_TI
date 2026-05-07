/*
Peça um número inteiro.
Mostre a tabuada de multiplicação desse número de 1 a 10.
*/

const readline = require("readline-sync");

//Entrada

const numero = readline.questionInt("Digite qualquer número inteiro: ");

//Processamento e saída
console.log(`\nTabuada do número ${numero}:`);

for (let i = 1; i<= 10; i++){
    console.log(`${numero} X ${i} = ${numero*i}`);
}