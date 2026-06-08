public class User {
    
    public String nome;
    public String sobrenome;
    private String nomeCompleto;
    
    private static int contagemUsuarios = 0; // static é atributo da junção de todos os objetos da classe.
    // Static é uma variável da classe.

    //CONSTRUCTOR
    public User(String nome, String sobrenome) {
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.nomeCompleto = nome + " " + sobrenome;
        contagemUsuarios = contagemUsuarios + 1; // cada usuário adiciona 1 na contagem de usuários.
    }

    public static int getContagemUsuarios() {
        return contagemUsuarios;
    }

    public void SetNomeCompleto(String nomeCompleto) {
        this.nomeCompleto = nomeCompleto.toUpperCase();
    }

    public String GetNomeCompleto() {
        return this.nomeCompleto;
    }

    @Override
    public String toString() { // sobreescrevendo o método toString().
        return "User {" + "firstname=" + this.nome + ", " + "lastname=" + this.sobrenome + "}"; 
    }
}