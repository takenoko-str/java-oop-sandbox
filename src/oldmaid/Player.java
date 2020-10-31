package oldmaid;

import java.awt.font.MultipleMaster;

public class Player {
    private Master master_;
    private Table table_;
    private Hand myHand_ = new Hand();

    private String name_;

    public Player(String name, Master master, Table table) {
        this.name_ = name;
        this.master_ = master;
        this.table_ = table;
    }

    public void play(Player nextPlayer) {
        Hand nextHand = nextPlayer.showHand();
        Card pickedCard = nextHand.pickCard();
        System.out.println(this + ":" + nextPlayer + "さんから" + pickedCard + "を引きました");

        dealCard(pickedCard);

        if (myHand_.getNumberOfCards() == 0) {
            master_.declareWin(this);
        }
        else {
            System.out.println(this + ":残りの手札は" + myHand_ + "です");
        }
    }

    public Hand showHand() {
        if (myHand_.getNumberOfCards() == 1) {
            master_.declareWin(this);
        }
        myHand_.shuffle();

        return myHand_;
    }

    public void receiveCard(Card card) {
        dealCard(card);
    }

    private void dealCard(Card card) {
        myHand_.addCard(card);

        Card[] sameCards = myHand_.findSameNumberCard();

        if (sameCards != null) {
            System.out.print(this + ":");
            table_.disposeCard(sameCards);
        }
    }

    public String toString() {
        return name_;
    }
}
