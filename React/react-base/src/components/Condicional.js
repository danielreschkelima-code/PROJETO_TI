import { useState } from "react";
function Condicional(props) {

    const [email, setEmail] = useState();
    const [userEmail, setUserEmail] = useState();

    function enviarEmail(e) {
        e.preventDefault();
        setUserEmail(email);
        console.log(userEmail);
    }

    function limparEmail() {
        setUserEmail('');
        console.log("E-mail esvaziado");
    }

    return (
        <div>
            <h3>Cadastre o seu email:</h3>
            <form>
                <label htmlFor="email">
                    Digite o seu email:
                    <input type="email" name="email" id="email" placeholder="E-mail..." onChange={(e) => setEmail(e.target.value)}/>
                </label>

                <br></br>

                <button type="submit" onClick={enviarEmail}>Enviar Email</button>

                {userEmail && (
                    <div> 
                        <p>O email do usuário é: {userEmail}</p>
                        <button onClick={limparEmail}>Limpar Email</button>
                    </div>
                )};
            </form>
        </div>
    );
}
export default Condicional;