console.log()

class Pessoa{
    constructor(nome, cpf){
        this.nome = nome;
        this.cpf = cpf;
    }
    apresentar(){
        console.log(`Nome: ${this.nome}
CPF: ${this.cpf}`);
    }
}

class Professor extends Pessoa{
    constructor(nome, cpf, disciplina){
        super(nome, cpf);
        this.disciplina = disciplina;
    }
    apresentar(){
        super.apresentar();
        console.log(`Disciplina: ${this.disciplina}
`)
    }
}

class Aluno extends Pessoa{
    constructor(nome, cpf, curso){
        super(nome, cpf);
        this.curso = curso;
    }
    apresentar(){
        super.apresentar();
        console.log(`Curso: ${this.curso}
`)
    }
}

const Daniel = new Aluno("Daniel", 1, "Informática");
Daniel.apresentar();

const Gustavo = new Professor("Gustavo", 2, "Programação");
Gustavo.apresentar();

console.log();