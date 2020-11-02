class Judge:

    # ジャンケンを開始する。
    def start_janken(self, player1, player2):
        # ジャンケンの開始を宣言する
        print("【ジャンケン開始】\n")

        # ジャンケンを3回行う
        for cnt in range(3):
            # 何回戦目か表示する
            print("【", (cnt + 1), "回戦目】")

            # プレイヤーの手を見て、どちらが勝ちかを判定する。
            winner = self.judge_janken(player1, player2)

            if (winner != None):
                # 勝者を表示する
                print("\n", winner.get_name(), "が勝ちました!\n")
                # 勝ったプレイヤーへ結果を伝える
                winner.notify_result(True)
            else:
                # 引き分けの場合
                print("\n引き分けです！\n")

        # ジャンケンの終了を宣言する
        print("【ジャンケン終了】\n")

        # 最終的な勝者を判定する
        final_winner = self.judge_final_winner(player1, player2)
        print(player1.get_win_count(), " 対 ", player2.get_win_count(), "で")
        if (final_winner != None):
            print(final_winner.get_name(), "の勝ちです！\n")
        else:
            print("引き分けです！\n")

    # プレイヤーの手を見て、どちらが勝ちかを判定する。
    def judge_janken(self,player1, player2):
        winner = None

        hand_dict = {0: "STONE",
                     1: "SCISSORS",
                     2: "PAPER"}

        # プレイヤーの手を出す
        player1hand = player1.show_hand()
        player2hand = player2.show_hand()
        player1hand_name = hand_dict[player1hand]
        player2hand_name = hand_dict[player2hand]

        # それぞれの手を表示する
        print(f"{player1hand_name} vs. {player2hand_name} \n")

        # プレイヤー１が勝つ場合
        if (player1hand_name == "STONE" and player2hand_name == "SCISSORS") or \
                (player1hand_name == "SCISSORS" and player2hand_name == "PAPER") or \
                (player1hand_name == "PAPER" and player2hand_name == "STONE") :
            winner = player1

        # プレイヤー２が勝つ場合
        if (player1hand_name == "STONE" and player2hand_name == "PAPER") or \
                (player1hand_name == "SCISSORS" and player2hand_name == "STONE") or \
                (player1hand_name == "PAPER" and player2hand_name == "SCISSORS") :
            winner = player2

        # どちらでもない場合は引き分け(nilを返す)
        return winner

    # 最終的な勝者を判定する。
    def judge_final_winner(self,player1, player2):
        final_winner = None

        # 勝ち数を聞く
        player1_win_count = player1.get_win_count()
        player2_win_count = player2.get_win_count()

        # 勝者を決定
        if (player1_win_count > player2_win_count):
            final_winner = player1
        elif(player1_win_count < player2_win_count):
            final_winner = player2
        else:
            final_winner = None

        return final_winner
