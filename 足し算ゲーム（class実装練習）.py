class Stage:
    def __init__(self,stage,quota,min,max):
        self.stage =stage#何ステージ目かを定義
        self.quota =quota#ステージのクリアノルマが何問かを定義
        self.minimum =min#ランダムで出てくる整数の最小値を定義
        self.maximum =max#ランダムで出てくる整数の最大値を定義
    def __repr__(self):
        stage="ステージ{}です。{}から{}の足し算だよ。{}問正解でクリア。頑張って！！".format(self.stage,self.minimum,self.maximum,self.quota)
        return stage
stage1=Stage(1,5,1,5)
stage2=Stage(2,5,1,10)
stage3=Stage(3,5,1,13)

class Game:
    def __init__(self,stages):
        self.stages=stages

    def play_game(self):
        import time
        import random
        print(self.stages)#ステージ stage です。 min から max の足し算だよ。 quota 問正解でクリア。頑張って！！
        min=int(play.stages.minimum)
        max=int(play.stages.maximum)
        quota=int(play.stages.quota)
        ans_count = 1
        total_score = 0
        print(input("10秒間に何問正解できるかな？ENTERキーでスタート！" ))
        start_time = time.time()#解答開始時間
        while True:
            a = random.randint(min, max)
            b = random.randint(min, max)
            c = random.randint(min, max)
            before_time = time.time()#この問題の出題時間。スコア作成にのみ使用。
            print(a, "+", b, "+", c, "=?")
            x = int(input())
            after_time = time.time()#答えた時間。
            if after_time - start_time >= 10:#答えた時間がスタート時間より10（秒）以上だとそこで終了。
                print("TIME UP 終了～！", ans_count - 1, "問正解でした。SCORE:", int(total_score), "点")
                if ans_count < quota:#Stageクラスで定義した問題数に達しているか判定。
                    print("残念。お疲れ様でした。")
                else:
                    print("ステージクリア！！")
                break
            elif not (a + b + c) == x:
                print("不正解。残念！！", ans_count - 1, "問正解でした。SCORE:", int(total_score), "点")
                print("お疲れ様でした。")
                break
            else:
                print("正解！！", ans_count, "問正解")
                partial_score = (10 - (after_time - before_time)) * 5#10引く解答にかかった時間の５倍がその問題のスコアとなる。
            ans_count = ans_count + 1
            total_score = total_score + partial_score

play=Game(stage1)#現状は、ここの数字を1～3で自分で変更して開始。ここを改良したい！
play.play_game()






