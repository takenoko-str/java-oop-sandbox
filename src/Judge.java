public class Judge {
    public void startJanken(Player player1, Player player2) {
        System.out.println("first comes lock...\n");
        for (int cnt = 0; cnt < 3; cnt++) {
            System.out.println("No." + (cnt + 1));
            Player winner = JudgeJanken(player1, player2);

            if (winner != null) {
                System.out.println(winner.getName());
            }
            else {
                System.out.println("draw!");
            }
        }
        System.out.println("Janken done.");

        Player finalWinner = judgeFinalWinner(player1, player2);

        if (finalWinner != null) {
            System.out.println(finalWinner.getName() + " wins.");
        }
        else {
            System.out.println("game set, draw!");
        }
    }

    private Player JudgeJanken(Player player1, Player player2) {
        Player winner = null;
        int player1hand = player1.showHand();
        int player2hand = player2.showHand();
        System.out.println(printHand(player1hand) + " vs " + printHand(player2hand));

        if (player1hand == Player.STONE && player2hand == Player.SCISSORS
        || player1hand == Player.SCISSORS && player2hand == Player.PAPER
        || player1hand == Player.PAPER && player2hand == Player.STONE){
            winner = player1;
            player1.notifyResult(true);
        }
        else if (player1hand == Player.STONE && player2hand == Player.PAPER
                || player1hand == Player.SCISSORS && player2hand == Player.STONE
                || player1hand == Player.PAPER && player2hand == Player.SCISSORS) {
            winner = player2;
            player2.notifyResult(true);
        }

        return winner;
    }

    private Player judgeFinalWinner(Player player1, Player player2) {
        Player winner = null;
        int player1WinCount = player1.getWinCount();
        int player2WinCount = player2.getWinCount();
        if (player1WinCount > player2WinCount) {
            winner = player1;
        }
        else if (player1WinCount < player2WinCount) {
            winner = player2;
        }

        return winner;
    }

    private String printHand(int hand) {
        switch (hand) {
            case Player.STONE:
                return "GOOOOO";
            case Player.PAPER:
                return "PAAAAA";
            case Player.SCISSORS:
                return "CHOOOO";
            default:
                return "ERROR";
        }
    }
}
