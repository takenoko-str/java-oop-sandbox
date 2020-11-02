class Master:

    def __init__(self, player_list):
        self.player_list = player_list

    def prepare_game(self, hand):
        print("【カードを配ります】\n")

        # トランプをシャッフルする
        hand.shuffle()

        # トランプの枚数を取得する
        number_of_cards = hand.getNumberOfCard()

        # プレイヤーの人数を取得する
        number_of_players = len(self.player_list)

        for index in range(number_of_cards):
            # カードから一枚引く
            card = hand.pick_card()

            # 各プレイヤーに順番にカードを配る
            player = self.player_list[index % number_of_players]
            player.receive_card(card)

    # ゲームを開始する。
    def start_game(self):
        print("\n【ばば抜きを開始します】\n")

        # プレイヤーの人数を取得する
        count = 0
        while len(self.player_list) > 1:
            player_index = count % len(self.player_list)
            next_player_index = (count + 1) % len(self.player_list)

            # 指名するプレイヤーの取得
            player = self.player_list[player_index]
            # 次のプレイヤーの取得
            next_player = self.player_list[next_player_index]

            # プレイヤーを指名する
            print("\n", player.name, "さんの番です --- ({})".format(count), "\n")
            player.play(next_player)
            count += 1

        # プレイヤーが上がって残り1名になるとループを抜ける
        print("【ばば抜きを終了しました】\n")

    # 上がりを宣言する。
    def declare_win(self, winner):
        # 上がったプレイヤー
        print(winner.name, "さんが上がりました！\n")

        # 上がったプレイヤーをリストからはずす
        self.player_list.remove(winner)

        # 残りプレイヤーが１人になった時は敗者を表示する
        if len(self.player_list) == 1:
            loser = self.player_list[0]
            print(loser.name, "さんの負けです！\n")

    # ゲームに参加するプレイヤーを登録する。
    def register_player(self, player):
        self.player_list.append(player)
