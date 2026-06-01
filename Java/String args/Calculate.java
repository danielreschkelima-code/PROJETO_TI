public class Calculate {
    public static void main(String[] args) { // quando o código é executado pelo cmd, as váriaveis após o comando separadas por um espaço ficam contidas no array args[].
        if("a".equals(args[0])) {
            System.out.println(Double.parseDouble(args[1]) + Double.parseDouble(args[2]));
        } else if("s".equals(args[0])) {
            System.out.println(Double.parseDouble(args[1]) - Double.parseDouble(args[2]));
        } else if("m".equals(args[0])) {
            System.out.println(Double.parseDouble(args[1]) * Double.parseDouble(args[2]));
        } else if("d".equals(args[0])) {
            System.out.println(Double.parseDouble(args[1]) / Double.parseDouble(args[2]));
        } else {
            System.out.println("Erro: operacao invalida!");
        }
    }
}