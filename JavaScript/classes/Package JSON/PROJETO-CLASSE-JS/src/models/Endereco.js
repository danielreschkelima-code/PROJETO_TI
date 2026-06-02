export default class Endereco {
    constructor(rua, numero, cidade="Porto Alegre") {
        this.rua = rua;
        this.numero = numero;
        this.cidade = cidade;
    }
    apresentarEndereco(){
        return `${this.rua}, ${this.numero} - ${this.cidade}`;
    }
}