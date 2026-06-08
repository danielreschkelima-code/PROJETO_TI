import java.util.ArrayList;
import java.util.List;

public class Arraylist {
    
    public static void main(String[] args) {
        List<User> users = new ArrayList<>();

        for(int i = 0; i < 10; i++) {
            User actual = new User("Nome" + i, "Sobrenome" + i);
            users.add(actual);
        }
        System.out.println();
        System.out.println(users.get(9).GetNomeCompleto());
        System.out.println(users.get(8).GetNomeCompleto());
        System.out.println(users.get(8).toString()); // sobreescrevendo o método toString().
        System.out.println(User.getContagemUsuarios()); // vendo quantos usuários existem com static.
        System.out.println();
    }
}