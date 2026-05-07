class Aluno{
    constructor(nome, matricula, nota){
        this.nome =  nome;
        this.matricula = matricula;
        this.nota = nota;
    }
    apresentar(){
        console.log(`\nOlá, meu nome é ${this.nome} e minha matrícula é ${this.matricula}.`);
    }
    situcao(){
        if (this.nota >= 6 && this.nota <= 10){
            console.log(`${this.nome} está APROVADO!`);
        } else if(this.nota < 6){
            console.log(`${this.nome} está REPROVADO!`);
        } else {
            console.log(`A nota ${this.nota} é inválida, pois não está entre 0 e 10.`);
        }
    }
}

const Daniel = new Aluno("Daniel", "2024", 4);
const Larissa = new Aluno("Larika", "Burra", 0)

Daniel.apresentar();
Daniel.situcao();

Larissa.apresentar();
Larissa.situcao();

console.log()