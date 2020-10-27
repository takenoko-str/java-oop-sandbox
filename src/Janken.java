public class Janken {
    public static void main(String[] args) {
        Judge saito = new Judge();
        Player murata = new Player("murata");
        Player yamada = new Player("yamada");
        saito.startJanken(murata, yamada);
    }
}
