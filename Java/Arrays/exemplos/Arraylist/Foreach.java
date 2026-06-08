import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Foreach {
    public static void main(String[] args) {
        List<String> names = new ArrayList<>();
        
        names.add("Nome 3");
        names.add("Nome 1");
        names.add("Nome 4");
        names.add("Nome 2");

        Collections.sort(names); // Organiza a lista.

        for(String name : names) { // For each
            System.out.println(name);
        }
    }
}