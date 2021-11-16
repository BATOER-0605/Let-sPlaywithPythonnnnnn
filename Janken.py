import random

while True:
    print("\nHey!お前ら準備はいいか？？\n")
    print("これからお前にはじゃんけんで遊んでもらう！\n")

    print("さあ！始めようか！じゃーんけーん.....\n")
    print("キミは何を出す！？　1,グー 2,チョキ 3,パー\n注）半角で入力してくれ！\n")

    players=int(input(">"))     #プレイヤーに自分の出す手を選ばせる

    bots=random.randint(1,3)    #Botの出す手をランダムに決める

    #プレイヤー側の手札の定義
    if players==1:
        playershand='グー'

    elif players==2:
        playershand='チョキ'

    elif players==3:
        playershand='パー'

    else : #プレイヤー側の不手際は見逃さない
        print("そんな手札はないよ！半角で1~3を入力してくれ！")
        errorcode=1

    #Bot側の手札の定義
    if bots==1:
        botshand='グー'

    elif bots==2:
        botshand='チョキ'

    elif bots==3:
        botshand='パー'

    #対戦結果の初期化
    win=0
    draw=0
    lose=0

    #Botの手札とプレイヤーが出した手札を表示
    print("Botが出した手札:\n",botshand)
    print("あなたがだした手札:",playershand)

    #判断フロー
    while True:
        if botshand=='グー':
            if playershand=='グー':
                print("あいこだ！そーれもういっちょ！！！")
                draw+=1

            if playershand=='チョキ':
                botres=random.randint(1,3)
                if botres==1:
                    print("はっはっはっはっはー！私のほうが強いのだ！")
                elif botres==2:
                    print("私の勝ちだ。どうして負けたか考えるがよい。")
                else:
                    print("どうやら神は私に味方するようだ。")
                lose+=1

            if playershand=='パー':
                botres=random.randint(1,3)
                if botres==1:
                    print("くっ、、、おぬし、強いなっ、、、！ﾊﾞﾀﾘ")
                elif botres==2:
                    print("私の負けだ。君は強いな。")
                else:
                    print("どうしてだよｵｵｵｵｵｵｵｵ!!!!!!!!!!!")
                win+=1

        if botshand=='チョキ':
            if playershand=='チョキ':
                print("あいこだ！そーれもういっちょ！！！")
                draw+=1

            if playershand=='パー':
                botres=random.randint(1,3)
                if botres==1:
                    print("はっはっはっはっはー！私のほうが強いのだ！")
                elif botres==2:
                    print("私の勝ちだ。どうして負けたか考えるがよい。")
                else:
                    print("どうやら神は私に味方するようだ。")
                lose+=1

            if playershand=='グー':
                botres=random.randint(1,3)
                if botres==1:
                    print("くっ、、、おぬし、強いなっ、、、！ﾊﾞﾀﾘ")
                elif botres==2:
                    print("私の負けだ。君は強いな。")
                else:
                    print("どうしてだよｵｵｵｵｵｵｵｵ!!!!!!!!!!!")
                win+=1

        if botshand=='パー':
            if playershand=='パー':
                print("あいこだ！そーれもういっちょ！！！")
                draw+=1

            if playershand=='グー':
                botres=random.randint(1,3)
                if botres==1:
                    print("はっはっはっはっはー！私のほうが強いのだ！")
                elif botres==2:
                    print("私の勝ちだ。どうして負けたか考えるがよい。")
                else:
                    print("どうやら神は私に味方するようだ。")
                lose+=1

            if playershand=='チョキ':
                botres=random.randint(1,3)
                if botres==1:
                    print("くっ、、、おぬし、強いなっ、、、！ﾊﾞﾀﾘ")
                elif botres==2:
                    print("私の負けだ。君は強いな。")
                else:
                    print("どうしてだよｵｵｵｵｵｵｵｵ!!!!!!!!!!!")
                    win+=1

    #対戦結果を表示
    print("対戦結果\n")
    print("勝った回数\n",win)
    print("負けた回数\n",lose)
    print("引き分けの回数\n",draw)

    #コンティニューの是非
    print("\n続けますか？(y/n)")
    playerres=str(input(">"))
    if playerres=='y' :
        continue

    elif playerres=='n' :
        break

    else :
        print("不明なyかnで答えろ言うてるやん。従わないならここから去るが良い！")
        break
