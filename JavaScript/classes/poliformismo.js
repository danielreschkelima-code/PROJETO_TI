// poliformismo = mesmo método tem diferentes comportamentos conforme subclasse.
console.log();
class Usuario {
    constructor (nome) {
        this.nome = nome;
    }
    acessarSistema(){
        console.log(`${this.nome} acessa o sistema.`);
    }
}

class Admin extends Usuario{
    acessarSistema(){
        console.log(`${this.nome} acessa o painel de administrador.`);
    }
}

class Aluno extends Usuario{
    acessarSistema(){
        console.log(`${this.nome} acessa o painel do curso.`);
    }
}

class Professor extends Usuario{
    acessarSistema(){
        console.log(`${this.nome} acessa o painel de notas.`);
    }
}

const usuarios = [new Admin("Daniel"), new Aluno("Carlos"), new Professor("Tales")];

for (let usuario of usuarios){
    usuario.acessarSistema();
}

console.log();