class Card():

    # ジョーカーを表す定数
    JOKER = 0
    # スペードを表す定数
    SUIT_SPADE = 1
    # ダイヤを表す定数
    SUIT_DIAMOND = 2
    # クラブを表す定数
    SUIT_CLUB = 3
    # ハートを表す定数
    SUIT_HEART = 4

    def __init__(self,suit,number):
        self.suit = suit
        self.number = number

    def getNumber(self):
        return self.number

    # toString関数をオーバーライド
    def toString(self):

        # JOKERの場合
        if self.suit == 0:
            card_code = "JK"

        # JOKER以外のカード
        else:
            suit_dict = {"SUIT_SPADE":"S", "SUIT_DIAMOND":"D",
                         "SUIT_CLUB":"C","SUIT_HEART":"H"}
            number_dict = {1:"A", 2:"2", 3:"3", 4:"4", 5:"5",
                           6:"6", 7:"7", 8:"8", 9:"9", 10:"T", 11:"J", 12:"Q", 13:"K"}
            card_code = suit_dict[self.suit] + number_dict[self.number]

        return card_code
