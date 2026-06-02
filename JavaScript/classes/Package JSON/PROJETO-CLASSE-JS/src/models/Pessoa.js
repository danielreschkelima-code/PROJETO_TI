export default class Pessoa {
    constructor(nome, idade, endereco) {
        this.nome = nome;
        this.idade = idade;
        this.endereco = endereco;
    }
    apresentarPessoa() {
        return `${this.nome}, ${this.idade}, mora em ${this.endereco.apresentarEndereco()}`;
    }
    apresentarCidade() {
        return `${this.nome} mora em ${this.endereco.cidade}`
    }
}