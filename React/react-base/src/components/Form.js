import {useState} from 'react';

function Form() {

    function cadastrarUsuario(e) {
        e.preventDefault();
        console.log("========== Cadastrou o usuário: ==========");
        console.log("\t Nome: ", {name});
        console.log("\t Senha: ", {password});
    }

    const [name, setName] = useState("Usuário não informou o nome");
    const [password, setPassword] = useState();

    return (
        <div>
            <h3>MEU CADASTRO: </h3>
            <form onSubmit={cadastrarUsuario}>
                
                <label htmlFor="nome">
                    Nome:
                    <input type="text" placeholder="Digite o seu nome: " id="nome" name="nome" onChange={(e) => setName(e.target.value)}/>
                </label>
                
                <br></br>
                
                <label htmlFor="senha">
                    Senha:
                    <input type="password" placeholder="Digite a sua senha: " id="senha" name="senha" onChange={(e) => setPassword(e.target.value)}/>
                </label>

                <br></br>

                <label htmlFor="enviar">
                    <input type="submit" placeholder="Enviar!" id="enviar" name="enviar"/>
                </label>

            </form>
        </div>
    );
}
export default Form;