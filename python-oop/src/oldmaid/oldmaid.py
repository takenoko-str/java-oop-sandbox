from card import *
from hand import *
from master import *
from player import *
from table import *

# ばば抜きプログラム。


# 53枚のトランプを生成する。
def create_trump():
    trump = Hand([])

    # 各スート13枚のカードを生成する
    for i in range(13):
        number = i + 1
        trump.add_card(Card("SUIT_CLUB", number))
        trump.add_card(Card("SUIT_DIAMOND", number))
        trump.add_card(Card("SUIT_HEART", number))
        trump.add_card(Card("SUIT_SPADE", number))

    # ジョーカーの作成
    trump.add_card(Card(0, 0))

    return trump

# 進行役の生成
master = Master([])

# 場の生成
field = Table()

# プレイヤーの生成
murata = Player("村田", Hand([]), master, field)
yamada = Player("山田", Hand([]), master, field)
saito = Player("斎藤", Hand([]),master, field)

# 進行役へプレイヤーを登録
master.register_player(murata)
master.register_player(yamada)
master.register_player(saito)

# トランプを生成する
trump = create_trump()

# ゲームの準備をする
master.prepare_game(trump)

# ゲームを開始する
master.start_game()
