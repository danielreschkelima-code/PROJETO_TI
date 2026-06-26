import Button from "./evento/Button";

function Evento({ numero }) {

    function meuEvento() {
        console.log("Evento ativado de nº ", {numero});
    }

    return (
        <div>
            <p>Clique para disparar um evento: </p>
            <Button event={meuEvento} text="Primeiro Evento"/>
            <button onClick={meuEvento}>Ativar!</button>
        </div>
    );
}
export default Evento;