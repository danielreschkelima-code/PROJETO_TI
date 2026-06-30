function SeuNome({ setNome }) {
    return (
        <div>
            <label htmlFor="nome">
                Digite o seu nome: 
                <input type="text" placeholder="Digite o seu nome..." name="nome" id="nome" onChange={(e) => setNome(e.target.value)}/>
            </label>
        </div>
    );
}
export default SeuNome;