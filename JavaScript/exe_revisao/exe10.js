/*
Menu Interativo
Crie um menu:
1 - Somar
2 - Subtrair
3 - Sair
Use while para repetir até escolher sair
*/
const readline = require("readline-sync");
console.log("\n----------------- MENU INTERATIVO -----------------");

let escolha;
while (escolha !== "3"){
    escolha = readline.question("\nDigite:\n1 - Somar\n2 - Subtrair\n3 - Sair\n>>> ");
    
    if (escolha === "1" || escolha === "2"){
        let n1 = readline.questionFloat("\nDigite o valor do primeiro número: ");
        let n2 = readline.questionFloat("Digite o valor do segundo número: ");
        if (escolha === "1"){
            console.log(`\nSOMA = ${(n1+n2).toFixed(2)}`);
        } else{
            console.log(`\nSUBTRAÇÃO = ${(n1-n2).toFixed(2)}`);
        }

    } else if (escolha === "3"){
        console.log("\nEncerrando o programa...\n");
        escolha = "3";

    } else{
        console.log("\nComando inválido!\n");
    }
}