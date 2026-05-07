/* Peça um número
Mostre todos os números de 1 até o valor informado.
Utilize for.
*/

const readline = require("readline-sync");

//Entrada
const numero = readline.questionInt("Digite um número inteiro: ");

//Processamento e saída
for (let i = 1; i <= numero; i++){
    console.log(i);
}
