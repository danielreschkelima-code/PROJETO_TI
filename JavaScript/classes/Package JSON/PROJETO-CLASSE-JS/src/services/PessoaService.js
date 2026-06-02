//Tem a função de guardar as regras ou ações do sistema.
export default class PessoaService {
    listarPessoas(pessoas) {
        console.log("Lista de Pessoas:");
        pessoas.forEach((pessoa) => {
            console.log(pessoa.apresentarPessoa());
        });
    }
}