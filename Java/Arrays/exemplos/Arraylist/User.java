public class User {
    
    public String nome;
    public String sobrenome;
    private String nomeCompleto;

    //CONSTRUCTOR
    public User(String nome, String sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.nomeCompleto = nome + " " + sobrenome;
    }

    public void SetNomeCompleto(String nomeCompleto) {
        this.nomeCompleto = nomeCompleto.toUpperCase();
    }

    public String GetNomeCompleto() {
        return this.nomeCompleto;
    }
}