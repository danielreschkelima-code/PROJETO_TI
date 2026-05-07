/*
Saudação personalizada:
Peça o nome e a idade do usuário e mostre uma mensagem de saudação.
*/

const readline = require('readline-sync');

//Entrada
const nome = readline.question("Digite seu nome: ");
const idade = parseInt(readline.question("Digite quantos anos você tem: "));

//Saída
console.log("Saudações, " + nome + ", parabéns por ter " + idade + " anos.");