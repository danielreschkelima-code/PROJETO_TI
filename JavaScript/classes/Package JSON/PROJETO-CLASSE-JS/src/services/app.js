import Endereco from "../models/Endereco.js";
import Pessoa from "../models/Pessoa.js";
import PessoaService from "./PessoaService.js";

const endereco1 = new Endereco("Rua das Flores", 100);
const endereco2 = new Endereco("Avenida Assis Brasil", 250, "Santa Maria");

const pessoa1 = new Pessoa("Ana", 20, endereco1);
const pessoa2 = new Pessoa("Carlos", 25, endereco2);

const pessoas = [pessoa1, pessoa2];

const pessoaService = new PessoaService();

console.log();
pessoaService.listarPessoas(pessoas);

console.log();
console.log("Somente as cidades: ");
console.log(pessoa1.apresentarCidade());
console.log(pessoa2.apresentarCidade());
console.log();