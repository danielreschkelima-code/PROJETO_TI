/* 
Peça números até o usuário digitar 0.
Some todos e mostre o total.
(Usar while)
*/

const readline = require("readline-sync");

//Entrada e processamento
console.log("\nDigite qualquer número para incluir no somatório. Ou digite 0 para encerrar e imprimir o resultado.\n");
let somatorio = 0;
while (true){
    let numero = readline.questionFloat("Digite um número: ");
    if(numero === 0){
        break;
    } 
    else{
        somatorio += numero;
    }
}

console.log(`\nSOMATÓRIO = ${somatorio.toFixed(2)}`);