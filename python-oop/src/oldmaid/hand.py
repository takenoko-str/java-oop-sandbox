import random as rm

class Hand():

    # card クラスをリストとして保持
    def __init__(self,list):
        self.hand = list

    # カードを追加
    def add_card(self,card):
        self.hand.append(card)

    # カードを引く（先頭）
    def pick_card(self):
        picked_card = self.hand.pop(0)
        return picked_card

    # 所持枚数を返す
    def getNumberOfCard(self):
        return len(self.hand)

    # 手札をシャッフル
    def shuffle(self):
        # カードをランダムに抜き取って最後に加える動作を繰り返す
        number = self.getNumberOfCard()
        for i in range(number):
            pos = int(rm.random() * number)
            picked_card = self.hand.pop(pos)
            self.hand.append(picked_card)

    # 同じ数のカードを探し、配列で戻す
    def find_same_number_card(self):

        same_cards = None

        # 最後に追加されたカードの数字を取得する
        last_added_card = self.hand[-1]
        last_added_card_num = last_added_card.number

        for index in range(len(self.hand)-1):

            card = self.hand[index]
            if card.number == last_added_card_num:

                # 最後に追加されたカードと同じカードが見つかった場合
                # 見つかった組み合わせをsameCardsに格納し、ループを抜ける
                same_cards = [self.hand.pop(-1),self.hand.pop(index)]
                break

        return same_cards

    # 手札にあるカードを文字列で表現する。
    def toString(self):
        hand_cards = ""
        for card in self.hand:
            hand_cards += card.toString() + " "
        return hand_cards
