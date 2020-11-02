class Player():

    def __init__(self,name,hand,master,table):
        self.hand = hand
        self.name = name
        self.master = master
        self.table = table

    # 順番を指名する（自分の番）
    def play(self,next_player):

        # 次のプレイヤーに手札を出してもらう
        next_hand = next_player.show_hand()

        # 相手の手札からカードを一枚引く
        picked_card = next_hand.pick_card()

        # 引いた結果を表示
        print(self.name, "：", next_player.name, "さんから ", picked_card.toString()," を引きました\n")

        # 引いたカードを自分の手札に加え、同じ数のカードがあったら捨てる
        self.deal_card(picked_card)

        # 手札がゼロになったかどうか調べる
        if self.hand.getNumberOfCard() == 0:
            # 進行役に上がりを宣言する
            self.master.declare_win(self)
        else:
            # 現在の手札を表示する
            print(self.name, "：残りの手札は ",self.hand.getNumberOfCard(), "です\n")

    # 手札をシャッフルして見せる
    def show_hand(self):
        if self.hand.getNumberOfCard() == 1:
            self.master.declare_win(self)
        self.hand.shuffle()
        return self.hand

    # カードを受け取る
    def receive_card(self,card):
        self.deal_card(card)

    # 同じカードがあったら捨てる
    def deal_card(self,card):

        # カードを自分の手札に加える
        self.hand.add_card(card)

        # 今加えたカードと同じカードを探す
        same_cards = self.hand.find_same_number_card()

        # 同じカードの組み合わせが存在した場合
        if (same_cards != None):
            # テーブルへカードを捨てる
            self.table.dispose_card(same_cards)

    # プレイヤー名を返す
    def toString(self):
        return self.name
