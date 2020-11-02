class Player:

    # ジャンケンの手を表す定数
    STONE = 0  # グー
    SCISSORS = 1  # チョキ
    PAPER = 2  # パー

    def __init__(self, name, tactics):
        self.name = name
        self.win_count = 0
        self.tactics = tactics

    # ジャンケンの手を出す。
    def show_hand(self):
        hand = self.tactics.read_tactics()
        return hand

    # 審判から勝敗を聞く。勝ったら、引数 result は true
    def notify_result(self,result):
        if (result):
            self.win_count += 1

    # 自分の勝った回数を答える。
    def get_win_count(self):
        return self.win_count

    # 自分の名前を答える。
    def get_name(self):
        return self.name

# 継承し子クラス作成
class Player_STONE(Player):
    def show_hand(self):
        return self.STONE
