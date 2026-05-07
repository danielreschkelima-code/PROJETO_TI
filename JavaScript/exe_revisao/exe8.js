/*
Exercício 8 – Soma até zero Peça números até o usuário digitar 0. 
Some todos e mostre o total. 
*/

const readline = require('readline-sync');

let soma = 0;
let numero;

// Entrada + processamento
while (true) {
    numero = readline.questionFloat("Digite um número (0 para sair): ");
    
    if (numero === 0) {
        break;
    }

    soma += numero;
}

// Saída
console.log(`Soma total: ${soma}`);


/*
Usando do while:

const readline = require('readline-sync');

let soma = 0;
let numero;

do {
    numero = readline.questionFloat("Digite um número (0 para sair): ");
    soma += numero;
} while (numero !== 0);

console.log(`Soma total: ${soma}`);


*/