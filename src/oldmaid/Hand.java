package oldmaid;

import java.util.ArrayList;

public class Hand {
    private ArrayList<Card> hand_ = new ArrayList<>();

    public void addCard(Card card) {
        hand_.add(card);
    }

    public Card pickCard(){
        Card pickedCard = (Card) hand_.remove(0);
        return pickedCard;
    }

    public void shuffle() {
        int number = hand_.size();
        int pos;
        for (int count = 0; count < number * 2; count++) {
            pos = (int) (Math.random() * number);
            Card pickedCard = (Card) hand_.remove(pos);
            hand_.add(pickedCard);
        }
    }

    public int getNumberOfCards() {
        return hand_.size();
    }

    public Card[] findSameNumberCard() {
        int numberOfCards = hand_.size();
        Card[] sameCards = null;

        if (numberOfCards > 0) {
            int lastIndex = numberOfCards -1;
            Card lastAddedCard = (Card) hand_.get(lastIndex);
            int lastAddedCardNum = lastAddedCard.getNumber();

            for (int index = 0; index < lastIndex; index++) {
                Card card = (Card) hand_.get(index);
                if (card.getNumber() == lastAddedCardNum) {
                    sameCards = new Card[2];
                    sameCards[0] = (Card) hand_.remove(lastIndex);
                    sameCards[1] = (Card) hand_.remove(index);
                    break;
                }
            }
        }
        return sameCards;
    }

    public String toString(){
        StringBuffer string = new StringBuffer();
        int size = hand_.size();
        if (size > 0) {
            for (int index = 0; index < size; index++) {
                Card card = (Card) hand_.get(index);
                string.append(card);
                string.append(" ");
            }
        }
        return string.toString();
    }
}
