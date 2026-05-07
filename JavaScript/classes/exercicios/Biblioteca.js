console.log();

class Livro {
    constructor (titulo, autor){
        this.titulo = titulo;
        this.autor = autor;
        this.emprestado = false;
    }
}

class Emprestimo {
    constructor(Usuario, Livro){
        if (!Livro.emprestado) {
            this.Usario = Usuario;
            this.Livro = Livro;
            this.dataEmprestimo = new Date();
            this.dataDevolução = null;
            Livro.emprestado = true;
            Usuario.emprestimos.push(this.titulo);
        
        } else {
            console.log(`ERRO: O livro ${Livro.titulo} já foi emprestado por ${Usuario.nome}.`);
        }
    }
    devolver() {
        this.dataDevolução = new Date();
        this.Livro.emprestado = false;
        this.Usuario.emprestimos.splice((this.Usuario.emprestimos.indexOf(this.titulo)), 1);
        console.log(`${this.Livro.titulo} devolvido!`);
    }
}

class Usuario {
    constructor(nome){
        this.nome = nome;
        this.emprestimos = [];
    }
}

const livro1 = new Livro ("Jogos Vorazes", "Suzanne Collis");
const livro2 = new Livro ("Em chamas", "Suzanne Collis");

const Daniel = new Usuario ("Daniel");

const emprestimo1 = new Emprestimo (Daniel, livro1);
const emprestimo2 = new Emprestimo (Daniel, livro1);
const emprestimo3 = new Emprestimo (Daniel, livro2);

console.log();
emprestimo1.devolver();
console.log();

console.log(Daniel.emprestimos);

console.log();