package oldmaid;

public class OldMaid {
    public static void main(String args[]) {
        Master master = new Master();
        Table field = new Table();

        Player yamamoto = new Player("山本", master, field);
        Player kamei = new Player("亀井", master, field);
        Player saito = new Player("齊藤", master, field);

        master.registerPlayer(yamamoto);
        master.registerPlayer(kamei);
        master.registerPlayer(saito);

        Hand trump = createTrump();

        master.prepareGame(trump);

        master.startGame();
    }

    private static Hand createTrump() {
        Hand trump = new Hand();

        for (int number = 1; number <= 13; number++) {
            trump.addCard(new Card(Card.SUIT_CLUB, number));
            trump.addCard(new Card(Card.SUIT_DIAMOND, number));
            trump.addCard(new Card(Card.SUIT_HEART, number));
            trump.addCard(new Card(Card.SUIT_SPADE, number));
        }

        trump.addCard(new Card(0, Card.JOKER));

        return trump;
    }
}
