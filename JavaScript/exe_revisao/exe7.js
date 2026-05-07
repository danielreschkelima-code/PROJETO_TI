/*
Login com tentativas
Usuário correto: admin
Senha correta: = 1234
*/

const readline = require("readline-sync");
const usuarioCorreto = "admin";
const senhaCorreta = "1234";

let usuario = null;
let senha = null;

console.log("LOGAR (3 tentativas)\n")
//Entrada

for (let i = 2; i >= 0; i--){
    usuario = readline.question("Digite o nome do usuário: ")
    senha = readline.question("Digite a senha: ", {hideEchoBack: true})
    if(usuario != usuarioCorreto || senha != senhaCorreta){
        console.log("\nSenha ou usuário incorretos.")
        console.log(`Tentativas restantes: ${i}\n`)
    }
    else{
        console.log("\nLogado!")
        break
    }
}