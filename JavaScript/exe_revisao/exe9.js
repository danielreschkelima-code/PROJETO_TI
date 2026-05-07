/*
Exercício 9 – Login com tentativa Usuário correto: admin Senha correta: 1234 
Permita no máximo 3 tentativas.
*/

const readline = require('readline-sync');

const usuarioCorreto = "admin";
const senhaCorreta = "1234";

let tentativas = 0;
let autenticado = false;

while (tentativas < 3) {

    let usuario = readline.question("Usuário: ");
    let senha = readline.question("Senha: ", { hideEchoBack: true });

    if (usuario === usuarioCorreto && senha === senhaCorreta) {
        console.log("Login realizado com sucesso!");
        autenticado = true;
        break;
    } else {
        console.log("Usuário ou senha incorretos.");
        tentativas++;
        console.log(`Tentativas restantes: ${3 - tentativas}`);
    }
}

if (!autenticado) {
    console.log("Acesso bloqueado. Número máximo de tentativas atingido.");
}