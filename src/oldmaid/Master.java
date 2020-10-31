package oldmaid;

import java.util.ArrayList;

public class Master {
    private ArrayList<Player> players_ = new ArrayList<Player>();

    public void prepareGame(Hand cards) {
        System.out.println("【カードを配ります】");
        cards.shuffle();
        int numberOfCards = cards.getNumberOfCards();

        int numberOfPlayers = players_.size();
        System.out.print(cards);

        for (int index = 0; index < numberOfCards; index++) {
            Card card = cards.pickCard();
            Player player = (Player) players_.get(index % numberOfPlayers);
        }
    }

    public void startGame() {
        System.out.println("\n【ババ抜きを開始します】");
        System.out.print(players_.size());

        for (int count = 0; players_.size() > 1; count++) {
            int playerIndex = count % players_.size();
            int nextPlayerIndex = (count + 1) % players_.size();

            Player player = (Player) players_.get(playerIndex);
            Player nextPlayer = (Player) players_.get(nextPlayerIndex);

            System.out.println("\n" + player + "さんの出番です");
            player.play(nextPlayer);
        }
        System.out.println("【ババ抜きを終了しました】");
    }

    public void declareWin(Player winner) {
        System.out.println(winner + "さんが上がりました！");

        players_.remove(players_.indexOf(winner));
        if (players_.size() == 1) {
            Player loser = (Player) players_.get(0);
            System.out.println(loser + "さんの負けです！");
        }
    }

    public void registerPlayer(Player player) {
        players_.add(player);
    }
}
