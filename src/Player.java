public class Player {
    public static final int STONE = 0;
    public static final int SCISSORS = 1;
    public static final int PAPER = 2;

    private String name_;

    private int winCount_ = 0;

    public Player(String name) {
        name_ = name;
    }

    public int showHand() {
        int hand = 0;
        double randomNum = Math.random() * 3;
        if (randomNum < 1) {
            hand = STONE;
        }
        else if (randomNum < 2) {
            hand = SCISSORS;
        } else if (randomNum < 3) {
            hand = PAPER;
        }
        return hand;
    }

    public void notifyResult(boolean result) {
        if ( result == true ) {
            winCount_ += 1;
        }
    }

    public String getName() {
        return name_;
    }

    public int getWinCount() {
        return winCount_;
    }
}
