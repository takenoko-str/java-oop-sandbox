class RandomTactics():

    def read_tactics(self):

        # 0.0以上3.0未満の小数として乱数を得る
        random_num = rm.random()* 3.0
        if (random_num < 1.0):
            hand = Player.STONE
        elif (random_num < 2.0):
            hand = Player.SCISSORS
        elif (random_num < 3.0):
            hand = Player.PAPER

        # 決定した手を戻り値として返す
        return hand


#==グーが大好き！」戦略クラス。
class StoneOnlyTactics():

    def read_tactics(self):
        # 必ずグーを出す
        return Player.STONE
