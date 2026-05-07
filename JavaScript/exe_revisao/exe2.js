/*
Solicite duas notas
Calcule a média
Mostre: Aprovado (>=7), Recuperacao (>=5 e <7)
e Reprovado ( <5)
*/

const readline = require('readline-sync');

//Entrada
while (true){
    var nota1 = readline.questionFloat("Digite o valor da sua primeira nota: ");
    if (nota1 > 10 || nota1 < 0){
        console.log("Por favor, digite uma nota váida entre 0 e 10.");
    }
    else{
        break;
    }r
}
while (true){
    var nota2 = readline.questionFloat("Digite o valor da sua segunda nota: ");
    if (nota2 > 10 || nota2 < 0){
        console.log("Por favor, digite uma nota váida entre 0 e 10.");
    }
    else{
        break;
    }
}

//Processamento
const media = (nota1 + nota2)/2;

//Saída
console.log(`Média: ${media.toFixed(2)}`);

if(media >=7){ 
    console.log("Aprovado");
} 
else if(media >=5){
    console.log("Recuperação");
}
else{
    console.log("Reprovado");
}