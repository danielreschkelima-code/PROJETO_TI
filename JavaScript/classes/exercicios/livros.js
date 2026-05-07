console.log();

class Livro {
    constructor(titulo, autor, ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
    }
    exibirInfo() {
        console.log(`Livro ${this.titulo} informações:
Nome do autor: ${this.autor}
Ano de lançamento: ${this.ano}`);
    }
}

const livroEstrangeiro = new Livro("Jogos Vorazes", "Suzanne Collins", 2008);
const livroBrasileiro = new Livro("Olhai os lírios do campo", "Erico Veríssimo", 1930);

livroEstrangeiro.exibirInfo();
console.log();
livroBrasileiro.exibirInfo();

console.log();