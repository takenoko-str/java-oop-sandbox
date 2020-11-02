from judge import *
from player import *
from tactics import *

# 審判（斎藤さん）のインスタンス生成
saito = Judge()

# プレイヤー１（村田さん）の生成
murata_tactics = RandomTactics()
murata = Player("村田さん",murata_tactics)

# プレイヤー２（山田さん）の生成
yamada_tactics = StoneOnlyTactics()
yamada = Player("山田さん",yamada_tactics)
# yamada = Player_STONE("山田さん")

# 村田さんと山田さんをプレイヤーとしてジャンケンを開始する
saito.start_janken(murata, yamada)
