class Table():

    def __init__(self):
        self.disposed_cards = []

    # カードを捨てる。
    def dispose_card(self,dispose_list):
        for card in dispose_list:
            print(f"{card.toString()} を捨てました")
            self.disposed_cards.append(card)

    # 捨てられたカードを文字列で表現する。
    def toString(self):
        disposed_cards = ""
        for card in self.disposed_cards:
            disposed_cards += card.toString() + " "
        return disposed_cards
